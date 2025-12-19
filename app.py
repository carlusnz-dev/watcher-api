import os, traceback, models, watcher
from flask import Flask, request, jsonify
from extensions import db
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.base import STATE_RUNNING, STATE_PAUSED, STATE_STOPPED

basedir = os.path.abspath(os.path.dirname(__file__))
scheduler = BackgroundScheduler()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(basedir, "watchs.db")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Routes

# Read all monitors
@app.route('/api/monitor/read_all', methods=['GET'])
def read_all_monitors():
  monitors = models.Monitor.query.all()
  monitors_formatted = []
  
  try:
    for monitor in monitors:
      new_monitor = {
        "name": monitor.name,
        "url": monitor.url,
        "frequency": monitor.frequency,
        "status": monitor.status,
        "description": monitor.description
      }
      monitors_formatted.append(new_monitor)
    
    return jsonify({
      "message": "Todos os monitores carregados!",
      "monitors": monitors_formatted
    }),200
    
  except Exception as e:
    full_traceback = traceback.format_exc()
    print(f"Erro ao carregar os monitores! \n{e}")
    return jsonify({
      "message": "Erro ao salvar o monitor!",
      "error": full_traceback
    }), 400
    
@app.route('/api/monitor/read/<int:monitor_id>', methods=['GET'])
def read_monitor_by_id(monitor_id):
  monitor = models.Monitor.query.get_or_404(monitor_id)
  monitor_formatted = {
    "id": monitor.id,
    "name": monitor.name,
    "url": monitor.url,
    "frequency": monitor.frequency,
    "status": monitor.status,
    "description": monitor.description
  }
  
  return jsonify({
    "message": "Monitor achado no banco de dados!",
    "monitor": monitor_formatted
  }), 200


# Create new monitor
@app.route('/api/monitor/add', methods=['POST'])
def add_monitor():
  data = request.json
  
  # Checking if there is monitor in the DB
  if 'url' in data:
    found_monitor = models.Monitor.query.filter_by(url=data['url']).first()
    if found_monitor:
      return jsonify({
        "message": "Erro ao salvar! Monitor já existente",
        "existing_id": found_monitor.id
      }), 400
    
  if 'name' in data and 'url' in data:
    new_monitor = models.Monitor(
      name = data['name'],
      url = data['url'],
      frequency = data.get('frequency', 5 * 60),
      status = data.get('status'),
      description = data.get('description', 'Has no description')
    )
    
    db.session.add(new_monitor)
    db.session.commit()
    return jsonify({
      "message": "Monitor salvo com sucesso!",
      "monitor_id": new_monitor.id
    }), 200
  
  return jsonify({"message": "Dados do produto inválidos ou faltantes!"}), 400

# Update monitor
@app.route('/api/monitor/update/<int:monitor_id>', methods=['PUT'])
def update_monitor(monitor_id):
  monitor = models.Monitor.query.get_or_404(monitor_id)
  new_monitor = request.get_json()
  
  if 'name' in new_monitor:
    monitor.name = new_monitor['name']
  if 'url' in new_monitor:
    monitor.url = new_monitor['url']
  if 'frequency' in new_monitor:
    monitor.frequency = new_monitor['frequency']
  if 'status' in new_monitor:
    monitor.status = new_monitor['status']
  if 'description' in new_monitor:
    monitor.description = new_monitor['description']
    
  db.session.commit()
    
  return jsonify({
    "message": f"Monitor atualizado com sucesso!",
    "new_monitor": new_monitor
  }), 200

# Detele monitor
@app.route('/api/monitor/delete/<int:monitor_id>', methods=['DELETE'])
def delete_monitor(monitor_id):
  monitor = models.Monitor.query.get_or_404(monitor_id)
  
  try:
    job_id = str(monitor.id)
    scheduler.remove_job(job_id)
  except Exception as e:
    print(f"Aviso: não foi possível remover o Job {job_id}. Ele pode não estar ativo. Erro {e}")
    
  db.session.delete(monitor)
  db.session.commit()
  
  return jsonify({
    "message": "Monitor deletado com sucesso!",
    "monitor_id": monitor.id
  }), 200
  
# Schedulers
@app.route('/api/monitor/watcher/<command>', methods=['GET'])
def watch_all_monitors(command):
  if command == 'start':
    try:
      if scheduler.state == STATE_RUNNING:
        return jsonify({
          "message": "Scheduler já está rodando!"
        }), 400
      
      if scheduler.state == STATE_STOPPED:
        scheduler.start()
        return jsonify({
          "message": "Scheduler foi iniciado!"
        }), 200
        
      if scheduler.state == STATE_PAUSED:
        scheduler.resume()
        return jsonify({
          "message": "Retornando as atividades do Scheduler!",
        }), 200
              
    except Exception:
      return jsonify({
        "message": f"Erro ao executar o comando <{command}>!",
        "error": traceback.format_exc()
      })
      
  if command == 'stop':
    try:
      scheduler.pause()
      return jsonify({
        "message": "Scheduler pausado com sucesso!"
      }), 200
    except Exception:
      return jsonify({
        "message": "Erro ao parar o scheduler!",
        "error": traceback.format_exc()
      })
  
@app.route('/api/monitor/watcher/<int:monitor_id>', methods=['GET'])
def watch_monitor(monitor_id):
  monitor = models.Monitor.query.get_or_404(monitor_id)
  job_id = str(monitor.id)
  
  try:
    if scheduler.state == STATE_STOPPED:
      scheduler.start()
    elif scheduler.state == STATE_PAUSED:
      scheduler.resume()
      
    scheduler.add_job(
      func=watcher.check_monitor_for_id,
      trigger='interval',
      seconds=monitor.frequency,
      args=[monitor.id],
      id=job_id,
      replace_existing=True
    )
    
    return jsonify({
      "message": f"Watcher do {monitor.name} iniciado!",
      "monitor_id": monitor.id
    }), 200
  except Exception as e:
    return jsonify({
      "message": "Erro durante a execução do código!",
      "error": traceback.format_exc()
    })

# Config
if __name__ == "__main__":
  with app.app_context():
    db.create_all()
  
  app.run(debug=False)

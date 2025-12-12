import os, traceback
from flask import Flask, request, jsonify
from extensions import db
import models

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(basedir, "watchs.db")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Routes
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

@app.route('/api/monitor/add', methods=['POST'])
def add_monitor():
  data = request.json
  if 'name' in data and 'url' in data:
    new_monitor = models.Monitor(
      name = data['name'],
      url = data['url'],
      frequency = data.get('frequency', 5),
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

@app.route('/api/monitor/delete/<int:monitor_id>', methods=['DELETE'])
def delete_monitor(monitor_id):
  monitor = models.Monitor.query.get_or_404(monitor_id)
  db.session.delete(monitor)
  db.session.commit()
  
  return jsonify({
    "message": "Monitor deletado com sucesso!",
    "monitor_id": monitor.id
  }), 200

# Config
if __name__ == "__main__":
  with app.app_context():
    db.create_all()
  
  app.run(debug=False)

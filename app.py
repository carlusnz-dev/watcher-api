import os
from flask import Flask, request, jsonify
from extensions import db
import models

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(basedir, "watchs.db")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Routes


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
    return jsonify({ "message": "Dados salvos com sucesso!" }), 200
  
  return jsonify({"message": "Dados do produto inválidos!"}), 400


# Config
if __name__ == "__main__":
  with app.app_context():
    db.create_all()
  
  app.run(debug=False)

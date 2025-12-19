import os
from flask import Flask
from app.extensions import db, scheduler

def create_app():
  app = Flask(__name__)
  
  basedir = os.path.abspath(os.path.dirname(__file__))
  database_path = os.path.join(basedir, '..', 'instance', 'watchs.db')
  
  app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{database_path}'
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  
  db.init_app(app)
  from app.routes.monitor import bp as monitor_bp
  app.register_blueprint(monitor_bp)
  
  with app.app_context():
    db.create_all()
  
  if not scheduler.running:
    scheduler.start()
  
  return app
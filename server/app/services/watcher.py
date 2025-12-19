import requests, app.models as models
from app import create_app
from app.extensions import db
from apscheduler.schedulers.blocking import BlockingScheduler

def check_monitors():
  print("\nRodando verificação...")
  app = create_app()
  with app.app_context():
    all_monitors = models.Monitor.query.all()

    for monitor in all_monitors:
      try:
        response = requests.get(monitor.url, timeout=3)
        print(f"\nSite {monitor.name}: {response.status_code}")
        if response.status_code != monitor.status:
          monitor.status = response.status_code
          db.session.commit()
          print(f"Alterações feitas: {monitor.name}")        
      except Exception as e:
        print(f"\nErro ao acessar {monitor.name}: {e}")
        if monitor.status != 0:
          monitor.status = 0
          db.session.commit()
          print(f"Alterações feitas: {monitor.name}")

def check_monitor_for_id(monitor_id):
  app = create_app()
  with app.app_context():    
    monitor = models.Monitor.query.get(monitor_id)
    if not monitor:
      return
    
    try:
      response = requests.get(monitor.url, timeout=5)
      print(f"\nSite: {monitor.name}\nStatus: {monitor.status}")
      if response.status_code != monitor.status:
        monitor.status = response.status_code
        db.session.commit()
        print(f"Alterações feitas: status alterado para {monitor.status}")
    except Exception as e:
      print(f"\nErro ao alterar o monitor! {e}")
      if monitor.status != 0:
        monitor.status = 0
        db.session.commit()
        print(f"Alterações feitas: status alterado para {monitor.status}")
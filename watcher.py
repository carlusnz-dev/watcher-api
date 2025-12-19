import requests, models
from app import app
from extensions import db
from apscheduler.schedulers.blocking import BlockingScheduler

def check_monitors():
  print("\nRodando verificação...")
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

if __name__ == "__main__":
  scheduler = BlockingScheduler()
  scheduler.add_job(check_monitors, 'interval', seconds=10)
  print("Robô rodando! Ctrl+C para cancelar.")
  try:
    scheduler.start()
  except (KeyboardInterrupt, SystemExit):
    pass
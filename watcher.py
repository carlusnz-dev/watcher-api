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

if __name__ == "__main__":
  scheduler = BlockingScheduler()
  scheduler.add_job(check_monitors, 'interval', seconds=10)
  print("Robô rodando! Ctrl+C para cancelar.")
  try:
    scheduler.start()
  except (KeyboardInterrupt, SystemExit):
    pass
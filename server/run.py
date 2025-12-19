from app import create_app

new_app = create_app()

if __name__ == "__main__":
  new_app.run(debug=True)
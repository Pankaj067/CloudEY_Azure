from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hey its Python Flask application! \n Dev In Progress!'

if __name__ == '__main__':
  app.run()

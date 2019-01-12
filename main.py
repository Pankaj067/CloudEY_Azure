from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return render_template('Presentation.html')

@app.route('/AI')
def AIModule():
    return render_template('ForTesting.html')

if __name__ == '__main__':
  app.run()

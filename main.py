from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
  return render_template('Presentation.html')

@app.route('/AI')
def AIModule():
    return render_template('Test.html')

if __name__ == '__main__':
  app.run()

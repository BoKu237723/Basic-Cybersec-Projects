from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "<h1 style='text-align': center> Hello World! </h1>" \
    "<p>This is a paragraph!</p>"

@app.route('/page/<int:number>')
def bye(number):
    return f"This is page {number}"

@app.route('/welcome/<string:name>')
def welcome(name):
    return f"Welcome {name}!"

if __name__ == "__main__":
    app.run(debug=True)
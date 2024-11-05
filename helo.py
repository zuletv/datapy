from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, Diana!</p>"

@app.route("/saludo")
def saludoatodos():
    return "<center>Saludos a todos</center>"

@app.route("/about")
def sobremi():
    return "<marquee><h1> Diana Talamantes </h1></marquee>"
from flask import Flask

app = Flask(__name__)
print(type(app))

@app.route("/")
def func():
    return "Ganpati Bappa Moraya"

@app.route("/moraya")
def function():
    return "Mangalmurti Moraya"

if __name__=='__main__':
    app.run()
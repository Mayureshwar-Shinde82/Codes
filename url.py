from flask import Flask,redirect,url_for

app = Flask(__name__)

@app.route("/pass/<int:score>")
def Pass(score):
    return "Student has Passed with marks obtained is " + str(score)

@app.route("/fail/<int:score>")
def Fail(score):
    return "The Student has failed and he got " + str(score) + " marks"

@app.route("/result/<int:marks>")
def Result(marks):
    result = ""
    if marks < 28:
        result = 'Fail'
    else:
        result = 'Pass'
    return redirect(url_for(result,score=marks))
    

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask
app = Flask(__name__)

from flask import request, render_template
import joblib

@app.route("/", methods = ["GET"])
def initialise():
    if request.method == "GET":
        return(render_template("main.html"))

@app.route("/linear", methods = ["GET", "POST"])
def linear():
    if request.method == "POST":
        name = request.form.get("name")
        print(name)
        num = request.form.get("rates")
        print(num)
        model = joblib.load('DBS_linear')
        if num == "":
            s = "Please input into the fields above!"
        else:
            num = float(num)
            pred = model.predict([[num]])
            print(pred)
            pred = pred[0][0]
            s = "Predicted DBS Share Price: " + str(pred)
            print(s)
        return(render_template("linear.html", linear_result=s))
    else:
        return render_template("linear.html", linear_result="Click on the submit button for prediction!")

@app.route("/tree", methods = ["GET", "POST"])
def tree():
    if request.method == "GET":
        return(render_template("tree.html", tree_result="Click on the submit button for prediction!"))
    if request.method == "POST":
        num = request.form.get("rates")
        print(num)
        model = joblib.load('DBS_tree')
        if num == "":
            s = "Please input into the fields above!"
        else:
            num = float(num)
            pred = model.predict([[num]])
            print(pred)
            pred = pred[0]
            s = "Predicted DBS Share Price: " + str(pred)
            print(s)
        return(render_template("tree.html", tree_result=s))
    else:
        return render_template("tree.html", tree_result="Click on the submit button for prediction!")

@app.route("/MLP", methods = ["GET", "POST"])
def MLP():
    if request.method == "GET":
        return(render_template("MLP.html", MLP_result="Click on the submit button for prediction!"))
    if request.method == "POST":
        num = request.form.get("rates")
        print(num)
        model = joblib.load('DBS_MLP')
        if num == "":
            s = "Please input into the fields above!"
        else:
            num = float(num)
            pred = model.predict([[num]])
            print(pred)
            pred = pred[0]
            s = "Predicted DBS Share Price: " + str(pred)
            print(s)
        return(render_template("MLP.html", MLP_result=s))
    else:
        return render_template("MLP.html", MLP_result="Click on the submit button for prediction!")

if __name__ == "__main__":
    app.run()
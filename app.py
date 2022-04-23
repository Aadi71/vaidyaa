from flask import Flask, render_template, request
import model as h

app = Flask(__name__, template_folder='templates')


@app.route("/", methods = ["GET", "POST"])
def model():
    if request.method == "POST":
        age = int(request.form["age"])

        gender = int(request.form["gender"])

        cp = int(request.form["cp"])

        trestbps = int(request.form["trestbps"])

        chol = int(request.form["chol"])

        restech = int(request.form["restech"])

        thalach = int(request.form["thalach"])

        exang = int(request.form["exang"])

        oldpeak = int(request.form["oldpeak"])

        slope = int(request.form["slope"])

        ca = int(request.form["ca"])

        thal = int(request.form["thal"])

        sample = [[age, gender, cp, trestbps, chol, restech, thalach, exang, oldpeak, slope, ca, thal]]
        #print(sample)
        heart_pred = h.heart_disease(sample)
        # print(heart_pred)
        # hp = heart_pred
    return render_template('main.html', heart_result = heart_pred)


# @app.route("/sub", methods = ["POST"])
# def submit():
#     if request.method == "POST":
#         age = request.form["age"]
#
#     return render_template("sub.html", age=age)


if __name__ == '__main__':
    app.run(debug=True)

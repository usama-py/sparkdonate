from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("charifit-master/index.html")

@app.route("/payment")
def payment():
    return render_template("charifit-master/payment.html")

app.run(debug=True)
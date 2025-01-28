from flask import Flask
from flask import render_template
from flask import url_for

app = Flask(__name__, static_folder='./static/')

@app.route('/',methods=["GET", "POST"])
def happy_new_year():
    return render_template("main.html")

@app.route('/senkyo')
def snekyo():
    return render_template('senkyo.html')


if __name__ == "__main__":
    app.run(debug = True,port=8888, threaded = True)
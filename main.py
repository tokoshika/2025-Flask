from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/',methods=["GET", "POST"])
def happy_new_year():
    return render_template("main.html")


if __name__ == "__main__":
    app.run(debug = True,port=8888, threaded = True)
#=====================IMPORTS=========================
from functions import login_required, error
from flask import Flask, render_template, request, session
#=====================================================

# Create Flask Application
app = Flask(__name__)


# Home Directory
@app.route("/")
def index():
    return render_template("home.html")


@app.route("/glass")
def glass():
    return render_template("glass.html")

@app.route("/neuralink")
def neuralink():
    return render_template("link.html")

@app.route("/nanobots")
def nanobots():
    return render_template("nano.html")

@app.route("/olfactorySenses")
def olfactory():
    return render_template("olfactory.html")

# Run The Application
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
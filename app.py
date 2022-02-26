#=====================IMPORTS=========================
from functions import login_required, error
from flask import Flask, render_template, request, session
from flask_session import Session
from simpleDB import Database
from tempfile import mkdtemp
#=====================================================

# Create Flask Application
app = Flask(__name__)


# Home Directory
@app.route("/")
def index():
    return render_template("home.html")



# Run The Application
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
#=====================IMPORTS=========================
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import redirect
from functions import login_required, error
from flask import Flask, render_template, request, session
from flask_session import Session
from simpleDB import Database
from tempfile import mkdtemp
from random import randint
#=====================================================

# Create Flask Application
app = Flask(__name__)

# Connect To Database
db = Database("Database.db")

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


# Home Directory
@app.route("/")
@login_required
def index():
    return render_template("index.html")

# Login Page
@app.route("/login", methods=["GET", "POST"])
def login():

    session.clear()

    if request.method == "GET":
        return render_template("login.html")
    
    request.form.get("pass")

    # Query database for username
    rows = db.execute("SELECT * FROM users WHERE username = ?", (request.form.get("username"),))

    # Ensure username exists and password is correct
    if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("pass")):

        return render_template("login.html", error=error(401, "Incorrect Password or Username"))
        # Remember which user has logged in

    session["user_id"] = rows[0]["user_id"]
    return redirect("/")



# Run The Application
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
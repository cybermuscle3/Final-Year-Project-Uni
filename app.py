from flask import Flask, render_template, request, redirect, session
from functools import wraps
from utils.nfc_tools import read_card, write_card, clone_card
from utils.db_manager import add_log, get_logs, register_user

app = Flask(__name__)
app.secret_key = "very_secret_key_123456"  # Change this to something random and strong

# Login protection decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get("logged_in"):
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

# Login route
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form["password"] == "yourSuperSecretPassword":  # Change this!
            session["logged_in"] = True
            return redirect("/")
        else:
            return "Wrong password. Try again."
    return '''
        <h2>Login</h2>
        <form method="post">
            <input type="password" name="password" placeholder="Enter Password">
            <button>Login</button>
        </form>
    '''

# Logout route
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

# Main dashboard (requires login)
@app.route("/")
@login_required
def index():
    return render_template("index.html", logs=get_logs())

# Dump UID from card
@app.route("/dump", methods=["POST"])
@login_required
def dump():
    uid = read_card()
    if uid:
        add_log(uid, result="Dumped", method="Web")
    return redirect("/")

# Write test data to card
@app.route("/write", methods=["POST"])
@login_required
def write():
    success = write_card()
    return redirect("/")

# Clone card data from one to another
@app.route("/clone", methods=["POST"])
@login_required
def clone():
    success = clone_card()
    return redirect("/")

# Register user
@app.route("/register", methods=["POST"])
@login_required
def register():
    name = request.form['name']
    email = request.form['email']
    register_user(name, email)
    return redirect("/")

# Run app
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)


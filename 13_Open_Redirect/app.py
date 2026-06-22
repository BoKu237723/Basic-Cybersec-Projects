from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
import requests

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost/mydb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# dbname = mydb
# username = root
# password = password
# host = localhost

db = SQLAlchemy(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about', methods = ['GET', 'POST'])
def about_me():
    user_input = ''
    if request.method == "POST":
        user_input = request.form.get('xss_input', '')
    return render_template('about_gliders.html', user_input = user_input)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    message = ''
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        query_stmt = f"SELECT username FROM users WHERE username='{username}' and password = '{password}'"
        with db.engine.connect() as conn:
            result = conn.execute(text(query_stmt))
        # user = result.fetchone()
        user = result.fetchall()

        if user:
            # message = f"Welcome, {username}"
            message = f"Welcome, {user}"
        else:
            message ="Incorrect username or password."
        
    return render_template('login.html', message = message)

# ===================================

# ------ GOOD CODE ------

bad_chars = ["'", ";", "--"]

def black_list(s):
    for char in bad_chars:
        if char in s.lower():
            return True
    return False

@app.route('/register', methods = ['GET', 'POST'])
def register():
    message = ''

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if black_list(username):
            message = "These are not allowed in a username: ; -- '"
            return render_template("register.html", message = message)

        # 1. Changed %s to :username
        check_query = "SELECT username FROM users WHERE username = :username"
        with db.engine.connect() as conn:
            # 2. Passed the variable as a dictionary mapping {"username": username}
            user_exists = conn.execute(text(check_query), {"username": username}).fetchone()

        if user_exists:
            message = "User already Exists!"
        else:
            # 3. Changed %s to :username and :password
            insert_query = "INSERT INTO users (username, password) VALUES (:username, :password)"
            with db.engine.connect() as conn:
                # 4. Passed variables as a dictionary, and added conn.commit() so it actually saves
                conn.execute(text(insert_query), {"username": username, "password": password})
                conn.commit() 
                message = "Registration Successful!"
        
    return render_template('register.html', message = message)

@app.route('/redirect', methods = ['GET'])
def redirect_page():
    return render_template('redirect.html')

@app.route('/open', methods = ['GET'])
def open():
    target_url = request.args.get('url')
    action = request.args.get('action', 'redirect')

    # open redirection
    if action == "redirect":
        return redirect(target_url)
    
    # SSRF

    elif action == 'fetch':
        try:
            response = request.get(target_url, timeout=5)
            if response.status_code == 200:
                return f"Received 200 ok: {target_url}"
            else:
                return f"Received: {response.status_code} from {target_url}"
        
        except requests.ConnectionError:
            return f"Connection refused by {target_url}"
        except requests.Timeout:
            return f"Connection timed out for {target_url}"
        except Exception as e:
            return f"An Error Occured: {e}"
    return "Spicify action and url parameters"

if __name__ == "__main__":
    app.run(debug=True)

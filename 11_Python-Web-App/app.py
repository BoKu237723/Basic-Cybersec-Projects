from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about', methods = ['GET', 'POST'])
def about_me():
    user_input = ''
    if request.method == "POST":
        user_input = request.form.get('xss_input', '')
    return render_template('about_gliders.html', user_input = user_input)

if __name__ == "__main__":
    app.run(debug=True)







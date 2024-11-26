
from flask import Flask,render_template

app = Flask(__name__)

# 1. Add a View Function for the Home page.
@app.route("/")
def homepage():
    return render_template("home.html")

# 2. Add a View Function for the About page.
@app.route("/about")
def about():
    return render_template("about.html")
     

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)
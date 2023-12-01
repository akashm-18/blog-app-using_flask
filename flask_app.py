from flask import Flask, render_template, url_for, request, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config["SECRET_KEY"] = "cf11bfa1c7ea958a4e36ea87451dedd0"

posts = [
    {
        "author": "Akash",
        "title": "First blog",
        "content": "First blog content",
        "date": "November 30",
    },
    {
        "author": "Abishek",
        "title": "second blog",
        "content": "Second blog content",
        "date": "November 30",
    },
]


# Creating the routes using the flask_app
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title="about")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account succesFully created for {form.username.data}!", "success")
        return redirect(url_for("home"))
    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data == "password":
            flash(f"Logged in successfully !", "success")
            return redirect(url_for("home"))
        else:
            flash(f"Login Failed ! Invalid username and password !!", "danger")
    return render_template("login.html", title="Login", form=form)


if __name__ == "__main__":
    app.run(debug=True)

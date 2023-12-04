from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User


class RegistrationForm(FlaskForm):
    username = StringField(
        "username",
        validators=[DataRequired(), Length(min=2, max=20)],
    )
    email = StringField(
        "Email",
        validators=[DataRequired(), Email()],
    )
    password = PasswordField("password", validators=[DataRequired()])
    confirm_password = PasswordField(
        "confirm Password", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("Sign up")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("username already Exists")

    def validate_email(self, email):
        email = User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError("Email Already exists")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("password", validators=[DataRequired()])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Login")

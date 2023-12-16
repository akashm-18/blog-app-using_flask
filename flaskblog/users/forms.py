from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, EqualTo, ValidationError, Email, Length
from flask_login import current_user
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


class UpdateAccountForm(FlaskForm):
    username = StringField(
        "username",
        validators=[DataRequired(), Length(min=2, max=20)],
    )
    email = StringField(
        "Email",
        validators=[DataRequired(), Email()],
    )
    picture = FileField(
        "Update Profile Picture", validators=[FileAllowed(["jpg", "png"])]
    )
    submit = SubmitField("Update Profile")

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError("username already Exists")

    def validate_email(self, email):
        if email.data != current_user.email:
            email = User.query.filter_by(email=email.data).first()
            if email:
                raise ValidationError("Email Already exists")


class RequestResetForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    submit = SubmitField("Request Password Reset")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError(
                "There is no Account with this Email.You need to Signup"
            )


class ResetPasswordForm(FlaskForm):
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField(
        "Confirm Password", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("Reset Password")

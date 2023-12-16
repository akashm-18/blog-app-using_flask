import os
import secrets
from PIL import Image
from flask import url_for
from flask_mail import Message
from flaskblog import mail
from flask import current_app


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_filename = random_hex + f_ext
    picture_path = os.path.join(
        current_app.root_path, "static/profile_pics", picture_filename
    )

    output_image_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_image_size)
    i.save(picture_path)

    return picture_filename


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message(
        "Password Reset Request", sender="noreply@demo.com", recipients=[user.email]
    )
    msg.body = f"""To Reset your password,please visit the link: {url_for('users.reset_token',token=token,_external=True)} 
    If you didnt need this then please ignore ..
    """
    mail.send(msg)

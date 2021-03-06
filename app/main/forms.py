from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField
from wtforms.validators import ValidationError, DataRequired, Length, EqualTo
from flask_babel import _, lazy_gettext as _l
from app.models import User



class EditProfileForm(FlaskForm):
    username = StringField(_l('Username'), validators=[DataRequired()])
    about_me = TextAreaField(_l('About me'),
                             validators=[Length(min=0, max=140)])
    submit = SubmitField(_l('Submit'))

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError(_('Please use a different username.'))


class ChangePasswordForm(FlaskForm):
    current_password = StringField(_l('Current Password'),validators=[DataRequired()])
    new_password = PasswordField(_('New Password'),validators=[DataRequired()])
    new_password2 = PasswordField(_('Repeat Password'),validators=[DataRequired(),EqualTo('new_password')])
    submit = SubmitField(_('Submit'))


class EmptyForm(FlaskForm):
    submit = SubmitField('Submit')


class PostForm(FlaskForm):
    post = TextAreaField(_l('Say something'), validators=[DataRequired()])
    submit = SubmitField(_l('Submit'))


class EditPostForm(FlaskForm):
    post = TextAreaField(_('Text'),validators=[DataRequired()])
    submit = SubmitField(_('Edit'))
    delete_post = SubmitField(_('Delete'))


class MessageForm(FlaskForm):
    message = TextAreaField(_('Message'),validators=[DataRequired(),Length(min=0,max=140)])
    submit = SubmitField(_('Submit'))
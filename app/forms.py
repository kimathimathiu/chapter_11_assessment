from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(1, 64)])
    password = PasswordField('Password' , validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log in')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(1, 64)])
    password = PasswordField('Password' , validators=[DataRequired()])
    confirmpassword = PasswordField('Confirm Password' , validators=[DataRequired(), EqualTo('password')])
    email = StringField('Email', validators=[DataRequired(), Email()] )
    submit = SubmitField('Register')

class AddForm(FlaskForm):
    stockavailable = SelectField(
        'Stock Available',  
        choices= [
            (1, 1),
            (5, 5),
            (8,8)
            ], 
            validators=[DataRequired()])
    productname= StringField('Product Name', validators=[DataRequired()])
    productdescription=StringField('Product Desctiption', validators=[DataRequired()])
    submit=SubmitField('Add Product',)

class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(1, 64)])
    about_me = StringField('Bio:', validators=[Length(min=0, max=200)])
    submit = SubmitField('Edit Profile')
    email = StringField('Email', validators=[DataRequired(), Email()] )

class PostForm(FlaskForm):
    """Comment Form"""
    body = TextAreaField('Body', validators=[DataRequired()])
    submit = SubmitField('Post')
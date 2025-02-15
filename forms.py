from wtforms import form
from flask_wtf import FlaskForm
from wtforms.validators import data_required, email, EqualTo, Length, NumberRange, Regexp
from wtforms import StringField, EmailField, PasswordField, SubmitField, IntegerField, SelectField, DecimalField

class UserForm(Form):
    matricula=StringField("Matricula")
    edad=IntegerField("Edad")
    nombre=StringField("Nombre")
    apellidos=StringField("Apellidos")
    correo=EmailField("Correo")
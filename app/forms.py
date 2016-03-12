from flask.ext.wtf import Form#, TextField, SubmitField
from wtforms import TextField, SubmitField
#from wtforms.validators import Required

def __init__(self):
    self.secret_key = 'development key'

class DataForm(Form):
    name = TextField("Full Name")
    username = TextField("Username")
    submit = SubmitField("Submit")
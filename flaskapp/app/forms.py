from flask.ext.wtf import Form
from wtforms.fields import TextField, DecimalField, SubmitField
 
class AddForm(Form):
  device = TextField("device")
  energyusage = DecimalField("energyusage(W)")
  hoursperweek = DecimalField("houerperweek")
  submit = SubmitField("save")

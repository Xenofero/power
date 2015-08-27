from flask_wtf import Form
from wtforms import TextField, DecimalField, SubmitField, validators

class AddForm(Form):
  device = TextField("device",  [validators.DataRequired("What device do you wish to add?")])
  energyusage = DecimalField("energyusage(W)",  [validators.DataRequired("How much energy need the device?"), validators.NumberRange(min=0, max=5000, message= "have to be between 0 and 5000")])
  hoursperweek = DecimalField("houerperweek",  [validators.DataRequired("How many hours per week is this device on?"), validators.NumberRange(min=0, max=168, message= "have to be between 0 and 168")])
  submit = SubmitField("save")

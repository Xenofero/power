from flask_wtf import Form
from wtforms import TextField, DecimalField, SubmitField, validators, BooleanField, TextAreaField, RadioField

class AddForm(Form):
  servername = TextField("Servername",  [validators.DataRequired("Please enter the servername of the VM! (e.g. z-wnmtrxsql02)")])
  internalname = TextField("How is the server named in the department?",  [validators.DataRequired("Please enter the internalname of the VM!")])
  mainresponsible = TextField("Who is main Person responsible fo this Server? (only Person no substition)", [validators.Email("Please enter a valid e-mail adress!")])
  substitute = TextField("Substitute", [validators.Email("Please enter a valid e-mail adress!")])
  costcenter = DecimalField("Costcenter",  [validators.DataRequired("Please enter the costcenter!"), validators.NumberRange(min=100000, max=9999999, message= "have to be between 100000 and 9999999")])
  location = TextField("Location", [validators.DataRequired("Service of server is used pimarily in which location?")])
  department = TextField("Department", [validators.DataRequired("The System is managed by wich department?")])
  servertype = BooleanField("None producitive server (testing system)?")
  serverdescription = TextAreaField("Short Description of the server, what are the main tasks?", [validators.DataRequired("The System is managed by wich department?")])
  serverservice = TextAreaField("Which services and programs are running on the server?", [validators.DataRequired("Please enter the programs!")])
  workloadservice = DecimalField("How many people are working with the service(s)?",  [validators.DataRequired("Please enter How many people are working with the service!"), validators.NumberRange(min=1, max=15000, message= "have to be between 1 and 15000")])
  workloadintime = RadioField("How often are the services in use? When?",[validators.Required()],choices=[("coretime","Kernarbeitszeit(core time)"),("24/7","24/7"),("night","at night"),("other","other")])
  submit = SubmitField("save")

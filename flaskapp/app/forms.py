from flask_wtf import Form
from wtforms import StringField, DecimalField, SubmitField, validators, BooleanField, TextAreaField, SelectField, IntegerField

class AddForm(Form):
  servername = StringField("Servername",  [validators.DataRequired("Please enter the servername of the VM! (e.g. z-wnmtrxsql02)")])
  internalname = StringField("How is the server named in the department?",  [validators.DataRequired("Please enter the internalname of the VM!")])
  mainresponsible = StringField("Who is main Person responsible fo this Server? (only Person no substition)", [validators.Email("Please enter a valid e-mail adress!")])
  substitute = StringField("Substitute", [validators.Email("Please enter a valid e-mail adress!")])
  costcenter = IntegerField("Costcenter",  [validators.DataRequired("Please enter the costcenter!"), validators.NumberRange(min=100000, max=9999999, message= "have to be between 100000 and 9999999")])
  location = StringField("Location", [validators.DataRequired("Service of server is used pimarily in which location?")])
  department = StringField("Department", [validators.DataRequired("The System is managed by wich department?")])
  servertype = BooleanField("None producitive server (testing system)?")
  serverdescription = TextAreaField("Short Description of the server, what are the main tasks?", [validators.DataRequired("The System is managed by wich department?")])
  serverservice = TextAreaField("Which services and programs are running on the server?", [validators.DataRequired("Please enter the programs!")])
  workloadservice = IntegerField("How many people are working with the service(s)?",  [validators.DataRequired("Please enter How many people are working with the service!"), validators.NumberRange(min=1, max=15000, message= "have to be between 1 and 15000")])
  workloadintime = SelectField("How often are the services in use? When?",[validators.Required()],choices=[("coretime","Kernarbeitszeit(core time)"),("24/7","24/7"),("night","at night"),("other","other")])
  privacyrelatedfiles = BooleanField("Are there privacy related files sved?")
  dependencies = TextAreaField("Are there any dependencies to other servers? Describe!")
  redundancy = StringField("Werden die Dienste auf diesem Server redundant betrieben?")
  bootorder = StringField("Muss eine Shutdown/Boot-Reihenfolge eingehalten werden, wenn ja, welche?")
  impactforotherserver = StringField("Welchen Effekt hat der Ausfall des Servers?", [validators.DataRequired("Please enter!")])
  departmentaffected = StringField("Betroffene Abteilungen")
  furtherwork = BooleanField(" Ist eine Weiterarbeit trotz dessen moeglich?")
  cost = DecimalField("Wenn bekannt, wie hoch sind die Kosten bei einem Ausfall pro Stunde")
  serviceaccount = TextAreaField("Welche Service Accounts werden zu welchem Zweck auf dem Server eingestzt")
  purposeaccount = TextAreaField("Zweck der Accounts")
  manuallyrestart = StringField("Muessen Dienste bei einem Neustart manuell gestartet werden")
  otherinformation = TextAreaField("Sonstige Informationen")
  submit = SubmitField("save")
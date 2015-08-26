from flask import Flask, render_template, request
from forms import AddForm
 
app = Flask(__name__)      
#app.secret_key = 'energy key'
 
@app.route('/')
def home():
  return render_template('home.html')

@app.route('/adddevice', methods=['GET', 'POST'])
def adddevice():
  if request.method == 'POST':
    return 'device added'

  elif request.method == 'POST':
    form = AddForm()
    return render_template('add.html', form=form)
 
if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')

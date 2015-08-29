# -*- coding: iso-8859-1 -*-
from flask import Flask, render_template, request, flash
from forms import AddForm
import simplejson

app = Flask(__name__)
app.secret_key = 'energy key'


@app.route('/')
def home():
    try:
        with open('devices.json', 'r') as fp:
            jsondata = simplejson.load(fp)
            print jsondata['name']
    except:
        print 'no Devices'
    return render_template('home.html')


@app.route('/adddevice', methods=['GET', 'POST'])
def adddevice():
    form = AddForm()

    # Eingabe
    if request.method == 'POST':
        # Fehler
        if not form.validate():
            flash('Error, validation faild.')
            return render_template('add.html', form=form)

        # Rückgabe + Speichern
        else:

            device = {'name': str(form.device.data),
                      'energy': str(form.energyusage.data),
                      'hours': str(form.hoursperweek.data)}

            with open('devices.json') as fp:
                devices = simplejson.load(fp)

            devicesd= str(devices)+str(device)

            with open('devices.json', 'w') as fp:
                simplejson.dump(device, fp)

            return render_template('add.html', success=True, device=str(form.device.data))

    elif request.method == 'GET':
        return render_template('add.html', form=form)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

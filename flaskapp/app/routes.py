# -*- coding: iso-8859-1 -*-
from flask import Flask, render_template, request, flash
from forms import AddForm
import json

app = Flask(__name__)
app.secret_key = 'energy key'


@app.route('/')
def home():
#    try:
    with open("devices.json", 'r') as fp:
        jsondata = json.load(fp)
        print jsondata
#    except:
#        print 'no Devices'
    return render_template('home.html', data=jsondata)


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
            with open('devices.json') as fp:
                devices = json.load(fp)
            print 'JSON', json.dumps(devices)

            devices.append({"name": str(form.device.data), "energy": str(form.energyusage.data), "hours": str(form.hoursperweek.data)})
            with open('devices.json', 'w') as fp:
                json.dump(devices, fp)

            return render_template('add.html', success=True, device=str(form.device.data))

    elif request.method == 'GET':
        return render_template('add.html', form=form)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

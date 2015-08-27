# -*- coding: iso-8859-1 -*-
from flask import Flask, render_template, request, flash
from forms import AddForm
import shelve

app = Flask(__name__)
app.secret_key = 'energy key'

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/adddevice', methods=['GET', 'POST'])
def adddevice():
    form = AddForm()

    # Eingabe
    if request.method == 'POST':
        # Fehler
        if form.validate() == False:
            flash('Error, validation faild.')
            return render_template('add.html', form=form)

        # Rückgabe + Speichern
        else:
            device = eval(form.device.data)
            energy = eval(form.energyusage.data)
            hours = eval(form.hoursperweek.data)
            sh = shelve.open("devices.slv", flag="c")
            sh[device] = {'energy': energy, 'hours': hours}
            sh.close()

            return render_template('add.html', success=True, device=device)

    elif request.method == 'GET':
        return render_template('add.html', form=form)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

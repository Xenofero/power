# -*- coding: iso-8859-1 -*-
import json
import ldap

from flask import Flask, render_template, request, flash
from forms import AddForm

#start flask
app = Flask(__name__)
app.secret_key = 'energy key'

#start ldap
ld = ldap.initialize('ldap://localhost')
user = "root"
password = "290992alex"
ld.simple_bind(user, password)
result_set = []

#search ldap
basedn = "ou=devices,dc=energy,dc=net"
scope = ldap.SCOPE_SUBTREE
filter = "cn=" + "*"
retrieve_attributes = ["*"]
timeout = 0
result_set = []


@app.route('/')
def home():


#   try:
#    with open("devices.json", 'r') as fp:
#        jsondata = json.load(fp)
#        print jsondata
#    except:
#        print 'no Devices'


    result_id=ld.search(basedn, scope, filter)
    result_type, result_data = ld.result(result_id, timeout)

    print(result_data)
    print(result_id)
    return render_template('home.html', data="")


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
#        else:
#            with open('devices.json') as fp:
#                devices = json.load(fp)
#            print 'JSON', json.dumps(devices)
#
#            devices.append({"name": str(form.device.data), "energy": str(form.energyusage.data), "hours": str(form.hoursperweek.data)})
#            with open('devices.json', 'w') as fp:
#                json.dump(devices, fp)

#            return render_template('add.html', success=True, device=str(form.device.data))

    elif request.method == 'GET':
        return render_template('add.html', form=form)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

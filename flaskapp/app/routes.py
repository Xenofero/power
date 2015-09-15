# -*- coding: iso-8859-1 -*-
import ldap
from flask import Flask, render_template, request, flash
from forms import AddForm

# start flask
app = Flask(__name__)
app.secret_key = 'energy key'

# start ldap
def ldap_search(filter):
    ld = ldap.initialize('ldap://localhost')
    user = "root"
    password = "290992alex"
    ld.simple_bind(user, password)

    basedn = "ou=Devices,dc=energy,dc=net"
    scope = ldap.SCOPE_SUBTREE

    # LDAP Suche
    result_id = ld.search(basedn, scope, filter)

    # Ergebnis einholen
    result_set = []
    while 1:
        result_type, result_data = ld.result(result_id, 0)
        if (result_data == []):
            break
        else:
            if result_type == ldap.RES_SEARCH_ENTRY:
                result_set.append(result_data)
    return result_set


def ldap_mod(dn, attr, value):
    ld = ldap.initialize('ldap://localhost')
    user = "root"
    password = "290992alex"
    ld.simple_bind(user, password)

    modlist = ['ldap.MOD_REPLACE', attr, value]

    # LDAP Suche
    result_id = ld.modify(dn, modlist)

    # Ergebnis einholen
    result_set = []
    while 1:
        result_type, result_data = ld.result(result_id, 0)
        if (result_data == []):
            break
        else:
            if result_type == ldap.RES_MODIFY:
                result_set.append(result_data)
    return result_set


@app.route('/')
def home():
    #   try:
    #    with open("devices.json", 'r') as fp:
    #        jsondata = json.load(fp)
    #        print jsondata
    #    except:.de
    #        print 'no Devices'

    vms = ldap_search("(objectClass=vm)")
    sn = (vms[0][0][1]["servername"][0])
    dn = "servername=%s,ou=Devices,dc=energy,dc=net" % sn
    print(dn)
    return render_template('home.html', data=vms)


@app.route('/adddevice', methods=['GET', 'POST'])
def adddevice():
    form = AddForm()

    # Eingabe
    if request.method == 'GET':
        # get args from home
        if request.args.get('servername'):
            sn = request.args.get('servername')
            print(sn)
            dn = "(servername=%s)" % sn
            print(dn)
            vms = ldap_search(dn)
            print(vms)

            form.servername.data = (vms[0][0][1]["servername"][0])
            form.internalname.data = (vms[0][0][1]["internalname"][0])
            form.mainresponsible.data = (vms[0][0][1]["mainresponsible"][0])
            form.substitute.data = (vms[0][0][1]["substitute"][0])
            form.costcenter.data = (int(vms[0][0][1]["costcenter"][0]))
            form.location.data = (vms[0][0][1]["location"][0])
            form.department.data = (vms[0][0][1]["department"][0])
            form.servertype.data = bool(vms[0][0][1]["servertype"][0])
            form.serverdescription.data = (vms[0][0][1]["serverdescription"][0])
            form.serverservice.data = (vms[0][0][1]["serverservice"][0])
            form.workloadservice.data = int(vms[0][0][1]["workloadservice"][0])
            form.workloadintime.data = (vms[0][0][1]["workloadintime"][0])
            form.privacyrelatedfiles.data = bool(vms[0][0][1]["privacyrelatedfiles"][0])
            form.dependencies.data = (vms[0][0][1]["dependencies"][0])
            form.redundancy.data = (vms[0][0][1]["redundancy"][0])
            form.bootorder.data = (vms[0][0][1]["bootorder"][0])
            form.impactforotherserver.data = (vms[0][0][1]["impactforotherserver"][0])
            form.departmentaffected.data = (vms[0][0][1]["departmentaffected"][0])
            form.furtherwork.data = bool(vms[0][0][1]["furtherwork"][0])
            form.cost.data = float(vms[0][0][1]["cost"][0])
            form.serviceaccount.data = (vms[0][0][1]["serviceaccount"][0])
            form.purposeaccount.data = (vms[0][0][1]["purposeaccount"][0])
            form.manuallyrestart.data = (vms[0][0][1]["manuallyrestart"][0])
            form.otherinformation.data = (vms[0][0][1]["otherinformation"][0])
            return render_template('add.html', form=form)
        else:
            return render_template('add.html', form=form)

    elif request.method == 'POST':
        # Fehler
        if not form.validate():
            flash('Error, validation faild.')
            return render_template('add.html', form=form)
        else:
            print (form.servername.data)
            return render_template('add.html', form=form)

            # Rückgabe + Speichern


# else:
#            with open('devices.json') as fp:
#                devices = json.load(fp)
#            print 'JSON', json.dumps(devices)
#
#            devices.append({"name": str(form.device.data), "energy": str(form.energyusage.data), "hours": str(form.hoursperweek.data)})
#            with open('devices.json', 'w') as fp:
#                json.dump(devices, fp)

#            return render_template('add.html', success=True, device=str(form.device.data))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

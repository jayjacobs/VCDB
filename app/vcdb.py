from flask import Flask, render_template, request, redirect, url_for
import json,uuid
vcdb = Flask(__name__)

@vcdb.route('/', methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        options = ["theft_physical",
                "tampering_physical",
                "loss_error",
                "publishing_error_error",
                "misdelivery_error",
                "disposal_error_error",
                "privilege_abuse_misuse",
                "embezzlement_misuse",
                "dos_hacking",
                "intrusion_hacking",
                "malware_malware",
                "long_form"]
        if request.form['which_form'] in options:
            return redirect(url_for(request.form['which_form']))
        else:
            return "invalid form selection"

@vcdb.route('/test')
def test():
    return render_template('temp.html')

@vcdb.route('/theft_physical', methods=['GET','POST'])
def theft_physical():
  if request.method == "GET":
    return render_template('theft_physical.html')
  else:
    id = str(uuid.uuid4()).upper()
    incident = {'schema_version':'1.2',
                'source_id':'osint',
                'incident_id' : id }
    incident['security_incident'] = request.form['security_incident']
    incident['summary'] = request.form['summary']
    incident['action'] = {'physical' : {'location':[request.form['location']],
                                        'variety':['Theft'],
                                        'vector' : ['Disabled controls'] } }
    incident['discovery_method'] = request.form['discovery_method']
    incident['actor'] = short_actor_object(request.form)
    incident['timeline'] = short_timeline_object(request.form)

    return json.dumps(incident,indent=2, sort_keys=True, separators=(',', ': '))

@vcdb.route('/tampering_physical')
def tampering_physical():
    return "tampering physical"

@vcdb.route('/loss_error')
def loss_error():
    return "loss error"

@vcdb.route('/publishing_error_error')
def publishing_error_error():
    return "Publishing Error (Error)"

@vcdb.route('/misdelivery_error')
def misdelivery_error():
    return "Misdelivery (Error)"

@vcdb.route('/disposal_error_error')
def disposal_error_error():
    return "Disposal error (Error)"

@vcdb.route('/privilege_abuse_misuse')
def privilege_abuse_misuse():
    return "Privilege abuse (Misuse)"

@vcdb.route('/embezzlement_misuse')
def embezzlement_misuse():
    return "Embezzlement (Misuse)"

@vcdb.route('/dos_hacking')
def dos_hacking():
    return "Denial of Service (Hacking)"

@vcdb.route('/intrusion_hacking')
def intrusion_hacking():
    return "Intrusion (Hacking)"

@vcdb.route('/malware_malware')
def malware_malware():
    return "Malware (Malware)"

@vcdb.route('/long_form')
def long_form():
    return "Seriously? Do I really need to make a long form?"

def short_actor_object(inDict):
  actor = {}
  if inDict['actor_variety'].startswith('e_'):
    actor['external'] = {'variety' : inDict['actor_variety'][2:]}
  if inDict['actor_variety'].startswith('i_'):
    actor['internal'] = {'variety' : inDict['actor_variety'][2:]}
  return actor

def short_timeline_object(inDict):
  timeline = {'compromise' : { 'year' : int(inDict['compromise_year']) } }
  if inDict['compromise_month'] != '':
    timeline['compromise']['month'] = int(inDict['compromise_month'])
  if inDict['compromise_day'] != '':
    timeline['compromise']['day'] = int(inDict['compromise_day'])
  return timeline



if __name__ == "__main__":
    vcdb.run(debug=True, host="0.0.0.0",port=3000)

import uuid
from datetime import datetime
import json

def short_stolen_laptop(i):
  incident_guid = str(uuid.uuid4()).upper()
  o = {'schema_version':'1.2.1',
       'action': {'physical' : {'variety' : ['Theft'] } },
       'actor' : {'external' : {'motive' : ['Financial'] } },
       'asset' : {'assets' : [{'variety': 'U - Laptop'}],
                  'ownership' : 'Victim'},
       'attribute' : {'availability' : {'variety':['Loss']},
                      'confidentiality' : {'data_disclosure':'Potentially'}},
       'impact' : {'overall_rating': 'Unknown'},
       'incident_id' : incident_guid,
       'plus' : { 'analysis_status' : 'First pass',
                  'created' : datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),
                  'master_id' : incident_guid },
       'security_incident' : 'Confirmed',
       'source_id' : 'vcdb' }
  # Fill in some of the root values for the incident. Only include if there is a value present
  for key in ['summary','security_incident','notes','discovery_method']:
    if i[key] != '':
      o[key] = i[key]
  
  o['timeline'] = get_incident_timeline(i)
  o['plus']['timeline'] = get_notification_date(i)
  o['reference'] = get_source_string(i)
  o['victim'] = get_victim(i)
      
  return make_pretty(o)

def get_victim(i):
  o = {}
  secondary = {}
  for key in ['victim_id','country','employee_count','state']:
    if key in i.keys() and i[key] != '':
      o[key] = i[key]
  if 'revenue' in i.keys() and i['revenue'] != '':
    if 'iso_currency_code' in i.keys() and i['iso_currency_code'] != '':
      o['revenue'] = {'amount': int(i['revenue']),'iso_currency_code':i['iso_currency_code']}
  if 'industry' in i.keys() and i['industry'] != '':
    o['industry'] = int(i['industry'])
  if 'victim_notes' in i.keys() and i['victim_notes'] != '':
    o['notes'] = i['victim_notes']
  
  if "secondary_victim_count" in i.keys() and i["secondary_victim_count"] != '':
    try:
      secondary['amount'] = int(i["secondary_victim_count"])
    except:
      next
  if "secondary_victim_ids" in i.keys() and i["secondary_victim_ids"] != '':
    if "secondary_victim_delim" in i.keys() and i["secondary_victim_delim"] != '':
      try:
        if i['secondary_victim_delim'] == 'newline':
          secondary['victim_id'] = i['secondary_victim_ids'].splitlines()
        else:
          secondary['victim_id'] = i['secondary_victim_ids'].split(i['secondary_victim_delim'])
      except:
        next
  if "secondary_victim_notes" in i.keys() and i["secondary_victim_notes"] != '':
    secondary['notes'] = i["secondary_victim_notes"]
  
  if len(secondary.keys()) > 0:
    o['secondary'] = secondary
  return o

def get_incident_timeline(i):
  o = {'incident' : {'year' : int(i['compromise_year']) }}
  if i['compromise_month'] != '' : o['incident']['month'] = int(i['compromise_month'])
  if i['compromise_day'] != '' : o['incident']['day'] = int(i['compromise_day'])
  return o

def get_notification_date(i):
  o = {'year': int(i['disclosure_year'])}
  if i['discovery_month'] != '': o['month'] = int(i['discovery_month'])
  if i['discovery_day'] != '': o['year'] = int(i['discovery_year'])
  return o

def get_source_string(i):
  s = ''
  for x in range(int(i['source_count'])):
    fieldcount = str(x + 1)
    s += i[fieldcount+'_source_url'] + ' (' + i[fieldcount+'_source_retrieved'] + ')'
    if int(x + 1) < int(i['source_count']):
      s += ';'
  return s
    

  
def make_pretty(i):
  o = json.dumps(i,indent=2, sort_keys=True, separators=(',', ': '))
  o = o.replace(' ', '&nbsp;')
  o = o.replace('\n', '<br />')
  return o
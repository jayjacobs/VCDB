import uuid
from datetime import datetime
import json

def short_stolen_laptop(i):
  incident_guid = str(uuid.uuid4()).upper()
  o = {'schema_version':'1.2',
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
      
  return make_pretty(o)

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

  
def make_pretty(i):
  o = json.dumps(i,indent=2, sort_keys=True, separators=(',', ': '))
  o = o.replace(' ', '&nbsp;')
  o = o.replace('\n', '<br />')
  return o
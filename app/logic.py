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
  for key in ['summary','security_incident','notes','discovery_method']:
    if i[key] != '':
      o[key] = i[key]
      
  return make_pretty(o)
                                           
def make_pretty(i):
  o = json.dumps(i,indent=2, sort_keys=True, separators=(',', ': '))
  o = o.replace(' ', '&nbsp;')
  o = o.replace('\n', '<br />')
  return o
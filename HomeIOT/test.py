import json
IOTask = dict(Type="Photo",Host="43ersf",Len="0",Upload="0")
print json.dumps(IOTask)

import requests

url = "http://localhost/HomeIOT/IOTAPI.php"
tp = 'Sound'
files = {'File': open('ben.wav', 'rb')}
r = requests.post(url, files=files,data={'Type':'Sound'})
print r.text
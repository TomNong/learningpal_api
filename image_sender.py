import requests
import json, time


IMG_NAME = "single_equation.png"

tic = time.time()

url = 'http://api.learningpal.com/math/upload'
files = {'file': open('./' + IMG_NAME, 'rb')}
headers = {'content-type': 'application/json'}

try:
  r = requests.post(url, files=files)
  print r.text
  response = json.loads(r.text)
  task_ID = response['task_ID']
  payload = {'task_ID' : task_ID, 'password' : ""}
  url2 = 'http://api.learningpal.com/math/result'
  while True:
    response = requests.post(url2, data=json.dumps(payload), headers=headers)
    print response.text
    if response.text and "processing" not in response.text:
    	break
except Exception as e :
	print e
print 'total time cost: ', time.time()-tic
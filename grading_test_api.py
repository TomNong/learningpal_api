import requests
import json
from time import sleep
import multiprocessing

IMG_NAMES = ["math_hw.jpg"]
#input image

def worker(IMG_NAME):
  try:
    url = "http://34.234.219.245:8500/upload_for_grading"
    files = {'file': open('./' + IMG_NAME, 'rb')}
    headers = {'content-type': 'application/json','Connection':'close'}
    r = requests.post(url, files=files)
    print r.text
    response = json.loads(r.text)
    task_ID = response['task_ID']
    payload = {'task_ID' : task_ID, 'password' : ""}
    url2 = 'http://34.234.219.245:8500/result'
    while True:
      response = requests.post(url2, data=json.dumps(payload), headers=headers)
      print response.text
      if response.text and "processing" not in response.text:
      	break
      sleep(2)
  except Exception as e :
  	print e

if __name__ == '__main__':
    jobs = []
    for i in IMG_NAMES:
        p = multiprocessing.Process(target=worker, args=(i,))
        jobs.append(p)
        p.start()

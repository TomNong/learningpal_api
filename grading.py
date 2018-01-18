import requests, json, sys 
import time

def worker(IMG_NAME):
    
    try:
        url = "http://api.learningpal.com:12500/upload_for_grading"
        files = {'file': open('./' + IMG_NAME, 'rb')}
        headers = {'content-type': 'application/json','Connection':'close', 'Cache-Control': 'no-cache'}
        r = requests.post(url, files=files)
        response1 = json.loads(r.text)
        task_ID = response1['task_ID']
        payload = {'task_ID' : task_ID, 'password' : ""}
        url2 = 'http://api.learningpal.com:12500/result'
        while True:
            response2 = requests.post(url2, data=json.dumps(payload), headers=headers)
            result = json.loads(response2.text)
            if result['isResult'] == 'true':
                break
            time.sleep(2)
            print 'Job is running...'
        return result
    except Exception as e :
        print 'except: ', e
        

def main(arg):
    print 'Job started...'
    tic = time.time()
    result = worker(arg)
    print result
    print 'Done! Time cost: ', str(time.time() - tic), 's'
        
if __name__=="__main__":
    main(sys.argv[1])
This repository includes:
  1. Handwritten math equation recognition API
  2. Math equation detection in a single image API
  3. Using above two API to achieve problem sheet auto grading

## For Usage of Handwritten math equation recognition API
You can use provided image to test.
If you want to change the image for testing, please replace the IMG_NAME in image_sender.py to the image that you put in the same directory.

### Dependency
```
pip install requests 
pip install json 
```

### Example

![alt text](https://github.com/TomNong/learningpal_api/blob/master/single_equation.png?raw=true)

```
python image_sender.py 
```
###### Output:
```
u'{"confidence": 0.9945661408039893, "isResult": "true", "result": "( 3 - x ) ( x - 2 ) = 0 "}'
```

Replace handwritten images as you like

note: image resize to height of 50 pixs is recommended

## For Usage of Math equation detection in a single image API
### Example
```
python run_imgApi.py
```
###### Output 
returns a list of [(x1,y1),(x2,y2)] box location coordinates

## For Problem Sheet Auto Grading
### Example
Testing on problem sheet image
![alt text](https://github.com/TomNong/learningpal_api/blob/master/homework.png?raw=true)
```
python recognize_hw.py homework.png
```
###### Output
The program draws boxes on detected math equtions on image, and put recognized text on the image, and output as result.png

![alt text](https://github.com/TomNong/learningpal_api/blob/master/result.png?raw=true)




# Update

![alt text](https://github.com/TomNong/learningpal_api/blob/master/math_hw.jpg?raw=true)


```
python grading.py math_hw.jpg
```
###### Output
```
Job started...
Job is running...
Job is running...
{u'isResult': u'true', u'results': [{u'confidence': 0.00574633688848334, u'isResult': u'true', u'result': u'Cannot \\  Recognize'}, {u'confidence': 0.00897819667315922, u'isResult': u'true', u'result': u'Cannot \\  Recognize'}, {u'confidence': 0.9784829496953737, u'isResult': u'true', u'result': u'( 2 ) '}, {u'confidence': 0.027648474982502023, u'isResult': u'true', u'result': u'Cannot \\  Recognize'}, {u'confidence': 0.01256038298277226, u'isResult': u'true', u'result': u'Cannot \\  Recognize'}, {u'confidence': 0.004918819152335317, u'isResult': u'true', u'result': u'Cannot \\  Recognize'}, {u'confidence': 0.0018917184502535499, u'isResult': u'true', u'result': u'Cannot \\  Recognize'}, {u'confidence': 0.9931954289869299, u'isResult': u'true', u'result': u'76 - 73 = 3 '}, {u'confidence': 0.9847410986113392, u'isResult': u'true', u'result': u'35 - 18 = 17 '}, {u'confidence': 1.1978180419593693e-08, u'isResult': u'true', u'result': u'Cannot \\  Recognize'}, {u'confidence': 0.00023705643007372137, u'isResult': u'true', u'result': u'Cannot \\  Recognize'}, {u'confidence': 0.9985613058095822, u'isResult': u'true', u'result': u'26 - 17 = 9 '}, {u'confidence': 0.9510795200898753, u'isResult': u'true', u'result': u'24 \\\\ d i v 4 = 6 '}, {u'confidence': 0.0007779687133725073, u'isResult': u'true', u'result': u'Cannot \\  Recognize'}, {u'confidence': 0.9506764398590967, u'isResult': u'true', u'result': u'48 \\\\ d i v 8 = 6 '}, {u'confidence': 0.9993689522797068, u'isResult': u'true', u'result': u'49 - 36 = 13 '}, {u'isResult': u'false', u'result': u'String processing...'}, {u'confidence': 0.4668459777221712, u'isResult': u'true', u'result': u'41 '}, {u'confidence': 0.9937675746672069, u'isResult': u'true', u'result': u'39 = 2 '}, {u'confidence': 0.9952693280702007, u'isResult': u'true', u'result': u'75 - 37 = 38 '}, {u'confidence': 2.257532659550509e-05, u'isResult': u'true', u'result': u'Cannot \\  Recognize'}, {u'confidence': 0.9973386086691871, u'isResult': u'true', u'result': u'38 - 32 = 6 '}, {u'confidence': 0.9640367808988001, u'isResult': u'true', u'result': u'56 + 42 = 98 '}, {u'confidence': 0.0025596210506983875, u'isResult': u'true', u'result': u'Cannot \\  Recognize'}, {u'confidence': 0.984718097021143, u'isResult': u'true', u'result': u'= 8 '}, {u'confidence': 0.9752830533696045, u'isResult': u'true', u'result': u'4 \\\\ t i m E s 2 '}, {u'confidence': 0.9907734651147534, u'isResult': u'true', u'result': u'87 + 11 = 98 '}, {u'confidence': 0.06277499660000882, u'isResult': u'true', u'result': u'( ) 53 \\sqrt [ 3 ] \\\\ d i '}, {u'confidence': 0.47555019478999544, u'isResult': u'true', u'result': u'5 \\\\ d i v 0 '}, {u'confidence': 0.9991213613005578, u'isResult': u'true', u'result': u'50 - 39 = 11 '}, {u'confidence': 0.710929131848033, u'isResult': u'true', u'result': u'83 + 14 = 97 '}, {u'confidence': 0.002265816535225978, u'isResult': u'true', u'result': u'Cannot \\  Recognize'}, {u'confidence': 0.983497318725131, u'isResult': u'true', u'result': u'15 \\\\ d i v 5 = 3 '}, {u'confidence': 0.9905513095204472, u'isResult': u'true', u'result': u'38 + 27 = 65 '}, {u'isResult': u'false', u'result': u'String processing...'}, {u'confidence': 0.9974486537696098, u'isResult': u'true', u'result': u'7 + 47 = 54 '}, {u'confidence': 0.9926402668342426, u'isResult': u'true', u'result': u'45 + 33 = 78 '}, {u'confidence': 0.004448260038905954, u'isResult': u'true', u'result': u'Cannot \\  Recognize'}, {u'confidence': 0.972875351698463, u'isResult': u'true', u'result': u'16 \\\\ d i v 4 = '}, {u'confidence': 0.9863698310335083, u'isResult': u'true', u'result': u'26 + 61 = 87 '}, {u'confidence': 6.579742272436218e-05, u'isResult': u'true', u'result': u'Cannot \\  Recognize'}, {u'confidence': 0.9823899451928392, u'isResult': u'true', u'result': u'68 - 68 = 0 '}, {u'confidence': 0.9808191664305614, u'isResult': u'true', u'result': u'52 + 20 = 72 '}, {u'confidence': 1.1251694500495151e-05, u'isResult': u'true', u'result': u'Cannot \\  Recognize'}, {u'confidence': 0.6912176815148366, u'isResult': u'true', u'result': u'78 + 16 = - 94 '}, {u'confidence': 0.9758130605400334, u'isResult': u'true', u'result': u'20 \\\\ d i v 4 = 5 '}, {u'confidence': 0.00020558492499407212, u'isResult': u'true', u'result': u'Cannot \\  Recognize'}, {u'confidence': 0.9987317203625146, u'isResult': u'true', u'result': u'13 = 20 '}, {u'confidence': 0.942043327758047, u'isResult': u'true', u'result': u'33 - '}, {u'confidence': 0.9995634609787384, u'isResult': u'true', u'result': u'34 + 46 = 80 '}, {u'confidence': 0.011076631413906118, u'isResult': u'true', u'result': u'Cannot \\  Recognize'}, {u'confidence': 0.984851977796358, u'isResult': u'true', u'result': u'15 \\\\ d i v 3 = 5 '}, {u'confidence': 0.9900257017865656, u'isResult': u'true', u'result': u'53 + 44 = 97 '}, {u'confidence': 0.24086583804698575, u'isResult': u'true', u'result': u'1 \\\\ t i m E s E '}, {u'confidence': 0.013693753330909652, u'isResult': u'true', u'result': u'Cannot \\  Recognize'}, {u'confidence': 0.9896972051404731, u'isResult': u'true', u'result': u'70 - 40 = 30 '}, {u'confidence': 0.966196426583856, u'isResult': u'true', u'result': u'62 + 31 = 93 '}, {u'isResult': u'false', u'result': u'String processing...'}, {u'confidence': 0.5135501345319009, u'isResult': u'true', u'result': u'5 \\\\ t i m E s 3 = 150 '}, {u'confidence': 0.9403108530487667, u'isResult': u'true', u'result': u'68 - 13 = 55 '}, {u'confidence': 0.9882512094491266, u'isResult': u'true', u'result': u'39 + 18 = 57 '}, {u'confidence': 0.008456246809765635, u'isResult': u'true', u'result': u'Cannot \\  Recognize'}, {u'confidence': 0.9991272380061389, u'isResult': u'true', u'result': u'37 - 25 = 12 '}, {u'confidence': 0.9639662512592992, u'isResult': u'true', u'result': u'36 \\\\ d i v 6 = 6 '}, {u'isResult': u'false', u'result': u'String processing...'}, {u'confidence': 0.9958013189796098, u'isResult': u'true', u'result': u'16 + 27 = 43 '}, {u'confidence': 0.0006705592002989899, u'isResult': u'true', u'result': u'Cannot \\  Recognize'}, {u'confidence': 0.0017534201537843267, u'isResult': u'true', u'result': u'Cannot \\  Recognize'}, {u'confidence': 0.0014113089771933343, u'isResult': u'true', u'result': u'Cannot \\  Recognize'}, {u'confidence': 0.047057898518943875, u'isResult': u'true', u'result': u'Cannot \\  Recognize'}, {u'confidence': 0.13967666085026947, u'isResult': u'true', u'result': u'3 \\\\ t i m E s 1150 '}, {u'confidence': 0.24791708536455806, u'isResult': u'true', u'result': u'0.4 '}, {u'confidence': 0.09847655341444271, u'isResult': u'true', u'result': u'\\frac { \\pi } { 28 } '}], u'correctRate': u'None'}
Done! Time cost:  5.243516922 s
```
The result JSON includes all problems in the paper that has been detected and return with prediction_result/coordinate/TrueOrFalse


## API calling guide
#### Swift3.0+
```
import Foundation
let url_str = "http://api.learningpal.com/math/upload"
let headers = ["content-type": "application/json"]
let request = URLRequest(url: NSURL(string: url_str)! as URL)

request.httpMethod = "POST"
for (key, value) in headers {request.addValue(value, forHTTPHeaderField: key)}

var body = NSMutableData()
fname = 'whatevernameyouwant.png'
image_data = UIImageJPEGRepresentation(img, 0.6) //note: img is your image
boundary = "Boundary-\(NSUUID().uuidString)"
body.append("--\(boundary)\r\n".data(using: String.Encoding.utf8)!)
body.append("Content-Disposition:form-data;name=\"\(fname)\"\r\n\r\n".data(using: String.Encoding.utf8)!)
body.append("\(image)\r\n".data(using: String.Encoding.utf8)!)
body.append("--\(boundary)--\r\n".data(using: String.Encoding.utf8)!)

request.httpBody = body as Data

let session = URLSession.shared
let task = session.dataTask(with: request as URLRequest) {
    (data, response, error) in
    guard let _:Data = data, let _:URLResponse = response , error
        == nil else {
            print("error occurs: ", error)
            return
    }
    let response = String(data: data!, encoding: String.Encoding(rawValue: String.Encoding.utf8.rawValue))
}
task.resume()
```

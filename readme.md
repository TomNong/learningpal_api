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
  {u'isResult': u'true', u'results': {u'reslist': [{u'confidence': 0.019415429848789783, u'task_ID': u'1516087358.74math_hw.jpg', u'label': 0, u'trueOrFalse': None, u'result': u'Cannot \\  Recognize', u'rightAnswer': None, u'coordinate': {u'y': 1424, u'x': 470, u'w': 81, u'h': 20}}, {u'confidence': 0.12879710976079153, u'task_ID': u'1516087358.74math_hw.jpg', u'label': 2, u'trueOrFalse': None, u'result': u'( 2 - 3  )', u'rightAnswer': None, u'coordinate': {u'y': 1380, u'x': 398, u'w': 65, u'h': 33}}, {u'confidence': 0.07037404212939267, u'task_ID': u'1516087358.74math_hw.jpg', u'label': 4, u'trueOrFalse': False, u'result': u'x _ { x } = + \\complement _ { 1 } ', u'rightAnswer': None, u'coordinate': {u'y': 1336, u'x': 111, u'w': 115, u'h': 48}}, {u'confidence': 0.002750702878951162, u'task_ID': u'1516087358.74math_hw.jpg', u'label': 6, u'trueOrFalse': None, u'result': u'Cannot \\  Recognize', u'rightAnswer': None, u'coordinate': {u'y': 1336, u'x': 664, u'w': 148, u'h': 36}}, {u'confidence': 0.9692670642500351, u'task_ID': u'1516087358.74math_hw.jpg', u'label': 8, u'trueOrFalse': True, u'result': u'35 - 18 = 17 ', u'rightAnswer': None, u'coordinate': {u'y': 1248, u'x': 378, u'w': 199, u'h': 36}}, {u'confidence': 0.008940236283773575, u'task_ID': u'1516087358.74math_hw.jpg', u'label': 10, u'trueOrFalse': None, u'result': u'Cannot \\  Recognize', u'rightAnswer': None, u'coordinate': {u'y': 1243, u'x': 763, u'w': 180, u'h': 40}}, {u'confidence': 0.008854714937935985, u'task_ID': u'1516087358.74math_hw.jpg', u'label': 12, u'trueOrFalse': None, u'result': u'Cannot \\  Recognize', u'rightAnswer': None, u'coordinate': {u'y': 1203, u'x': 377, u'w': 180, u'h': 33}}, {u'confidence': 0.22374146023428293, u'task_ID': u'1516087358.74math_hw.jpg', u'label': 14, u'trueOrFalse': None, u'result': u'48 \\div \\frac { 3 } 8 = 6 ', u'rightAnswer': None, u'coordinate': {u'y': 1152, u'x': 364, u'w': 189, u'h': 41}}, {u'confidence': 3.2934249840282563e-06, u'task_ID': u'1516087358.74math_hw.jpg', u'label': 16, u'trueOrFalse': None, u'result': u'Cannot \\  Recognize', u'rightAnswer': None, u'coordinate': {u'y': 1137, u'x': 658, u'w': 324, u'h': 48}}, {u'confidence': 0.3910402038710861, u'task_ID': u'1516087358.74math_hw.jpg', u'label': 18, u'trueOrFalse': None, u'result': u'3 y = 2 _ { 1 } ', u'rightAnswer': None, u'coordinate': {u'y': 1106, u'x': 457, u'w': 118, u'h': 29}}, {u'confidence': 0.0011199120874650441, u'task_ID': u'1516087358.74math_hw.jpg', u'label': 20, u'trueOrFalse': None, u'result': u'Cannot \\  Recognize', u'rightAnswer': None, u'coordinate': {u'y': 1086, u'x': 671, u'w': 294, u'h': 45}}, {u'confidence': 0.4851600106001797, u'task_ID': u'1516087358.74math_hw.jpg', u'label': 22, u'trueOrFalse': False, u'result': u'56 + 42 = - 18 ', u'rightAnswer': None, u'coordinate': {u'y': 1053, u'x': 82, u'w': 219, u'h': 49}}, {u'confidence': 0.14592352734774572, u'task_ID': u'1516087358.74math_hw.jpg', u'label': 24, u'trueOrFalse': None, u'result': u'= 8 s ', u'rightAnswer': None, u'coordinate': {u'y': 1009, u'x': 474, u'w': 72, u'h': 33}}, {u'confidence': 0.20558660182182484, u'task_ID': u'1516087358.74math_hw.jpg', u'label': 26, u'trueOrFalse': True, u'result': u'87 + 11 = 98 ', u'rightAnswer': None, u'coordinate': {u'y': 1004, u'x': 77, u'w': 217, u'h': 48}}, {u'confidence': 0.13377748924602073, u'task_ID': u'1516087358.74math_hw.jpg', u'label': 28, u'trueOrFalse': None, u'result': u'5 \\div E ', u'rightAnswer': None, u'coordinate': {u'y': 987, u'x': 674, u'w': 96, u'h': 33}}, {u'confidence': 0.8673192673179964, u'task_ID': u'1516087358.74math_hw.jpg', u'label': 30, u'trueOrFalse': False, u'result': u'83 + x = 97 ', u'rightAnswer': None, u'coordinate': {u'y': 956, u'x': 376, u'w': 204, u'h': 37}}, {u'confidence': 0.7655359132171398, u'task_ID': u'1516087358.74math_hw.jpg', u'label': 32, u'trueOrFalse': True, u'result': u'15 \\div 5 = 3 ', u'rightAnswer': None, u'coordinate': {u'y': 911, u'x': 382, u'w': 175, u'h': 37}}, {u'confidence': 0.7732808935186332, u'task_ID': u'1516087358.74math_hw.jpg', u'label': 35, u'trueOrFalse': True, u'result': u'7 + 47 = 54 ', u'rightAnswer': None, u'coordinate': {u'y': 859, u'x': 373, u'w': 204, u'h': 48}}, {u'confidence': 6.272466286344822e-05, u'task_ID': u'1516087358.74math_hw.jpg', u'label': 37, u'trueOrFalse': None, u'result': u'Cannot \\  Recognize', u'rightAnswer': None, u'coordinate': {u'y': 829, u'x': 688, u'w': 302, u'h': 44}}, {u'confidence': 0.7338351895858212, u'task_ID': u'1516087358.74math_hw.jpg', u'label': 39, u'trueOrFalse': True, u'result': u'26 + 61 = 87 ', u'rightAnswer': None, u'coordinate': {u'y': 806, u'x': 77, u'w': 205, u'h': 49}}, {u'confidence': 0.1290447224362987, u'task_ID': u'1516087358.74math_hw.jpg', u'label': 41, u'trueOrFalse': None, u'result': u'1 x \\in ( 0  )', u'rightAnswer': None, u'coordinate': {u'y': 777, u'x': 683, u'w': 90, u'h': 40}}, {u'confidence': 0.4123122241963585, u'task_ID': u'1516087358.74math_hw.jpg', u'label': 43, u'trueOrFalse': False, u'result': u'52 + 2 v = 72 ', u'rightAnswer': None, u'coordinate': {u'y': 756, u'x': 374, u'w': 212, u'h': 45}}, {u'confidence': 0.6958783907647862, u'task_ID': u'1516087358.74math_hw.jpg', u'label': 45, u'trueOrFalse': True, u'result': u'78 + 16 = 94 ', u'rightAnswer': None, u'coordinate': {u'y': 705, u'x': 72, u'w': 215, u'h': 49}}, {u'confidence': 0.5986933177134134, u'task_ID': u'1516087358.74math_hw.jpg', u'label': 48, u'trueOrFalse': False, u'result': u'13 = 20 ', u'rightAnswer': None, u'coordinate': {u'y': 656, u'x': 454, u'w': 135, u'h': 45}}, {u'confidence': 0.6649987572484177, u'task_ID': u'1516087358.74math_hw.jpg', u'label': 50, u'trueOrFalse': False, u'result': u'3 A + 46 = 80 ', u'rightAnswer': None, u'coordinate': {u'y': 655, u'x': 63, u'w': 214, u'h': 40}}, {u'confidence': 0.19547368242361685, u'task_ID': u'1516087358.74math_hw.jpg', u'label': 52, u'trueOrFalse': None, u'result': u'( { 3 } + 3 = 5  )', u'rightAnswer': None, u'coordinate': {u'y': 604, u'x': 381, u'w': 175, u'h': 45}}, {u'confidence': 0.0644034147280596, u'task_ID': u'1516087358.74math_hw.jpg', u'label': 54, u'trueOrFalse': None, u'result': u'3 x ^ { 1 } = (  )', u'rightAnswer': None, u'coordinate': {u'y': 562, u'x': 686, u'w': 92, u'h': 36}}, {u'confidence': 0.8231921696893921, u'task_ID': u'1516087358.74math_hw.jpg', u'label': 56, u'trueOrFalse': True, u'result': u'70 - 40 = 30 ', u'rightAnswer': None, u'coordinate': {u'y': 552, u'x': 373, u'w': 213, u'h': 49}}, {u'confidence': 0.0031733356106470297, u'task_ID': u'1516087358.74math_hw.jpg', u'label': 58, u'trueOrFalse': None, u'result': u'Cannot \\  Recognize', u'rightAnswer': None, u'coordinate': {u'y': 500, u'x': 679, u'w': 251, u'h': 49}}, {u'confidence': 0.11285201552883889, u'task_ID': u'1516087358.74math_hw.jpg', u'label': 60, u'trueOrFalse': False, u'result': u'68 - 13 = 3 \\frac { 4 } { 5 } ', u'rightAnswer': None, u'coordinate': {u'y': 497, u'x': 57, u'w': 230, u'h': 53}}, {u'confidence': 0.02258632085469643, u'task_ID': u'1516087358.74math_hw.jpg', u'label': 62, u'trueOrFalse': None, u'result': u'Cannot \\  Recognize', u'rightAnswer': None, u'coordinate': {u'y': 446, u'x': 681, u'w': 287, u'h': 48}}, {u'confidence': 0.11104015407914974, u'task_ID': u'1516087358.74math_hw.jpg', u'label': 64, u'trueOrFalse': False, u'result': u'36 + 6 = 1 ', u'rightAnswer': None, u'coordinate': {u'y': 395, u'x': 364, u'w': 197, u'h': 45}}, {u'confidence': 0.8826611636675205, u'task_ID': u'1516087358.74math_hw.jpg', u'label': 66, u'trueOrFalse': True, u'result': u'16 + 27 = 43 ', u'rightAnswer': None, u'coordinate': {u'y': 390, u'x': 68, u'w': 209, u'h': 44}}, {u'confidence': 0.0859429298135834, u'task_ID': u'1516087358.74math_hw.jpg', u'label': 68, u'trueOrFalse': None, u'result': u'x ^ { 3 } ( 30 = 0 k  )', u'rightAnswer': None, u'coordinate': {u'y': 294, u'x': 357, u'w': 271, u'h': 88}}, {u'confidence': 0.0002900129006041702, u'task_ID': u'1516087358.74math_hw.jpg', u'label': 70, u'trueOrFalse': None, u'result': u'Cannot \\  Recognize', u'rightAnswer': None, u'coordinate': {u'y': 241, u'x': 852, u'w': 164, u'h': 48}}, {u'confidence': 0.0003956076200337159, u'task_ID': u'1516087358.74math_hw.jpg', u'label': 72, u'trueOrFalse': None, u'result': u'Cannot \\  Recognize', u'rightAnswer': None, u'coordinate': {u'y': 213, u'x': 925, u'w': 93, u'h': 53}}, {u'confidence': 0.006453673492640913, u'task_ID': u'1516087358.74math_hw.jpg', u'label': 1, u'trueOrFalse': None, u'result': u'Cannot \\  Recognize', u'rightAnswer': None, u'coordinate': {u'y': 1388, u'x': 185, u'w': 100, u'h': 33}}, {u'confidence': 0.23031104735980135, u'task_ID': u'1516087358.74math_hw.jpg', u'label': 5, u'trueOrFalse': None, u'result': u'\\frac { x - 2 } { 2 ^ { 2 } } + 16 ', u'rightAnswer': None, u'coordinate': {u'y': 1338, u'x': 372, u'w': 148, u'h': 37}}, {u'confidence': 0.08913369661016518, u'task_ID': u'1516087358.74math_hw.jpg', u'label': 9, u'trueOrFalse': None, u'result': u'( 5.3 ^ { 2 }  )', u'rightAnswer': None, u'coordinate': {u'y': 1247, u'x': 669, u'w': 65, u'h': 28}}, {u'confidence': 9.247203010272063e-05, u'task_ID': u'1516087358.74math_hw.jpg', u'label': 13, u'trueOrFalse': None, u'result': u'Cannot \\  Recognize', u'rightAnswer': None, u'coordinate': {u'y': 1190, u'x': 678, u'w': 250, u'h': 40}}, {u'confidence': 0.3480800815956643, u'task_ID': u'1516087358.74math_hw.jpg', u'label': 17, u'trueOrFalse': None, u'result': u'411 = ', u'rightAnswer': None, u'coordinate': {u'y': 1108, u'x': 374, u'w': 73, u'h': 29}}, {u'confidence': 0.5420381196975973, u'task_ID': u'1516087358.74math_hw.jpg', u'label': 21, u'trueOrFalse': False, u'result': u'38 - 32 = 1 ', u'rightAnswer': None, u'coordinate': {u'y': 1055, u'x': 377, u'w': 200, u'h': 40}}, {u'confidence': 0.2506879213062844, u'task_ID': u'1516087358.74math_hw.jpg', u'label': 25, u'trueOrFalse': False, u'result': u'4 \\cdot x = 2 ', u'rightAnswer': None, u'coordinate': {u'y': 1009, u'x': 374, u'w': 93, u'h': 32}}, {u'confidence': 0.17290915801648624, u'task_ID': u'1516087358.74math_hw.jpg', u'label': 29, u'trueOrFalse': False, u'result': u'5 a - 3 g = 11 ', u'rightAnswer': None, u'coordinate': {u'y': 959, u'x': 69, u'w': 198, u'h': 36}}, {u'confidence': 0.9353383157924062, u'task_ID': u'1516087358.74math_hw.jpg', u'label': 33, u'trueOrFalse': True, u'result': u'38 + 27 = 65 ', u'rightAnswer': None, u'coordinate': {u'y': 909, u'x': 77, u'w': 213, u'h': 40}}, {u'confidence': 0.29296845167444435, u'task_ID': u'1516087358.74math_hw.jpg', u'label': 36, u'trueOrFalse': True, u'result': u'45 + 33 = 78 ', u'rightAnswer': None, u'coordinate': {u'y': 859, u'x': 73, u'w': 215, u'h': 45}}, {u'confidence': 0.002273282143695387, u'task_ID': u'1516087358.74math_hw.jpg', u'label': 40, u'trueOrFalse': None, u'result': u'Cannot \\  Recognize', u'rightAnswer': None, u'coordinate': {u'y': 779, u'x': 794, u'w': 162, u'h': 37}}, {u'confidence': 0.0011670951563493817, u'task_ID': u'1516087358.74math_hw.jpg', u'label': 44, u'trueOrFalse': None, u'result': u'Cannot \\  Recognize', u'rightAnswer': None, u'coordinate': {u'y': 719, u'x': 677, u'w': 277, u'h': 44}}, {u'confidence': 0.0007094001904640711, u'task_ID': u'1516087358.74math_hw.jpg', u'label': 47, u'trueOrFalse': None, u'result': u'Cannot \\  Recognize', u'rightAnswer': None, u'coordinate': {u'y': 665, u'x': 676, u'w': 282, u'h': 48}}, {u'confidence': 0.06804963320870153, u'task_ID': u'1516087358.74math_hw.jpg', u'label': 51, u'trueOrFalse': None, u'result': u'1 x ^ { k } 55 ( - 3 ) 1 x ', u'rightAnswer': None, u'coordinate': {u'y': 616, u'x': 685, u'w': 294, u'h': 37}}, {u'confidence': 0.034988523557696376, u'task_ID': u'1516087358.74math_hw.jpg', u'label': 55, u'trueOrFalse': None, u'result': u'Cannot \\  Recognize', u'rightAnswer': None, u'coordinate': {u'y': 561, u'x': 799, u'w': 132, u'h': 37}}, {u'confidence': 0.2680886964540815, u'task_ID': u'1516087358.74math_hw.jpg', u'label': 59, u'trueOrFalse': False, u'result': u'5 x \\cdot 3 = 15 ', u'rightAnswer': None, u'coordinate': {u'y': 500, u'x': 372, u'w': 175, u'h': 44}}, {u'confidence': 0.35415268006313394, u'task_ID': u'1516087358.74math_hw.jpg', u'label': 63, u'trueOrFalse': True, u'result': u'37 - 25 = 12 ', u'rightAnswer': None, u'coordinate': {u'y': 445, u'x': 65, u'w': 207, u'h': 44}}, {u'confidence': 0.015535661079890442, u'task_ID': u'1516087358.74math_hw.jpg', u'label': 67, u'trueOrFalse': None, u'result': u'Cannot \\  Recognize', u'rightAnswer': None, u'coordinate': {u'y': 295, u'x': 665, u'w': 261, u'h': 85}}, {u'confidence': 0.9708450431327549, u'task_ID': u'1516087358.74math_hw.jpg', u'label': 71, u'trueOrFalse': None, u'result': u'3 ', u'rightAnswer': None, u'coordinate': {u'y': 222, u'x': 733, u'w': 158, u'h': 36}}, {u'confidence': 0.027358054195381894, u'task_ID': u'1516087358.74math_hw.jpg', u'label': 3, u'trueOrFalse': None, u'result': u'Cannot \\  Recognize', u'rightAnswer': None, u'coordinate': {u'y': 1372, u'x': 481, u'w': 117, u'h': 56}}, {u'confidence': 0.7851901630455339, u'task_ID': u'1516087358.74math_hw.jpg', u'label': 11, u'trueOrFalse': True, u'result': u'26 - 17 = 9 ', u'rightAnswer': None, u'coordinate': {u'y': 1201, u'x': 96, u'w': 179, u'h': 44}}, {u'confidence': 0.5190084167312707, u'task_ID': u'1516087358.74math_hw.jpg', u'label': 19, u'trueOrFalse': True, u'result': u'75 - 37 = 38 ', u'rightAnswer': None, u'coordinate': {u'y': 1102, u'x': 79, u'w': 218, u'h': 45}}, {u'confidence': 0.008811800480136774, u'task_ID': u'1516087358.74math_hw.jpg', u'label': 27, u'trueOrFalse': None, u'result': u'Cannot \\  Recognize', u'rightAnswer': None, u'coordinate': {u'y': 987, u'x': 785, u'w': 148, u'h': 36}}, {u'confidence': 2.6715305095806415e-05, u'task_ID': u'1516087358.74math_hw.jpg', u'label': 34, u'trueOrFalse': None, u'result': u'Cannot \\  Recognize', u'rightAnswer': None, u'coordinate': {u'y': 882, u'x': 675, u'w': 280, u'h': 45}}, {u'confidence': 0.9686808158914612, u'task_ID': u'1516087358.74math_hw.jpg', u'label': 42, u'trueOrFalse': True, u'result': u'68 - 68 = 0 ', u'rightAnswer': None, u'coordinate': {u'y': 761, u'x': 76, u'w': 190, u'h': 36}}, {u'confidence': 0.019210292523986986, u'task_ID': u'1516087358.74math_hw.jpg', u'label': 49, u'trueOrFalse': None, u'result': u'Cannot \\  Recognize', u'rightAnswer': None, u'coordinate': {u'y': 658, u'x': 376, u'w': 77, u'h': 32}}, {u'confidence': 0.23405496904189363, u'task_ID': u'1516087358.74math_hw.jpg', u'label': 57, u'trueOrFalse': False, u'result': u'62 + 31 = x ^ { 3 } ', u'rightAnswer': None, u'coordinate': {u'y': 546, u'x': 65, u'w': 212, u'h': 60}}, {u'confidence': 0.04474432990611704, u'task_ID': u'1516087358.74math_hw.jpg', u'label': 65, u'trueOrFalse': None, u'result': u'Cannot \\  Recognize', u'rightAnswer': None, u'coordinate': {u'y': 391, u'x': 676, u'w': 208, u'h': 52}}, {u'confidence': 0.003833317030035709, u'task_ID': u'1516087358.74math_hw.jpg', u'label': 73, u'trueOrFalse': None, u'result': u'Cannot \\  Recognize', u'rightAnswer': None, u'coordinate': {u'y': 15, u'x': 1029, u'w': 51, u'h': 85}}, {u'confidence': 0.9484025220379056, u'task_ID': u'1516087358.74math_hw.jpg', u'label': 7, u'trueOrFalse': True, u'result': u'76 - 73 = 3 ', u'rightAnswer': None, u'coordinate': {u'y': 1244, u'x': 84, u'w': 189, u'h': 57}}, {u'confidence': 0.016972418176281524, u'task_ID': u'1516087358.74math_hw.jpg', u'label': 23, u'trueOrFalse': None, u'result': u'Cannot \\  Recognize', u'rightAnswer': None, u'coordinate': {u'y': 1030, u'x': 671, u'w': 239, u'h': 48}}, {u'confidence': 0.02469806955095913, u'task_ID': u'1516087358.74math_hw.jpg', u'label': 38, u'trueOrFalse': None, u'result': u'Cannot \\  Recognize', u'rightAnswer': None, u'coordinate': {u'y': 812, u'x': 382, u'w': 129, u'h': 33}}, {u'confidence': 0.47600703452863224, u'task_ID': u'1516087358.74math_hw.jpg', u'label': 53, u'trueOrFalse': None, u'result': u'[ 53 + 44 = 9 ] ', u'rightAnswer': None, u'coordinate': {u'y': 601, u'x': 68, u'w': 211, u'h': 53}}, {u'confidence': 0.006073618931591045, u'task_ID': u'1516087358.74math_hw.jpg', u'label': 69, u'trueOrFalse': None, u'result': u'Cannot \\  Recognize', u'rightAnswer': None, u'coordinate': {u'y': 290, u'x': 44, u'w': 273, u'h': 89}}, {u'confidence': 0.2907614870715431, u'task_ID': u'1516087358.74math_hw.jpg', u'label': 15, u'trueOrFalse': False, u'result': u'49 - 3 C = 13 ', u'rightAnswer': None, u'coordinate': {u'y': 1150, u'x': 80, u'w': 198, u'h': 49}}, {u'confidence': 0.3458846315104192, u'task_ID': u'1516087358.74math_hw.jpg', u'label': 46, u'trueOrFalse': False, u'result': u'20 + 4 = 5 ', u'rightAnswer': None, u'coordinate': {u'y': 705, u'x': 376, u'w': 183, u'h': 45}}, {u'confidence': 0.0011999284448164025, u'task_ID': u'1516087358.74math_hw.jpg', u'label': 31, u'trueOrFalse': None, u'result': u'Cannot \\  Recognize', u'rightAnswer': None, u'coordinate': {u'y': 934, u'x': 694, u'w': 206, u'h': 40}}, {u'confidence': 0.5143082883228928, u'task_ID': u'1516087358.74math_hw.jpg', u'label': 61, u'trueOrFalse': True, u'result': u'39 + 18 = 57 ', u'rightAnswer': None, u'coordinate': {u'y': 449, u'x': 373, u'w': 209, u'h': 41}}]}, u'correctRate': 0.21621621621621623}
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

# JPEG-image


## Introduction
Images we capture today, contains so much extra information that is not needed. <br/>
And also our human eye have some limitations. <br/>
So, removing what our eyes can't see is the basic idea. <br/>
Our eye is high sensitive to 'luma' than 'chroma'. So, according to that, image can be optimized.<br/>


## Setup
#### Frameworks and Packages
Make sure you have the following is installed:
 - [Python 3](https://www.python.org/)
 - [NumPy](http://www.numpy.org/)
 - [SciPy](https://www.scipy.org/)
 - PIL (Python Image Library)

## Usage
Give image path by command line argument.<br/>
```
python optimizer.py IMAGE_PATH
```
<br/>
Give relative image path inplace of IMAGE_PATH


 
## Future improvements
Average time for optimizing a 1280 x 720 image is around 2 minutes. That is very long.<br/>
I will try to reduce that time.

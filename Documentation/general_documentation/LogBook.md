# Welcome to the LogBook of our progress

Here the user can find notes on each step taken in the development of the project.

## 26/09/2022, Monday
+ Initial attempt to make pi camera work. 
+ :warning: DO NOT turn on RaspberryPi before attaching the camera. Always plug everything out, attach the camera and then plug the cords in to turn on RasPi. Otherwise, you will blow the camera. :warning:

## 29/09/2022, Thursday
### Instructions on how to connect the pi camera and taking a picture
+ Plug the camera in the RasPi. 
  + (instructions on how to open the holder, put the cord in and locking it, maybe with pictures)
+ Plug all the other necessary components to turn on RasPi. These are:
    + Mouse and keyboard
    +  Monitor
    +  Powercord
    +  **Note**: When the camera is attached, it takes the RasPi longer to turn on. If it takes too long, plug out the power and put it in again.
 +  You will see the screen of the RasPi on the monitor. Using the icon on the top, open a terminal. 
    + Use the command: `vcgencmd get_camera` to check that the camera is connected. If it is, you will get the output: `supported = 1, connected = 1`.
    + To take a picture use the command: `raspstill -o ~/Desktop/image.jpg`
    + **Note:** If the camera is out of focus, you can gently move the camera lens (counter-) clockwise to adjust the focus. 

## 30/09/22, Friday, First use of OpenCV
Yesterday the [first image](first-pic.jpg) was taken. The goal of this session is to use OpenCV to analyze the image and get a measure of the filament's thickness. Following sources are to be studied and used:
+ [Ordering coordinates clockwise with Python and OpenCV](https://pyimagesearch.com/2016/03/21/ordering-coordinates-clockwise-with-python-and-opencv/)
+ [Measuring size of objects in an image with OpenCV](https://pyimagesearch.com/2016/03/28/measuring-size-of-objects-in-an-image-with-opencv/)

Using the [code](../Software/code/edge_detection.py) to detect the edges of the filament we get [this](../Software/output/edged_first.png) kind of images. **Notes on the image:**
+ It seems that the lightning of the image is important for edge detection. It can be seen that the bright section on the top of the filament is detected as two lines. We need to avoid bright reflections off the surface of the filament. 
  + **Proposed solution**: We should aim to make a casing covering the camera, with a fixed light illuminating the sample. This would eliminate the light source as a random variable, increasing the reproducability. 
  + [ ] **Task**: Think about and ask for a small light source that might work for this purpose. Can the red LEDs we have would be useful?  

## 01/10/22, Saturday
**Today's goals**:
+ [ ] Achieving recognition of the top and bottom lines of the filament by the code
+ [ ] Figuring out the required distance between the filament and the camera such that the edges of it is not blurred.
+ [ ] Installing OpenCV in RasPi.
  + Apparently Python 10.2 crashed our OS... Reinstalling for next time. 
+ [X] Delving more into the tools of OpenCV.
  + It seems that the method used [here](https://pyimagesearch.com/2016/03/28/measuring-size-of-objects-in-an-image-with-opencv/) might not be applicable in our case, because that code requires the complete object to be in the image. It works by recognizing the object, drawing a rectangular contour around it and then taking the corners. In our images the filament will span across the whole image, hence the code might not recognize it as one object.  

## 02/10/2022 Sunday
**Today's goals**
+ [X] Reinstalling Pi OS (try the newest version since we knew that the camera was the issue the first time)
+ [X] Reinstall Python on Pi
  + We actually ended up leaving the Python that already came with Bullseye (Python 3.9) in fear of breaking it again. If there's any conflicts between our computers and the Pi, we'll downgrade in our computers. 
+ [X] Reinstall OpenCV
  + It worked first time...
+ [X] Reinstall GIT to simplify the process by coding on our computers
  + Already had the latest version installed! I can see the appeal in this new OS...
+ [X] Preliminary Camera Module Housing

## 03/10/22, Monday
+ [X] Go to the protolab and print the preliminary camera housing.
  + [This design](../Hardware/SLT_Files/FilamentObserver_w_LED_and_Chamfer_V1.stl) is being printed. 
+ [X] Get RGB LED
  + No need for it, red LED works pretty well already.
+ [X] Screw everything in the casing and take a picture
  + The picture is taken under the name pic_v1 
+ [X] Use edge detection software in the image
  + It seems that putting the light source at the side causes bright spots on one side, leading to a bad recognition of the edge on that side. 
  + **Proposed solution**: Put the light source at the side of one of the filament holes.
    + We did that by drilling a hole and the processing of the image leads to [this](../previous_pictures/edged_v140_100.png)
    + Now we get more clear lines detectable by eyes. Next step is to make it so that the computer also recognizes them as lines. 
  + New method to detect lines: [Houghline](https://www.geeksforgeeks.org/line-detection-python-opencv-houghline-method/)

## 07/10/22, Friday
**Summary of the progress since monday**:
+ We designed and printed V2 of the casing this time with a longer distance between the camera and the filament
  + Requires us to crop the image to analyze only the region around the middle of the filament, thus reducing unwanted edges that are recognized due to illumination of the sorrounding area.
  + Tried a white LED but it is too bright, causing unwanted edge detection --> stick to the red LED.
+ The [algorithm](../Software/code/edge_detection.py) to detect the edges of the filament as lines and measure the average distance (in pixels) between them works. 
  + There is variation however between initial measurements. We could see different measurements in pixels of the same, industrial filament
+ **Shortcomings for now**
  + In order to categorize which of the recognized lines belong to which edge of the filament, the code seperates the image in the middle. This poses a problem if the filament is positioned in such a way that it's curved. Then the code fails.
  + **Possible solutions:**
    + Design a casing such that the filament is strecthed, thus reducing the curvature.
    + Instruct the user to position the filament accordingly. 
  
### Progress today
+ Ana created the first version of the interface
  + Does temporal measurements (in pixels) and records them in a graph 
+ Yoldaş wrote more on the README
  + The skeleton seems to be ready to instruct the user to make a first measurement
  + [X] Images of the set up needs to be added
  + [X] Extra documents need to be created for further help if the user needs such as:
    + [X] How to connect another LED and changing the analysis parameters if the user uses other LEDs or resistors
    + [X] A summary of the working principles of the code (with images)

## 08/10/22, Saturday
+ Zach designed a nice interface.
+ Yoldaş put images of the set up in README and created the instructions of how to connect the LED and summary of the working principles.
+ Ana perfected the measurements and the interface.

## 10/10/22, Monday
**Goals:**
+ [X] Make the final presentable interface.
+ [X] Go over the doumentation and instructions to finalize them.

## 17/10/22, Monday
+ [X] Respond to the feedback.

## 20/10/22, Thursday
+ [ ] Make new casing with a hole for a light diffuser.
+ [ ] 
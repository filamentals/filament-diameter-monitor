# Reproducibility report

## Experiment/team: 
Filamentals by Ana Martins (@1760068), Yoldas Cinemre (@64795611) and Zach Meredith (@1069713)

## Reviewers: 
Riya Banerjee (@5073014) and Carlo van Maaren (@6835791)

## Report 

### Documentation:

1. **Could you understand the purpose of the experiment? Explain.**  
> Yes, this was very clear from the start as the README file in the main directory runs you through the motivation for the project and the project description.

2. **Were the safety instructions clear?**
> There were warning messages for the code and the setup (e.g. having to make sure that the camera is connected to the RaspberryPi before powering it), as well as a “Possible errors” section, but there was no true safety instructions which in our opinion also is not truly required since the project is very safe.

3. **Was the starting point and the expected duration of the measurements clear in the documentation?**  
> The starting point was easy to find because the main README file contained links to the documents in which the setup, calibration and measurement instructions were explained. The duration of the actual measurement or an estimate thereof, however, was not documented, but the GUI conveniently shows when the program settles to a particular filament diameter. For the calibration, it is said to run the program for 10 cycles, however we feel the number of cycles is not clearly indicated (the x-label of the graph in the GUI is labeled "timesteps").

4. **Does the documentation contain all necessary information to successfully reproduce the measurement? If not, what was missing?**
> We think the documentation mostly contains all the necessary information, perhaps having some extra README files in each subfolder would be helpful to better navigate through the project. 

5. **Did you get stuck at some point? What extra help did you need to proceed?**
> Initially, we got stuck trying to install all the required programs on our laptops which resulted in a few bugs we had to resolve (i.e. “from main import main errors” and having some problems installing picamera on Windows). After discussing with the project team, we figured out that we could simply use the desktop that was already connected to the device and from there everything went smoothly.

6. **Are you encouraged to reproduce previous measurements? How easily could you navigate through the project documentation?**
> The measurements we reproduced were the calibration and test measurement, after which we tried the extruded filament and a few cables to test the device. The calibration and test measurement were well-explained and we were encouraged to actually perform them in the documentation. 
Navigating through the project documentation was clear, but we do have a few pointers which will be given below (7).

7. **What can be improved in the documentation?**
> We like the use of the PIP install via the requirements file, but it is only described in the installation file. It would be useful if this was also mentioned in the software folder. For our purposes, however, it was fine since we did not have to install anything ourselves. 
To continue, the gui.py file is now located in the code folder (within the software folder) but there is also a “gui” folder in which there are only an image and a psd-file of the graphical user interface. We could imagine that people would look into the gui folder for the Python code as well, so perhaps renaming that folder to “GUI_images” or something similar would be better. You could also [convert your Python program to an executable file](https://www.geeksforgeeks.org/convert-python-script-to-exe-file/) and place that in the folder (while also having the actual code in the “code” folder). 
In addition, we would advise you to make the “Documentation” folder more structured by the use of subfolders, similar to those in the hard- and software folders.
Finally, as stated, we would use README files in the subfolders as well so that the reader is guided better through your documentation. This would also resolve some of the improvements mentioned above.

**On the scale of 1-5 (1: top quality, 5: disappointing) how do you assess the documentation? Please justify your grade based on the questions above.**

#### Documentation grade: <mark>**2**</mark>

### Measurements:

1. **Can you operate the setup with the provided instructions?**
> Once we figured out that we had to connect the power cable and use the desktop that was already connected, operating the setup was rather easy because of the graphical user interface. The provided instructions were clear and sufficient, but – as mentioned in the documentation – the software returned “Edges not found” a lot, especially when using the extruded filament. We will go more into some ideas we have  to resolve this in the following.

2. **How close were the results you obtain to the previously reported results?** 
> The calibration and test measurements were spot on. The measurements we performed after that were also pretty close (± 0.1 mm).

3. **Is the analysis procedure easy to understand? Summarize it briefly in your own words.**
> The analysis is done by the software itself. Its function is described in a working principles summary which was a very nice addition. This procedure we now want to describe in our own words.
The camera makes an image of the interior of the device in which the filament is placed. Behind the filament there is a LED which illuminates the interior of the chamber, so that the camera can capture the silhouette of the filament. This image is then cropped so that the variation in filament diameter will not influence the analysis. After that, you use a set of OpenCV functions to find the edges of the filament cross section (`cv2.canny`). Next, you use the `Houghlines()` method from OpenCV to recognize the edges as lines and compute the distance between the two. This should then give the diameter of the filament. 

4. **Is the setup robust and safe to operate?** 
> Yes, it mostly is. We would suggest making a holder for the RaspberryPi and all the electronics since they seem somewhat fragile.

5. **Did you encounter any issues? Could you troubleshoot those issues without contacting the owners?**  
> Once we have figured that we had to use the desktop that was already connected to the RaspberryPi, we only encountered issues in the form of the “Edges not found” warning which, as stated, was already mentioned in the documentation. Sometimes by adjusting the filament (which is something you also give as a possible solution), the warning went away, but most of time this was not the case. After discussing with a member of the project team we came to the conclusion that we should just accept this for the current standing of the project.

6. **What part of the measurement procedure did you appreciate most?**  
> We think the GUI is a very nice touch as this makes the experience for the user a lot nicer. Though not technically part of the measurement, we would also like to comment that getting an insight into the working principles of the algorithm was also a highlight of the reproducibility exercise.

**On the scale of 1-5 (1: top quality, 5: disappointing) how do you assess the measurements reproducibility? Please justify your grade based on the questions above.**

#### Reproducibility grade: <mark>**1.5**</mark>

### Interactions:

1. **If you had to perform work on this part of the project, would you have selected the same goal or aimed at something else? Please, explain.**  
> Initially we thought that you were going to actually build a full filament extruder from which we personally would not have immediately thought of making a filament sensor. After the presentation it became clear that there was already a filament extruder in Lili’s Proto Lab. From here, it indeed seems logical to look into improving this device instead and a filament sensor is a step we also could have taken from there. 

2. **Which instructions did you need from the owners on top of the written files?**  
> As beforementioned, the only thing we really needed was the pointer that we had to work on the desktop that was already connected to the device. We were initially starting to download the required libraries and trying to get the code working, but in the end all of that was already done for us! Thank you, team Filamentals!

3. **Does the experiment accomplish its stated purpose?**
> It does. We were able to determine the diameter of several filaments and wires. 

4. **What do you recommend to the project owners to improve their complete package?**

> _Documentation_


We think most of the project documentation is clearly ordered and complete. That being said, we do have a few tips (some of which are already discussed above):
1.	Add README files to the subfolders as well. This way you know where to find what in the subfolder. For example, when we looked for the gui.py file, we initially were looking in the “gui” folder, assuming the graphical user interface might be located in a separate folder. Something to add here, is that you could look into converting the GUI to an executable file and only place that file in the “gui” folder while keeping the actual code in the “code” folder ([conversion instructions](https://www.geeksforgeeks.org/convert-python-script-to-exe-file/)).
2.	Installing the required libraries via a single PIP install (through the requirements file) is a very good addition. For now it is only described in the installation file, however. We think it would be useful if this was also mentioned in the software folder. 
3.	We would advise you to make the “Documentation” folder more structured by the use of subfolders, similar to those in the hard- and software folders.

> _Measurements_


The measurements were very easy to perform because of the graphical interface. This is really nicely done! The graph shown in the GUI had a x-label “timesteps”. We wondered whether those actually refer to the number of cycles or an actual measure of time. In the former case, we would advise you to alter the calibration instructions so that they match. Otherwise, in the latter case, we would advise you to also include the number of cycles / elements that were used for the averaging so that you do not have to keep track of that yourself. You could also inform the user that the calibration (and with that the 10 cycles) are done.

> _Hardware (bonus)_


Since you guys did so well in the documentation and measurement side of the project, we also wanted to include some ideas we had on fixing some of the issues that you are still trying to solve (e.g. hopefully get rid of the “Edges not found” warnings). 
1.	To start, we noticed that the LED results in a flair in the images which in turn causes the OpenCV modules to recognize different edges than the ones of the actual filament. This could maybe be resolved by using a dim (homogeneous) back light which covers the entire back wall (i.e. the wall which is captured by the camera), or by making a ‘hallway’ for the LED (to reduce difference in radial distance from the light source) and using a diffusive plastic sheet (to dim the LED – might not be necessary anymore after including the hallway). This way the entire background will be illuminated in the same manner and contrast will be improved. In the images we clearly see the print lines which result in unwanted analysis results. By removing the back wall and replacing it with something non-3D printed (i.e. the back light), these lines will no longer be present and the OpenCV detection will most likely function a lot better. Furthermore, due to the light being a lot dimmer, the flairs should not be there anymore. If you manage to find a multi-color back light, you will also be able to adjust the color to have maximum contrast with the filament. 
2.	To tie in on this, we would also suggest painting the side walls of the chamber in black so that more of the indirect light is absorbed. This way the filament will only be illuminated from the back and print lines in the side walls will not cause lines in the images which could be recognized by the OpenCV modules. 
3.	Furthermore, you could look into using adjustable rollers on either side of the filament entrance and exit holes as this would make the feeding a lot more consistent, with less bending of the filament. By making them adjustable you are still able to use different filament gauges.
4.	As stated, we would also like to suggest making an enclosure for the wiring to improve the robustness of the device.
5.	In some talks we had about your project, you mentioned that you were also in the process of speeding-up the code. We think you will find a way to do this, but we also want to give you a different option that involves more of the hardware side. We encountered [this YouTube video]( https://www.youtube.com/watch?v=RYgdLPe_T0c) which describes a cheap solutions that requires much less computational power and analysis. Perhaps you can combine the two mechanisms and write an algorithm that uses the pre-estimated diameter to more quickly find the filament diameter through the optical path.
6.	Finally, we came across [this article](https://www.researchgate.net/publication/346555509_Open_Source_3-D_Filament_Diameter_Sensor_for_Recycling_Winding_and_Additive_Manufacturing_Machines) in which a multi-axes measurement is described using mirrors. This would give you a better indication of the actual shape of the filament, thereby making it a much better sensor than the 1D alternatives. If you guys have time, it would be awesome if you could also implement this!   



______

### Response to reviewers

_This part must be filled by the project owners based on the peer feedback_

1. **Which major adjustments did you make based on this feedback?**
 1. [ ] We are planning to redesign our lighting system to try to elimintate the "no edge found" error.
- [X] Design a diffuser slot
- [X] Design more reflective (homogenous) background
 2. [X] We plan on changing the x-label in our live graph from timesteps to cycles.
 3. [ ] We will design a more robust housing and consider the touch screen for the Raspberry Pi.
 4. [ ] We will further explain the calibration principle to clarify future confusion.
 5. [X] We will output the diameter of the filament
 6. [X] We will implement a red = recording
 7. [ ] We will upload our project details to JOGL.
 8. [ ] We will write down our clear goals, how far we plan to get, and the following steps of our project.
 9. [X] Update project canvas.
 10. [ ] We will clarify that the Raspbery Pi is a desktop and only needs a monitor and keyboard to use, not a separate laptop.
 11. [ ] We will clarify the link why making diameter measurements correlates to recycling plastic.
 12. [ ] We will try and record information aobut how long each measurement takes.
 13. [ ] We will look into the theoretical background of this project.
 14. [ ] We will clean up and reorganize our subfolders to adapt to the knowledge of each individual user.
- [X] Rename image folder to GUI images
- [X] More sub-folders in Documentation
- [X] README in each sub-folder with description of that sub-folder

 

2. **Do you agree with the graded assessment of the reviewer?**
In the context of this course, our team believes that our documentation is clear and precise enough to be considered a 1.5 over the 2 that we were originally scored.

**On the scale of 1-5 (1: really helpful, 5: disappointing) how do you assess the peer evaluation? Please explain.**
1.5: We believe that the feedback given was very descriptiive and near a perfect response. We were given, not just the problems of our project, but also possible solutions to overcome these problems. The only negative we found was that some of the advice was a little unhelpful simply due to them not being possible for integration to rasberry pi. Feedback is good, only when it applies to the project.
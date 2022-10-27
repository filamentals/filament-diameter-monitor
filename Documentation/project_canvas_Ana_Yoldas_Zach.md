*Utrecht Experiment Design 2022*

# Project canvas

### POP

+ **Purpose**: to make the project requirements, boundaries, and goals as concrete as possible  
+ **Outcome(s)**: list your project steps, the best possible outcome, and the minimum desired outcome  
+ **Process**: self-reflection and discussion with your mentors

PROJECT NAME: Filamentals

TEAM: Ana Martins, Yoldaş Cinemre, Zach Meredith

# Project description  
Our main goal is to create a monitoring system for a filament extruder.
We wanted to start by following an Open Source project that consists of an optical sensor that measures the width of plastic filament in real time. From there, assuming we have the time, we want to extend to monitor other parameters, like density or extrusion rate.

*25/09/2022 Update*
- We are no longer following the open source project that uses the optical sensor, since the sensor array used in the project is no longer manufacuted.
- As a result we are now creating a method of optical measurement through the combination of a Raspberry Pi and a Pi Camera.
- The new method will need a redesinged camera mount and a way to attach the sensor to the extruder.
- We plan on using OpenCV algorithm for diamater detection of the filament.

### Open Hardware and its purpose
We started by looking at this project: https://www.sciencedirect.com/science/article/pii/S2468067218300208, which is the full filament extruder, and then looking closely at what they use for monitoring, we want to follow this open source project: https://www.thingiverse.com/thing:454584
We connect with the idea of recycling plastic and giving it a new life. Especially considering the current popularity of 3D printing, one of our ideas is to recycle failed prints or unused prints, so as to not generate so much waste.

### Potential users of the hardware and its added value
While producing the filament, it is important to know its properties, to make sure it is of high enough quality.
The potential users are the general public, since 3D printing is now so widespread. This will allow people to produce their own filament at a low cost value, while also recycling.
This can also be used for high end level prototyping, when considering extrusion rate and a time involved in 3D printing.

### Underlying physics and working principles
The first sensor we are planning on using is an optical sensor. From there, mainly thermodynamics will be involved.
The sensor directly monitors the filament being extruded and displays it in real-time.

### Required components and planned alteration to the reported recipe

*Required Components*:
- Raspberry Pi
- Pi Camera
- 3D Printed Casing
- OpenCV

Something we want to add is displaying a graph with the history of the monitored data, so that we can figure out the optimal set up for extruding. Comparing our filament with industry-produced would also be a goal.

### Chosen method of interfacing with a computer
Using a RaspberryPi, we want to create a feedback loop, where the system controlls itself when parameters are outside the acceptable values, and through this we will be able to start and stop the monitoring.

### Planned measurements
Diameter, moisture content, density, extrusion rate, elasticity, temperature.


## Mid-course review of your project state (fill this mid-course)
### Current status (24/10/22):
+ **Hardware:** Currently we have designs for 3D-printed casings that create a suitable environment for the imaging of filaments. The [installation](instructions/Installation.md) is shown to be easy, as tested by an independent group of users who had no prior experience with the set-up.
+ **Software:** We have a code that analyzes an image of the filament in the casing, and calculate the average thickness. The principles of how this works can be found [here](../Software/working_principles_summary.md).
+ **Interfacing:** The user can interact with the device by connecting the RaspberryPi to a monitor and running the code to access a graphical user interface. This interface contains a live readout of the measured diameter, as well as means to start, stop, calibrate the device. The output is then recorded in a seperate text file. Instructions to make measurements can be found [here](instructions/measurement_instructions.md).

### Deviations from the original plan:
+ We decided to restrict our measurements to filament diameters, as opposed to the initial plan to measure temperature, density, extrusion rate etc. Such goals are not within the capabilities of our current equipments and would require seperate designs of their own. We do not have the time to work on this in the timeframe allocated to the project.
+ Given the time restrictions, it is also improbable that we will manage to connect the device to a filament extruder and establish a feedback circuit. The next step for any future work on the project would be on this aspect. 

### Planned adjustments:
+ Currently, the device is not as robust as we want it to be. It seems that little changes in the positioning of filaments may cause the device to fail in making measurements. We aim to increase robustness by adding a diffuser in our design, so that the light will be more uniform. We think that this will make it easier for the device to recognize the edges of filaments.

### Updated Projects Description:
*(As written in the main README)*

FilaMentals is a project to develop an optical device to monitor the diameter of 3D-printer filaments that are produced by an extractor. Custom made extractors are susceptible to produce inhomogenous filaments which would not be useful for re-use in a 3D printer. So, the future aspiration of the project is to create a feedback loop between a FilaMental device and a filament extractor, such that the extractor parameters are automatically adjusted based on the FilaMental output and the desired filament diameter is achieved.  

 A Raspberry Pi NoIR Camera (V2) is controlled by a Raspberry Pi 3 to monitor the filament. The camera and the filament are attached to a 3D-printed casing. The casing also involves a hole for a LED, which illuminates the filament. Later, the images of the filament are analyzed with the help of [OpenCV](https://opencv.org/) package to calculate the thickness. 

## Final review of the project accomplishments (fill at the end of the course)

+ list the achievements of your project  
+ write down your plans for improving your project or making it more widely accessible

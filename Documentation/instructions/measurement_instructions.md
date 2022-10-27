# **Making measurements:**

The filament you wish to measure should be pushed through the two holes on the 3D-printed casing. It is most probable that the filament will be curved because of its elastic properties. To make the device work correctly, position the filament as shown below. 

![filament_insertion](../Hardware/Images/filament_insertion.png)

This will ensure that the filament sits symmetrically in the middle of the images. To understand why this is required, see the [summary of working principles](../../Software/working_principles_summary.md) of the code. 

Since the casing is a prototype and not designed to be attached a filament extruder, you will need to move the filament by hand.

Now, locate to the code folder in the project repository using: 

`cd Desktop/ued2020/projects/Filamentals_Ana_Yoldas_Zach/Software/code`

and run:

`python gui.py`

A graph will appear with the y-axis showing the thickness measurements while the x-axis shows the timesteps. You can also see the  buttons to start/stop, calibrate, and clear measurements.

## How to calibrate 
The device has a default calibration using an industrial 3D-printer filament with a diameter of 1.75 mm. However, it can be calibrated with another filament. To do that:

1. Insert a filament in the 3D-casing whose diameter you know.
2. Run the program, and let it run for at least 10 cycles. 
3. Insert the real diameter of the filament on the top right and click on "Calibrate".
4. Now you are ready to measure other filaments.

## Test measurement
Now let us make a measurement to check that the calibration is done well.

1. Insert the piece of calibration filament by paying attention to its curvature as instructed before. 
2. Start the program. The measurements will begin immediately, but you can stop and start it any time with the buttons.
3. After each measurement that appears in the graph, pull the filament slightly by hand to analyze a different segment.
4. The interface should calculate 1.75 mm for the thickness. Congratulations! The calibration is confirmed.
5. Now the device is ready to be used with other filaments.
## Possible errors
+ The terminal might show `Edges not found`. This indicates that the code failed to recognize the filament edges and/or distinguish them. When this happens, the measurement is ignored and it's not registered in the interfacial graph. **Possible Solutions:**
  + Adjust the filament as instructed above such that it's positioned symmetrically in the middle of the image (see [here](../Software/WorkingPrinciples_summary.md) to read more about why it is important.) 
  + It might also be that the filament is deformed in that region. Pull the filament a little bit to measure a different segment.
  + If the problem persists, investigate the edge detection seen by the camera. The symmetry and uniformity of the filament can be visualized here. This can be done by locating the stored photos taken by the camera. These photos can be found under [Software > output](../software/output/) and are labeled by their set min/max threshold. Select the file with the current threshold values. The current version is:
    + Min Threshold: 100
    + Max Threshold: 120
  
     *Thus the file name is as follows: edged_pic_100_120.png*
## Notes
+ For a summary of the working principles of the algorithm see [here](../Software/WorkingPrinciples_summary.md) 

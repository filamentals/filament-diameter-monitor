import cv2
import globals
import numpy as np


def get_lines(original, edged):
    """
    function that uses the Hough line method to search for lines in
    the image and returns arrays with the lines from left and right
    for Hugh lines context:
    https://www.geeksforgeeks.org/line-detection-python-opencv-houghline-method/
    """

    left_lines = []
    lines = cv2.HoughLines(edged, 1, np.pi / 180, 200)

    if lines is not None and lines is not None:
        print("Taking the average of " + str(len(lines)) + " detected lines...")
    else:
        print("We were not able to find any lines.")
        cv2.imwrite("../output/edged_pic.png", edged)

    # The below for loop runs till r and theta values
    # are in the range of the 2d array

    left_lines = []
    leftn = 0
    right_lines = []
    rightn = 0
    
    if lines is not None and lines is not None:
        x0 = []
        y0 = []
        a = []
        b = []
        j = 0
        
        for r_theta in lines:
            r, theta = r_theta[0]
            a.append(np.cos(theta))
            b.append(np.sin(theta))

            x0.append(a[j] * r)  # r cos(theta)
            y0.append(b[j] * r)  # r sin(theta)


            # CALCULATING DISTANCE

            if (x0[j] < globals.XCROPPED / 2) and not left_lines:
                leftn += 1
                for i in range(-200, 200):
                    x = round(x0[j] + i * b[j])
                    y = round(y0[j] + i * a[j])
                    arr = [x, y]
                    left_lines.append(arr)
            elif (x0[j] >= globals.XCROPPED / 2) and not right_lines:
                rightn += 1
                for i in range(-200, 200):
                    x = round(x0[j] + i * b[j])
                    y = round(y0[j] + i * a[j])
                    arr = [x, y]
                    right_lines.append(arr)
            elif x0[j] < globals.XCROPPED / 2:
                leftn += 1
                for i in range(-200, 200):
                    x = round(x0[j] + i * b[j])
                    y = round(y0[j] + i * a[j])
                    left_lines[i + 200][0] += x
                    left_lines[i + 200][1] += y
            elif x0[j] >= globals.XCROPPED / 2:
                rightn += 1
                for i in range(-200, 200):
                    x = round(x0[j] + i * b[j])
                    y = round(y0[j] + i * a[j])
                    right_lines[i + 200][0] += x
                    right_lines[i + 200][1] += y
            j += 1

        return right_lines, left_lines, rightn, leftn, x0, y0, a, b
    else:
        return right_lines, left_lines, rightn, leftn, [0], [0], [0], [0]
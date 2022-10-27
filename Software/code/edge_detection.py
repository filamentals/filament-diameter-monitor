import cv2


def get_edge(filename, min_threshold, max_threshold):
    """
    function that uses open cv to create a contrast in the image such
    that you can recognise lines
    """
    original = cv2.imread(filename)
    cropped = original[340:740, 750:1180]
    cv2.imwrite("../output/cropped_pic.png", cropped)

    # code for line recognition
    edged = cv2.Canny(cropped, min_threshold, max_threshold)
    edged = cv2.dilate(edged, None, iterations=1)
    edged = cv2.erode(edged, None, iterations=1)

    return original, edged

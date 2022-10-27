from camera import get_picture
from edge_detection import get_edge
from line_detection import get_lines
from distance_calculator import get_distance


def main():
    # original image from the camera

    filename = "../output/pic.png"

    time2adjust = 1

    min_threshold = 100
    max_threshold = 120

    get_picture(filename, time2adjust)
    original, edged = get_edge(filename, min_threshold, max_threshold)
    right_lines, left_lines, rightn, leftn, x0, y0, a, b = get_lines(original, edged)
    if x0 != [0]:
        distance = get_distance(right_lines, left_lines, rightn, leftn, x0, y0, a, b, original)
        return distance
    else:
        return 0
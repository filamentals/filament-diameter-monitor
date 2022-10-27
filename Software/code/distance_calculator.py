import cv2

def get_distance(right_lines, left_lines, rightn, leftn, x0, y0, a, b, original):
    """
    function that takes the prevously made right and left lines
    arrays and calculates the distance between the average
    """

    i = 0
    # ADDING ALL LEFT LINES
    for element in left_lines:
        left_lines[i][0] = round(element[0] / leftn)
        left_lines[i][1] = round(element[1] / leftn)
        i += 1

    i = 0
    # ADDING ALL RIGHT LINES
    for element in right_lines:
        right_lines[i][0] = round(element[0] / rightn)
        right_lines[i][1] = round(element[1] / rightn)
        i += 1

    sum_dist = 0
    summed = 0

    for pl in left_lines:
        for pr in right_lines:
            if pl[1] == pr[1]:
                sum_dist += abs(pr[0] - pl[0])
                summed += 1

    if summed != 0:
        print(
            "The distance (in pixels) between the lines is "
            + str(round(sum_dist / summed))
        )
        return sum_dist / summed
    else:
        print("The lines found cannot be used.")
        print()
        
        for i in range(0, len(x0)):
            # for the picture - 200 each side to be recognise only the lines in the crop DEBUGGING
            x1 = round(x0[i] + 200 * (-b[i])) + 750
            y1 = round(y0[i] + 200 * (a[i])) + 345
            x2 = round(x0[i] - 200 * (-b[i])) + 750
            y2 = round(y0[i] - 200 * (a[i])) + 345

            # for the picture DEBUGING
            cv2.line(original, (x1, y1), (x2, y2), (255, 0, 0), 2)

            # for the picture DEBUGGING
            cv2.imwrite("../output/lines_pic.png", original)
        return 0

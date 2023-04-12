# TODO take pixel from every square. 3x3 first 3 then 4x4... etc

import pyautogui
import time

# 3x3 grid checker

# Point(x=819, y=309)
# Point(x=953, y=314)
# Point(x=1093, y=315)
# Point(x=817, y=441)
# Point(x=951, y=444)
# Point(x=1081, y=444)
# Point(x=820, y=574)
# Point(x=961, y=583)
# Point(x=1084, y=572)

# if False:
for a in range(2):
    print(a)

    isBlank = True

    # 3x3 grid
    squares = [[(819, 309),(953, 314),(1093, 315)],[(817, 441),(951, 444),(1081, 444)],[(820, 574),(961, 583),(1084,572)]]
    # square_rgb = []

    while isBlank:
        square_colors = []

        for i in range(3):
            row = []
            for j in squares[i]:
                pix = pyautogui.pixel(j[0],j[1])
                if pix == (255, 255, 255):
                    row.append("white")
                else:
                    row.append("blue")
            square_colors.append(row)

        time.sleep(0.1)

        for i in square_colors:
            if 'white' in i:
                print("has white")
                isBlank = False

    print(square_colors)

    time.sleep(2)

    for i in range(3):
        for j in range(3):
            if square_colors[i][j] == 'white':
                print("white")
                pyautogui.click(squares[i][j][0], squares[i][j][1])

    time.sleep(2)


for a in range(3):
    print(a)

    isBlank = True

    squares = [[(802, 298),(903, 298),(1003, 303),(1100, 297)],[(806, 391),(901, 393),(1004, 395),(1104, 392)],[(806, 498),(913, 491),(996, 490),(1099, 492)],[(812, 588),(909, 586),(997, 585),(1091, 586)]]

    while isBlank:
        square_colors = []

        for i in range(4):
            row = []
            for j in range(4):
                # pyautogui.moveTo(squares[i][j][0], squares[i][j][1])
                pix = pyautogui.pixel(squares[i][j][0], squares[i][j][1])
                print(pix)
                if pix == (255, 255, 255):
                    row.append("white")
                else:
                    row.append("blue")
            square_colors.append(row)

        time.sleep(0.1)

        for i in square_colors:
            if 'white' in i:
                print("has white")
                isBlank = False

        print(square_colors)

        time.sleep(2)

        for i in range(4):
            for j in range(4):
                if square_colors[i][j] == 'white':
                    print("white")
                    pyautogui.click(squares[i][j][0], squares[i][j][1])

        time.sleep(1.5)

print("end")
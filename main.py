import numpy as np
import matplotlib.pyplot as plt
from mss import mss
import cv2
# from pynput import mouse
from pynput.keyboard import Key, Controller
import random
import time

keyboard = Controller()
offset_x = 10
offset_y = 0
# box = [0+offset_x, 0+offset_y, 800+offset_x, 522+offset_y]
box = [440+offset_x, 355+offset_y, 600+offset_x, 522+offset_y]
sensor1 = (80, 79)
sensor = (135-10, 86)
orange_sensor = (78, 72)
# sensor = [71, 39, 73, 122]
mon = {'top': box[1], 'left': box[0],
       'width': box[2]-box[0], 'height': box[3]-box[1]}
sct = mss()

red = "2847f3"
yellow = "00b5f3"
blue = "bbbd65"
orange = "0077f8"
white = "e0eff7"

def get_image_array(sct):
    return np.array(sct.grab(mon))


def push(k, t=0.02):
    keyboard.press(key=k)
    time.sleep(t)
    keyboard.release(key=k)


def random_push():
    push(random.choice(['d', 'f', 'j', 'k']), t=0.01)
    push(random.choice(['d', 'f', 'j', 'k']), t=0.01)


def get_data(screen):
    vertical = []
    for y in range(mon['height']):
        vertical.append(screen[y][sensor[0]])
    return vertical

def rgb_to_hex(rgb):
    return '%02x%02x%02x' % (rgb[0], rgb[1], rgb[2])

wait = ''
def play_taiko(screen, beats=0.04):
    global wait
    # print(screen[sensor[1]][sensor[0]])
    color1 = rgb_to_hex(screen[sensor1[1]][sensor1[0]])
    color = rgb_to_hex(screen[sensor[1]][sensor[0]])
    color2 = rgb_to_hex(screen[orange_sensor[1]][orange_sensor[0]])
    if color == red:
        push('j')
        time.sleep(beats)
    elif color == blue:
        push('k')
        time.sleep(beats)
    elif color == yellow:
        random_push()
    elif color2 == orange:
        random_push()
    # if color1 == white and wait != '':
    #     push(wait)
    #     wait = ''
    # if color == red:
    #     wait = 'j'
    # elif color == blue:
    #     wait = 'k'
    # elif color == yellow:
    #     random_push()
    # elif color2 == orange:
    #     random_push()
    # if color1 == white and wait != '':
    #     push(wait)
    #     wait = ''
t1 = time.time()
count = 0
# find_circle()
while(True):
    # screen = cv2.cvtColor(get_image_array(sct), cv2.COLOR_RGB2GRAY)
    screen = get_image_array(sct)
    # cv2.imshow('rgb', screen)
    # cv2.waitKey(0)
    # plt.imshow(screen)
    # plt.show()
    play_taiko(screen)
    # Frame counter
    count += 1
    if time.time() - t1 >1:
        print(count)
        count = 0
        t1 = time.time()


# img.save("screen.jpg")

# with mouse.Listener(on_click= lambda x,y,_,__: print(x, y)) as listener:
#     listener.join()

# def find_circle():
#     image = np.array(sct.grab(mon))
#     output = image.copy()
#     hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
#     # detect circles in the image
#     circles = cv2.HoughCircles(hsv[:,:,0], cv2.HOUGH_GRADIENT, 1, 10, param1=30,
#                                param2=50, minRadius=10, maxRadius=100)
#
#     # ensure at least some circles were found
#     if circles is not None:
#         # convert the (x, y) coordinates and radius of the circles to integers
#         circles = np.round(circles[0, :]).astype("int")
#         # loop over the (x, y) coordinates and radius of the circles
#         for (x, y, r) in circles:
#             print(x, r, r)
#             cv2.circle(output, (x, y), r, (0, 255, 0), 2)
#             cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
#         cv2.imshow("hsv", hsv)
#         cv2.imshow("output", np.hstack([image, output]))
#         cv2.waitKey(0)


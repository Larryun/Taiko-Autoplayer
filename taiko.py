import numpy as np
from mss import mss
from pynput.keyboard import Key, Controller
import random
import time

keyboard = Controller()
offset_x = 10
offset_y = 0

# The screenshots box
# [x1, y1, x2, y2]
box = [440+offset_x, 355+offset_y, 600+offset_x, 522+offset_y]

# Adjust the offset for better accuracy
sensor_offset = -15
sensor = (135+sensor_offset, 86)

# For the balloon
orange_sensor = (78, 72)


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


def rgb_to_hex(rgb):
    return '%02x%02x%02x' % (rgb[0], rgb[1], rgb[2])


def play_taiko(screen, beats=0.04):
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


# Timer for frame counter
t1 = time.time()
count = 0
while(True):
    screen = get_image_array(sct)
    play_taiko(screen)

    # Frame counter
    count += 1
    if time.time() - t1 >1:
        print(count)
        count = 0
        t1 = time.time()

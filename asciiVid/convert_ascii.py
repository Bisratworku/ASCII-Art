import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import os
from termcolor import colored

path = f'{os.getcwd()}\\Garp vs Aokiji Full Fight _ One Piece Anime.mp4'
video = cv.VideoCapture(path)
def get_frames(path):
    #path = f'{os.getcwd()}\\Garp vs Aokiji.mp4'
    vid = cv.VideoCapture(path)
    frames = []
    while True:
        ret, frame = vid.read()
        if ret == False:
            print("the video is finished")
            break
        gray = cv.cvtColor(frame , cv.COLOR_BGR2GRAY)
        gray = cv.resize(gray, (60, 45))
        color = cv.resize(frame, (60, 45))
        yield np.array(color),  np.array(gray)
    return 0

def ascii_frames(path):
    img = get_frames(path)
    density = ['@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@']
    for idx,i in enumerate(img):
        atxt = ''
        color, gray = i
        gray = gray //25
        for row in zip(color, gray):
            Crow, Grow = row
            txt = ''
            for col in zip(Crow, Grow):
                Ccol , Gcol = col
                txt += colored(density[Gcol], (Ccol[0], Ccol[1], Ccol[2]),attrs=['bold'])
            atxt += txt + '\n'
        print(atxt)

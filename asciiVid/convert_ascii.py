import numpy as np
import cv2 as cv
import os
from termcolor import colored
from pytubefix import YouTube
from pytubefix.cli import on_progress

'''
url = 'https://www.youtube.com/watch?v=GkOLkuHhU7s&t=14s'
ytube = YouTube(url=url, on_progress_callback= on_progress)
video = ytube.streams.get_by_resolution(360)
print(video.title)
video.download()'''

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

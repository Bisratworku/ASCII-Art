import numpy as np
import cv2 as cv
import os
import time
from termcolor import colored
from pytubefix import YouTube
from pytubefix.cli import on_progress


def get_frames(path):
    vid = cv.VideoCapture(path)
    while True:
        ret, frame = vid.read()
        if ret == False:
            print("the video is finished")
            break
        gray = cv.cvtColor(frame , cv.COLOR_BGR2GRAY)
        gray = cv.resize(gray, (100, 35))
        color = cv.resize(frame, (100, 35))
        yield np.array(color),  np.array(gray)
    return 0
def download_vid(link):
    yt = YouTube(link, on_progress_callback = on_progress)
    ys = yt.streams.get_highest_resolution()
    path =  ys.download(filename = f'{ys.title}.mp4')
    return path

def ascii_frames(path):
    img = get_frames(path)
    density = ['@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@']
    for i in img:
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
        time.sleep(0.01)
    os.remove(path)
def main():
    url = input("Enter Youtube LInk  : ")
    path = download_vid(url)
    ascii_frames(path)
main()
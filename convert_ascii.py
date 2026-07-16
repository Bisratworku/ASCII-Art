
import threading
import numpy as np
import cv2 as cv
import os
import time
from termcolor import colored
from pytubefix import YouTube
from pytubefix.cli import on_progress
from pygame import mixer
from pydub import AudioSegment
mixer.init()

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
    video =  ys.download(filename = f'{ys.title}.mp4')
    audio = yt.streams.get_audio_only()
    audio = audio.download(filename = f'{ys.title}.wav')
    sound = AudioSegment.from_file(audio)
    sound = sound.set_frame_rate(44100)
    sound = sound.set_sample_width(2)
    sound = sound.set_channels(2)
    sound.export('output.wav', format = 'wav')
    os.remove(audio)
    return video, 'output.wav'
#v, s =  download_vid('https://www.youtube.com/watch?v=pfZ5-sV2RlY&list=RDpfZ5-sV2RlY&start_radio=1')
def play_sound(music):
    try:
        mixer.music.load(music)
        mixer.music.set_volume(0.1)
        mixer.music.play()   
        while mixer.music.get_busy():
            time.sleep(0.1)
    except Exception as e:
        print(e)
    mixer.music.stop()
    mixer.music.unload()
#play_sound('output.wav')
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
def remove_file(file):
    os.remove(file)

def main():
    url = input("Enter Youtube LInk  : ")
    video, sound = download_vid(url)
    video_thread = threading.Thread(target = ascii_frames, args = (video, ))
    audio_thread = threading.Thread(target = play_sound, args = (sound, ))
    video_thread.start()
    audio_thread.start()
    video_thread.join()
    audio_thread.join()
    return video, sound  
if __name__ == '__main__' :
    v, s = main()
    os.remove(v)
    os.remove(s)
    



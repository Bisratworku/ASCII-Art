import threading
import numpy as np
import cv2 as cv
import os
import sys
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
        gray = cv.resize(gray, (100, 36))
        color = cv.resize(frame, (100, 36))
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
def play_sound(music, start_event, start_time_holder):
    try:
        mixer.music.load(music)
        mixer.music.set_volume(0.2)
        start_event.wait()
        start_time_holder['value'] = time.monotonic()
        mixer.music.play()
        while mixer.music.get_busy():
            time.sleep(0.01)
    except Exception as e:
        print(e)
 
def ascii_frames(path, start_event, start_time_holder):
    img = get_frames(path)
    density = ['@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@']
    start_event.wait()
    while 'value' not in start_time_holder:
        time.sleep(0.001)

    start_time = start_time_holder['value']
    frame_index = 0
    sys.stdout.write('\x1b[2J\x1b[H\x1b[?25l')
    sys.stdout.flush()
    try:
        for i in img:
            atxt = ''
            color, gray = i
            gray = gray //25
            for row in zip(color, gray):
                Crow, Grow = row
                txt = ''
                for col in zip(Crow, Grow):
                    Ccol , Gcol = col
                    txt += colored(density[Gcol], (Ccol[2], Ccol[1], Ccol[0]))
                atxt += txt + '\n'

            target_time = start_time + (frame_index / 24.0)
            sleep_for = target_time - time.monotonic()
            if sleep_for > 0:
                time.sleep(sleep_for)

            sys.stdout.write('\x1b[H' + atxt)
            sys.stdout.flush()
            frame_index += 1
    finally:
        sys.stdout.write('\x1b[?25h')
        sys.stdout.flush()


def main(url):
    video, sound = download_vid(url)
    start_event = threading.Event()
    start_time_holder = {}
    video_thread = threading.Thread(target=ascii_frames, args=(video, start_event, start_time_holder))
    audio_thread = threading.Thread(target=play_sound, args=(sound, start_event, start_time_holder))
    video_thread.start()
    audio_thread.start()
    start_event.set()
    video_thread.join()
    audio_thread.join()
    
    return video, sound


if __name__ == '__main__' :
    url = input("Enter Youtube LInk [Press 'q' to quit] : ")
    while True:
        if url == 'q':
            break
        v, s = main(url)
        mixer.music.stop()
        mixer.music.unload()
        os.remove(v)
        os.remove(s)

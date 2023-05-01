"""
    Project: Soundify is an add on to spotify where you can input a song that you like and you will be returned with
    a playlist of songs that are similar to the given song. It also includes side functions such as a search bar that
    spotify has so you don't have to switch between the two, and a text input to search for a song in the given playlist.
    Each song that is printed is linked to the song in spotif and when clicked, will play the song in spotify. When
    setting the queue, I print the sample links that I would have used to play the songs in Soundify. However, I did not
    have the time nor the resources to know how to play sounds or get mp3 files in python.

    @Author Nicolas Ekstrand
    @version 05/13/2022

"""
import copy
import queue
import random
from tkinter import *

class Playlist:

    def __init__(self, songs):
        self.songs = songs
        self.queue = queue.Queue()

    def __repr__(self):
        for i in range(len(self.songs)):
            print(self.songs[i].__repr__())
        print("Hello")

    def displayQueue(self):
        for i in range(self.queue.qsize()):
            print(self.queue.get().__repr__())

    def setQueue(self, mode):
        temp = copy.deepcopy(self.songs)
        #Will randomly order the queue
        if mode == "shuffle":
            while len(temp) != 0:
                n = random.randint(0, len(temp) - 1)
                self.queue.put(temp[n])
                temp.pop(n)
        #Will queue songs in the order of the playlist
        elif mode == "in order":
            for i in range(len(self.songs)):
                self.queue.put(self.songs[i])

    def playQueue(self):
        temp = self.queue
        for i in range(self.queue.qsize()):
            print(temp.pop().getUri())



import sys
import pygame
#sudo apt-get install python-pygame 
import os.path

class Song:
	def __init__(self,name,filepath,length):
		self.song_name=name
		self.song_path=filepath
		self.song_length=length


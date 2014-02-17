import sys
import pyglet
#sudo apt-get install libavbin-dev libavbin0
import os.path

class Song:
	def __init__(self,name,filepath,length):
		self.song_name=name
		self.song_path=filepath
		self.song_length=length

	def getSongName(self):
		return self.song_name

	def getFiles(path)
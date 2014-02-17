import sys
from raspjb_song_class import Song
import os.path


class SongQeueu:
	def __init__(self):
		self.song_number=0
		self.song_qeueu=[]

	def addToQeueu(self,Song):
		self.song_qeueu.append(Song)
		print "added"


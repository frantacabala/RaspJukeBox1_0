import sys
from raspjb_song_class import Song
import os.path


class SongQeueu:
	def __init__(self):
		self.song_number=0
		self.song_qeueu=[]

	def addToEndQeueu(self,song):
		self.song_qeueu.append(song)
		s1=Song(song.song_name, song.song_path, song.song_length)


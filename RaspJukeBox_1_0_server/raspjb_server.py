#!/usr/bin/env python

import sys
from raspjb_song_class import Song
from SongQeueu import SongQeueu



def createSongList():
	x=SongQeueu()
	return x


def serverStart(port):
	print "Starting server on: " + port
	print "Searching and creating song qeueu..."
	qeueu=createSongList()
	song = Song("name", "~/Music", "1234")
	qeueu.addToEndQeueu(song)

if __name__ == "__main__":
	print "Configuring port: "
	port="1234"
	serverStart(port)

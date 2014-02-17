#!/usr/bin/env python

import sys
from raspjb_song_class import Song




def createSongList():
	song=Song("hovno","hovno",1234)
	print song.getSongName()


def serverStart(port):
	print "Starting server on: " + port
	createSongList()

if __name__ == "__main__":
	print "Configuring port: "
	port="1234"
	serverStart(port)

import os
import mutagen
from mutagen.flac import FLAC
from mutagen.mp3 import EasyMP3 as MP3

def main():
	curDir = os.getcwd()
	for root, dirs, files in os.walk(curDir, topdown=False):
		trackNum = 1
		for f in files:
			change(f,root, trackNum)
			trackNum += 1

def change(f, path, trackNum):
	type = f.split(".")[-1]
	if type  == "flac":
		try:
			audio = FLAC(path + "\\" + f)
			title = audio["title"][0]
		except:
			print "error: " + path + "\\" + f + "\n"
			return
		try:
			track = audio["tracknumber"][0]
			track = track.split("/")[0]
		except:
			track = str(trackNum)
		try:
			name =  track + " - " + title + "." + type
			# print name 
			os.rename(path + "\\" +  f, path + "\\" + name)
		except:
			print "error: " + path + "\\" + f + "\n"
			return
	elif type == "mp3":
		try:
			audio = MP3(path + "\\" + f)
			title = audio["title"][0]
		except:
			print "error: " + path + "\\" + f + "\n"
			return
		try:
			track = audio["tracknumber"][0]
			track = track.split("/")[0]
		except:
			track = str(trackNum)
		try:
			name =  track + " - " + title + "." + type
			# print name 
			os.rename(path + "\\" +  f, path + "\\" + name)
		except:
			print "error: " + path + "\\" + f + "\n"
			return

if __name__ == "__main__":
    main() 

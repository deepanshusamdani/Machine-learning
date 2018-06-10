#!/usr/bin/python3

import os
import subprocess as sub 
import speech_recognition as sr
from os import path
r=sr.Recognizer()

with sr.Microphone() as source:
	r.adjust_for_ambient_noise(source)	
	print("speak: ")
	audio=r.listen(source)
	print("done")


try:
	audio_txt=r.recognize_google(audio)
	print(audio_txt)
	strip_txt=audio_txt.strip()
	final_txt=strip_txt.split()
	print(strip_txt)
	if 'remove' in final_txt:
		for i in range(0,len(final_txt)):
			if final_txt[i]=='directory':
				dir_name=final_txt[i+1]
				break
	
	if dir_name:
		os.system('rmdir '+dir_name)
	else:
		print("try again !")

except:
	print("hr kuch")
	pass

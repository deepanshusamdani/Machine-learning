#!/usr/bin/python3

import os
import subprocess as sub 
import speech_recognition as sr

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
	if 'delete' in final_txt:
		for i in range(0,len(final_txt)):
			if final_txt[i]=='file':			
				file_name=final_txt[i+1]
				break

	if file_name:
		os.system('rm -f '+file_name)
	else:
		print("try again !")
	

except:
	print("could not understand !")
	pass

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
	if 'please' in final_txt:
		for i in range(0,len(final_txt)):
			if final_txt[i]=='install':			
				module_name=final_txt[i+1]
			
			if final_txt[i]=='in':			
				platformname=final_txt[i+1]
				break

	print("in which platform do you want to install the module")
	print("1. python")
	print("2. python3")
	print("choose choice(in number)")
	
	ch=input()

	if platformname == 'python' or '1' :
		s='sudo'+ " " + 'pip3'+  " "+ 'install' + " " + module_name  
		os.system(s)
	
	elif platformname == 'python3' or '2':
		s='sudo'+ " " + 'apt'+  " "+ 'install' + " " + module_name
		os.system(s)

	else :
		s='sudo'+ " " +'apt-get'+ " " + install + " " +module_name
		os.system(s)


except:
	print("something gonna wrong")
	pass

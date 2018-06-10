#!/usr/bin/python3

import os

# Search folder in a current location 

import os



def openfile():
	fo=open(fi,'r+')
	g=fo.read()
	print(g)
	fo.close()

search=input("enter Folder name")

fi=input("enter file name")

file1=search.capitalize() #......to make first letter of a word in upper case

file2=search.upper()  #.... to convert whole string into upper case

filename=[file1,file2]

for filename in os.listdir(os.getcwd()):

	if os.path.exists(fi) == True:


		if os.path.exists(fi) == True :
		
			print("YES Folder Exists here")
			
			openfile()
	
		elif  os.path.exists(fi) == True :
		
			print("does exists")
			openfile()

		elif  os.path.exists(fi) == True :
			print("does exists")
			openfile()

		else :
			print("Doesnot exist")





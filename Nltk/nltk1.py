#!/usr/bin/python3

from bs4 import BeautifulSoup
import urllib.request


web_data = urllib.request.urlopen(website)

#printing the data
print(web_data.read())

clean_data=web_data.read()

get_clean=BeautifulSoup(clean_data,'html5lib')

final_data=get_clean.get_text()

good_data=final_data.strip()
new_data=[]

for i in good_data:
	j=i.split()
	new_data.append(j)

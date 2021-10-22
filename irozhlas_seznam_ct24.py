import requests
from bs4 import BeautifulSoup
import time

#irozhlas
def irozhlas():
	get_irozhlas = requests.get("https://www.irozhlas.cz/")
	#print (get_irozhlas.status_code) #pokud != 200 -> nepristupne
	source_irozhlas = get_irozhlas.content
	soup_irozhlas = BeautifulSoup(source_irozhlas, features="html.parser")#, "lxml")
	h3_irozhlas = soup_irozhlas.find_all("h3")
	hlavni_zprava_irozhlas = h3_irozhlas[0]
	return("iRozhlas: " + hlavni_zprava_irozhlas.get_text().strip())

#seznam zpravy
def seznam():
	get_seznam = requests.get("https://www.seznamzpravy.cz/")
	source_seznam = get_seznam.content
	soup_seznam = BeautifulSoup(source_seznam, features="html.parser")
	h3_seznam = soup_seznam.find_all("h3")
	hlavni_zprava_seznam = h3_seznam[0]
	return("Seznam: " + hlavni_zprava_seznam.get_text().strip())


#ct24
def ct24():
	get_ct24 = requests.get("https://ct24.ceskatelevize.cz/") 
	source_ct24 = get_ct24.content
	soup_ct24 = BeautifulSoup(source_ct24, features="html.parser")
	h2_ct24 = soup_ct24.find_all("h2")
	#print(h2_ct24)
	if (h2_ct24[2].get_text().strip() == "COVID-19 v ČR"):
        hlavni_zprava_ct24 = h2_ct24[3]
    else:
        hlavni_zprava_ct24 = h2_ct24[2]
	return( "ČT24: " + hlavni_zprava_ct24.get_text().strip())

irozhlas()
seznam()
ct24()



#print (time_now)
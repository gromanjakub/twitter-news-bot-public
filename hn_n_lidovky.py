import requests
from bs4 import BeautifulSoup

#iHNed
def HN():
    get_HN = requests.get("https://ihned.cz/")
    source_HN = get_HN.content
    soup_HN = BeautifulSoup(source_HN, features="html.parser")#, "lxml")
    h2_HN = soup_HN.find_all("h2")
  #v souvislosti s koronakrizí a snahou HN pomoct firmám a OSVČ, jsem musel udělat workaround
    if "Hledám pomoc, jak zvládnout virovou krizi" in h2_HN[0]:
        hlavni_zprava_HN = h2_HN[1]
    else:
    	hlavni_zprava_HN = h2_HN[0]
    return( "iHNed: " + hlavni_zprava_HN.get_text().strip())

#denik N
def DenikN():
    get_N = requests.get("https://denikn.cz/")
    source_N = get_N.content
    soup_N = BeautifulSoup(source_N, features="html.parser")
    h3_N = soup_N.find_all("h3")
#print(h3_N)
    hlavni_zprava_N = h3_N[0]
    hlavni_zprava_N_cleaned1 = hlavni_zprava_N.get_text()[:-20]
    cabrio = hlavni_zprava_N_cleaned1.find("cabrioST") # z nějakého záhadného důvodu se to vždycky přidalo do nadpisu, tak to prostě ručně vyndám
    if cabrio > 0:
        hlavni_zprava_N_cleaned = hlavni_zprava_N_cleaned1[:cabrio] #titulek jen po cabrio
    else:
        hlavni_zprava_N_cleaned = hlavni_zprava_N_cleaned1  
    odpad = "if (typeof" #z nějakého ještě záhadnějšího důvodu se tam najednou začalo přidávat i tohle. tak jsem to taky vyndal
    if odpad not in hlavni_zprava_N_cleaned:
        pass
    else:
        hlavni_zprava_N_cleaned = hlavni_zprava_N_cleaned.replace(odpad, " ")
        
    return("Deník N: " + hlavni_zprava_N_cleaned)

#lidovky
def Lidovky():
    get_LN = requests.get("https://www.lidovky.cz/") 
    source_LN = get_LN.content
    soup_LN = BeautifulSoup(source_LN, features="html.parser")
    h1_LN = soup_LN.find_all("h1")
    hlavni_zprava_LN = h1_LN[1]
    return("Lidovky: " + hlavni_zprava_LN.get_text().strip())

HN()
DenikN()
Lidovky()
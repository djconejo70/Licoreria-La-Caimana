import requests 
from bs4 import BeautifulSoup
import re
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings

def valorDolar():
    disable_warnings(InsecureRequestWarning)
        
    try:        
        # print("aqui")
        url='https://www.bcv.org.ve/'        
        html_text=requests.get(url, verify=False).text
        html_text=requests.get(url, verify=False).text
        soup=BeautifulSoup(html_text,'html.parser')
        price_with_dolar=soup.find('div', { "id": "dolar","class":"col-sm-12 col-xs-12"})
        price_with_euro=soup.find('div', { "id": "euro","class":"col-sm-12 col-xs-12"})
        fecha=soup.find('span', {"class":"date-display-single"})
        # print("1",price_with_dolar,price_with_euro)
        price_with_dolar1=price_with_dolar.strong
        price_with_euro1=price_with_euro.strong
        fecha1=str(fecha)        
        a1=str(price_with_dolar1)
        a=a1[9:16]
        b1=str(price_with_euro1)
        b=b1[9:16]        
        c2=fecha1[113:140]        
        if c2.find("</span>"):
            c1=c2.replace("</span>", "")
            c2=c1
        if c2.find("/span>"):
            c1=c2.replace("</span", "")
            c2=c1
        if c2.find("span>"):        
            c1=c2.replace("</spa", "")
            c2=c1
        if c2.find("pan>"): 
            c1=c2.replace("</sp", "")
            c2=c1
        if c2.find("an>"):
            c1=c2.replace("</s", "")
            c2=c1
        if c2.find("n>"):
            c1=c2.replace("</", "")
            c2=c1
        if c2.find(">"):
            c1=c2.replace("<", "")
            c2=c1
        c=c2
        
    except:
        # print(e)
        a=0.0
        b=0.0
        c=0.0
        
    
    return a,b,c

# x=valorDolar()
# a=x[0]
# b=x[1]
# c=x[2]
# print("a", a,b,c)


    


    
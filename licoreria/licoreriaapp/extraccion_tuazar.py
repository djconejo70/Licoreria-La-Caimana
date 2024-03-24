import requests 
from bs4 import BeautifulSoup
import re
import pandas as pd


datos=pd.read_excel('D:/Licoreria/licoreria/lotoactivo.xlsx', header=None)
url=requests.get('https://www.tuazar.com/loteria/animalitos/resultados/')
soup = BeautifulSoup(url.content, "html.parser")
resultado_loto=[]
resultado_granja=[]
resultado_loto_numerico=[]
elementos=soup.find_all('div', class_="col-xs-6 col-sm-3")
c=0
for elementos_div in elementos:
    x = elementos_div.find('span')
    c=c+1
    if x and (c>12 and c<24):
        resultado_loto.append(x.text.strip())        
    if x and (c>23 and c<36):
        resultado_granja.append(x.text.strip())

for animales in resultado_loto:   
    resultado_loto_numerico.append(re.findall('\d+', animales))
lista=[]   
for valores in resultado_loto_numerico:
    for numeros in valores:
        lista.append(numeros)    
df=pd.DataFrame(lista)
a=pd.concat([datos, df], axis=0)
a.to_excel('D:/Licoreria/licoreria/lotoactivo.xlsx', sheet_name='Hoja1', index=None)


datos_granja=pd.read_excel('D:/Licoreria/licoreria/Granja.xlsx', header=None)
resultado_granja_numerico=[]
for animales in resultado_granja:   
    resultado_granja_numerico.append(re.findall('\d+', animales))
lista_granja=[]   
for valores in resultado_granja_numerico:
    for numeros in valores:
        lista_granja.append(numeros)    
df=pd.DataFrame(lista_granja)
a=pd.concat([datos_granja, df], axis=0)
a.to_excel('D:/Licoreria/licoreria/Granja.xlsx', sheet_name='Hoja1', index=None)




print('LotoActivo')
print(lista)
print('Granja')
print(lista_granja)
         
       







# br_items=soup.find_all('br')
# for br in br_items:
#     resultado=br.find(class_='visible-xs-block').text
#     if resultado:
#         print(resultado)
    


# codigo= soup.find_all("br", {"class":"visible-xs-block"}).br
# for br in codigo:
#     print(br, codigo)


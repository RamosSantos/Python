import urllib.request
import sqlite3
import re
import json

#requisição da URL    
pagina= urllib.request.urlopen('http://economia.terra.com.br/stock/divisas.aspx/tiposdolar.aspx')
texto=pagina.read().decode(pagina.headers.get_content_charset())

#Crawler de maneira simples usando posicionamento dos elementos no site
cotaComercial=texto[29199:29215]
cotaTurismo=texto[29655:29669]
cotaPtax=texto[30125:30140]

def search(a,b,c):#Limpa o texto e retorna os dados necessarios
    er=re.compile(r'[a-z< >/\n\r]',re.I)
    cotaComercial= er.sub('',a)
    cotaTurismo=er.sub('',b)
    cotaPtax=er.sub('',c)
    data={'Comercial':cotaComercial,'Turismo':cotaTurismo,'Ptax':cotaPtax}
    return data

def dataentry(data):
    storage=json.dumps(data,sort_keys=True,indent=5,separators=(',', ':'))
    f=open('storage.json','w')
    f.write(storage)
    f.close()
        


if __name__=="__main__":
    dataentry(search(cotaComercial,cotaTurismo,cotaPtax))
    

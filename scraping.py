__author__ = 'Josue Hernandez'

from bs4 import BeautifulSoup
import requests
import csv
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

data = []
URL = "http://jarroba.com/"

req = requests.get(URL)

status_code = req.status_code
if status_code == 200:
    print("Status Code... %d" % status_code)
    html = BeautifulSoup(req.text, "html.parser")

    entradas = html.find_all('div', {'class': 'col-md-4 col-xs-12'})

    for i, entrada in enumerate(entradas):
        titulo = entrada.find('span', {'class': 'tituloPost'}).getText()
        autor = entrada.find('span', {'class': 'autor'}).getText()
        fecha = entrada.find('span', {'class': 'fecha'}).getText()
        data.append((titulo,autor,fecha))

        print("%d - %s  |  %s  |  %s" % (i + 1, titulo, autor, fecha))

else:
    print("Status Code... %d" % status_code)

with open('newfile.csv', 'wb') as result:
    writer = csv.writer(result, dialect='excel')
    writer.writerows(data)

'''
    Descripcion: Consumiendo API con Python
    Autor: Bryan Adrian Reyes Ibarra
    Fecha: 20 de octubre 2023

'''

import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Dolores Hidalgo"
dest = "San de Allende"
key = "O5CMuqQZ1j0AtUnjztO0XB1FtjkKOUvY"

url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest}) 
json_data = requests.get(url).json()
print(json_data['route']['sessionId'])

#Extraer distancia y el tiempo

#


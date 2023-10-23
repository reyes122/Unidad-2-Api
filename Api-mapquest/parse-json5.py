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

#Extrae la distancia y tiempo
print(json_data['route']['distance'])
print(json_data['route']['time'])
#Extrae del primer elemento Legs el campo formattedTime
formatted_time = json_data['route']['legs'][0]['formattedTime']
print(formatted_time)

print("URL: " + (url))

json_data = requests.get(url).json()
json_status = json_data["info"]["statuscode"]

if json_status == 0:
    print("API Status: " + str(json_status) + " = A successful route call.\n")
    
if json_status == 0:
    print("API Status: " + str(json_status) + " = A successful route call.\n")
    print("=============================================")
    print("Directions from " + (orig) + " to " + (dest))
    print("Trip Duration:   " + (json_data["route"]["formattedTime"]))
    print("Miles:           " + str(json_data["route"]["distance"]))
    print("Kilometers:      " + str((json_data["route"]["distance"])*1.61))
    #print("Fuel Used (Ltr): " + str((json_data["route"]["fuelUsed"])*3.78))
    print("=============================================")

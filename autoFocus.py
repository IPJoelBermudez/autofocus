"""
    Este script está diseñado para realizar un autoenfoque en las cámaras a horas específicas. 

    Configuración:
    - Edita el archivo `credentials.json` para establecer las horas de enfoque y las credenciales del LPR.
    - Las horas deben especificarse en formato de 24 horas, de la siguiente manera:
    
    json
    "Horas de enfoque": ["06:01", "10:36", "15:01", "18:01"]
"""

import requests
import time
from requests.auth import HTTPDigestAuth
import json
import schedule

def enfocar(user, password, ip):
    # Es importante que la camara tenga activado la Autenticacion "digest/basic"
    # configuracion - red - Servicio de Red  - HTTPS(S) - Autenticación WEB - Modo de autenticación = digest/basic
    url_base = f"http://{ip}/ISAPI"

    # Mando una secuencia de reinicio del lente 
    requests_data = [ 
        {"url": f"{url_base}/System/Video/inputs/channels/1/focus", "xml_data": '<?xml version="1.0" encoding="UTF-8"?><FocusData><focus>0</focus></FocusData>'},
        {"url": f"{url_base}/PTZCtrl/channels/1/continuous", "xml_data": '<?xml version="1.0" encoding="UTF-8"?><PTZData><zoom>0</zoom></PTZData>'},
        {"url": f"{url_base}/PTZCtrl/channels/1/onepushfoucs/reset", "xml_data": ""}
    ]

    # Recorremos las requests
    for request_data in requests_data:
        url = request_data["url"]
        xml_data = request_data["xml_data"]
        headers = {'Content-Type': 'text/xml'}
        # Y la mandamos
        response = requests.put(url, headers=headers, data=xml_data,auth=HTTPDigestAuth(user,password))
        print(f"[ENFOCANDO] {ip} {request_data}")

def main():

    # Obtengo las credenciales
    with open('./credentials.json') as f:
        credenciales      = json.loads(f.read())
    
    
    # Obtengo los valores correspondientes de las credenciales
    user     = credenciales['lpr']['user']
    password = credenciales['lpr']['password']
    ip       = credenciales['lpr']['ip']

    # Y las horas de enfoque
    horas_enfoque = credenciales['lpr']['Hora de enfoque']

    # Programo un enfoque segun la hora correspondiente
    for hora_enfoque in horas_enfoque:
        schedule.every().day.at(hora_enfoque).do(enfocar,user,password,ip)

    
    # Este bucle esta al pendiente de las tareas creada
    while True:
        # Cuando llega la hora las ejecuta
        schedule.run_pending()
        time.sleep(1)


if (__name__ == "__main__"):
    main()


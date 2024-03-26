import smtplib
import time
import requests
from datetime import datetime
from constants import *


#latitud y longitud de sapporo, mi posicion
MY_LAT = 	43.066671 
MY_LONG = 141.35 

my_email = EMAIL
my_password = PASSWORD


# Current Location of the International Space Station (ISS),  It returns the current latitude and longitude of the space station
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()


#convertimos el resultado en formato json
data = response.json()


#latitud y longitud el  International Space Station (ISS)
iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


#paso mi posicion como parametru, los parametros que recibe la API, se encuentran en su documentacion
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0, #para poder tener la hora del sunset y sunrise en formato 24 hours
}


#para mi posicion averiguamos el sunset y el sunrise, esta en formato 24 hours, UTC time
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)


response.raise_for_status()


data = response.json()
print(f"All data from the sunset-sunrise-api: {data}")


#sunrise and sunset de mi posision, en formato 24 hours , y formato UTC time
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
print(f'the sunset UTC time {sunset}')


#como el sunset y sunrise esta en formato UTC los convierto a formato hora local japon
sunset_local=sunset+9
sunrise_local=(sunrise+9)-24
print(f'sunset  formato hora local {sunset_local}')

#para saber los datos de fecha actual, mes, dia, hora etc...
time_now = datetime.now()


#la hora actual, formtato 24 hours
time_now_hour=time_now.hour
print(f'hora actual {time_now_hour}')


#Deseo que mi codigo corra cada 60 segundos 
while True:
    time.sleep(60)

    #TODO: averigurar si el ISS, esta cerca ami posicion, 
    if abs(MY_LAT-iss_latitude)<=5 and abs(MY_LONG-iss_longitude)<=5:
        
        #TODO:averiguar si actualmente esta oscuro es decir 'sunset', para poder mirar el ISS
        if time_now_hour>sunset_local or time_now_hour<sunrise_local:
            
            #EL ISS esta sobre mi cicudad, por lo tanto nos enviamos un correo avizandonos que es visible
            with smtplib.SMTP('smtp.gmail.com', 587) as connection:
                
                #para seguridad
                connection.starttls()
                
                #login
                connection.login(my_email, my_password)
                
                
                message='subject:  (ISS) is visible \n\nthe The nternational Space Station is visible now'
                
                
                connection.sendmail(my_email, "bardack134@gmail.com", message)
                
                




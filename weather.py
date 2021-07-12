# from typing_extensions import final
import requests, json
import datetime
import time

BASE_URL = "https://api.openweathermap.org/data/2.5/forecast?"
API_KEY = "967ceca5dfb9d8a4dba23010c6e885a3"
print('1 -> Get Weather\n2 -> Get Wind Speed\n3 -> Get Pressure\n0 -> Exit')
OPTION = int(input())
while OPTION != 0:
    print("Enter City")
    CITY = input()
    print("Enter Day-Month-Year")
    date=input().split("-")
    day=date[0]
    month=date[1]
    year=date[2]
    finaldate= year+"-"+month+"-"+day
    print(finaldate)
    URL = BASE_URL + "q=" + CITY + "&units=metric&appid=" + API_KEY
    response = requests.get(URL)
    # print(response)
    # getting data in the json format
    data = response.json()
    # print(data)
    for item in data['list']:
        time = item['dt_txt']
        next_date, hour = time.split(' ')
        # print(next_date)
        if finaldate == next_date:
            # getting the main dict block
            main = item['main']
            # getting temperature
            temperature = main['temp']
                    
                    # weather report
            if OPTION == 1:
                # report = item['weather']
                # print(item['weather'][0]['description'])
                print(f"Weather Report: {item['weather'][0]['description']}\nTemperature(Cel): {item['main']['temp']}")
                break;
            if OPTION == 2:
                wind = item['wind']
                speed = wind['speed']
                print(f"Wind Speed: {speed}")
                break;
            if OPTION == 3:
                # getting the pressure
                pressure = main['pressure']
                print(f"Pressure(hPa): {pressure}")
                break;

                # else :
                #     # showing the error message
                #     print("Error in the HTTP request")
                
    print('1 -> Get Weather\n2 -> Get Wind Speed\n3 -> Get Pressure\n0 -> Exit')
    OPTION = int(input())

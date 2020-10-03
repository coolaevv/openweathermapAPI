import requests
from pprint import pprint
from collections import OrderedDict

while True:
    print("Введите название, либо координаты(Широту и долготу, разделите запятой)")
    inData = input('=> ')

    api_key = "876423556a49ee06d1c76debbac3a8b7"


    def Main():
        if inData.isalpha():
            print('Погода в городе: ', inData)
            url = "http://api.openweathermap.org/data/2.5/forecast?q=" + inData + "&appid=" + api_key + ""
            connect = requests.get(url)
            data = connect.json()
            for i in data['list']:
                date = i['dt_txt'].split(" ")[0].replace("-",".")
                date = date.replace(date[:5], "")
                time = i['dt_txt'].split(" ")[1].replace("-",":")
                time = time[:5]
                temp = int(i['main']['temp']) - 273
                temp_min = int(i['main']['temp_min']) - 273
                print(date, " в ", time, " Средняя температура: ", temp, " Минимальная температура: ", temp_min)
        else:
            print('Погода в точке: ', inData)
            lat = inData.split(",")[0].replace(" ", "")
            lon = inData.split(",")[1].replace(" ", "")
            url = "http://api.openweathermap.org/data/2.5/forecast?lat=" + lat + "&lon=" + lon + "&appid=" + api_key +""
            connect = requests.get(url)
            data = connect.json()
            for i in data['list']:
                date = i['dt_txt'].split(" ")[0].replace("-",".")
                date = date.replace(date[:5], "")
                time = i['dt_txt'].split(" ")[1].replace("-",":")
                time = time[:5]
                temp = int(i['main']['temp']) - 273
                temp_min = int(i['main']['temp_min']) - 273
                print(date, " в ", time,  " Средняя температура: ", temp, " Минимальная температура: ", temp_min)
    Main()
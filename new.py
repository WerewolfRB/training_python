#============================================================
#Подключаем библиотеки

import urllib.request
import json
import sys
import os

# Формируем набор регионов
regionsList = {
  "краснодар": 1,
  "краснодарский край": 1,
  "республика адыгея": 1,
  "майкоп": 1,
  "москва": 2,
  "московская область": 2,
  "астрахань": 3,
  "астраханская область": 3
}

try:
  with open(sys.argv[1], "rb") as fileLink:
    # Формируем запрос
    url = urllib.request.Request("https://stt.api.cloud.yandex.net/speech/v1/stt:recognize?topic=general&format=lpcm&sampleRateHertz=8000&lang=ru-RU", data=fileLink.read())
    url.add_header("Authorization", "Api-Key *************************")

    # Выполняем запрос
    responseData = urllib.request.urlopen(url).read().decode('UTF-8')
    responseData = json.loads(responseData)
    responseRegion = responseData.get("result", "0").lower().strip();

    # Возвращем результат
    print(regionsList[responseRegion] if responseRegion in regionsList else 0, end="")
except Exception as e:
  print(0, end="")

#=========================================

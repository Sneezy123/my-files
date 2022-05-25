import requests

api_key = "caaf4f6774853b35a72638955f15e304"
city_name = input("Name der Stadt / Name des Ortes: ")
unit = input("Einheit der Temperatur: ")

try:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&lang=de"

    req = requests.get(url)
    data = req.json()

    lat = data["coord"]["lat"]
    lon = data["coord"]["lon"]
    exclude = "minutly,hourly"
except KeyError:
    print("Fehler: Name der Stadt / Name des Ortes ist unbekannt oder ungültig")
else:
    url2 = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={exclude}&appid={api_key}&lang=de"
    req2 = requests.get(url2)
    data2 = req2.json()

    days = []
    nights = []
    descr = []

    if unit.lower() == "c" or unit.lower() == "celsius" or unit.lower() == "°c":
        for i in data2["daily"]:
            days.append(round(i["temp"]["day"] - 273.15, 2))

            nights.append(round(i["temp"]["night"] - 273.15, 2))

            descr.append(i["weather"][0]["description"].title())

        string = f"\n\n[{data['name']}, {data['sys']['country']} - 7 Tage Wettervorhersage]\n"

        for i in range(len(days)):

            if i == 0:
                string += f"\nTag {i+1} (Heute):\n"
            elif i == 1:
                string += f"\nTag {i+1} (Morgen):\n"
            else:
                string += f"\nTag {i+1}:\n"

            string += "Temperatur tagsüber: " + str(days[i]) + "°C" + "\n"
            string += "Temperatur nachts: " + str(nights[i]) + "°C" + "\n"
            string += "Wetter: " + str(descr[i]) + "\n"

        print(string)
    elif unit.lower() == "f" or unit.lower() == "fahrenheit" or unit.lower() == "°f":
        for i in data2["daily"]:
            days.append(round((i["temp"]["day"] - 273.15) * 1.8 + 32, 2))

            nights.append(round((i["temp"]["night"] - 273.15) * 1.8 + 32, 2))

            descr.append(i["weather"][0]["description"].title())

        string = f"\n\n[{data['name']}, {data['sys']['country']} - 7 Tage Wettervorhersage]\n"

        for i in range(len(days)):

            if i == 0:
                string += f"\nTag {i+1} (Heute):\n"
            elif i == 1:
                string += f"\nTag {i+1} (Morgen):\n"
            else:
                string += f"\nTag {i+1}:\n"

            string += "Temperatur tagsüber: " + str(days[i]) + "°F" + "\n"
            string += "Temperatur nachts: " + str(nights[i]) + "°F" + "\n"
            string += "Wetter: " + str(descr[i]) + "\n"

        print(string)
    else:
        for i in data2["daily"]:
            days.append(round(i["temp"]["day"] - 273.15, 2))

            nights.append(round(i["temp"]["night"] - 273.15, 2))

            descr.append(i["weather"][0]["description"].title())

        string = f"\n\n[{data['name']}, {data['sys']['country']} - 7 Tage Wettervorhersage]\n"

        for i in range(len(days)):

            if i == 0:
                string += f"\nTag {i+1} (Heute):\n"
            elif i == 1:
                string += f"\nTag {i+1} (Morgen):\n"
            else:
                string += f"\nTag {i+1}:\n"

            string += "Temperatur tagsüber: " + str(days[i]) + "°C" + "\n"
            string += "Temperatur nachts: " + str(nights[i]) + "°C" + "\n"
            string += "Wetter: " + str(descr[i]) + "\n"

        print(string)

from bs4 import BeautifulSoup
import requests

print("---------------------------------------")
country = input("Country : ")
city = input("City : ")
url = f"https://www.google.com/search?q=weather-{city}-{country}"

try:
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")
    blocs = doc.find_all(class_="kCrYT")

    bloc_1 = blocs[0]
    city = bloc_1.text.split(" / ")[0]

    bloc_2 = blocs[1]
    text = bloc_2.text.split("\n")
    t = text[0].split("\xa0")
    date = t[1][2:]
    temp = t[0] + t[1][0:2]
    weather = text[1].replace("weather.com", "")

    print("---------------------------------------------------------------")
    print(city, "|", date, "|", temp, "|", weather)
    print("---------------------------------------------------------------")

except Exception as e:
    print("Error")

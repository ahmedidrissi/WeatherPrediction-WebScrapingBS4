from bs4 import BeautifulSoup
import requests

print("---------------------------------------")
country = input("Country : ")
city = input("City : ")
print("---------------------------------------")

try:
    url = f"https://www.timeanddate.com/weather/{country}/{city}"

    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")
    bloc = doc.find(class_="bk-focus")

    bloc_qlook = bloc.find(class_="bk-focus__qlook")
    current_data = []
    current_data.append("Temperature: " + bloc_qlook.find(class_="h2").text.replace("\xa0", ""))
    current_data.append("Weather: " + bloc_qlook.find("p").text)
    tags = bloc_qlook.find("p").next_sibling.next_sibling
    for tag in tags:
        text = tag.text.replace("\xa0", "")
        if text != "": current_data.append(text)
    
    current_data = current_data[:4] + [current_data[4] + current_data[5] + current_data[6]] + current_data[7:]

    bloc_info = bloc.find(class_="bk-focus__info")
    table = bloc_info.find("tbody")
    for tag in table:
        current_data.append(tag.text.replace("\xa0", ""))

    for info in current_data:
        print(info)
    
    print("---------------------------------------")
    
except Exception as e:
    url = f"https://www.google.com/search?q=weather-{city}-{country}"
    
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

except :
    print("Error")

from bs4 import BeautifulSoup
import requests

print("---------------------------------------")
country = input("Country : ")
city = input("City : ")
url = f"https://www.timeanddate.com/weather/{country}/{city}"
print("---------------------------------------")

try:
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
    print("Error")

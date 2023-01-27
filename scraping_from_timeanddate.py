from bs4 import BeautifulSoup
import requests

print("---------------------------------------")
country = "morocco" #input("Country : ")
city = "rabat" #input("City : ")
url = f"https://www.timeanddate.com/weather/{country}/{city}"

try:
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")
    bloc = doc.find(class_="bk-focus")

    bloc_qlook = bloc.find(class_="bk-focus__qlook")
    current_data = []
    current_data.append(bloc_qlook.find(class_="h2").text.replace("\xa0", ""))
    current_data.append(bloc_qlook.find("p").text)
    tags = bloc_qlook.find("p").next_sibling.next_sibling
    for tag in tags:
        text = tag.text.replace("\xa0", "")
        if text != "": current_data.append(text)

    print(current_data)

    #bloc_info = bloc.find(class_="bk-focus__info")
    
    #temp = doc.find_all(text = re.compile("\°C.*"), limit=1)

    

except Exception as e:
    print("Error")
from bs4 import BeautifulSoup
import requests

country = "Morocco"
city = "Casablanca"
url = f"https://www.google.com/search?q=weather-{city}-{country}"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")
bloc = doc.find_all(class_="kCrYT")
print("\n----------------------------------------\n")
print(bloc[0].text)
print("\n----------------------------------------\n")
print(bloc[1].text)
print("\n----------------------------------------\n")
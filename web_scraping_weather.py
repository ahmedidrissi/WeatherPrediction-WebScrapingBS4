from bs4 import BeautifulSoup
import requests

country = "morocco"
city = "casablanca"
url = f"https://www.google.com/search?q=weather-{city}-{country}"

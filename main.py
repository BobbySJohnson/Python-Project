# Importing important libraries
import requests
from bs4 import BeautifulSoup



soup = BeautifulSoup(
    requests.get("https://distrowatch.com/").content,
    "html.parser")



top_ten_distros = []
distro_tds = soup("td", class_="phr2", limit=10)
for td in distro_tds:
    top_ten_distros.append(td.find("a").contents[0])

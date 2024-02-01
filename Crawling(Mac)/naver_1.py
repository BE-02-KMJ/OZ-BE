import requests
from bs4 import BeautifulSoup

url = "https://www.naver.com"

req = requests.get(url)
# print(req)

html = req.text
soup = BeautifulSoup(html, "html.parser")
query = soup.select_one("#query")
print(query)
import requests
from bs4 import BeautifulSoup

url = "http://mfd.ru/currency/?currency=USD"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
table = soup.find_all("table", {"class": "mfd-currency-table"})[0]
rows = table.find_all("tr")

title = ['Дата', 'Курс рубля к доллару', 'Изменение']
print(title[0] + 7 * " ", title[1] + " ", title[2])
for i in range(40, 0, -1):
    cells = rows[i].find_all('td')
    if len(cells) > 0:
        print(cells[0].text.strip()[2:] + " ", cells[1].text.strip() + " " * 14, cells[2].text.strip())

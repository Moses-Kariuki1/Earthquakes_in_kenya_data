import requests
from bs4 import BeautifulSoup

url = "https://earthquaketrack.com/p/kenya/recent"

results = requests.get("https://earthquaketrack.com/p/kenya/recent")

src = results.content

soup = BeautifulSoup(src, 'lxml')

yester = soup.find('div', class_='alert alert-warning noteworthy')
#headline = yester.h4.a.text
# print(headline)

summary = soup.find('ul', class_='list-unstyled')
summary_order = summary.text
print('Number of earthquakes in Kenya...' +summary_order)

biggest = soup.find('div', class_='text-warning')
big_earth = biggest.text
print('The biggest earthquake in Kenya recently'+big_earth)

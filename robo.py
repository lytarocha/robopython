import requests
from bs4 import BeautifulSoup


site= requests.get("https://www.imdb.com/chart/top/") 

html = site.content
print(html)
soup = BeautifulSoup(html, 'lxml')

tbody = soup.find('tbody', {'class': 'lister-list'})

tr = tbody.find('tr')

td= tr.find('td',{'çlass': 'titleColumm'})
a= td.find('a')

print(a.text)


import requests
from bs4 import BeautifulSoup as bs


url = 'https://brasil.io/dataset/documentos-brasil/documents/'

data = requests.get(url).text

parsed = bs(data, 'html.parser')

tr = parsed.find_all('tr')

result = [ele.next for ele in ([x.a for x in tr]) if ele != None ]

print(result)

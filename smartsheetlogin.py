import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
r=requests.get('https://app.smartsheet.com/workspaces/gqG3Vj3rhJ4h4XPcxQmFXXhg7j7jh2W2R6FWrF71', headers=headers)

print(r.text)
from bs4 import BeautifulSoup
import requests as r

result = r.get('https://divar.ir/s/tehran');
soup = BeautifulSoup(result.text, 'html.parser')
els = soup.findAll('div',attrs={'class':'kt-post-card__description'})
for el in els:
  if el.text == "توافقی":
    value = reversed(el.previous_sibling.text)
    print(''.join(value))
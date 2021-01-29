import os
import requests
from bs4 import BeautifulSoup

os.system("clear")
url = "https://www.iban.com/currency-codes"

def machine():
  request = requests.get(url)
  soup = BeautifulSoup(request.text,'html.parser')

  table = soup.find("table", {"class":"table table-bordered downloads tablesorter"})
  tds = table.find_all('td')
  
  fir_list = []
  country = []
  currency = []
  code = [] 
  

  for first in tds:
    first = str(first)
    first = first.replace('<td>','').replace('</td>','')
    fir_list.append(first)
  for idx, val in enumerate(fir_list):
    if idx % 4 == 0:
      country.append(val)
    elif idx % 4 == 1:
      currency.append(val)
    elif idx % 4 == 2:
      code.append(val)
    else:
      pass
  country_info = list(zip(country,code))
  for sift in country_info:
    if '' in sift:
      country.remove(sift[0])
      code.remove(sift[1])
    else:
      pass
  n = len(country)
  
  for run in range(n):
    print(f"# {run} {country[run]}")
  answer(country,code) 



def main():
  print("Hello! Please choose select a country by number.")
  machine()

def answer(cnt,cod):
  try:
    ans = int(input("#: "))
    if ans >= 0 and ans <= 267:
      print(f"You choose {cnt[ans]}")
      print(f"The currency code is {cod[ans]}")
    else:
      print("Choose a number from the list.")
      return answer(cnt,cod)

  except:
    print("That wasn't a number.")
    return answer(cnt,cod)

    
main()

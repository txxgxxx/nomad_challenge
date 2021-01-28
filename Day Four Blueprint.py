import os
import requests
start = True
while start == True:
  print("Welcome to IsItDown.py!")
  url = input(str("Please write a URL or URLs you want to check. (separated by comma) \n")).split(',')
  
  
  def restart():
    global start
    result = input(str("Do you want to start over? y/n \n"))
    if result == 'y': 
      os.system('clear')
    elif result == 'n':
      print("ok, bye!")
      start = result
    else:
      print("That's not a valid answer.")
      return restart()

    
  for link in url:
    link = link.strip()
    finding = len(link) - 4
    will_find = '.com'
    com = link.find(will_find,finding)
    if com != -1 :
      if 'http' not in link:
        try:
          link = 'http://' + link
          url_link = requests.get(link)
          check = url_link.status_code
          if check == 200:
            print(f"{link} is up!")
          elif check == 404:
            print(f"{link} is down!")
        except:
          print(f"{link} is down!")
      else:
        try:
          url_link = requests.get(link)
          check = url_link.status_code
          if check == 200:
            print(f"{link} is up!")
          elif check == 404:
            print(f"{link} is down!") 
        except:
          print(f"{link} is down!")   
    else:
      print(f"{link} is not a valid URL.")
  
  restart()

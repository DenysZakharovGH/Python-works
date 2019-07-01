#AIzaSyB84uRYc9lZMl8uGRx2oeT11vkAEli7F80
#selenium 
from bs4 import BeautifulSoup
import requests
import time
query = input('What are you searching for?:   ' )
url ='http://www.google.com/search?q='
page = requests.get(url + query + "download torrent")
soup = BeautifulSoup(page.text, "html.parser")
h3 = soup.find_all("a")
links_array =[]
for elem in h3:
    #https://www.youtube.com/
    link=("https://www.google.com" + elem["href"])
    if "/url?q=https://" in link and "youtube" not in link :
        links_array.append(link)
time.sleep(5)
for link in links_array:
    try:
        time.sleep(5)
        page = requests.get(link) 
        soup = BeautifulSoup(page.text, "html.parser")
        h3 = soup.find_all("a")
        print(h3)
        for elem in h3:
            if "download" in elem or "torrent" in elem:
                print("------------------------------------------------------------------------------------------------------------")
                print(elem)
                
    except requests.exceptions.ConnectionError:
        print("Connection error")
   



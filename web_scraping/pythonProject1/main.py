import requests
from bs4 import BeautifulSoup

movies_response= requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
# print(movies_response.text)
soup=BeautifulSoup(movies_response.text,"html.parser")
titles= [soup.getText() for soup in soup.find_all("h3",class_="title")]
title_list_in_order=titles[::-1]

with open("movies.txt","w") as file:
    for movie in title_list_in_order:
        file.write(f"{movie}\n")
from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

movies_name = soup.find_all(name="h3", class_="title")

movie_list = []

for movie in movies_name:
    my_list = movie.getText()
    movie_list.append(my_list)

movie_list.reverse()

with open("movies_list.txt", "w") as file:
    for movie in movie_list:
        file.write(f"{movie}\n")








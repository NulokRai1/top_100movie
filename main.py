from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
website_data = response.text

soup = BeautifulSoup(website_data, "html.parser")
website_list = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__hW_Kn")
all_movies = []
for movie in website_list:
    all_movies.append(movie.getText())

all_movies.reverse()
print(all_movies)

with open("100_movies.txt", mode="w") as file:
    for movie in all_movies:
        file.write(f"{movie}\n")



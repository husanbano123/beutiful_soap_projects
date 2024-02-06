from bs4 import BeautifulSoup
import requests

url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response=requests.get(url)
#print(response.text)

web_page=response.text
soup=BeautifulSoup(web_page,'html.parser')
#print(soup.title)

movie_title=soup.find_all(name='h3',class_='title')
for i,title in enumerate(reversed(movie_title),start=1) :
    text=title.getText().strip()
    print(text)





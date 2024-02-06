from bs4 import BeautifulSoup
import requests

response=requests.get("https://news.ycombinator.com/")
#print(response.text)

yc_web_page=response.text
soup=BeautifulSoup(yc_web_page,'html.parser')
print(soup.title)

anchor_tag_Articles=soup.find_all(name="a")
#print(anchor_tag_Articles)
article_text=[]
article_link=[]
for i in anchor_tag_Articles:
    text=i.getText()
    article_text.append(text)
    links=i.get('href')
    article_link.append(links)

article_votes=[int(score.getText().split()[0]) for score in soup.find_all(name="span",class_="score")]
largest_number=max(article_votes)
#print(largest_number)
largest_index=article_votes.index(largest_number)
#print(largest_index)
print(article_text[largest_index])
print(article_link[largest_index])
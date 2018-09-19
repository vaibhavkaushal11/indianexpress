from bs4 import BeautifulSoup
import requests

res = requests.get('https://www.news18.com/')
soup = BeautifulSoup(res.text , 'lxml')

news_go = soup.find('ul', {'class' : "lead-mstory"})
all_news = news_go.find_all('a')

for news in all_news:
 	print(news.text)
 	print('')
 	
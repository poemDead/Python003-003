import requests
from bs4 import BeautifulSoup as bs
from time import sleep
import pandas as pd

#获取电影详细信息功能
def get_movie_info(file_url):

    #抓取网页
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
    headers = {'user-agent':user_agent}
    r = requests.get(url, headers=headers)
    #bs解析网页
    bs_info = bs(r.text, 'html.parser')
    #电影标题
    movie_title = bs_info.find('h1',attrs={'class':'name'}).text
    #电影类型
    movie_genre = ''
    for genre in bs_info.find_all('a',attrs={'class':'text-link'}):
        movie_genre += genre.text
    movie_genre = movie_genre.strip()
    #电影上映日期
    movie_date = bs_info.find_all('li',attrs={'class':'ellipsis'})[-1].text[:10]

    movie_info = [movie_title,movie_genre,movie_date]
    print(movie_info)
    top10list.append(movie_info)
    print('ok')

#抓取前十电影链接
url = 'https://maoyan.com/films?sortId=3'

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'

headers = {'user-agent':user_agent}

r = requests.get(url, headers=headers)

bs_info = bs(r.text, 'html.parser')

urls = []
for tags in bs_info.find_all('div',attrs={'class':'movie-item film-channel'},limit=10):
    urls.append(f'https://maoyan.com' + tags.find('a').get('href'))

sleep(10)

#抓取前十电影信息
top10list = []

for url in urls:
    get_movie_info(url)
    sleep(10)

#保存到文件
maoyan_top10 = pd.DataFrame(data = top10list)
maoyan_top10.to_csv('./maoyanTop10.csv',encoding='utf-8',index=False,header=False)


'''
本地网页测试
with open('c:/Users/mcrim/Desktop/GeekPython/maoyan-jingdian.html',encoding='utf-8') as page:
        page_content = page.read()

def get_urls(page_content):
    bs_info = bs(page_content, 'html.parser')

    # 前十个电影的链接：
    urls = []
    for tags in bs_info.find_all('div',attrs={'class':'movie-item film-channel'},limit=10):
        urls.append(tags.find('a').get('href'))
    
    return urls

with open('c:/Users/mcrim/Desktop/GeekPython/babai.html',encoding='utf-8') as page:
        page_content = page.read()

bs_info = bs(page_content, 'html.parser')
'''


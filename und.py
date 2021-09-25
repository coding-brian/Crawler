import htmlrequest

startpage=input('請輸入要抓的第幾頁數(請輸入大於0的數字):')


url=f'https://udn.com/tokyo2020/get_article/{str(startpage)}/0/index'
soup=htmlrequest.htmlparse(url)
newslist=soup.find_all(class_='story-list__news')

result=[]

for news in newslist:
    temp={'image':'','link':'','tag':'','time':'','title':''}

    # 圖案來源
    imagesrc=news.find(class_='story-list__image').find('img')['src']

    #文章內容來源
    link=news.find(class_='story-list__image').find_all('a')[1].get('href')

    #tag
    tag=news.find(class_='story-list__image').find_all('a')[0].getText()

    #時間
    time=news.find(class_='story-list__text').find(class_='story-list__time').getText()
    
    #title
    title=news.find(class_='story-list__text').find('h3').find('a').getText()

    temp['image']=imagesrc
    temp['link']='https://udn.com'+link
    temp['tag']=tag
    temp['time']=time
    temp['title']=title
    result.append(temp)


print(result)
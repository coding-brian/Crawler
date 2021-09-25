import requests
from bs4 import BeautifulSoup
import exportExcel

excelname=input('請輸入excel的名字:')
sheetname=input('請輸入excel中worksheet的名字:')

#頁數
pageNum=list(range(1,6))

#excel輸出
export=exportExcel.export

url='https://tw.noxinfluencer.com/youtube-channel-rank/top-100-id-film%20%26%20animation-youtuber-sorted-by-subs-weekly'
#網站的request請求
r=requests.get(url)

#html分析
html_doc=r.text
soup=BeautifulSoup(html_doc,'html.parser')

#整個表格
table=soup.find(class_='kol-table')

#表頭
thead=table.find('thead')
#基本資料
profile=thead.find(class_='profile')
#粉絲數
follower=thead.find(class_='follower')
#平均觀看量
avgView=thead.find(class_='avgView')
#Nox評級
noxscore=thead.find(class_='nox-score')

headers=(profile.getText(),follower.getText(),avgView.getText(),noxscore.getText())
dataList=[]

for page in pageNum:
    url='https://tw.noxinfluencer.com/youtube-channel-rank/_influencer-rank?country=id&category=film+%26+animation&rankSize=250&type=0&interval=weekly&pageNum={}&r=SpXqt%2BBX%2BUARz7fRmxYrUfOXQMXUfNU%2FjFub6My58NJGql3usQrfRq0yWJC4UIRirYpAmpHh95%2BUJu16ccndA7%2FOxiG4RM2PI67x8djWAP50%2FdJN5nijVRQca7Nm2D34%2B8xGXNBKpN3x68pqU79uQK%2Fy8A1RMe7rM7S5DVKaFjw%3D'.format(page)
    #網站的request請求
    r=requests.get(url)

    #html分析
    html_doc=r.text
    soup=BeautifulSoup(html_doc,'html.parser')

    #資料
    tbody=soup.find(id='rank-table-body')
    items=tbody.find_all('tr')

    for item in items:
       channelName=item.find(class_='name kol-name')
       followerNumber=item.find(class_='text followerNum with-num').find(class_='num')
       avgViewNumber=item.find(class_='text avgView with-num').find(class_='num')
       noxscore=item.find(class_='text nox-score').get('data-score')
       data=[channelName.string,followerNumber.string,avgViewNumber.string,noxscore]
       dataList.append(data)
    #    print(channelName.string+' '+followerNumber.string+' '+ avgViewNumber.string+' '+noxscore)

export(headers,tuple(dataList),'印尼','結果1')
 

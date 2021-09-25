import requests
from bs4 import BeautifulSoup
import exportExcel

excelname=input('請輸入excel的名字:')
sheetname=input('請輸入excel中worksheet的名字:')

#頁數
pageNum=list(range(1,2))

#excel輸出
export=exportExcel.export

url='https://tw.noxinfluencer.com/youtube-channel-rank/top-100-id-film%20%26%20animation-youtuber-sorted-by-subs-weekly'
#網站的request請求
r=requests.get(url)

#html分析
html_doc=r.text
soup=BeautifulSoup(html_doc,'html.parser')

#整個表格
table=soup.find(class_='result-table-wrap')

#表頭
thead=table.find(class_='table-header')

#基本資料
profile=thead.find(class_='rank-desc')
#粉絲數
follower=thead.find(class_='rank-subs')
#平均觀看量
avgView=thead.find(class_='rank-avg-view')

headers=(profile.getText(),follower.getText(),avgView.getText())
dataList=[]

#資料
tbody=soup.find(id='table-body')
items=tbody.find_all(class_='table-line')

for item in items:
    channelName=item.find(class_='title pull-left ellipsis')
    followerNumber=item.find(class_='rank-cell pull-left rank-subs').find(class_='number')
    avgViewNumber=item.find(class_='rank-cell pull-left rank-avg-view').find(class_='number')
    data=[channelName.string,followerNumber.string,avgViewNumber.string]
    dataList.append(data)


export(headers,tuple(dataList),sheetname,excelname)
 

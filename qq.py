# import requests
# from bs4 import BeautifulSoup
import htmlrequest
import exportExcel


excelname=input('請輸入excel的名字:')
sheetname=input('請輸入excel中worksheet的名字:')

url=input("請輸入騰訊視頻的網址:")
soup=htmlrequest.htmlparse(url)
videolist=soup.find(class_="mod_column")
items=videolist.find(class_="figure_list").find_all(class_="list_item")
datalist=[]
for item in  items:
    title=item.find(class_='figure_detail_two_row').find(class_='figure_title').string
    number=item.find(class_='figure_num').find(class_='num').string
    print(str(title).encode('utf-8').decode('utf-8'))
    data=(title,number)
    datalist.append(data)

headers=('標題','觀看數')

exportExcel.export(headers,tuple(datalist),str(sheetname),str(excelname))
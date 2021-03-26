import requests as reqs
from bs4 import BeautifulSoup

r=reqs.get("http://210.70.80.21/~bs109021089/Publication.html")

r.encoding="utf-8"

print(r.status_code)

if r.status_code==200:
    #print(r.text)列印r裡面的資料
    soup=BeautifulSoup(r.text, "lxml")
    #print(soup)列印網址中所有的資料
    result1=soup.find_all("li")
    #print(result1)列印網址中有li的資料
    fp=open("out1.txt","w",encoding="utf-8")
    for val in result1:
        text1=val.text.replace('\n','')
        text2=text1.replace('  ','')
        print(text2)
        fp.write(text2+'\n')   
    fp.close()
else:
    print("oops")
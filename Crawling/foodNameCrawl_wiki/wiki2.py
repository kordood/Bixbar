import requests
from bs4 import BeautifulSoup
 
#url = 'https://ko.wiktionary.org/w/index.php?title=분류:한국어_음식'
url = 'https://en.wiktionary.org/w/index.php?title=Category:en:Foods'
res = requests.get(url)
html = res.text
bs = BeautifulSoup(html,'html.parser')
 
wordlist = bs.find_all('a','external text')
wordlist2 = []
 
for i in wordlist:
    word = i.get_text()
    wordlist2.append(word)
 
 
for i in wordlist2:
    #sUrl = 'https://ko.wiktionary.org/w/index.php?title=분류:한국어_음식&from='+i
    sUrl = 'https://en.wiktionary.org/w/index.php?title=Category:en:Foods&from='+i
    res = requests.get(sUrl)
    html = res.text
    bs = BeautifulSoup(html,'html.parser')
    print(i+ " 파싱완료")
    result = bs.find('div',{'id':'mw-pages'}).find('ul')
    result = result.find_all('a')
    
    for j in result:
        word = j.get_text()
        #with open('result.txt','a') as f:
        with open('result_en.txt','a', encoding="utf-8") as f:
            f.write(word+'\n')
            
    print(i+ " 기록완료")

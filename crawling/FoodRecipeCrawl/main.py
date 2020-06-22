from bs4 import BeautifulSoup
import requests
import crawling

page = 1

while True:
    url = 'https://www.10000recipe.com/recipe/list.html?order=reco&page=' + str(page)
    response = requests.get(url)
    source = response.text
    soup = BeautifulSoup(source, 'html.parser')
    print(page)

    tag1 = soup.body.find_all('div', attrs={'class': 'col-xs-3'})
    num = 1
    for tag2 in tag1:
        # if(tag2.find('a', attrs={'class': 'thumbnail'})['href'])
        try:
            newURL = 'https://www.10000recipe.com' + tag2.find('a', attrs={'class': 'thumbnail'})['href']
            print(newURL)
            print(num)
            num += 1
            crawling.getInfo(newURL)
        except:
            continue
    if num == 1:
        print(page)
        print('finish')
        break
    page += 1
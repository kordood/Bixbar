from selenium import webdriver
from urllib.request import urlopen
from bs4 import BeautifulSoup
import crawling

url = 'https://www.liquor.com/hub/cocktail-recipes/#gs.opmes6'

driver = webdriver.Chrome('/Users/hyeryeongsong/chromedriver') #빈 브라우저 띄움

driver.get(url)


# In[6]:


html = urlopen(url)
soupFirst = BeautifulSoup(html, 'html5lib')


# In[7]:


childUrls = []
tag1 = soupFirst.body.find_all('div', attrs={'class': 'row inner-content-width clearfix hub-slug'})
for tag2 in tag1:
    tag3 = tag2.find_all('div', attrs={'class': 'col-xs-6 col-sm-4'})
    for tag4 in tag3:
        childUrls.append(tag4.find('a', attrs={'class': 'overlay'})['href'])


# In[8]:


for i in range(len(childUrls)):
    if(childUrls[i][0] != 'h'):
        childUrls[i] = 'http://liquor.com' + childUrls[i]


# In[21]:


for currentURLs in childUrls:
    html = urlopen(currentURLs)
    soupSecond = BeautifulSoup(html, 'html5lib')
    if(currentURLs == 'http://liquor.com/mosaic/how-to-drink-at-your-labor-day-party/'):
        break
    print(currentURLs)
    currentUrls = []
    tag1 = soupSecond.body.find_all('a', attrs = {'class': 'overlay'})
    for tag2 in tag1:
        tmpUrl = tag2['href']
        if(tmpUrl[0] != 'h'):
            tmpUrl = 'http://liquor.com' + tmpUrl
        currentUrls.append(tmpUrl)
    for currentUrl in currentUrls:
        if(currentUrl != 'http://liquor.com/recipes/cucumber-fizz/'):
            if(currentUrl != 'http://liquor.com/sparkling-rose-margarita/'):
                if(currentUrl != 'http://liquor.com/articles/red-white-blue-cocktails/'):
                    print(currentUrl)
                    crawling.getInfo(currentUrl)

driver.close()
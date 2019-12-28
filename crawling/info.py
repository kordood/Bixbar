from selenium import webdriver
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import json
import os

url = 'https://www.liquor.com/mosaic/martini-recipes/#gs.nz35w3'

driver = webdriver.Chrome('/Users/hyeryeongsong/chromedriver') #빈 브라우저 띄움

driver.get(url)

## python 파일의 위치
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#BASE_DIR = os.path.dirname(os.path.abspath(''))


# In[355]:


sel_xpath = driver.find_element_by_xpath('/html/body/div[12]/div[1]/div[2]/div[1]/div[1]/a')
#print(sel_xpath.tag_name)
#print(sel_xpath.text)
sel_xpath.click()


# In[356]:


parent_window = driver.current_window_handle
all_windows = driver.window_handles
child_window = [window for window in all_windows if window != parent_window][0]
driver.switch_to.window(child_window)


# In[357]:


curr_url = driver.current_url
print(curr_url)
html = urlopen(curr_url)
soup = BeautifulSoup(html, 'html5lib')


# In[358]:


title = soup.body.find('div', attrs={'class': 'row head-row text-center'}).find('div', attrs={'class': 'col-xs-12'}).find('h1').text
print(title)


# In[359]:


imgUrl = soup.find('div', attrs = {'class': 'center-block img-hero heart-me'}).find("img")["src"]
imgUrl = 'https:' + imgUrl
print(imgUrl)


# In[360]:


all_ingredient = soup.body.find_all('div', attrs={'class': 'measure'})
ingredients_key = []
ingredients_value = []
for one_ingredient in all_ingredient:
    one_ele = one_ingredient.text.strip()
    print(one_ele)
    ingredients_value.append(one_ele)


# In[361]:


all_ingredient = soup.body.find_all('div', attrs={'class': 'col-xs-9 x-recipe-ingredient'})
for one_ingredient in all_ingredient:
    one_ele = one_ingredient.text.strip()
    print(one_ele)
    ingredients_key.append(one_ele)


# In[362]:


all_ingredient = soup.body.find_all('div', attrs={'class': 'col-xs-3 text-right recipe-label no-padding'})
for one_ingredient in all_ingredient:
    one_ele = one_ingredient.text
    one_ele = one_ele.rstrip().rstrip(':')
    print(one_ele)
    ingredients_key.append(one_ele)


# In[363]:


all_ingredient = soup.body.find('div', attrs={'class': 'col-xs-9 recipe-link no-padding'})
one_ele = all_ingredient.find('span').string
print(one_ele)
ingredients_value.append(one_ele)

all_ingredient = soup.body.find('div', attrs={'class': 'col-xs-9 recipe-link x-recipe-glasstype no-padding'})
one_ele = all_ingredient.find('a').string
print(one_ele)
ingredients_value.append(one_ele)


# In[364]:


all_recipe = []
allRecipe = soup.body.find('div', attrs={'class': 'row x-recipe-prep'}).find_all('p')
for oneRecipe in allRecipe:
    one_ele = oneRecipe.string
    print(one_ele)
    all_recipe.append(one_ele)


# In[365]:


profile_key = []
profile_value = []
profile_key = ['Flavor','Base Spirit','Cocktail Type','Served','Preparation','Strength','Difficulty','Hours','Brands']
allProfileValue = soup.body.find('div', attrs={'class': 'col-xs-12 text-center x-recipe-flavor recipe-link'}).find_all('a')
val = []
for oneValue in allProfileValue:
    one_ele = oneValue.string
    val.append(one_ele)
profile_value.append(val)

print(val)
print(profile_value)
print(profile_key)


# In[366]:


#allProfileKey = soup.body.find_all('div', attrs={'class': 'col-xs-5 text-right no-wrap'})
#for oneKey in allProfileKey:
#    one_ele = oneKey.string.rstrip().rstrip(':')
#    print(one_ele)
#    profile_key.append(one_ele)


# In[367]:


allProfileValue = soup.body.find('div', attrs={'class': 'col-xs-7 x-recipe-spirit'}).find_all('a')
val = []
print(profile_value)
for oneValue in allProfileValue:
    one_ele = oneValue.string
    val.append(one_ele)
profile_value.append(val)

print(val)
print(profile_value)


# In[368]:


allProfileValue = soup.body.find('div', attrs={'class': 'col-xs-7 x-recipe-type'}).find_all('a')
val = []
print(profile_value)
for oneValue in allProfileValue:
    one_ele = oneValue.string
    val.append(one_ele)
profile_value.append(val)

print(val)
print(profile_value)


# In[369]:


allProfileValue = soup.body.find('div', attrs={'class': 'col-xs-7 x-recipe-served'}).find_all('a')
val = []
print(profile_value)
for oneValue in allProfileValue:
    one_ele = oneValue.string
    val.append(one_ele)
profile_value.append(val)

print(val)
print(profile_value)


# In[370]:


allProfileValue = soup.body.find('div', attrs={'class': 'col-xs-7 x-recipe-preparation'}).find_all('a')
val = []
print(profile_value)
for oneValue in allProfileValue:
    one_ele = oneValue.string
    val.append(one_ele)
profile_value.append(val)

print(val)
print(profile_value)


# In[371]:


allProfileValue = soup.body.find('div', attrs={'class': 'col-xs-7 x-recipe-strength'}).find_all('a')
val = []
print(profile_value)
for oneValue in allProfileValue:
    one_ele = oneValue.string
    val.append(one_ele)
profile_value.append(val)

print(val)
print(profile_value)


# In[372]:


allProfileValue = soup.body.find('div', attrs={'class': 'col-xs-7 x-recipe-difficulty'}).find_all('a')
val = []
print(profile_value)
for oneValue in allProfileValue:
    one_ele = oneValue.string
    val.append(one_ele)
profile_value.append(val)

print(val)
print(profile_value)


# In[373]:


allProfileValue = soup.body.find('div', attrs={'class': 'col-xs-7 x-recipe-hours'}).find_all('a')
val = []
print(profile_value)
for oneValue in allProfileValue:
    one_ele = oneValue.string
    val.append(one_ele)
profile_value.append(val)

print(val)
print(profile_value)


# In[374]:


allProfileValue = soup.body.find('div', attrs={'class': 'col-xs-7 x-recipe-brands'}).find_all('a')
val = []
print(profile_value)
for oneValue in allProfileValue:
    one_ele = oneValue.string
    val.append(one_ele)
profile_value.append(val)

print(val)
print(profile_value)


# In[375]:


data = {}
data['title'] = title
data['img'] = imgUrl
data['ingredients_key'] = ingredients_key
data['ingredients_value'] = ingredients_value
data['recipe'] = all_recipe
data['profile_key'] = profile_key
data['profile_value'] = profile_value
data


# In[376]:


with open(os.path.join(BASE_DIR, 'result.json'), 'w+') as json_file:
    json.dump(data, json_file)


# In[377]:


driver.close()
driver.switch_to.window(parent_window)


# In[378]:


print(ingredients_key)
print(ingredients_value)
print(all_recipe)
print(profile_key)
print(profile_value)
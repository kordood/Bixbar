from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
import os


def getInfo(url):

    ## python 파일의 위치
    #filenames = os.path.abspath(__file__)
    #for filename in filenames:
    #    full_filename = os.path.join(filenames, filename)
    #    print(full_filename)

    #BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    #BASE_DIR = os.path.dirname(os.path.abspath(''))
    BASE_DIR = os.path.dirname('/Users/hyeryeongsong/bixby-workspace/ccookncook/crawling/json/')

    html = urlopen(url)
    soup = BeautifulSoup(html, 'html5lib')

    # In[56]:


    title = soup.body.find('div', attrs={'class': 'row head-row text-center'}).find('div', attrs={'class': 'col-xs-12'}).find('h1').text
    title = title.replace(" ", "")
    title = title.replace("/", "_")
    title = title.replace(".", "_")
    # print(title)


    # In[57]:


    imgUrl = soup.find('div', attrs={'class': 'center-block img-hero heart-me'}).find("img")["src"]
    imgUrl = 'https://' + imgUrl
    # print(imgUrl)


    # In[58]:

    ingredients_key = []
    ingredients_value = []

    try:
        all_ingredient = soup.body.find_all('div', attrs={'class': 'measure'})
        for one_ingredient in all_ingredient:
            one_ele = one_ingredient.text.strip()
            # print(one_ele)
            ingredients_value.append(one_ele)

    except:
        ingredients_value.append('None')

    # In[59]:


    try:
        all_ingredient = soup.body.find_all('div', attrs={'class': 'col-xs-9 x-recipe-ingredient'})
        for one_ingredient in all_ingredient:
            one_ele = one_ingredient.text.strip()
            # print(one_ele)
            ingredients_key.append(one_ele)

    except:
        ingredients_value.append('None')

    # In[60]:

    try:
        all_ingredient = soup.body.find_all('div', attrs={'class': 'col-xs-3 text-right recipe-label no-padding'})
        for one_ingredient in all_ingredient:
            one_ele = one_ingredient.text
            one_ele = one_ele.rstrip().rstrip(':')
            # print(one_ele)
            ingredients_key.append(one_ele)

    except:
        ingredients_value.append('None')

    # In[61]:


    try:
        all_ingredient = soup.body.find('div', attrs={'class': 'col-xs-9 recipe-link no-padding'})
        one_ele = all_ingredient.find('span').string
        # print(one_ele)
        ingredients_value.append(one_ele)

    except:
        ingredients_value.append('None')


    try:
        all_ingredient = soup.body.find('div', attrs={'class': 'col-xs-9 recipe-link x-recipe-glasstype no-padding'})
        one_ele = all_ingredient.find('a').string
        # print(one_ele)
        ingredients_value.append(one_ele)

    except:
        ingredients_value.append('None')


    # In[62]:


    all_recipe = []
    allRecipe = soup.body.find('div', attrs={'class': 'row x-recipe-prep'}).find_all('p')
    for oneRecipe in allRecipe:
        one_ele = oneRecipe.string
        # print(one_ele)
        all_recipe.append(one_ele)

    # In[63]:


    profile_key = []
    profile_value = []
    profile_key = ['Flavor', 'Base Spirit', 'Cocktail Type', 'Served', 'Preparation', 'Strength', 'Difficulty', 'Hours','Brands']
    allProfileValue = soup.body.find('div', attrs={'class': 'col-xs-12 text-center x-recipe-flavor recipe-link'}).find_all('a')
    val = []
    for oneValue in allProfileValue:
        one_ele = oneValue.string
        val.append(one_ele)
    profile_value.append(val)

    # print(val)
    # print(profile_value)
    # print(profile_key)


    # In[64]:


    # allProfileKey = soup.body.find_all('div', attrs={'class': 'col-xs-5 text-right no-wrap'})
    # for oneKey in allProfileKey:
    #    one_ele = oneKey.string.rstrip().rstrip(':')
    #    print(one_ele)
    #    profile_key.append(one_ele)


    # In[65]:


    try:
        allProfileValue = soup.body.find('div', attrs={'class': 'col-xs-7 x-recipe-spirit'}).find_all('a')
        val = []
        # print(profile_value)
        for oneValue in allProfileValue:
            one_ele = oneValue.string
            val.append(one_ele)
        profile_value.append(val)

    except:
        val = []
        val.append('None')
        profile_value.append(val)

    # print(val)
    # print(profile_value)


    # In[66]:


    try:
        allProfileValue = soup.body.find('div', attrs={'class': 'col-xs-7 x-recipe-type'}).find_all('a')
        val = []
        # print(profile_value)
        for oneValue in allProfileValue:
            one_ele = oneValue.string
            val.append(one_ele)
        profile_value.append(val)

    except:
        val = []
        val.append('None')
        profile_value.append(val)

    # print(val)
    # print(profile_value)


    # In[67]:


    try:
        allProfileValue = soup.body.find('div', attrs={'class': 'col-xs-7 x-recipe-served'}).find_all('a')
        val = []
        # print(profile_value)
        for oneValue in allProfileValue:
            one_ele = oneValue.string
            val.append(one_ele)
        profile_value.append(val)

    except:
        val = []
        val.append('None')
        profile_value.append(val)

    # print(val)
    # print(profile_value)


    # In[68]:


    try:
        allProfileValue = soup.body.find('div', attrs={'class': 'col-xs-7 x-recipe-preparation'}).find_all('a')
        val = []
        # print(profile_value)
        for oneValue in allProfileValue:
            one_ele = oneValue.string
            val.append(one_ele)
        profile_value.append(val)

    except:
        val = []
        val.append('None')
        profile_value.append(val)

    # print(val)
    # print(profile_value)


    # In[69]:


    try:
        allProfileValue = soup.body.find('div', attrs={'class': 'col-xs-7 x-recipe-strength'}).find_all('a')
        val = []
        # print(profile_value)
        for oneValue in allProfileValue:
            one_ele = oneValue.string
            val.append(one_ele)
        profile_value.append(val)

    except:
        val = []
        val.append('None')
        profile_value.append(val)

    # print(val)
    # print(profile_value)


    # In[70]:

    try:
        allProfileValue = soup.body.find('div', attrs={'class': 'col-xs-7 x-recipe-difficulty'}).find_all('a')
        val = []
        # print(profile_value)
        for oneValue in allProfileValue:
            one_ele = oneValue.string
            val.append(one_ele)
        profile_value.append(val)

    except:
        val = []
        val.append('None')
        profile_value.append(val)

    # print(val)
    # print(profile_value)


    # In[71]:


    try:
        allProfileValue = soup.body.find('div', attrs={'class': 'col-xs-7 x-recipe-hours'}).find_all('a')
        val = []
        # print(profile_value)
        for oneValue in allProfileValue:
            one_ele = oneValue.string
            val.append(one_ele)
        profile_value.append(val)

    except:
        val = []
        val.append('None')
        profile_value.append(val)

    # print(val)
    # print(profile_value)


    # In[72]:

    try:
        allProfileValue = soup.body.find('div', attrs={'class': 'col-xs-7 x-recipe-brands'}).find_all('a')
        val = []
        # print(profile_value)
        for oneValue in allProfileValue:
            one_ele = oneValue.string
            val.append(one_ele)
        profile_value.append(val)

    except:
        val = []
        val.append('None')
        profile_value.append(val)

    # print(val)
    # print(profile_value)


    # In[73]:


    data = {}
    data['title'] = title
    data['img'] = imgUrl
    data['ingredients_key'] = ingredients_key
    data['ingredients_value'] = ingredients_value
    data['recipe'] = all_recipe
    data['profile_key'] = profile_key
    data['profile_value'] = profile_value
    data

    # In[74]:


    jsonName = title + '.json'
    print(jsonName)
    with open(os.path.join(BASE_DIR, jsonName), 'w+') as json_file:
        json.dump(data, json_file)

    # In[77]:


    print(ingredients_key)
    print(ingredients_value)
    print(all_recipe)
    print(profile_key)
    print(profile_value)

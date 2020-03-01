from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
import os
import unicodedata


def getInfo(url):
    BASE_DIR = os.path.dirname('/Users/hyeryeongsong/bixby-workspace/ccookncook/FoodRecipeCrawl/json/')

    html = urlopen(url)
    soup = BeautifulSoup(html, 'html5lib')
    stripped = lambda s: "".join(i for i in s if 31 < ord(i) < 127)

    title = soup.body.find('div', attrs={'class': 'view2_summary'}).find('h3').text
    title = unicodedata.normalize("NFKD", title)
    print(title)

    ingredients = []
    split_ingredients = []
    ingredients_key = []
    ingredients_value = []

    try:
        all_ingredient = soup.body.find('div', attrs={'class': 'cont_ingre'}).find('dl').find('dd').text
        # print(all_ingredient)
        ingredients = all_ingredient.split(', ')
        # print(ingredients)
        for one_ele in ingredients:
            # print(one_ele)
            split_ingredients = one_ele.split()
            # print(split_ingredients)
            # print(split_ingredients[0])
            # print(split_ingredients[1])
            ingredients_key.append(split_ingredients[0])
            if len(split_ingredients) == 2:
                ingredients_value.append(split_ingredients[1])
            else:
                ingredients_value.append('None')
        #print(ingredients_key)
        #print(ingredients_value)


    except:

        try:
            all_ingredient = soup.body.find('div', attrs={'class': 'ready_ingre3'}).find_all('ul')

            for one_ingre in all_ingredient:
                all_ingre = one_ingre.find_all('li')
                for one_ele in all_ingre:
                    ingredients = one_ele.text.split()
                    ingredients_key.append(ingredients[0])
                    if len(ingredients) == 2:
                        ingredients_value.append(ingredients[1])
                    else:
                        ingredients_value.append('None')

            #print(ingredients_key)
            #print(ingredients_value)

        except:
            print("except")
            return

    data = {}
    data['title'] = title
    data['ingredients_key'] = ingredients_key
    data['ingredients_value'] = ingredients_value

    #print(data)
    print(len(ingredients_key))
    print(len(ingredients_value))
    print(ingredients_key)
    print(ingredients_value)

    jsonName = title + '.json'
    print(jsonName)
    with open(os.path.join(BASE_DIR, jsonName), 'w+', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False)

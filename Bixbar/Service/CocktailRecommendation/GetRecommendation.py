#!/usr/bin/env python
# coding: utf-8

# In[114]:

import boto3
import numpy as np
import pandas as pd
import csv


# In[115]:


class Recommendation:

    def getRecommendation(USER_ID: str):

        personalizeRt = boto3.client('personalize-runtime')
        
        response = personalizeRt.get_recommendations(
            campaignArn = 'arn:aws:personalize:ap-northeast-2:027405227226:campaign/Recommend-campaign',
            userId = USER_ID)

        # In[116]:

        import csv
        item_path = "/srv/Bixbar/bixbar/CocktailRecommendation/itemList.csv"
        cocktailList = [0]
        with open(item_path, newline='', encoding = 'UTF-8') as f:
            reader = csv.reader(f)
            for row in reader:
                cocktailList.extend(row)

        # In[117]:

        itemRecommendation = []
        finalRecommendation = []
        for item in response['itemList']:
            idx = int(item['itemId'])
            #print(cocktailList[idx])
            itemRecommendation.append(cocktailList[idx])
        for i in [0,1,2]:
            finalRecommendation.append(itemRecommendation[i])
        #print(finalRecommendation)
        return finalRecommendation

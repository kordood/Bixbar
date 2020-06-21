{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 114,
   "metadata": {},
   "outputs": [],
   "source": [
    "import boto3\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "import csv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 115,
   "metadata": {},
   "outputs": [],
   "source": [
    "personalizeRt = boto3.client('personalize-runtime')\n",
    "\n",
    "response = personalizeRt.get_recommendations(\n",
    "    campaignArn = 'arn:aws:personalize:ap-northeast-2:027405227226:campaign/Recommend-campaign',\n",
    "    userId = '40')\n",
    "\n",
    "#print(\"Recommended items\")\n",
    "#for item in response['itemList']:\n",
    "#    print (item['itemId'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 116,
   "metadata": {},
   "outputs": [],
   "source": [
    "import csv\n",
    "cocktailList = [0]\n",
    "with open('itemList.csv', newline='', encoding = 'UTF-8') as f:\n",
    "    reader = csv.reader(f)\n",
    "    for row in reader:\n",
    "        #print(row)\n",
    "        cocktailList.extend(row)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 117,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Screwdriver', 'Cosmopolitan', 'SexontheBeach', 'Margarita', 'PinaColada']\n"
     ]
    }
   ],
   "source": [
    "itemRecommendation = []\n",
    "finalRecommendation = []\n",
    "for item in response['itemList']:\n",
    "    idx = int(item['itemId'])\n",
    "    #print(cocktailList[idx])\n",
    "    itemRecommendation.append(cocktailList[idx])\n",
    "for i in [0,1,2,3,4]:\n",
    "    finalRecommendation.append(itemRecommendation[i])\n",
    "print(finalRecommendation)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

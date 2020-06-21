from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, Http404
from bixbar.models import *
import requests
import json
import os
import csv
import random
import urllib
from bixbar.CocktailRecommendation.GetRecommendation import Recommendation as CocktailRecommend
from bixbar.CocktailRecommendation.PutEvent import EventHandle

###########################################################################################################
# 유저 정보 저장
###########################################################################################################
def createUser(request):
    print(request)
    if request.method == "GET":
        return HttpResponse("test OK", status=200)
    elif request.method == "POST":
        request_json = json.loads(request.body)
        user_id = request_json["userID"]
        gender = request_json["gender"]
        age = int(request_json["age"])
        EventHandle.putUser(user_id, gender, age)
        return HttpResponse("User put OK", status=200)


###########################################################################################################
# 링크 - 노션 연결
###########################################################################################################
def redirectBixbar(request):
    return HttpResponseRedirect('https://www.notion.so/ccookncook/Bixbar-b5401104a0d64fdc838d27505fbf27b2')


###########################################################################################################
# 저장
###########################################################################################################
def querySave(request):
    # DB확인
    querySet = Cocktail.objects.all()
    if querySet: 
        return JsonResponse({'status':'No','message':'Failed!'}, status=400)
    # json to query
    jsonlist = os.listdir('/workspace/Bixbar/json')
    for eachfile in jsonlist:
        print(eachfile)
        with open('/workspace/Bixbar/json/' + eachfile) as jsonFile:
            jsonString = json.loads(jsonFile.read())
            print('\n\n\n')
            print(jsonString)
            
            # title, img, recipe
            title = jsonString['title']
            img = jsonString['img']
            recipe = jsonString['recipe']
            
            try:
                # Glass
                glassNum = jsonString['ingredients_key'].index('Glass')
                glass = jsonString['ingredients_value'][glassNum]
            except :
                glass = "none"

            try:
                # Garnish
                garnishNum = jsonString['ingredients_key'].index('Garnish')
                garnish = jsonString['ingredients_value'][garnishNum]
            except :
                garnish = "none"

                
            # ingredients            
            ingNum = len(jsonString['ingredients_key']) - 2
            num = 0
            liquorList = []
            for ingList in jsonString['ingredients_key']:
                liquorList.append(ingList)
                num += 1
                if num == ingNum:
                    break
                    
            num = 0
            mlList = []
            for ingList in jsonString['ingredients_value']:
                mlList.append(ingList)
                num += 1
                if num == ingNum:
                    break
            print(liquorList)
            liquor = liquorList
            liquorml = mlList
            
            # Flavor, Base Spririt, Cocktail Type, Served, Preparation, Strength, Difficulty, Hours, Brands
            try:
                # flavor
                flavorNum = jsonString['profile_key'].index('Flavor')
                flavor = jsonString['profile_value'][flavorNum]
            except :
                flavor = "none"
            try:
                # baseSpirit
                baseSpiritNum = jsonString['profile_key'].index('Base Spirit')
                baseSpirit = jsonString['profile_value'][baseSpiritNum]
            except :
                baseSpirit = "none"
            try:
                # cocktailType
                cocktailTypeNum = jsonString['profile_key'].index('Cocktail Type')
                cocktailType = jsonString['profile_value'][cocktailTypeNum]
            except :
                cocktailType = "none"
            try:
                # served
                servedNum = jsonString['profile_key'].index('Served')
                served = jsonString['profile_value'][servedNum]
            except :
                served = "none"
            try:
                # preparation
                preparationNum = jsonString['profile_key'].index('Preparation')
                preparation = jsonString['profile_value'][preparationNum]
            except :
                preparation = "none"
            try:
                # strength
                strengthNum = jsonString['profile_key'].index('Strength')
                strength = jsonString['profile_value'][strengthNum]
            except :
                strength = "none"
            try:
                # difficulty
                difficultyNum = jsonString['profile_key'].index('Difficulty')
                difficulty = jsonString['profile_value'][difficultyNum]
            except :
                difficulty = "none"
            try:
                # hours
                hoursNum = jsonString['profile_key'].index('Hours')
                hours = jsonString['profile_value'][hoursNum]
            except :
                hours = "none"
            try:
                # brands
                brandsNum = jsonString['profile_key'].index('Brands')
                brands = jsonString['profile_value'][brandsNum]
            except :
                brands = "none"

            # query에 저장
            newCocktail = Cocktail(title=title, img=img, recipe=recipe, glass=glass, garnish=garnish, liquor=liquor, liquorml = liquorml, flavor=flavor, baseSpirit=baseSpirit, cocktailType=cocktailType, served=served, preparation=preparation, strength=strength, difficulty=difficulty, hours=hours, brands=brands)
            newCocktail.save()
            '''
            # recipe test
            newRecipe = RecipeModel(recipe2=jsonString['recipe'][0], cocktail=newCocktail)
            newRecipe.save()
            newRecipe = RecipeModel(recipe2=jsonString['recipe'][1], cocktail=newCocktail)
            newRecipe.save()
            
            querySet = RecipeModel.objects.all()
            querySet = querySet.objects.filter(title__iexact = jsonFile['title'])
            item = querySet.values_list()
            print(item)
            '''
    # Foods
    # food-cocktail.csv
    foodCocktail = open('/workspace/Bixbar/foods/food-cocktail.csv', 'r', encoding='utf-8')
    foodReader1 = csv.reader(foodCocktail)
    for line in foodReader1:
        matchCocktails = (line[1])
        foodsTitle = (line[2])

        newFoodCocktail = FoodCocktail(matchCocktails=matchCocktails,foodsTitle=foodsTitle)
        newFoodCocktail.save()
    foodCocktail.close() 
    
    # food-baseSpirit.csv
    foodBase = open('/workspace/Bixbar/foods/food-baseSpirit.csv', 'r', encoding='utf-8')
    foodReader2 = csv.reader(foodBase)
    for line in foodReader2:
        matchLiquor = (line[1])
        foodsTitle = (line[2])
        
        newFoodBase = FoodBase(matchLiquor=matchLiquor,foodsTitle=foodsTitle)
        newFoodBase.save()
    foodBase.close() 
    
    return JsonResponse({'status':'OK','message':'DB set.'}, status=200)


###########################################################################################################
# cocktail - Food
###########################################################################################################
def FoodList(request):
    q = request.GET.get('q','')
    querySet = FoodCocktail.objects.order_by('?')
    querySetList = []
    tmpList = list(querySet.values())[-3:]
    
    # 칵테일과 정확히 일치 시
    if q:
        querySet = querySet.filter(matchCocktails__iexact=q)[:3]
        querySetList = querySetAppend(querySet, querySetList)
    # liquor is "exact"
        querySet2 = FoodBase.objects.order_by('?')
        querySet2 = querySet2.filter(matchLiquor__iexact=q)[:3]
        querySetList = querySetAppend(querySet2, querySetList)
    #if not querySet and len(q) > 2:
        querySet3 = FoodCocktail.objects.order_by('?')
        querySet3 = querySet3.filter(matchCocktails__icontains=q)[:3]
        querySetList = querySetAppend(querySet3, querySetList)
    # base에 포함
    #if not querySet and len(q) > 2:
        querySet4 = FoodBase.objects.order_by('?')
        querySet4 = querySet4.filter(matchLiquor__icontains=q)[:3]
        querySetList = querySetAppend(querySet4, querySetList)
    for element in tmpList:
        querySetList.append(element)
    # 
    # 결과 X
    if not querySetList or len(q) == 0:
        return JsonResponse({'status':'false','message':'Cocktail not found.'}, status=500)
    
    
    resultList = []
    for element in querySetList:
        if element not in resultList:
            resultList.append(element)
    
    # querySet = list(querySet.values())
    jsonqs = json.dumps(resultList)
    return HttpResponse(jsonqs, content_type="text/json")

def querySetAppend(querySet, querySetList: list):
    qs = list(querySet.values())
    for element in qs:
        querySetList.append(element)
    return querySetList


###########################################################################################################
# 검색
###########################################################################################################
def lookupQuery(queryType, q):
    # query 내용을 전부 가져옴
    querySet = Cocktail.objects.all()
    
    # q의 값이 존재할 때
    if q:
        # liquor 이 q인 값 가져오기
        if queryType == "title":
            querySet = querySet.filter(title__iexact=q)
        elif queryType == "liquor":
            querySet = querySet.filter(liquor__iexact=q)
        elif queryType == "base":
            querySet = querySet.filter(baseSpirit__iexact=q)
        # Working!!!
        elif queryType == "recommend":
            querySet = Cocktail.objects.order_by('title').filter(title__contains = q[0]) | Cocktail.objects.order_by('title').filter(title__contains = q[1]) | Cocktail.objects.order_by('title').filter(title__contains = q[2]) | Cocktail.objects.order_by('title').filter(title__contains = q[3]) | Cocktail.objects.order_by('title').filter(title__contains = q[4])
            
        
        # margarita 제외하고 2개 더 추천으로 띄어주기!!!!!!!!!!@@@@@@@@@@@@@@@@@@@@@@@@@@
        
        # q가 포함된 값 가져오기 q의 길이는 2보다 커야함!
        if not querySet and len(q) > 2:
            querySet = Cocktail.objects.all()
            if queryType == "title":
                querySet = querySet.filter(title__icontains=q)[:3]
            elif queryType == "liquor":
                querySet = querySet.filter(liquor__icontains=q)[:3]
            elif queryType == "base":
                querySet = querySet.filter(baseSpirit__icontains=q)[:3]
        print(querySet.values_list(),'\n\n')
        
        # querySet이 비어있거나 q가 존재하지 않을 때
    if not querySet or len(q) == 0:
        return JsonResponse({'status':'false','message':'Cocktail not found.'}, status=500)

    # for qSetList in querySet.values_list() // DryMartini, DirtyMartini
    group_items = []
    k = 0
    for test in querySet:
        item = querySet.values_list()[k]
        recipeList = []
        recipeList = json.loads(item[3].replace("'", '"'))
        bakRecipeList = recipeList
        trunliquor = item[6].replace("\\xa0"," ")
        liquorList = json.loads(trunliquor.replace("'", '"'))
        truncate = item[7].replace("\\xa0"," ")
        mlList = json.loads(truncate.replace("'", '"'))
        flavorList = json.loads(item[8].replace("'", '"'))
        baseList = json.loads(item[9].replace("'", '"'))
        typeList = json.loads(item[10].replace("'", '"'))
        servedList = json.loads(item[11].replace("'", '"'))
        prepList = json.loads(item[12].replace("'", '"'))
        strengthList = json.loads(item[13].replace("'", '"'))
        diffList = json.loads(item[14].replace("'", '"'))
        hoursList = json.loads(item[15].replace("'", '"'))
        brandList = json.loads(item[16].replace("'", '"'))
        
        try:# 글자 한도 초과시 오류 방지
            # 레시피 리스트 번역    
            url = 'https://openapi.naver.com/v1/papago/n2mt' # api url
            headers = { 
                'X-Naver-Client-Id': 'o05sh5nBEu08qGa3G_Yx',
                'X-Naver-Client-Secret': '6H3tuMceUu', 
            } 
            params = { 
                'source': 'en', 
                'target': 'ko', 
                'text': item[1],
            }

            # title 번역
            titleRes = requests.post(url, headers=headers, data=params) # post 형식으로 request
            titleResult = titleRes.json() # json 형식으로 받아옴
            titleResult2 = titleResult['message']['result']['translatedText'] # 번역된 Text만 추출

            title = []
            title = item[1] + '(' + titleResult2 + ')' # text(텍스트)


            # recipe 번역
            i = 0
            for reList in recipeList:
                params = { 
                    'source': 'en', 
                    'target': 'ko', 
                    'honorific': 'true', # 높임말
                    'text': reList, # 번역할 Text
                }

                res = requests.post(url, headers=headers, data=params)
                result = res.json()
                translatedRecipe = result['message']['result']['translatedText']
                recipeList[i] = translatedRecipe

                print(translatedRecipe)

                i+=1
        except: # 원문으로 복구
            title = item[1]
            recipeList = bakRecipeList
        
        group_items.append( {'title': title, 'img': item[2], 'recipe': recipeList, 'glass': item[4], 'garnish': item[5], 'liquor': liquorList, 'liquorml': mlList, 'flavor': flavorList, 'baseSpirit': baseList, 'cocktailType': typeList, 'served': servedList, 'preparation': prepList, 'strength': strengthList, 'difficulty': diffList, 'hours': hoursList, 'brands': brandList} )
        k+=1
        
    jsonqs = json.dumps(group_items)
        
    return jsonqs
    
       
###########################################################################################################
# 조회
###########################################################################################################
def cocktailList(request):
    # GET request의 인자 중 q 값이 있으면 가져옴, 없으면 빈 문자열
    q = request.GET.get('q','')
    jsonqs = lookupQuery("title", q)
    return HttpResponse(jsonqs, content_type="text/json")


###########################################################################################################
# 재료를 이용한 조회
###########################################################################################################
def ingredientList(request):
    # GET request의 인자 중 q 값이 있으면 가져옴, 없으면 빈 문자열
    q = request.GET.get('q','')
    jsonqs = lookupQuery("liquor", q)
    return HttpResponse(jsonqs, content_type="text/json")


###########################################################################################################
# baseSpirit을 이용한 조회
###########################################################################################################
def baseList(request):
    # GET request의 인자 중 q 값이 있으면 가져옴, 없으면 빈 문자열
    q = request.GET.get('q','')
    jsonqs = lookupQuery("base", q)
    return HttpResponse(jsonqs, content_type="text/json")

###########################################################################################################
# Cocktail Recommendation 기능(AWS Personalize API 활용)
###########################################################################################################
def cocktailRecommend(request):
    # Preprocessing
    id_cocktail_match_list = ["50_50Martini","All-PurposeEggnog","Aristocrat","Ascot","AudreySaundersTomJerry","Aviation","B-52","BananaSurfer","BayouBloodyMary","BentonsOldFashioned","BigRed","BlackberryMintJulepMargarita","BloodyBulldog","BloodyKirby","BloodyMaria","BloodyMary","BloodyRoman","BlowJob","BlueBlazer","BoatHousePunch","Boulevardier","BourbonCiderSlushie","BourbonLift","BourbonManhattan","BourbonOldFashioned","BourbonRootBeer","BourbonRosemaryPunch","BourbonStrawberryIcedTea","Bramble","BrownDerby","Caesar","ChampagneCocktail","ChristmasPunch","CloverClub","CobrasFang","Cosmopolitan","Cranberry-GingerMimosa","Daiquiri","DalesRainbowPlantersPunch","DarknStormy","DeadbeatDaiquiri","DevilsMargarita","DiamondDistrict","DirtyMartini","DistritoFederal(AKATequilaManhattan)","DIYPinkGinCocktail","DryMartini","DubiousManhattan","DutchmansDaiquiri","EasterBunnyShot","Eggnog","ElixirBloodyMary","Emerald","EmployeesOnlyManhattan","Fennel75","FlamingDr_PepperShot","FortDefianceIrishCoffee","French75","FrenchMartini","Frohito","Frose","FrozenMargarita","FrozenSangria","Gibson","Gimlet","GinFizz","GoldRush","GreenBeast","GreenHoliday","GreenMargarita","Greyhound","HemingwayDaiquiri","HibiscusSummerGardenPunch","HolidayHooch","HotButteredRum","HotToddy","Hurricane","IrishCoffee","JeffreyMorgenthalersHotToddy","Jell-OShots","JingleBall","Kamikaze","KirRoyale","KombuchaMimosa","Last-MinuteMulledWine","LemonDrop","LetsPumpkin","MaiTai","MangoBravaDaiquiri","Manhattan","Margarita","MargaritasbythePitcher","MasterCleanseShot","Mimosa","MintJulep","Mojito","MoscowMule","MuddledPine","Negroni","NegroniSbagliato","NewYorkSour","OaxacanOldFashioned","OldFashioned","Painkiller","Paloma","PinaColada","PoncheNavideno","Preakness","PumpkinToddy","RamosGinFizz","RedSnapper","ReverseManhattan","ReverseMartiniBartendersSpecial","RoomTemperatureMartiniNo_1","Saturn","Sazerac","Scofflaw","Screwdriver","SexontheBeach","ShamrockShot","SingaporeSling","SnapChatRum","SourT-iesel","SouthSide","SpanishGinTonic","SparklingRoseMargarita","SparklingWatermelonPunch","SpicyMintAvocadoMargarita","StrawberryBasilMargarita","StrawberryDaiquiri","SufferingBastard","SummerthymeScrewdriver","Teal-quilaSunrise","TequilaManhattan","TheDeadRabbitIrishCoffee","TomCollins","ToughtoHear","TurfClub","UncleAngelosEggnog","UptownWays","Vesper","VieuxCarre","Vladimiry","VodkaSoda","WatermelonBlackberryMargaritaPopsicles","WatermelonMargarita","WatermelonWhiteWineSpritzer","WhiskeySmash","WhiskeySour","WinterDaiquiri","X-MasSin","YodaSour"]
    ###############
    # Check USER_ID
    
    if request.method == "GET":
        return HttpResponse("test OK", status=200)
    elif request.method == "POST":
        request_json = json.loads(request.body)
        user_id = request_json["userID"]
    
    # GET Recommendation with USER_ID
    # result_list = CocktailRecommend.getRecommendation(str(user_id))
    result_num = ['10', '5', '67']
    for i in range(10):
        if(len(result_num) >= 5):
            break
        candidate = random.randint(1,152)
        if candidate not in result_num:
            result_num.append(str(candidate))
    print(result_num)
    result_list = []
    for num in result_num:
        result_list.append(id_cocktail_match_list[int(num)])
    print(result_list)
    jsonqs = lookupQuery("recommend", result_list)
    #print(jsonqs)
    print("done")
    # Response Cocktail list(json)
    ##############################
    ######       ToDo       ######
    ##############################
    return HttpResponse(jsonqs, content_type="text/json")


###########################################################################################################
# Cocktail Recommendation 데모용!!!! (AWS Personalize API 활용)
###########################################################################################################
def cocktailRecommend1(request):
    # Preprocessing
    id_cocktail_match_list = ["50_50Martini","All-PurposeEggnog","Aristocrat","Ascot","AudreySaundersTomJerry","Aviation","B-52","BananaSurfer","BayouBloodyMary","BentonsOldFashioned","BigRed","BlackberryMintJulepMargarita","BloodyBulldog","BloodyKirby","BloodyMaria","BloodyMary","BloodyRoman","BlowJob","BlueBlazer","BoatHousePunch","Boulevardier","BourbonCiderSlushie","BourbonLift","BourbonManhattan","BourbonOldFashioned","BourbonRootBeer","BourbonRosemaryPunch","BourbonStrawberryIcedTea","Bramble","BrownDerby","Caesar","ChampagneCocktail","ChristmasPunch","CloverClub","CobrasFang","Cosmopolitan","Cranberry-GingerMimosa","Daiquiri","DalesRainbowPlantersPunch","DarknStormy","DeadbeatDaiquiri","DevilsMargarita","DiamondDistrict","DirtyMartini","DistritoFederal(AKATequilaManhattan)","DIYPinkGinCocktail","DryMartini","DubiousManhattan","DutchmansDaiquiri","EasterBunnyShot","Eggnog","ElixirBloodyMary","Emerald","EmployeesOnlyManhattan","Fennel75","FlamingDr_PepperShot","FortDefianceIrishCoffee","French75","FrenchMartini","Frohito","Frose","FrozenMargarita","FrozenSangria","Gibson","Gimlet","GinFizz","GoldRush","GreenBeast","GreenHoliday","GreenMargarita","Greyhound","HemingwayDaiquiri","HibiscusSummerGardenPunch","HolidayHooch","HotButteredRum","HotToddy","Hurricane","IrishCoffee","JeffreyMorgenthalersHotToddy","Jell-OShots","JingleBall","Kamikaze","KirRoyale","KombuchaMimosa","Last-MinuteMulledWine","LemonDrop","LetsPumpkin","MaiTai","MangoBravaDaiquiri","Manhattan","Margarita","MargaritasbythePitcher","MasterCleanseShot","Mimosa","MintJulep","Mojito","MoscowMule","MuddledPine","Negroni","NegroniSbagliato","NewYorkSour","OaxacanOldFashioned","OldFashioned","Painkiller","Paloma","PinaColada","PoncheNavideno","Preakness","PumpkinToddy","RamosGinFizz","RedSnapper","ReverseManhattan","ReverseMartiniBartendersSpecial","RoomTemperatureMartiniNo_1","Saturn","Sazerac","Scofflaw","Screwdriver","SexontheBeach","ShamrockShot","SingaporeSling","SnapChatRum","SourT-iesel","SouthSide","SpanishGinTonic","SparklingRoseMargarita","SparklingWatermelonPunch","SpicyMintAvocadoMargarita","StrawberryBasilMargarita","StrawberryDaiquiri","SufferingBastard","SummerthymeScrewdriver","Teal-quilaSunrise","TequilaManhattan","TheDeadRabbitIrishCoffee","TomCollins","ToughtoHear","TurfClub","UncleAngelosEggnog","UptownWays","Vesper","VieuxCarre","Vladimiry","VodkaSoda","WatermelonBlackberryMargaritaPopsicles","WatermelonMargarita","WatermelonWhiteWineSpritzer","WhiskeySmash","WhiskeySour","WinterDaiquiri","X-MasSin","YodaSour"]
    ###############
    # Check USER_ID
    
    if request.method == "GET":
        return HttpResponse("test OK", status=200)
    elif request.method == "POST":
        request_json = json.loads(request.body)
        user_id = "13"
    
    # GET Recommendation with USER_ID
    # result_list = CocktailRecommend.getRecommendation(str(user_id))
    result_num = ['10', '5', '67']
    for i in range(10):
        if(len(result_num) >= 5):
            break
        candidate = random.randint(1,152)
        if candidate not in result_num:
            result_num.append(str(candidate))
    print(result_num)
    result_list = []
    for num in result_num:
        result_list.append(id_cocktail_match_list[int(num)])
    print(result_list)
    jsonqs = lookupQuery("recommend", result_list)
    #print(jsonqs)
    print("done")
    # Response Cocktail list(json)
    ##############################
    ######       ToDo       ######
    ##############################
    return HttpResponse(jsonqs, content_type="text/json")

def cocktailInteraction(request):
    # Check USER_ID
    if request.method == "GET":
        return HttpResponse("test OK", status=200)
    elif request.method == "POST":
        request_json = json.loads(request.body)
        TIMESTAMP = request_json["TIMESTAMP"]
        user_id = request_json["userID"]
        item_name = request_json["title"]
        EventHandle.putEvent(user_id, item_name)
        return HttpResponse("Event put OK", status=200)
    else:
        return HttpResponse("Unknown method", status=400)

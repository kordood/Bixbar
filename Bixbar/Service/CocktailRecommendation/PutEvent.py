import boto3
import json
import time

class EventHandle:
    
    def putUser(USER_ID: str, GENDER: str, AGE: int):
        timestamp = int(time.time())
        TIMESTAMP = str(timestamp)
        try:
            personalize_events = boto3.client(service_name='personalize-events')
            result = personalize_events.put_events(
             trackingId = '840f1b0b-301b-47a7-9526-cf2684be90f9',
             userId= USER_ID,
             sessionId = 'session2',
             eventList = [ {
             'eventId': 'event2',
             'sentAt': TIMESTAMP,
             'eventType': 'USERS',
             'properties': json.dumps({
             'USER_ID': USER_ID,
             'GENDER': GENDER,
             'AGE' : AGE,
             'itemId': '0'
             })
             }]
            )
            print(result)
        except:
            return False
        return True
        
    def putEvent(USER_ID: str, item_name: str):
        id_cocktail_match_list = ["50_50Martini","All-PurposeEggnog","Aristocrat","Ascot","AudreySaundersTomJerry","Aviation","B-52","BananaSurfer","BayouBloodyMary","BentonsOldFashioned","BigRed","BlackberryMintJulepMargarita","BloodyBulldog","BloodyKirby","BloodyMaria","BloodyMary","BloodyRoman","BlowJob","BlueBlazer","BoatHousePunch","Boulevardier","BourbonCiderSlushie","BourbonLift","BourbonManhattan","BourbonOldFashioned","BourbonRootBeer","BourbonRosemaryPunch","BourbonStrawberryIcedTea","Bramble","BrownDerby","Caesar","ChampagneCocktail","ChristmasPunch","CloverClub","CobrasFang","Cosmopolitan","Cranberry-GingerMimosa","Daiquiri","DalesRainbowPlantersPunch","DarknStormy","DeadbeatDaiquiri","DevilsMargarita","DiamondDistrict","DirtyMartini","DistritoFederal(AKATequilaManhattan)","DIYPinkGinCocktail","DryMartini","DubiousManhattan","DutchmansDaiquiri","EasterBunnyShot","Eggnog","ElixirBloodyMary","Emerald","EmployeesOnlyManhattan","Fennel75","FlamingDr_PepperShot","FortDefianceIrishCoffee","French75","FrenchMartini","Frohito","Frose","FrozenMargarita","FrozenSangria","Gibson","Gimlet","GinFizz","GoldRush","GreenBeast","GreenHoliday","GreenMargarita","Greyhound","HemingwayDaiquiri","HibiscusSummerGardenPunch","HolidayHooch","HotButteredRum","HotToddy","Hurricane","IrishCoffee","JeffreyMorgenthalersHotToddy","Jell-OShots","JingleBall","Kamikaze","KirRoyale","KombuchaMimosa","Last-MinuteMulledWine","LemonDrop","LetsPumpkin","MaiTai","MangoBravaDaiquiri","Manhattan","Margarita","MargaritasbythePitcher","MasterCleanseShot","Mimosa","MintJulep","Mojito","MoscowMule","MuddledPine","Negroni","NegroniSbagliato","NewYorkSour","OaxacanOldFashioned","OldFashioned","Painkiller","Paloma","PinaColada","PoncheNavideno","Preakness","PumpkinToddy","RamosGinFizz","RedSnapper","ReverseManhattan","ReverseMartiniBartendersSpecial","RoomTemperatureMartiniNo_1","Saturn","Sazerac","Scofflaw","Screwdriver","SexontheBeach","ShamrockShot","SingaporeSling","SnapChatRum","SourT-iesel","SouthSide","SpanishGinTonic","SparklingRoseMargarita","SparklingWatermelonPunch","SpicyMintAvocadoMargarita","StrawberryBasilMargarita","StrawberryDaiquiri","SufferingBastard","SummerthymeScrewdriver","Teal-quilaSunrise","TequilaManhattan","TheDeadRabbitIrishCoffee","TomCollins","ToughtoHear","TurfClub","UncleAngelosEggnog","UptownWays","Vesper","VieuxCarre","Vladimiry","VodkaSoda","WatermelonBlackberryMargaritaPopsicles","WatermelonMargarita","WatermelonWhiteWineSpritzer","WhiskeySmash","WhiskeySour","WinterDaiquiri","X-MasSin","YodaSour"]
        ITEM_ID = str(id_cocktail_match_list.index(item_name))
        
        timestamp = int(time.time())
        TIMESTAMP = str(timestamp)
    ###############
        try:
            personalize_events = boto3.client(service_name='personalize-events')
            result = personalize_events.put_events(
             trackingId = '840f1b0b-301b-47a7-9526-cf2684be90f9',
             userId= USER_ID,
             sessionId = 'session1',
             eventList = [ {
             'eventId': 'event1',
             'sentAt': TIMESTAMP,
             'eventType': 'INTERACTION',
             'properties': json.dumps({
             'TIMESTAMP': TIMESTAMP,
             'USER_ID': USER_ID,
             'itemId': ITEM_ID
             })
             }]
            )
            print(result)
        except:
            return False
        return True
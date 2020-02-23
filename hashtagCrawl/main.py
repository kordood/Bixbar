import crawling

cocktailBase = ["Vodka", "Rum", "Liqueurs", "Cognac", "Gin", "Brandy", "Bourbon", "AmericanWhiskey",\
                "Whiskey", "Beer", "Scotch", "Tequila", "Vermouth", "AperitifWine", \
                "Amaretto", "Champagne", "SparklingWine", "IrishWhiskey", "RyeWhiskey",\
                "Wine", "Absinthe", "RhumAgricole", "Pisco", "Armagnac"]

for oneCocktail in cocktailBase:
    crawling.getInfo(oneCocktail)
#search = urllib.parse.quote(search)

#"Vodka", "Rum", "Liqueurs", "Cognac", "Gin", "Brandy", "Bourbon", "AmericanWhiskey",\
#                "Whiskey", "Beer", "Scotch", "Tequila", "Vermouth", "AperitifWine", \
#                "Amaretto", "Champagne", "SparklingWine", "IrishWhiskey", "RyeWhiskey",\
#                "Wine", "Absinthe", "RhumAgricole", "Pisco", "Armagnac"
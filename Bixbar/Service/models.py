from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import JSONField

# python manage.py makemigrations bixbar
# python manage.py migrate bixbar

'''
# cocktail
class cocktail(models.Model):
    cocktailName = models.CharField(max_length = 50)
    howToMake = models.TextField()
    
    def __str__(self):
        return self.cocktailName
    
# glass
# 1 cocktail : N glass
class glass(models.Model):
    cocktailName = models.ForeignKey(cocktail, on_delete = models.CASCADE)
    glassName = models.CharField(max_length = 20)
        
    def __str__(self):
        return self.glassName
    
    
# garnish
# 1 cocktail : N garnish
class garnish(models.Model):
    cocktailName = models.ForeignKey(cocktail, on_delete = models.CASCADE)
    garnishName = models.CharField(max_length = 50)
    
    def __str__(self):
        return self.garnishName

    
# liquor profile
# 1 cocktail : N liquor profile
class liquor_profile(models.Model):
    cocktailName = models.ForeignKey(cocktail, on_delete = models.CASCADE)
    baseSpirit = models.CharField(max_length = 50)
    cocktailType = models.CharField(max_length = 50)
    served = models.CharField(max_length = 50)
    preparation = models.CharField(max_length = 50)
    stregth = models.CharField(max_length = 50)
    difficulty = models.CharField(max_length = 50)

    def __str__(self):
        return self.baseSpirit

    
# liquor
class liquor(models.Model):
    liquorName = models.CharField(max_length = 50)
    
    def __str__(self):
        return self.liquorName

    
# ingredient liquor 
# 1 cocktail : N ingredient liquor
# 1 liquor : N ingredient liquor
class ingredient_liquor(models.Model):
    cocktailName = models.ForeignKey(cocktail, on_delete = models.CASCADE)
    liquorName = models.ForeignKey(liquor, on_delete = models.CASCADE)
    liquorml = models.IntegerField(default = 0)
    
    def __str__(self):
        return self.liquorml  
'''
class FoodCocktail(models.Model):
    matchCocktails = models.CharField(max_length = 50)
    foodsTitle = models.CharField(max_length = 50)
    ingFoods = models.CharField(max_length = 50, null = True)
    ingFoodsUnit = models.CharField(max_length = 50, null = True)
    def __str__(self):
        return self.foodsTitle
    
class FoodBase(models.Model):
    matchLiquor = models.CharField(max_length = 50)
    foodsTitle = models.CharField(max_length = 50)
    ingFoods = models.CharField(max_length = 50, null = True)
    ingFoodsUnit = models.CharField(max_length = 50, null = True)
    def __str__(self):
        return self.foodsTitle
    
class Cocktail(models.Model):
    title = models.CharField(max_length = 50)
    img = models.CharField(max_length = 200, null = True)
    recipe = models.TextField(null = True)
    
    glass = models.CharField(max_length = 50, null = True)
    garnish = models.CharField(max_length = 50, null = True)
    
    liquor = models.CharField(max_length = 50, null = True)
    liquorml = models.CharField(max_length = 50, null = True)
    
    flavor = models.CharField(max_length = 200, null = True)
    baseSpirit = models.CharField(max_length = 200, null = True)
    cocktailType = models.CharField(max_length = 200, null = True)
    served = models.CharField(max_length = 200, null = True)
    preparation = models.CharField(max_length = 200, null = True)
    strength = models.CharField(max_length = 200, null = True)
    difficulty = models.CharField(max_length = 200, null = True)
    hours = models.CharField(max_length = 200, null = True)
    brands = models.CharField(max_length = 200, null = True)
    
    def __str__(self):
        return self.cocktailName  
'''
class RecipeModel(models.Model):
    recipe2 = models.TextField(null = True)
    cocktail = models.ForeignKey(Cocktail, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.recipe2
'''

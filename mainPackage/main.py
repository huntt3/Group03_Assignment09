#main.py
#*********************************************************************************************************
# Names: Trevor Hunt, Aimee Madrigal, Rhodas Yemaneab                                                                        *
# emails: huntt3@mail.uc.edu, ignaciac@mail.uc.edu, yemanert@mail.uc.edu                                                                   *
# Assignment Number: Assignment 09                                                                       *
# Due Date: 04/04/2024                                                                                   *
# Course/Section: IS4010-001                                                                             *
# Semester/Year: Spring 2024                                                                             *
# Brief Description of the assignment: Demonstrates usage of APIs, and dictionaries                      *
#                                                                                                        *
# Brief Description of what this module does: Calls functions to extract data from database using an API *
# Citations: https://www.thecocktaildb.com/api.php                                                       *
# Anything else that's relevant:                                                                         *
#*********************************************************************************************************
'''
    To Do:
        Extract some interesting data from the dictionary and print it to the console in a friendly
    and informative format
        Finish Documentation
        Finish Modularity
        
'''
from cocktailsPackage.cocktails import *
import requests
import json
if __name__ == "__main__":
    #Note: On the given links, change the "www." to "https://"
    
    champangeFlute = getDrinkDict('https://thecocktaildb.com/api/json/v1/1/filter.php?g=Champagne_flute')
    eggDrinks = getDrinkDict('https://thecocktaildb.com/api/json/v1/1/filter.php?i=egg')
    
    print("There are" , len(eggDrinks["drinks"]) , "drinks that contain eggs.")# These are our interesting facts!
    print("There are" , len(champangeFlute["drinks"]) , "drinks that use champange flutes as the glass.")

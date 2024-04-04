#cocktails.py
#***********************************************************************************************************
# Names: Trevor Hunt, Aimee Madrigal, Rhodas Yemaneab                                                                              *
# emails: huntt3@mail.uc.edu, ignaciac@mail.uc.edu, yemanert@mail.uc.edu                                                                       *
# Assignment Number: Assignment 09                                                                         *
# Due Date: 04/04/2024                                                                                     *
# Course/Section: IS4010-001                                                                               *
# Semester/Year: Spring 2024                                                                               *
# Brief Description of the assignment: Demonstrates usage of APIs, and dictionaries                        *
#                                                                                                          *
# Brief Description of what this module does: Defines functions to extract data from database using an API *
# Citations: https://www.thecocktaildb.com/api.php                                                         *
# Anything else that's relevant:                                                                           *
#***********************************************************************************************************
import requests
import json
def getDrinkDict(URL):
    '''
    Given API URL, retrieves data in a JSON file, and parses into a dictionary
    @param URL: API URL from desired database
    @return: Results from API in a Python dictionary
    '''
    response = requests.get(URL)
    
    json_string = response.content
    
    parsed_json = json.loads(json_string)   # Now we have a python dictionary
    return(parsed_json)
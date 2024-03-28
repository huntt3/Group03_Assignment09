#main.py
#*************************************************************************************************************************************
# Names: Trevor Hunt, [], []                                                                                     *
# emails: huntt3@mail.uc.edu, [], []                                                                                                *
# Assignment Number: Assignment 08                                                                                                   *
# Due Date: 04/04/2024                                                                                                               *
# Course/Section: IS4010-001                                                                                                         *
# Semester/Year: Spring 2024                                                                                                         *
# Brief Description of the assignment: [insert description here]                           *
#                                                                                                                                    *
# Brief Description of what this module does: [insert description here]*
# Citations: https://github.com/apilayer/restcountries                                                                               *
# Anything else that's relevant:                                                                                                     *
#*************************************************************************************************************************************\
import requests
import json
if __name__ == "__main__":
    response = requests.get('https://developer.nps.gov/api/v1/parks?parkCode=acad&api_key=pfJKDXPzTykVL73ehnPyY8pkDQLjfq5cz5LqCkl3')
    json_string = response.content
    parsed_json = json.loads(json_string) # Now we have a python dictionary
    #print(parsed_json)
    #print(parsed_json['data'][0]['description'])
    #print(parsed_json['data'][0]['directionsInfo'])
    total = int(parsed_json['total']) # The number of parks that were returned
    for park in parsed_json['data']:
        print (park)
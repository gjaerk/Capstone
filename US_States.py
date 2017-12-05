#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 08:06:09 2017

@author: kgjaeringen
"""
#Source: http://code.activestate.com/recipes/577305-python-dictionary-of-us-states-and-territories/

#Create a number for each US state
states = {
        'AK': 1, #'Alaska',
        'AL': 2, #'Alabama',
        'AR': 3, #'Arkansas',
        'AS': 4, #'American Samoa',
        'AZ': 5, #'Arizona',
        'CA': 6, #'California',
        'CO': 7, #'Colorado',
        'CT': 8, #'Connecticut',
        'DC': 9, #'District of Columbia',
        'DE': 10, #'Delaware',
        'FL': 11, #'Florida',
        'GA': 12, #'Georgia',
        'GU': 13, #'Guam',
        'HI': 14, #'Hawaii',
        'IA': 15, #'Iowa',
        'ID': 16, #'Idaho',
        'IL': 17, #'Illinois',
        'IN': 18, #'Indiana',
        'KS': 19, #'Kansas',
        'KY': 20, #'Kentucky',
        'LA': 21, #'Louisiana',
        'MA': 22, #'Massachusetts',
        'MD': 23, #'Maryland',
        'ME': 24, #'Maine',
        'MI': 25, #'Michigan',
        'MN': 26, #'Minnesota',
        'MO': 27, #'Missouri',
        'MP': 28, #'Northern Mariana Islands',
        'MS': 29, #'Mississippi',
        'MT': 30, #'Montana',
        'NA': 31, #'National',
        'NC': 32, #'North Carolina',
        'ND': 33, #'North Dakota',
        'NE': 34, #'Nebraska',
        'NH': 35, #'New Hampshire',
        'NJ': 36, #'New Jersey',
        'NM': 37, #'New Mexico',
        'NV': 38, #'Nevada',
        'NY': 39, #'New York',
        'OH': 40, #'Ohio',
        'OK': 41, #'Oklahoma',
        'OR': 42, #'Oregon',
        'PA': 43, #'Pennsylvania',
        'PR': 44, #'Puerto Rico',
        'RI': 45, #'Rhode Island',
        'SC': 46, #'South Carolina',
        'SD': 47, #'South Dakota',
        'TN': 48, #'Tennessee',
        'TX': 49, #'Texas',
        'UT': 50, #'Utah',
        'VA': 51, #'Virginia',
        'VI': 52, #'Virgin Islands',
        'VT': 53, #'Vermont',
        'WA': 54, #'Washington',
        'WI': 55, #'Wisconsin',
        'WV': 56, #'West Virginia',
        'WY': 57, #'Wyoming'
}

states = dict(states)

#class US_States:
def US_States_Lookup(text):
    return states[text]
    
#print(US_States.US_States_Lookup('NV'))


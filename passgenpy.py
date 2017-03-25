# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 13:25:22 2017

@author: Trevor Stolber

Passgen 

passgen($chars) function
Generates a random password of n characters from a list of possible characters

The maximum number of characters in the password is set at 255 by default
The minimum number of characters must be 1 otherwise it will default to 15 characters
The input must be an integer or it will default to a 15 character password.

"""


from random import randint

def passgen(chars):
    try:
        chars = chars + 1   # Check to see if the value is an integer by adding to it
        chars = chars - 1   # subtract 1 if successful so that the umber of characters used is correct
    except:
        chars = 15  # if it is not default to a 15 integer character password
    if chars > 255: # if there is a large input limit it to 15 characters
        chars = 15
    if chars < 1:   # if the input is too small, set it to 15 characters
        chars = 15
    i = 0   # Random Integer value pointer    
    j = 0   # loop counter 
    # l = 0   # list counter
    l = [] #start list
    list = ["a", "b", "c", "d", "e", "f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A", "B", "C", "D", "E", "F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9","!","@","#","$","%","^","&","*","(",")","-","+"]
    while (j < chars):
        i = randint(0,73) # hard coded dictionary length 
        l.append(list[i])
        j = j+1 # increment counter
        # print (j, i, list[i])
    pwd = ''.join(l)
    # pwd = l        
    return pwd

k = passgen(12)

print (k)
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 19:14:27 2021

@author: John Byrne 

Project: Word Count 
"""
#Asking the user whats on their mind.
#Using Regex module.
import re 

def your_mind():
    name = input("What's your name? :") 
    #Ask the user their name.
    thoughts = input("What's on your mind {}?\n".format(name)) 
    #Ask user what is on their mind
    count = len(re.findall(r'\w+', thoughts))
    #Finding position of words in a sentence and truncating.
    print("Your word count is {}:".format(count))
    #printing output
    
your_mind()


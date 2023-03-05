#!/usr/bin/env bash
#! python
# regexStrip.py - regex version of strip() function in python 
import re

def regexstrip(mytext, removechars=''): 
	# remove requested characters from beginning and end 
	if removechars == '': # default case: remove spaces 
		spaceregex = re.compile('^\s*(.*?)\s*$')
		print(spaceregex.findall(mytext))
	else: # remove requested characters  
		charregex = re.compile('^['+removechars+']*(.*?)['+removechars+']*$')
		print(charregex.findall(mytext))

# test the regex strip function
inputText = 'ssshiddenword...'
remove = 's. '
regexstrip(inputText,remove) 
#!/usr/bin/env bash 
#! python
# Adds Wikipedia bullet points to the start of each line on the clipboard 

import pyperclip 
text = pyperclip.paste()

# separate lines and add stars 
lines = text.split('\n')
for i in range(len(lines)): # loop through all indices in lines list  
	lines[i] = '* ' + lines[i] # add star to each string in lines list 

text = '\n'.join(lines)


pyperclip.copy(text) 


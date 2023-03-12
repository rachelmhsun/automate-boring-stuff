#!/usr/bin/env bash
#! python
# idiot.py - Checks if user is idiot
import pyinputplus as pyip 

while True: 
	prompt = 'Want to know how to keep an idiot busy for hours?\n'
	response = pyip.inputYesNo(prompt) 

	if response == 'no': 
		break
		

print('Thank you. Have a nice day.')

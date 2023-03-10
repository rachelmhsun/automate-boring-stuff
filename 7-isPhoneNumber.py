#!/usr/bin/env bash
#! python
# check if a number is a phone number 
import re

def isPhoneNumber(text): 
	# check if text is a phone number
	if len(text) != 12: 
		return False 
	for i in range(0,3): 
		if not text[i].isdecimal(): 
			return False
	if text[3] != '-':
		return False
	for i in range(4,7): 
		if not text[i].isdecimal(): 
			return False
	if text[7] != '-': 
		return False
	for i in range(8,12): 
		if not text[i].isdecimal(): 
			return False
	return True 

def isPhoneNumberReg(text): 
	# check if text is a phone number using regex 
	phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
	mo = phoneNumRegex.search(text)
	print('Phone number found: ' + mo.group())

def isPhoneNumberRegFindAll(text): 
	# check if text is a phone number using regex 
	phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
	mo = phoneNumRegex.findall(text)
	print('Phone numbers found: ')
	for i in range(0,len(mo)): 
		print(mo[i])

# print('Is 415-555-4242 a phone number?')
# print(isPhoneNumber('415-555-4242'))
# print('Is Moshi moshi a phone number?')
# print(isPhoneNumber('Moshi moshi'))

message = 'Call me at 415-555-4242 tomorrow. 415-555-4333 is my office.'
message2 = 'Is Moshi moshi a phone number?'
for i in range(len(message)): 
	chunk = message[i:i+12]
	if isPhoneNumber(chunk): 
		print('Phone number found: ' + chunk)
print('Done')

# use regex functions now
isPhoneNumberRegFindAll(message)



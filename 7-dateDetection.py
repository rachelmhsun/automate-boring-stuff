#!/usr/bin/env bash
#! python
# dateDetection.py - Checks if date is valid 
import re

# create date regex in DD/MM/YYYY format
dateRegex = re.compile(r'''(
	([0-9]{1,2})							# day
	(/)										# slash
	([0-9]{1,2})							# month
	(/)										# slash
	([0-9]{4})								# year
	)''',re.VERBOSE)

# input date here
text = '9/2/2000' 

for groups in dateRegex.findall(text): 
	# print(groups)
	date = '/'.join([groups[1], groups[3], groups[5]])
	if int(groups[5]) > 2999: 
		raise ValueError("Year out of range. Try another one.")
	elif int(groups[5])%4 == 0: # leap years are every year evenly divisible by 4
		febmax = 29
		if int(groups[5])%100 == 0: # except years evenly divisible by 100
			febmax = 28
			if int(groups[5])%400 == 0: # unless year is also evenly divisible by 400 
				febmax = 29
	else: 
		febmax = 28

	if int(groups[3]) > 12: # check if month is valid 
		raise ValueError("Month invalid. Try another one.")

	if int(groups[3]) in [4, 6, 9, 11]: # for months April, June, September, November 
		if int(groups[1]) > 30: # check if day is 30 or under 
			raise ValueError("Day invalid. Try another one.")
	elif int(groups[3]) == 2: # for month of February 
		if int(groups[1]) > febmax: # check if day is valid (given (leap) year max defined above)
			raise ValueError("Day invalid. Could be a leap year. Try another one.")
	else: # all other months 
		if int(groups[1]) > 31: # check if day is 31 or under 
			raise ValueError("Day invalid. Try another one.")
	
	print(date + ' is a valid date')

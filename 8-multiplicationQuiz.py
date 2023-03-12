#!/usr/bin/env bash
#! python
# multiplicationQuiz.py - quiz on multiplication of two integers 0 through 9 
import pyinputplus as pyip 
import random, time

numQuestions = 10
correctAnswers = 0

for questionNumber in range(numQuestions):
	num1 = random.randint(0,9)
	num2 = random.randint(0,9)

	prompt = '#%s: %s x %s = ' % (questionNumber, num1, num2) 
	try: 
		# right answers handled by allowRegexes
		# wrong ansers handled by blockRegexes, with custom message
		pyip.inputStr(prompt, allowRegexes=['^%s$' % (num1 * num2)],
							  blockRegexes=[('.*','Incorrect!')],
							  timeout=8, limit=3)
	except pyip.TimeoutException: 
		print('Out of time!')
	except pyip.RetryLimitException: 
		print('Out of tries!') 
	else: 
		# block runs if no exceptions were rai;sed in try block 
		print('Correct!') 
		correctAnswers += 1 
	time.sleep(1) # brief pause to let user see result 
print('Score: %s / %s' % (correctAnswers, numQuestions))
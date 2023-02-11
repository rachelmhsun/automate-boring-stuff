#!/usr/bin/env bash
#! python
# English to Pig Latin
print('Enter the English message to translate into Pig Latin:')
message = input()

VOWELS = ('a','e','i','o','u','y')
pigLatin = [] # list of words in pig latin
for word in message.split(): 
# separate non-letters at start of this word: 
	prefixNonLetters = ''
	while len(word) > 0 and not word[0].isalpha(): 
		prefixNonLetters += word[0]
		word = word[1:]
	if len(word) == 0: 
		pigLatin.append(prefixNonLetters)
		continue 

	# separate non-letters at end of this word: 
	suffixNonLetters = ''
	while not word[-1].isalpha():
		suffixNonLetters += word[-1]
		word = word[:-1]

	# Remember if word was in uppercase or title case 
	wasUpper = word.isupper()
	wasTitle = word.istitle()

	word = word.lower() # make word lowercase for transition 

	# separate consonants at start of word
	prefixConsonants = ''
	while len(word) > 0 and not word[0] in VOWELS: 
		prefixConsonants += word[0]
		word = word[1:]

	# add pig latin ending to word 
	if prefixConsonants != '': 
		word += prefixConsonants + 'ay'
	else: 
		word += 'yay'

	# set word back to uppercase or title case: 
	if wasUpper: 
		word = word.upper()
	if wasTitle: 
		word = word.title()

	# add non-letters back to start or end of word 
	pigLatin.append(prefixNonLetters + word + suffixNonLetters) 

# join all words back into single string 
print(' '.join(pigLatin))
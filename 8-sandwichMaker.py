#!/usr/bin/env bash
#! python
# sandwichMaker.py - asks users for sandwich preferences 
import pyinputplus as pyip 

# store dictionaries of costs here
breadcost = {'white': 2, 'wheat': 2.2, 'sourdough': 3}
proteincost = {'chicken': 3, 'turkey': 3.25, 'ham': 3.5, 'tofu': 2.75} 
cheesecost = {'cheddar': 0.5, 'Swiss': 1, 'mozzarella': 0.75}
toppingCost = {'mayo': 0.25, 'mustard': 0.25, 'lettuce': 0.75, 'tomato': 1} 

# request inputs from user and calculate costs incrementally 
bread = pyip.inputMenu(['white', 'wheat', 'sourdough'],prompt='Hello, welcome to Sandwich Maker! Please request a bread type:\n') 
protein = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'],prompt='Please select a protein: \n')
totalCost = breadcost[bread] + proteincost[protein] 

cheese = pyip.inputYesNo(prompt='Do you want cheese?\n')

if cheese == 'yes': 
	cheeseType = pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella'],prompt='Please select a cheese: \n') 
	totalCost += cheesecost[cheeseType]

toppingList = ['mayo', 'mustard', 'lettuce', 'tomato']
requestedToppings = []
for item in toppingList: 
	topping = pyip.inputYesNo(prompt='Do you want %s?\n' % (item))
	if topping == 'yes': 
		requestedToppings.append(item)
		totalCost += toppingCost[item]

numSandwiches = pyip.inputInt(prompt='How many sandwiches do you want?\n')
totalCost *= numSandwiches

# display total cost of sandwich after user enters selection 
print('Your sandwich costs: $%s' % (str(totalCost)))

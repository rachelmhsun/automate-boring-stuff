#!/usr/bin/env bash
#! python
# Right Justified Table Printer 

tableIn = [['apples', 'oranges', 'cherries', 'banana'], 
		   ['Alice', 'Bob', 'Carol', 'David'], 
		   ['dogs', 'cats', 'moose', 'goose']]

def printTable(tableData): 
	# takes input table and print columns of each sub-list as right justified items in each column 
	# find length of longest string in each column to pass to rjust()
	colWidths = [0]*len(tableData)
	for cInd, row in enumerate(tableData): 
		longestLen = 0 # reset longest length variable 
		for string in row: 
			newLen = len(string)
			if newLen > longestLen: 
				# set longest length to length of latest string if new string is longer than old longest string 
				longestLen = newLen 
		colWidths[cInd] = longestLen # allocate length of longest string in column 

	# print table with rjust() 
	# find number of rows and columns for loop ranges 
	numRows = len(tableData[0])
	numCols = len(tableData)
	for newCol in range(numRows): 
		rowVec = [] # initialize row vector to append to 
		for newRow in range(numCols):
			rowVec.append(tableData[newRow][newCol].rjust(colWidths[newRow]))
		print(' '.join(rowVec)) # print current row 

# call printTable function 
printTable(tableIn)
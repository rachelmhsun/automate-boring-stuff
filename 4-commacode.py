# comma code
def addComma(myList):
# this function takes a list, and returns a string
# with all items separated by comma and space
# with "and" inserted before the last item
    outputString = ''
    for item in myList[0:-1]:
        outputString += item + ', '
    outputString += 'and ' + myList[-1]
    return outputString

# input a list of strings
inputList = ['apples', 'bananas', 'memes', 'fun', 'tofu', 'cats']
print(addComma(inputList)) # print the result of addComma function

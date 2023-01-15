# collatz sequence
def collatz(number): # collatz conditions
    if number % 2 == 0:
        result = number // 2
    else:
        result = 3 * number + 1
    print(str(result))
    return result

print('input a number')

try:
    numInput = int(input())
except ValueError:
    print('please enter an integer')

numOut = 0
while numOut != 1:
    numOut = collatz(numInput)
    numInput = numOut

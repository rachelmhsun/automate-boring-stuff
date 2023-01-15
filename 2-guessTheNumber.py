# guess the number game
import random
secretNumber = random.randint(1, 20)
print('Choose a number between 1 and 20.')

# ask player to guess N times
N = 6 # number of guesses player is allowed to have
for guessesTaken in range(1,N):
    print('Please guess!')
    guess = int(input())

    if guess < secretNumber:
        print('guess too low')
    elif guess > secretNumber:
        print('guess too high')
    else:
        break # condition for correct guess

if guess == secretNumber:
    print('you guessed my number in ' + str(guessesTaken) + ' guesses')
else:
    print('Sorry, the number I was thinking of was ' + str(secretNumber))

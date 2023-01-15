# rock paper scissors game
import random, sys

print("ROCK, PAPER, SCISSORS")
# variables to keep track of wins, losses, ties
wins = 0
losses = 0
ties = 0

while True: # main game loop
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True: # player input loop
        print('Enter your move: (r)ock, (p)aper, (s)cissors or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit()
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break
        print('Type one of r, p, s, or q.')

    # display what player chose:
    if playerMove == 'r':
        print('Rock vs...')
    elif playerMove == 'p':
        print('Paper vs...')
    elif playerMove == 's':
        print('Scissors vs...')

    # display what computer chose:
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'r'
        print('Rock')
    if randomNumber == 2:
        computerMove = 'p'
        print('Paper')
    if randomNumber == 3:
        computerMove = 's'
        print('Scissors')

    # display and record win/loss/tie:
    if playerMove == computerMove:
        print('tie!')
        ties += 1
    elif playerMove == 'r' and computerMove == 's':
        print('you win!')
        wins += 1
    elif playerMove == 'p' and computerMove == 'r':
        print('you win!')
        wins += 1
    elif playerMove == 's' and computerMove == 'p':
        print('you win!')
        wins += 1
    elif playerMove == 'r' and computerMove == 'p':
        print('you lose!')
        losses += 1
    elif playerMove == 'p' and computerMove == 's':
        print('you lose!')
        losses += 1
    elif playerMove == 's' and computerMove == 'r':
        print('you lose!')
        losses += 1

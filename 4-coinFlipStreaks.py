# Coin Flip Streaks
import random
numTotalExp = 10000 # number of experiments to perform
streak = 0 # counts streak of 6 heads or tails in a row
streakprob = 0 # streak probability (i.e., number of streaks / total trials in list)
for experimentNumber in range(numTotalExp):
    # perform experiment numTotalExp number of times
    prevResult = 10 # set previous result for comparison to some number not 0 or 1
    numStreaks = 0 # reset number of streaks of 6 in list of 100
    randfliplist = [] # initialize randomly seeded list of 100 heads or tails values
    # create list of 100 heads or tails values
    for numFlips in range(100):
        randfliplist.append(random.randint(0,1))

    # check if there is a streak of 6 heads or tails in row
    for result in randfliplist:
        if result == prevResult:
            streak += 1 # continue adding to streak count until 6 reached
            if streak == 6:
                numStreaks += 1 # increment count of number of streaks of 6
                streak = 0 # reset counts of streak of 6 back to 0
        prevResult = result # set previous result to current result for comparison
    streakprob += numStreaks/100 # number of streaks / total trials in list, add to streak probability
print('Chance of Streak: %s%%' % (streakprob / numTotalExp)) # return average streak probability

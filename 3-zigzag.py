# zigzag animation
import time, sys
indent = 0 # number of spaces to indent
indentIncreasing = True # whether indent increasing or not
zigzag = 'hello'

try:
    while True: # main loop
        print(zigzag,end='')
        print('o' * indent, end='')
        print('')
        time.sleep(0.1) # pause for 1/10 of second

        if indentIncreasing:
            # increase number of spaces
            indent += 1
            if indent == 20:
                # change direction
                indentIncreasing = False
        else:
            # decrease number of spaces
            indent -= 1
            if indent == 0:
                # change direction
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()

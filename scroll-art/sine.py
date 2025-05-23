# code reference: https://github.com/asweigart/scrollart/blob/main/python/sinemessage.py
# live demo: https://scrollart.org/sine-message/

import math, time, os, sys

os.system('cls | clear')  # Clear the screen

width = os.get_terminal_size()[0] - 1
DELAY = 0.1
STEP_INCREASE = 0.2

def main():
    if len(sys.argv) > 1:
        message = sys.argv[1]
    else:
        message = '...'

    step = 0.0
    while True:  # Main program loop.
        width = os.get_terminal_size()[0] - 1
        multiplier = (width - len(message)) / 2
        sinOfStep = math.sin(step)
        padding = ' ' * int((sinOfStep + 1) * multiplier)
        print(padding + message)
        time.sleep(DELAY)
        step += STEP_INCREASE

try:
    main()
except KeyboardInterrupt:
    print('Sine Message, by Al Sweigart al@inventwithpython.com 2021')
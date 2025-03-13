# code reference: https://github.com/asweigart/scrollart/blob/main/python/spike.py
# live demo: https://scrollart.org/spike/

import math
import os
import time

DELAY = 0.2

def main():
    while True:
        for i in range(1, int(math.sqrt(os.get_terminal_size()[0] - 1))):
            print('𓆝 𓆟 𓆞 𓆝 𓆟' * (i*2))
            time.sleep(DELAY)
        for i in range(int(math.sqrt(os.get_terminal_size()[0] - 1)), 1, -2):
            print('-' * (i*i))
            time.sleep(DELAY)


try:
    main()
except KeyboardInterrupt:
    print('Spike, by Al Sweigart al@inventwithpython.com')
#print("hello world")

# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits: 
#     print(fruit)

# for x in range(6):
#     print(x)

# count = 0
# while count < 6: #if i put it at "if" it only runs it 1 time, which gives one 0 in the terminal 
#     print(count)
#     count += 1



#hit ctrl C to kill the function in the terminal

# count = 0
# while True: 
#     print(count)
#     count += 1

# import time
# i = 0
# while True:
#     #print("hello") #this will continually print hello
#     width = os.get_terminal_size()[0] - 1 #this will set the width of the text to go across the whole terminal
#     print("@" * 50)
#     i += 1
#     time.sleep(0.1)


import time, random, os
i = 0
while True:
    line = ' '
    width = os.get_terminal_size()[0] - 1 #this will set the width of the text to go across the whole terminal
    for i in range(width):
        if random.randint(0,13) < 5:
            line += " strawb"
        elif random.randint(0,13) > 7:
            line += "✧˖°ʚ🍓ɞ♡"
        elif random.randint(0,13) > 10:
            line += "erry"
        else: 
            line += " "

    print(line)
    time.sleep(0.5)

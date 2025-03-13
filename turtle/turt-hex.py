from turtle import*
import random
colormode(255)

#colors=["#7299F7","#97F772","#AE8DB9"]

title("my third turtle")
shape('turtle')
speed(15)

# for i in range(6): 
#     forward(100)
#     left(60)

# #colored hexagons
# for i in range(36):
#     c = colors[i % 3]
#     color(c)
#     fillcolor(c)
#     begin_fill()
#     for j in range(6):
#         forward(100)
#         left(60)
#     end_fill()
#     left(10)
# #colored hexegons end


#random colors 
colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "cyan"]
for n in range(36):
    color(random.choice(colors))
    # repeat 6 times - move forward and turn
    for i in range(6):
        forward(100)
        left(60)
    right(10) # add a turn
#random colors end



mainloop()
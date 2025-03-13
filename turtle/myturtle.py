from turtle import*
colormode(255)

title("my first sketch")

shape('turtle') 
speed(50)
bgcolor("lightblue") #set background color

colors = ['blue','green','red']
for i in range(100):   
    c = colors[i % 3]
    color(c)
    forward(100)
    right(45) # play around with a different angle value

speed(0)
color("#F7AC9C")
fillcolor("#9CF7BD")

begin_fill()
while True:
    forward(100)
    left(140) # change a different angle value
    if abs(pos()) < 1: # use `abs(pos()) < 1` to determine if turtle is back at it home position
        break
end_fill()

# #square 1
# pencolor(255,255,0) #set pen color
# fillcolor("#F7AC9C")
# def draw_square():
#     for i in range(4):
#         forward(100)
#         left(90)

# begin_fill()
# draw_square()
# end_fill()

# penup()
# forward(110)
# pendown()

# #square 2
# color("#9CF7BD")
# fillcolor("#F24C39")
# begin_fill()
# draw_square()
# end_fill()

# #square 3
# goto(100,200)
# color("#F2CDFE")
# fillcolor("#AE8DB9")

# begin_fill()
# draw_square()
# end_fill()

# #square 4
# goto(0,200)
# color("#7299F7")
# fillcolor("#97F772")

# begin_fill()
# draw_square()
# end_fill()




mainloop()



#python3 myturtle.py
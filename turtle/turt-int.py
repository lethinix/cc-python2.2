from turtle import*
import random
colormode(225)

# speed(15)
# def draw_flower(x, y):
#     penup()
#     goto(x, y)
#     pendown()
#     for i in range(5):
#         circle(20)
#         left(360/5)
# onscreenclick(draw_flower)

colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "cyan"]
def draw_flower(x, y):
    color(random.choice(colors))
    penup()
    goto(x, -150)
    pendown()
    goto(x, y)
    fillcolor(random.choice(colors))
    begin_fill()
    for i in range(8):
        circle(20)
        left(360/8)
    end_fill
onscreenclick(draw_flower)


#python3 turt-int.py

mainloop()
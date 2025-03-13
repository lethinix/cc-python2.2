from turtle import*
colormode(255)

title("my second sketch")
shape("turtle")

colors = ['blue', 'green', 'yellow']
speed(100)

# count = 5
# angle = 360 / count
# size = 100
# for i in range(count):
#     c = colors[i % 3]
#     left(angle)
#     circle(size -i * 11) # try `circle(size - i * 10)`


count = 5
angle = 360 / count
size = 100

# for i in range(count):
#     left(angle)
#     for j in range(count):
#         circle(size - j * 10)



# # dual flower example
# fillcolor("#FAC96E")
# begin_fill()
# for i in range(count):
#     left(angle)
#     for j in range(count):
#         circle(size)
#         size = size
# end_fill()

# fillcolor("#9CF7BD")
# begin_fill()
# pencolor("blue")
# pensize(2)
# for i in range(6):
#     left(360/6)
#     for j in range(count):
#         circle(size/2 + j * 5)
# end_fill()
# #dual flower example end

#flower example 2
count = 25 
speed(100)
fillcolor("#FAC96E")
begin_fill()
for i in range(count):
    left(angle)
    for j in range(count):
        circle(size + i*15)
        size = size
end_fill()
#flower example 2 end


mainloop()

#python3 turt.py
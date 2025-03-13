def setup():
    size(400, 400) 

def draw():
    for column in range(6):
        for row in range(6):
            x_pos = column * 80
            y_pos = row * 80
            drawBear(x_pos, y_pos)
#             circle(x_pos - 20, y_pos - 20, 30)
#             circle(x_pos + 20, y_pos - 20, 30)
#             circle(x_pos, y_pos, 50)
    print(mouse_x,mouse_y)




def drawBear(x_pos, y_pos):
    earSize = 30
    spacing = 20
    #colorRan = random(0,255)
    #colorr = (colorRan,colorRan,colorRan)
    #fill(color1)
    circle(x_pos - spacing, y_pos - spacing, earSize)
    circle(x_pos + spacing, y_pos - spacing, earSize)
    circle(x_pos, y_pos, 50)



run_sketch()
    
   
    


positions = []


def setup():
    size(400, 400) 

def draw():
    background(100)
    for pos in positions:
        drawBear(x, y)



def mouse_clicked(e):
    pos = {
        "x": mouse_x, #this s the key - it must be wrapped in double quotes in python
        "y": mouse_y
    }
    positions.append(pos)
    print(positions)


def key_pressed(e):
    print(e)
    key_value = e.get_key()
    if key_value== 's' or key_value == 'S':
        save('sketch.jpg')


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
    
   
    



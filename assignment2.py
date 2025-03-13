def setup():
    size(400, 400)
    no_loop()
    
def draw():
    background(53,29,7)
    
    #blend_mode(ADD)
    for j in range(620):
        cX2 = random(0,400)
        cY2 = random(0,400)
        cR2 = 27
        drawStems(cX2,cY2,cR2)
        
    #blend_mode(BLEND)
    
    for i in range(60):
        cX = random(0,400)
        cY = random(0,400)
        cR = 23
        drawFlower(cX,cY,cR)
        
 
def drawStems(cX2,cY2,cR2):
    stroke(31,120,220,150)
    #fill(31,120,220,150)
    #circle(cX2, cY2, cR2)
    fill(253,197,11, 80)
    circle(cX2, cY2, cR2-4)
 
 
def drawFlower(cX,cY,cR):
    
    

    push()
    stroke(31,89,250)
    fill(55,100,255,170)
    push()
    translate(cX, cY)
    rotate(HALF_PI)
    ellipse(0,0,15,40)
    pop()
    
    push()
    translate(cX, cY)
    rotate(PI/4)
    ellipse(0,0,15,40)
    pop()
    
    push()
    translate(cX, cY)
    rotate(PI/6)
    ellipse(0,0,15,40)
    pop()
    
    push()
    translate(cX, cY)
    rotate(PI/-4)
    ellipse(0,0,15,40)
    pop()
    
    push()
    translate(cX, cY)
    rotate(PI/3)
    ellipse(0,0,15,40)
    pop()
    
    ellipse(cX,cY,15,40)
    pop()
    
    push()
    fill(100,86,56,200)
    circle(cX,cY,cR)
    pop()
    
    push()
    fill(193,170,77,200)
    circle(cX,cY,5)
    pop()
    
    
run_sketch()
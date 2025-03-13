positions = [0 , 80 ,160 , 240]


def setup():
    size(400,400)
def draw():
    circle(0, height/2, 50)
   
   #for loop
#     for pos in positions:
#         circle(pos, height/2,50)

#     for i in range(10):
#         circle(width/2, i * 50, 50)

# 
#     for i in range(10):
#         fill(random(0, 255),random(0, 255),random(0, 255)
#         )
#         circle(random(width), random(height), 50)
#         
#     no_loop()
    
    
    
    
#     for i in range(10):
#         if i % 2 == 0:
#             fill(0,0,255)
#         else:
#             fill(255,255,255)
#             
#         for j in range(10):
#             circle(j*80, i*80, 50)
        
        
    for i in range(10):
        for j in range(10):
            if i == j:
                fill(0,0,255)
                
            else:
                fill(255,255,255)
            circle(j*80, i*80, 50)
        
        


run_sketch()
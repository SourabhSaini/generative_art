angle = 0
w = 24
maxD = 0

def setup():
    global angle, w, maxD
    size(500, 500, P3D)
    maxD = dist(0, 0, 200, 200)
    
def draw():
    global angle, w, maxD
    background(042)
    ortho(-400, 400, 400, -400, 0, 600)
    #directionalLight(56, 99, 100, .1, .2, 1)
    #directionalLight(150, 99, 15, 1, .2, 0)
    #directionalLight(18, 99, 11, 0, 2, 0)
    spotLight(156, 102, 106, 80, 20, 40, 1, 1, 1, -PI, .1)
    
    translate(width/2, height/2)
    # rectMode(CENTER)
    
    rotate(angle/10, 0, 1, 1)
    rotateX(QUARTER_PI)
    rotateY(-atan(1/sqrt(2)))
    
    for z in range(0, height, w):
        for x in range(0, width, w):
            push()
            d = dist(x, z, width/2, height/2)
            xoff = map(d, 0, maxD, -PI, PI)
            a = angle + xoff
            h = map(sin(a), -1, 1, 50, 400)
            
            translate(x-width/2, 0, z-height/2) 
            box(w-2, h, w-2)
            
            pop()
            
        xoff += .1
    
        
    angle -= 0.05

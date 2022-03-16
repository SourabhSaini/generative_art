angle = 0
aVel = 0
aAcc = 0.0001

def setup():
    size(500, 500)
    

def draw():
    global angle, aVel, aAcc
    background(023)
    translate(width/2, height/2)
    rotate(angle)
    
    ellipse(50, 0, 16, 16);
    ellipse(-50, 0, 16, 16);
    
    aVel += aAcc
    angle += aVel
    
    
    
    
    

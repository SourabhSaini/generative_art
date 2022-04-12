   
def setup():
    size(500, 500)
    
def draw():
    
    background(023)
    translate(width/2, height/2)
    x = 100 * cos(TWO_PI * frameCount / 120)
    noStroke()
    ellipse(x, 0, 20, 20)

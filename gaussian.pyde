x = dict()
w = 500

def setup():
    global x, w
    
    size(500, 500)
    background(023)
    
    for _ in range(w):
        x[_] = 0
    
    
def draw():
    global x
    
    rg = randomGaussian()
    
    sd = 50  # more deviation/wider bell
    # sd = 10  # less deviation/narrow bell
    mean = 250
    c = int(sd * rg + mean)
    
    noStroke()
    fill(255, 10)
    ellipse(c, 400, 16, 16)
    
    x[c] = x[c]+1
    
    stroke(250, 10)
    for _ in range(w):
        point(_, 300-x[_])
    
    
    
    
    
    

    

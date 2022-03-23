scl = 20
gap = 5
w = 500
h = 500
bars = int((w+gap)/(scl+gap))
r = rb = []

def setup():
    global bars, gap, scl, r, rb
    size(500, 400)        
    
    # Uniform
    u = [-10, 0, 10]
    r = [u[int(random(len(u)))] for _ in range(bars)] 

    # Non-Uniform as picking -10 has more probability
    nu = [-10, 0, 10, 0, 0, -10, -10, -10, -10, -10]
    rb = [nu[int(random(len(nu)))] for _ in range(bars)] 
              
        
def draw():
    global bars, gap, scl, h, r, rb
    background(023)
    stroke(230)

    # Normal/Uniform Distribution
    for i in range(bars):
        rect(i*(scl+gap), scl+r[i], scl, h/3-r[i])
        
    # Non Uniform Distribution
    for i in range(bars):
        rect(i*(scl+gap), h/2-scl+rb[i], scl, h/3-rb[i])
    
    

cols=rows=fly=0
scl=25
w = 1000
h = 1000

def setup():
    global cols, rows, scl, w, h
    size(500,500, P3D)
    cols = w/scl
    rows = h/scl
    
def draw():
    global w, h, cols, rows, fly
        
    fly-=0.02
    yoff = fly
    terrain=[]
    for y in range(rows):
        tmp = []
        xoff=0
        for x in range(cols):
            tmp.append(map(noise(xoff, yoff), 0, 1, -10, 80))
            xoff+=0.2
        terrain.append(tmp)
        yoff+=0.2
    
    background(053)
    noFill()
    strokeWeight(1)
    stroke(255)
    translate(width/2, height/2+200)
    rotateX(PI/3)
    translate(-w/2, -h/2)
    
    for y in range(rows-1):
        
        beginShape(TRIANGLE_STRIP)
        for x in range(cols):
            stroke(255, 255-y*6, x*3)
            vertex(x*scl, y*scl, terrain[y][x])
            vertex(x*scl, (y+1)*scl, terrain[y+1][x])
        endShape()

    stroke(255, 219, 8)
    translate(width/3, -height-150, 0);
    rotateZ(fly/5);
    sphereDetail(10, 5)
    sphere(200)
    
    
    
    

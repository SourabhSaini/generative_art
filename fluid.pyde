mover = 0
fluid = 0

def setup():
    global mover, fluid
    size(500, 500)
    mover = Mover()
    fluid = Fluid(0, height/2, width, height/2, 0.7)
    #frameRate(5)

def draw():
    global mover, fluid
    background(023)
    fluid.display()
    if mover.isInside(fluid):
            mover.drag(fluid)
    gravity = PVector(0, 0.1*mover.mass)
    mover.applyForce(gravity)
    mover.update()
    mover.display()
    mover.checkEdges()

class Mover:
    def __init__(self):
        self.loc = PVector(width/2, 0)
        self.vel = PVector(0, 0)
        self.acc = PVector(0, 0)
        self.mass = int(random(15, 30))
    
    def update(self):
        v = self.vel.get()
        v.add(self.acc)
        self.loc.add(v)
        self.acc.mult(0)
    
    def applyForce(self, force):
        f = PVector.div(force,self.mass)
        self.vel.add(f)
        
    def drag(self, medium):
        speed = self.vel.mag()
        dragMag = medium.c*(speed**2)
        drag = self.vel.get()
        drag.mult(-1)
        drag.mult(dragMag)
        self.applyForce(drag)
         
    def isInside(self, medium):
        if self.loc.y > medium.y and self.loc.y < medium.y+medium.h:
            return True
        else:
            return False
    
    def checkEdges(self):
        if self.loc.x > width:
            self.loc.x = width
            self.vel.x *= -1
        elif self.loc.x < 0:
            self.loc.x = 0
            self.vel.x *= -1
        if self.loc.y > height:
            self.loc.y = height
            self.vel.y *= -1   
        elif self.loc.y < 0:
            self.loc.y = 0
            self.vel.y *= -1
    
    def display(self):
        noStroke()
        fill(230)
        ellipse(self.loc.x, self.loc.y, self.mass, self.mass)
        
class Fluid:
    def __init__(self, x, y, w, h, c):
        self.x = x
        self.y = y
        self.w = w
        self.h = h 
        self.c = c # Coefficient of Drag

    def display(self):
        noStroke()
        fill(93, 115, 255)
        rect(self.x, self.y, self.w, self.h)

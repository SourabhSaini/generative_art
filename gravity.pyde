mover1 = 0
mover2 = 0

def setup():
    global mover1, mover2
    
    size(500, 500)
    mover1 = Mover()
    mover2 = Mover()
    
def draw():
    global mover1, mover2
    background(023)
    
    mover1.update()
    mover2.update()
    mover1.applyForce(mover2)
    mover2.applyForce(mover1)
    mover1.display()
    mover2.display()
    
class Mover:
    def __init__(self):
        self.loc = PVector(random(width), random(height))
        self.vel = PVector(0, 0)
        self.acc = PVector(0, 0)
        self.mass = int(random(10, 50))
    def update(self):
        v = self.vel.get()
        self.acc.add(v)
        self.loc.add(self.acc)
        self.acc.mult(0)
    def applyForce(self, ast):
        force = PVector.sub(ast.loc, self.loc)
        dist = force.mag()
        dist = constrain(dist, 5, 25)
        m  = (self.mass * ast.mass)/(dist**2)
        force.normalize()
        force.mult(m)
        force.div(self.mass)
        self.vel.add(force)
    def display(self):
        fill(255, 112, 90)
        stroke(255)
        ellipse(self.loc.x, self.loc.y, self.mass, self.mass)    
    

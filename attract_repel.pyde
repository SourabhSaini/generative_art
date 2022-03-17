movers = []
a = 0

def setup():
    global movers, a
    size(600, 600)
    a = Attractor()
    for i in range(5):
        movers.append(Mover(random(4, 12), random(width), random(height)))

def draw():
    global movers, a
    background(255)
    a.display()
    for i in range(len(movers)):
        for j in range(len(movers)):
            if i != j:
                force = movers[j].repel(movers[i])
                movers[i].applyForce(force)
            force = a.attract(movers[i])
            movers[i].applyForce(force)
            movers[i].update()
            movers[i].display()


class Attractor:
    def __init__(self):
        self.position = PVector(width/2, height/2)
        self.mass = 10
        self.radius = self.mass*3
        
    def attract(self, mover):
        force = PVector.sub(self.position, mover.position)
        d = force.mag()
        d = constrain(d, 5, 25)
        force.normalize()
        strength = (0.05* self.mass * mover.mass) / (d * d)
        force.mult(strength)
        return force
    
    def display(self):
        ellipseMode(CENTER)
        noStroke()
        fill(023)
        ellipse(self.position.x, self.position.y, self.radius*2, self.radius*2)
    
class Mover:
    def __init__(self, m, x, y):
        self.position = PVector(x, y)
        self.velocity = PVector(0, 0)
        self.acceleration = PVector(0, 0)
        self.mass = m
        
    def applyForce(self, force):
        f = PVector.div(force, self.mass)
        self.acceleration.add(f)
    
    def update(self):
        self.velocity.add(self.acceleration)
        self.position.add(self.velocity)
        self.acceleration.mult(0)
    
    def display(self):
        noStroke()
        fill(175, 200)
        ellipse(self.position.x, self.position.y, self.mass*2, self.mass*2)
    
    def repel(self, mover):
        force = PVector.sub(self.position, mover.position)
        d = force.mag()
        d = constrain(d, 1, 500)
        force.normalize()
        strength = (self.mass * mover.mass) / (d * d)
        force.mult(-1*strength)
        return force
    
    def checkEdges(self):
        if self.position.x > width:
            self.position.x = width
            self.velocity.x *= -1
        elif self.position.x < 0:
            self.position.x = 0
            self.velocity.x *= -1
        if self.position.y > height:
            self.position.y = height
            self.velocity.y *= -1
        elif self.position.y < 0:
            self.position.y = 0
            self.velocity.y *= -1

    
        
        

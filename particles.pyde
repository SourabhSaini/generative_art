particles = []

def setup():
    size(500, 500)
    
def draw():
    global particles
    background(0)
    
    particles.append(Particle(PVector(width/2, 400)))
        
    for p in particles:
        p.run()
        
        if p.isDead():
            particles.remove(p)
    
class Particle:
    def __init__(self, l):
        self.loc = l
        self.vel = PVector(random(-1, 1), random(-3, -50))
        self.acc = PVector(0, random(0.001, 0.03))
        self.hue_v = random(0, 500)
        self.lifespan = 255
        
    def run(self):
        self.update()
        self.display()
        
    def update(self):
        self.vel.add(self.acc)
        self.loc.add(self.vel)
        self.lifespan -= 1
    
    def display(self):
        noStroke()
        colorMode(HSB, 500, 500, 500)
        fill(self.hue_v, 500, 300, self.lifespan)
        ellipse(self.loc.x, self.loc.y, self.lifespan/8, self.lifespan/8)
    
    def isDead(self):
        if self.lifespan <= 50:
            return True
        else:
            return False
        
    

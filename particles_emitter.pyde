ps = None

def setup():
    global ps
    size(500, 500)
    ps = System()
    
def draw():
    global ps
    background(0)

    ps.run()            

class System:
    def __init__(self):
        self.systems = []
        
    def addSystem(self):
        self.systems.append(ParticleSystem(PVector(mouseX, mouseY)))
        
    def run(self):
        if mousePressed:
            self.addSystem()
        for s in self.systems:
            s.run()

class ParticleSystem:
    def __init__(self, position):
        self.particles = []
        self.origin = position
        
    def addParticle(self):
        self.particles.append(Particle(self.origin))
    
    def run(self):
        self.addParticle()
        for p in self.particles:
            p.run()

            if p.isDead():
                self.particles.remove(p)
                    
class Particle:
    def __init__(self, origin):
        self.loc = origin.get()
        self.vel = PVector(random(-1, 1), random(-3, -5))
        self.acc = PVector(0, random(0.01, 0.03))
        self.hue_v = int(random(0, 500))
        self.lifespan = 255
        
    def run(self):
        self.update()
        self.display()
            
    def update(self):
        self.vel.add(self.acc)
        self.loc.add(self.vel)
        self.lifespan -= 5
    
    def display(self):
        noStroke()
        colorMode(HSB, 500, 500, 500)
        fill(self.hue_v, 500, 300, self.lifespan)
        ellipse(self.loc.x, self.loc.y, self.lifespan/20, self.lifespan/20)
    
    def isDead(self):
        if self.lifespan <= 0:
            return True
        else:
            return False
    

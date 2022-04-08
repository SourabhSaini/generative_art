ranges = 150

def setup():
  size(1000, 1000)
  background(0)

def mouseClicked(event): 
    noLoop()
    save("heart.png")
        
def draw():
  global ranges
  background(0)
  noFill()
  #strokeWeight(2)

  for i in range(ranges):
    paint = map(i, 0, ranges, 0, 255)
    stroke(paint)
    
    beginShape();
    for x in range(0, width + 11, 20):
      n = noise(x * 0.001, i * 0.01, frameCount * 0.005)
      y = map(n, 0, 1, 0, height)
      curveVertex(x, y)
    
    endShape()

  

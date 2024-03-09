g=0
d=600
def setup():
    size(600,600)
def draw():
    global g,d
    background(0)
    fill(46,149,255)
    ellipse(g,g,100,100)
    fill(255,46,217)
    ellipse(d,d,100,100)
    g=g+1
    if g > 300:
        noLoop()
    d=d-1
    if d == 300:
        noLoop()

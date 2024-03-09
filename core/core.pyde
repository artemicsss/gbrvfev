x=0
def setup():
    size(600,600)
def draw():
    global x
    background(0)
    ellipse(300,300,x,x)
    x=x+1
    if x > 598:
        x=0    

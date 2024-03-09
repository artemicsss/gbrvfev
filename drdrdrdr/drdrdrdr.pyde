w=0
def setup():
    size(600,600)
def draw():
    global w
    fill(w,w,w)
    ellipse(300,300,100,100)
    w=w+1
    if w > 255:
        w=0
        

s=0
def setup():
    size(600,600)



def draw():
    global s
    background(0)
    translate(300,300)
    rotate(radians(s))
    rect(0,0,s,s)
    s=s+1

    

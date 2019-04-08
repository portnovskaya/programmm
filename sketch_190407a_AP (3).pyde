def setup():
    background(0,255,255);
    size (400, 400)
    textAlign(CENTER)
    textSize(120)
    global c
    global b
    c =('FFFFFFFF')
    b =('FF000000')
def draw():
    global c
    global b
    if keyPressed == True:
        fill(0)
        if key == 'A' or key == 'a': 
          text('A', width/2+70, height/2)
        if mousePressed and keyCode==RIGHT:
         fill(255,0,0)
         text('A', width/2+70, height/2) 
    else:
       if mousePressed:
         fill(255,255,255)
         text('P', width/2-70, height/2)
    if mousePressed and keyCode==LEFT: 
         fill(20,13,200)
         text('P', width/2-70, height/2)  
    if hex(get(mouseX,mouseY)) == c:
         fill(255,0,255)
         text('P', width/2-70, height/2)
    else:
       if hex(get(mouseX,mouseY)) == b:
         fill(0,255,0)   
         text('A', width/2+70, height/2)
   

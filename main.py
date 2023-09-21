import turtle

#turtle.tracer(0,0)

def draw_coordinate_plane():
  for i in range(-310, 310, 10):
    turtle.goto(0, i)
    turtle.write(f"0, {i}")
  turtle.goto(0, 0)

#draw_coordinate_plane()

def move_pen(x,y):
  turtle.up()
  turtle.goto(x,y)
  turtle.down()

def penguin_eyes(size, direction):
  '''Draws eyes in given direction "right" or "left"'''
  if direction == "left":
    right_left = -55
  if direction == "right":
    right_left = 55
  move_pen(right_left*size,100*size)
  turtle.circle(10*size,360)



def penguin_head(size):
  penguin_eyes (size,"left")
  penguin_eyes (size,"right")
  move_pen(0*size,0*size)
  turtle.up()
  turtle.circle(125*size,60)
  turtle.down()
  print(turtle.position())
  turtle.circle(125*size,240)
  print(turtle.position())
  turtle.circle(75*size,-145)
  turtle.left(120)
  turtle.forward(80*size)
  turtle.left(130)
  for i in range (2):
    turtle.forward(15*size)
    turtle.right(90)
    turtle.forward(15*size)
    turtle.right(90)
  
  turtle.right(50)
  turtle.forward(21.2132034356*size)
  
  turtle.left(92)
  turtle.forward(80*size)
  turtle.right(248)
  turtle.circle(75*size,-120)

penguin_head(1)

move_pen(108.25,62.50)

turtle.left(180)
turtle.circle(50,100)

move_pen(-108.25,62.50)

turtle.left(100)
turtle.circle(50,-100)



move_pen(240,200)

move_pen(-100,-300)

offset = 0
radius = 0

for h in range (1,4):
  offset = offset+radius
  radius = 5*(h+1)
  move_pen(-100+(offset),-300)
  turtle.circle(radius)
  offset = offset+radius
  print (offset)

move_pen(100,-300)

offset = 0
radius = 0

for h in range (1,4):
  offset = offset+radius
  radius = 5*(h+1)
  move_pen(100-(offset),-300)
  turtle.circle(radius)
  offset = offset+radius
  print (offset)

#turtle.update()
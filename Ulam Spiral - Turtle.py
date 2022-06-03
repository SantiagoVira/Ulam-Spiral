# Prime/Ulam spiral

import turtle, math

turtle.Screen().bgcolor("black")
turtle.screensize(canvwidth=800, canvheight=800)
turtle.tracer(0,0)

bob = turtle.Turtle()
layout_size = 250                                                         # Width of final spiral
layout_count = layout_size ** 2
show_lines = False                                                        # Showing lines connecting dots?
dot_size = 3                                                              # Dot size
space = 2 * dot_size 

def isprime(num):
  for i in range(2, math.ceil(num**0.5) + 1):
    if num % i == 0 and num != i:
      return False
  if num == 1:
    return False
  return True

if not show_lines:
  bob.pu()
bob.speed(0)
bob.color("white")

leg = 1
num_left = 1

for i in range(1, layout_count + 1):
  
  if isprime(i):
    bob.dot(dot_size)
  bob.forward(space)
  
  num_left -= 1
  if num_left <= 0:
    leg +=1
    num_left = math.ceil(leg/2)
    bob.left(90)

turtle.mainloop()
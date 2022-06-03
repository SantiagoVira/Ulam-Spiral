# Prime/Ulam spiral

import pygame, math

# Setup Pygame window
pygame.init()
W, H = 800, 800
center = (W/2, H/2)
screen = pygame.display.set_mode([W, H])

# program constants
font_size = 32                                                            # Number size
font = pygame.font.Font('freesansbold.ttf', font_size)
radius = 1                                                                # Dot size
show_lines = False

# layout constants
layout_size = 250                                                         # Width of final spiral
layout_count = layout_size ** 2
show_nums = False                                                         # True if displaying number values, False for dots
step_size = font_size + 15 if show_nums else 3*radius #W / layout_size

def isprime(num):
  for i in range(2, math.ceil(num**0.5) + 1):
    if num % i == 0 and num != i:
      return False
  if num == 1:
    return False
  return True

def draw_text(x, y, text):
  object = font.render(text, True, (255, 255, 255))
  object_rect = object.get_rect()
  object_rect.center = (x, y)

  screen.blit(object, object_rect)

def draw_spot(x, y, num):
  if isprime(num):
    if show_nums:
      draw_text(x, y, str(num))
    else:
      pygame.draw.circle(screen, (255, 255, 255), (x, y), radius)

# Start a loop
running = True
while running:
  # If the user closes the window, quit the program
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    # if event.type == pygame.MOUSEBUTTONDOWN:

  # Draw the background
  screen.fill((0, 0, 0))
  #pygame.draw.circle(screen, (255, 0, 0), center, 5)

  # Draw the numbers
  (x, y) = center
  if layout_size % 2 == 0:
    x -= step_size / 2
    y += step_size / 2

  draw_spot(x, y, 1)


  leg = 1
  dir = 0
  num_left = 1

  for i in range(2, layout_count + 1):
    # num_steps_in_leg = math.ceil((i+1)/2)
    prev = (x, y)

    dir = dir%4
    if dir == 0:
      x += step_size
    elif dir == 1:
      y -= step_size
    elif dir == 2:
      x -= step_size
    elif dir == 3:
      y += step_size
    
    draw_spot(x, y, i)
    if show_lines:
      pygame.draw.line(screen, (255, 255, 255), prev, (x, y))
    
    num_left -= 1
    if num_left <= 0:
      leg +=1
      num_left = math.ceil(leg/2)
      # 1 2 3 4
      dir += 1

  # Update the screen
  pygame.display.update()

# Quit the program
pygame.quit()
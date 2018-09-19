#imports the pygame module
import pygame
pygame.init()

#sets the dimensions of the pygame window
win = pygame.display.set_mode((800, 800))

#sets the caption for the game
pygame.display.set_caption("Python Arcade")

#========================CHARACTER VARIABLES====================================
#these variables will describe the state of the main sprite
##x and y will control the placement. Note that the sprite is placed from the--
##--upper left.
x = 50
y =  750

##Height and Width are the dimensions of the character
height = 50
width = 40

##represents the character's velocity
velocity = 5
#==============================================================================

#==================MAIN LOOP===================================================
#this variable will toggle to terminate the main loop
run = True
while run:
#   #we give the game a time delay (in ms) to allow some time to process things.
  pygame.time.delay(100)

  #afterwards we check for events such as keystrokes using a for loop
  for event in pygame.event.get():
    #handles the eventuality that the user quits
    if event.type == pygame.QUIT:
      run = False

  #we set the keys variable to load the state of all keyboard keys being pressed
  keys = pygame.key.get_pressed()

  ##then we check for the key-presses using the pygame key ascii and bind--
  ##--actions to them
  ### pygame key ASCII : https://www.pygame.org/docs/ref/key.html
  if keys[pygame.K_LEFT]: 
    x-=velocity

  if keys[pygame.K_RIGHT]: 
    x+=velocity

  if keys[pygame.K_UP]:
    y-=velocity

  if keys[pygame.K_DOWN]: 
    y+=velocity

  #we fill the rest of the window before updating to clear old shapes
  
  win.fill((0,0,0))

  #pygame.draw is the pygame module for drawing shapes!
  ##place the surface you want to draw on as the first argument.
  ##in this case the surface is the window.

  ##the second arg will be the color, defined in rgb ()

  ##the third argument is the position of the shape, passed in as--
  ##-- (x position, y position, width, height)
  pygame.draw.rect(win, (255, 0, 255), (x, y, width, height))

  #this line refreshes the pygame gui, updating it.
  pygame.display.update()

pygame.quit()

#===================================MAIN LOOP END===============================

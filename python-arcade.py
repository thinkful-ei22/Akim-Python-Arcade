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
# run = True
# while run:
#   #we give the game a time delay (in ms) to allow some time to process things.
#   pygame.time.delay(100)

#   #afterwards we check for events such as keystrokes using a for loop
#   for event in pygame.event.get():
#     if event.type == pygame.QUIT:
#       run false

# pygame.quit()



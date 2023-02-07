import pygame
import random
 
# Initialize the game engine
pygame.init()
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# Starting position of the rectangle
rect_x = 50
rect_y = 50
 
# Speed and direction of rectangle
rect_change_x = 5
rect_change_y = 5
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
 
    # Move the rectangle starting point
    rect_x += rect_change_x
    rect_y += rect_change_y
 
    # Bounce the ball if needed
    if rect_y > 450 or rect_y < 0:
        rect_change_y = rect_change_y * -1
    if rect_x > 650 or rect_x < 0:
        rect_change_x = rect_change_x * -1
 
    # Clear the screen
    screen.fill(WHITE)
 
    # Draw the rectangle
    pygame.draw.rect(screen, BLACK, [rect_x, rect_y, 50, 50])
 
    # --- Drawing code should go here
 
    # --- Go ahead and update the screen.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
sys.exit()

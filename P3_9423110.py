import numpy as np
import pygame
import random
import  cv2

# Initialize the game engine
pygame.init()

width = 600
height = 300

WHITE = [255, 255, 255]

# Set the height and width of the screen
SIZE = [width, height]

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Snow Animation")

# Create an empty array
snow_list = []
cam = cv2.VideoCapture(0)

# Loop 50 times and add a snow flake in a random x,y position
for i in range(50):
    x = random.randrange(0, width)
    y = random.randrange(0, height)
    snow_list.append([x, y])

clock = pygame.time.Clock()

# Loop until the user clicks the close button.
done = False
while not done:

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    # Set the screen background
    ret_val, img = cam.read()
    # img_width = img.shape[1]
    # img_height = img.shape[0]
    screen.fill([0, 0, 0])
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = np.rot90(img)
    img = pygame.surfarray.make_surface(img)

    screen.blit(img, (0,-100))

    # Process each snow flake in the list
    for i in range(len(snow_list)):

        # Draw the snow flake
        pygame.draw.circle(screen, WHITE, snow_list[i], 2)

        # Move the snow flake down one pixel
        snow_list[i][1] += 1

        # If the snow flake has moved off the bottom of the screen
        if snow_list[i][1] > height:
            # Reset it just above the top
            y = random.randrange(-50, -10)
            snow_list[i][1] = y
            # Give it a new x position
            x = random.randrange(0, width)
            snow_list[i][0] = x

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    clock.tick(20)

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()
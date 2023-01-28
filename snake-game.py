import pygame
import time

# Initialize pygame
pygame.init()

# Set the size of the screen (width, height).
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Snake Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Set the snake's starting position
x_pos = 50
y_pos = 50

# Set the snake's block size
block_size = 10

# Set the snake's initial speed
x_speed = 0
y_speed = 0

# Main game loop
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # Move the snake
    x_pos += x_speed
    y_pos += y_speed

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the snake
    pygame.draw.rect(screen, (255, 255, 255), [x_pos, y_pos, block_size, block_size])

    # --- Drawing code should go here

    # --- Go ahead and update the screen.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()

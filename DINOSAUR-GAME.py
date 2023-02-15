import pygame
import random

# Set up the game screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 300
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dinosaur Game")

# Set up the dinosaur
dino_width = 40
dino_height = 50
dino_x = 50
dino_y = SCREEN_HEIGHT - dino_height - 50
dino_speed = 5
dino_jump_height = 100
dino_jump_speed = 10
dino_is_jumping = False
dino_rect = pygame.Rect(dino_x, dino_y, dino_width, dino_height)

# Set up the cactus obstacles
cactus_width = 20
cactus_height = 50
cactus_x = SCREEN_WIDTH
cactus_y = SCREEN_HEIGHT - cactus_height - 50
cactus_speed = 5
cactus_rect = pygame.Rect(cactus_x, cactus_y, cactus_width, cactus_height)

# Set up the score
score = 0
font = pygame.font.SysFont(None, 30)

# Set up the game loop
game_over = False
clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not dino_is_jumping:
                dino_is_jumping = True

    # Move the dinosaur
    if dino_is_jumping:
        if dino_jump_height >= 0:
            dino_y -= dino_jump_speed
            dino_jump_height -= dino_jump_speed
        else:
            dino_is_jumping = False
            dino_jump_height = 100
    else:
        dino_y += dino_speed
    dino_rect = pygame.Rect(dino_x, dino_y, dino_width, dino_height)

    # Move the cactus
    cactus_x -= cactus_speed
    if cactus_x < -cactus_width:
        cactus_x = SCREEN_WIDTH
        cactus_y = SCREEN_HEIGHT - cactus_height - 50
        score += 1
    cactus_rect = pygame.Rect(cactus_x, cactus_y, cactus_width, cactus_height)

    # Check for collisions
    if dino_rect.colliderect(cactus_rect):
        game_over = True

    # Draw the game objects
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 0, 0), dino_rect)
    pygame.draw.rect(screen, (0, 0, 0), cactus_rect)
    score_text = font.render("Score: " + str(score), True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    pygame.display.update()

    # Increase the difficulty as the score increases
    if score % 10 == 0:
        cactus_speed += 1

    clock.tick(60)

# Clean up the game
pygame.quit()

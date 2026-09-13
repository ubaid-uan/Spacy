import random
import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((650, 500))
pygame.display.set_caption('Spacy')
clock = pygame.time.Clock()
score = pygame.font.Font(None, 50)


# Score...........
score_surface = score.render('Score:', False, '#fff8f0')
score_surface = pygame.transform.scale(score_surface, (80, 40))
score_rec = score_surface.get_rect(topleft=(20, 20))

# Background.............
space_back = pygame.image.load('Spacy/images/back.png').convert_alpha()
space_back = pygame.transform.scale(space_back, (650, 500))

# Spaceship..............
spacer = pygame.image.load('Spacy/images/spacer.png').convert_alpha()
spacer = pygame.transform.scale(spacer, (100, 100))
spacer_rect = spacer.get_rect(midbottom=(325, 500))

# Astroids.........
ast1 = pygame.image.load('Spacy/images/ast1.png').convert_alpha()
ast1 = pygame.transform.scale(ast1, (60, 60))
ast1_rect = ast1.get_rect(topleft=(300, -50))

ast2 = pygame.image.load('Spacy/images/ast2.png').convert_alpha()
ast2 = pygame.transform.scale(ast2, (100, 100))
ast2_rect = ast2.get_rect(topright=(140, -120))

ast3 = pygame.image.load('Spacy/images/ast3.png').convert_alpha()
ast3 = pygame.transform.scale(ast3, (70, 70))
ast3_rect = ast3.get_rect(topleft=(20, -19))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # if event.type == pygame.MOUSEMOTION:
        #     print(event.pos)

    screen.blit(space_back, (0, 0))
    screen.blit(spacer, spacer_rect)
    # pygame.draw.rect(screen, "#5a4847", score_rec)
    screen.blit(score_surface, (20, 20))

    # Astroids...........
    ast1_rect.top += 4
    if ast1_rect.bottom >= 549:
        random_x = random.randint(0, 250)
        random_y = random.randint(251, 590)
        ast1_rect.top = random.randint(-450, -120)
        ast1_rect.x = random.randint(random_x, random_y)
    screen.blit(ast1, ast1_rect)

    ast2_rect.top += 2
    if ast2_rect.bottom >= 569:
        ast2_rect.top = random.randint(-200, -100)
        ast2_rect.x = random.randint(0, 550)
    screen.blit(ast2, ast2_rect)

    ast3_rect.top += 3
    if ast3_rect.bottom >= 649:
        ast3_rect.top = -19
    screen.blit(ast3, ast3_rect)

    # keys.........
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and spacer_rect.left > -2:
        spacer_rect.right -= 3

    if keys[pygame.K_d] and spacer_rect.right < 650:
        spacer_rect.left += 3

    if keys[pygame.K_w] and spacer_rect.top > 0:
        spacer_rect.top -= 3

    if keys[pygame.K_s] and spacer_rect.bottom < 500:
        spacer_rect.bottom += 3

    # mouse_po = pygame.mouse.get_pos()
    # if spacer_rect.collidepoint(mouse_po):
    #     print(pygame.mouse.get_pressed)

    pygame.display.update()
    clock.tick(60)

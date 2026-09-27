import random
import pygame
from sys import exit


def scoring():
    cur_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surface = score.render(f'Score: {cur_time}', False, "#fff0f0")
    score_surface = pygame.transform.scale(score_surface, (100, 50))
    score_rec = score_surface.get_rect(topright=(630, 16))
    screen.blit(score_surface, score_rec)


def level_display():
    cur_time = int(pygame.time.get_ticks() / 1000) - start_time
    level = (cur_time // 10) + 1

    level_surface = score.render(
        f'Level: {level}', False, "#e2b728")
    level_surface = pygame.transform.scale(level_surface, (120, 50))
    level_rec = level_surface.get_rect(topleft=(10, 16))
    screen.blit(level_surface, level_rec)


def asteroid_col():
    global ast1_vx, ast2_vx, ast3_vx, ast4_vx, ast5_vx

    if ast1_rect.colliderect(ast2_rect):
        ast1_vx = -2 if ast1_rect.centerx < ast2_rect.centerx else 2
        ast2_vx = 2 if ast1_rect.centerx < ast2_rect.centerx else -2

    if ast1_rect.colliderect(ast3_rect):
        ast1_vx = -2 if ast1_rect.centerx < ast3_rect.centerx else 2
        ast3_vx = 2 if ast1_rect.centerx < ast3_rect.centerx else -2

    if ast2_rect.colliderect(ast3_rect):
        ast2_vx = -2 if ast2_rect.centerx < ast3_rect.centerx else 2
        ast3_vx = 2 if ast2_rect.centerx < ast3_rect.centerx else -2

    if ast1_rect.colliderect(ast4_rect):
        ast1_vx = -2 if ast1_rect.centerx < ast4_rect.centerx else 2
        ast4_vx = 2 if ast1_rect.centerx < ast4_rect.centerx else -2

    if ast1_rect.colliderect(ast5_rect):
        ast1_vx = -2 if ast1_rect.centerx < ast5_rect.centerx else 2
        ast5_vx = 2 if ast1_rect.centerx < ast5_rect.centerx else -2

    if ast2_rect.colliderect(ast4_rect):
        ast2_vx = -2 if ast2_rect.centerx < ast4_rect.centerx else 2
        ast4_vx = 2 if ast2_rect.centerx < ast4_rect.centerx else -2

    if ast2_rect.colliderect(ast5_rect):
        ast2_vx = -2 if ast2_rect.centerx < ast5_rect.centerx else 2
        ast5_vx = 2 if ast2_rect.centerx < ast5_rect.centerx else -2

    if ast3_rect.colliderect(ast4_rect):
        ast3_vx = -2 if ast3_rect.centerx < ast4_rect.centerx else 2
        ast4_vx = 2 if ast3_rect.centerx < ast4_rect.centerx else -2

    if ast3_rect.colliderect(ast5_rect):
        ast3_vx = -2 if ast3_rect.centerx < ast5_rect.centerx else 2
        ast5_vx = 2 if ast3_rect.centerx < ast5_rect.centerx else -2

    if ast4_rect.colliderect(ast5_rect):
        ast4_vx = -2 if ast4_rect.centerx < ast5_rect.centerx else 2
        ast5_vx = 2 if ast4_rect.centerx < ast5_rect.centerx else -2


pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((650, 500))
pygame.display.set_caption('Spacy')
clock = pygame.time.Clock()

# Sounds
impact_sound = pygame.mixer.Sound('Spacy/sounds/impact.mp3')
pygame.mixer.music.load('Spacy/sounds/background.mp3')
pygame.mixer.music.set_volume(0.5)

# Fonts.......
score = pygame.font.Font(None, 50)
game_over_font = pygame.font.Font(None, 50)
game_restart_font = pygame.font.Font(None, 22)
title_font = pygame.font.Font(None, 80)
start_font = pygame.font.Font(None, 32)

title_text = title_font.render('Spacy', False, "#e2b728")
start_text = start_font.render(
    'Press [Space] to start',
    False,
    '#e2dfdc'
)
subtitle_font = pygame.font.Font(None, 26)
subtitle_text = subtitle_font.render(
    'Dodge the asteroids and survive!',
    False,
    '#aaaabb'
)

game_active = False
opening = True
start_time = 0

# Collision animation
collision_active = False
collision_start_time = 0

# Keep this around 3 seconds so the impact sound has time to finish.
collision_duration = 3000

collision_x = 0
collision_y = 0

# Store the ACTUAL asteroid involved in the collision
collision_asteroid = None
collision_asteroid_angle = 0
collision_asteroid_start_x = 0
collision_asteroid_start_y = 0
collision_direction_x = 0
collision_direction_y = 0

# Game_over........
game_over_text = game_over_font.render('Game Over', False, "#f12525")
game_restart_text = game_restart_font.render(
    'Press [Space] to restart the game', False, "#e2dfdc")

# Background.............
space_back = pygame.image.load('Spacy/images/v5.jpg').convert_alpha()
space_back = pygame.transform.scale(space_back, (650, 500))
space_back.set_alpha(130)
bg_v1 = 0
bg_speed = 1.4


earth = pygame.image.load('Spacy/images/planets/earth2.png').convert_alpha()
earth = pygame.transform.scale(earth, (650, 500))
earth_rect = earth.get_rect(midbottom=(325, 750))

# Planets..........
planets = {
    "mercury": pygame.image.load('Spacy/images/planets/mercury.png').convert_alpha(),
    "venus": pygame.image.load('Spacy/images/planets/venus.png').convert_alpha(),
    "mars": pygame.image.load('Spacy/images/planets/mars.png').convert_alpha(),
    "jupiter": pygame.image.load('Spacy/images/planets/jupiter.png').convert_alpha(),
    "saturn": pygame.image.load('Spacy/images/planets/saturn.jpg').convert_alpha(),
    "uranus": pygame.image.load('Spacy/images/planets/uranus.png').convert_alpha(),
    "neptune": pygame.image.load('Spacy/images/planets/neptune.png').convert_alpha()
}

planet_keys = list(planets.keys())
avaliable_plan = planet_keys.copy()
random.shuffle(avaliable_plan)

cur_planet = avaliable_plan.pop(0)
planet_size = random.randint(450, 700)
planet_speed = 0.3 + (planet_size / 600.0) * 0.35

max_clip = 60
planet_x = random.choice([
    random.randint(-max_clip, -20),
    random.randint(650 - planet_size + 20, 650 - planet_size +
                   max_clip)
])
planet_float_x = float(planet_x)
planet_float_y = -float(planet_size)
cur_planet_surf = pygame.transform.smoothscale(
    planets[cur_planet], (planet_size, planet_size))
planets_rect = cur_planet_surf.get_rect(
    topleft=(planet_x, int(planet_float_y)))

# Spaceship..............
spacer = pygame.image.load('Spacy/images/spacer.png').convert_alpha()
spacer = pygame.transform.scale(spacer, (90, 90))
spacer_rect = spacer.get_rect(midbottom=(300, 500))

# Astroids.........
ast1 = pygame.image.load('Spacy/images/ast/ast1.png').convert_alpha()
ast1 = pygame.transform.scale(ast1, (60, 60))
ast1_rect = ast1.get_rect(topleft=(300, -50))

ast2 = pygame.image.load('Spacy/images/ast/ast2.png').convert_alpha()
ast2 = pygame.transform.scale(ast2, (100, 100))
ast2_rect = ast2.get_rect(topright=(140, -120))

ast3 = pygame.image.load('Spacy/images/ast/ast3.png').convert_alpha()
ast3 = pygame.transform.scale(ast3, (70, 70))
ast3_rect = ast3.get_rect(topleft=(500, -19))

ast4 = pygame.image.load('Spacy/images/ast/ast4.png').convert_alpha()
ast4 = pygame.transform.scale(ast4, (120, 120))
ast4_rect = ast4.get_rect(topleft=(200, -250))

ast5 = pygame.image.load('Spacy/images/ast/ast5.png').convert_alpha()
ast5 = pygame.transform.scale(ast5, (90, 90))
ast5_rect = ast5.get_rect(topleft=(450, -350))

angle1 = 0
angle2 = 0
angle3 = 0
angle4 = 0
angle5 = 0

ast1_vx, ast1_vy = 0, 4
ast2_vx, ast2_vy = 0, 2
ast3_vx, ast3_vy = 0, 3
ast4_vx, ast4_vy = 0, 2
ast5_vx, ast5_vy = 0, 3

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()

    # Opening screen
    if keys[pygame.K_SPACE] and opening:
        opening = False
        game_active = True

        # Start background music
        pygame.mixer.music.play(-1)

        spacer_rect.midbottom = (300, 500)

        ast1_rect.topleft = (100, -50)
        ast2_rect.topright = (300, -120)
        ast3_rect.topleft = (500, -19)

        ast4_rect.topleft = (
            random.randint(0, 650 - ast4_rect.width),
            random.randint(-500, -300)
        )

        ast5_rect.topleft = (
            random.randint(0, 650 - ast5_rect.width),
            random.randint(-700, -500)
        )

        ast1_vx, ast2_vx, ast3_vx = 0, 0, 0
        ast4_vx, ast5_vx = 0, 0

        start_time = int(pygame.time.get_ticks() / 1000)

        # Reset Earth
        earth_rect.midbottom = (325, 750)

        # Reset planet
        if not avaliable_plan:
            avaliable_plan = planet_keys.copy()
            random.shuffle(avaliable_plan)

        cur_planet = avaliable_plan.pop(0)

        planet_size = random.randint(450, 700)
        planet_speed = 0.3 + (planet_size / 600.0) * 0.35

        planet_x = random.choice([
            random.randint(-max_clip, -20),
            random.randint(
                650 - planet_size + 20,
                650 - planet_size + max_clip
            )
        ])

        planet_float_x = float(planet_x)
        planet_float_y = -float(planet_size)

        cur_planet_surf = pygame.transform.smoothscale(
            planets[cur_planet],
            (planet_size, planet_size)
        )

        planets_rect = cur_planet_surf.get_rect(
            topleft=(planet_x, int(planet_float_y))
        )

    # Restart after Game Over
    if keys[pygame.K_SPACE] and not game_active and not opening and not collision_active:
        game_active = True

        # Start background music again
        pygame.mixer.music.play(-1)

        spacer_rect.midbottom = (300, 500)

        ast1_rect.topleft = (
            random.randint(0, 650 - ast1_rect.width),
            random.randint(-500, -300)
        )

        ast2_rect.topleft = (
            random.randint(0, 650 - ast2_rect.width),
            random.randint(-300, -100)
        )

        ast3_rect.topleft = (
            random.randint(0, 650 - ast3_rect.width),
            random.randint(-100, 0)
        )

        ast4_rect.topleft = (
            random.randint(0, 650 - ast4_rect.width),
            random.randint(-500, -300)
        )

        ast5_rect.topleft = (
            random.randint(0, 650 - ast5_rect.width),
            random.randint(-700, -500)
        )

        ast1_vx, ast2_vx, ast3_vx = 0, 0, 0
        ast4_vx, ast5_vx = 0, 0

        start_time = int(pygame.time.get_ticks() / 1000)

        # Reset Earth
        earth_rect.midbottom = (325, 750)

        # Reset planet
        if not avaliable_plan:
            avaliable_plan = planet_keys.copy()
            random.shuffle(avaliable_plan)

        cur_planet = avaliable_plan.pop(0)

        planet_size = random.randint(450, 700)
        planet_speed = 0.3 + (planet_size / 600.0) * 0.35

        planet_x = random.choice([
            random.randint(-max_clip, -20),
            random.randint(
                650 - planet_size + 20,
                650 - planet_size + max_clip
            )
        ])

        planet_float_x = float(planet_x)
        planet_float_y = -float(planet_size)

        cur_planet_surf = pygame.transform.smoothscale(
            planets[cur_planet],
            (planet_size, planet_size)
        )

        planets_rect = cur_planet_surf.get_rect(
            topleft=(planet_x, int(planet_float_y))
        )

    # ==========================================================
    # COLLISION ANIMATION
    # ==========================================================
    if collision_active:
        collision_elapsed = pygame.time.get_ticks() - collision_start_time

        screen.fill((5, 5, 12))

        # Keep background visible during collision
        screen.blit(space_back, (0, bg_v1))
        screen.blit(space_back, (0, bg_v1 - 500))

        progress = collision_elapsed / collision_duration

        if progress < 1:

            # --------------------------------------------------
            # Camera / screen shake
            # Strong at the beginning, then fades out.
            # --------------------------------------------------
            shake_strength = int(8 * (1 - progress))

            if shake_strength > 0:
                shake_x = random.randint(
                    -shake_strength,
                    shake_strength
                )
                shake_y = random.randint(
                    -shake_strength,
                    shake_strength
                )
            else:
                shake_x = 0
                shake_y = 0

            # --------------------------------------------------
            # Draw a small impact flash
            # --------------------------------------------------
            if progress < 0.18:
                flash_progress = progress / 0.18
                flash_alpha = int(180 * (1 - flash_progress))

                flash_surface = pygame.Surface(
                    (650, 500),
                    pygame.SRCALPHA
                )

                flash_surface.fill(
                    (255, 210, 120, flash_alpha)
                )

                screen.blit(
                    flash_surface,
                    (shake_x, shake_y)
                )

            # --------------------------------------------------
            # Ship impact movement
            # The ship moves slightly backwards from collision.
            # --------------------------------------------------
            ship_push = min(progress / 0.35, 1)

            ship_x = collision_x
            ship_y = collision_y

            ship_x += collision_direction_x * ship_push * 35
            ship_y += collision_direction_y * ship_push * 35

            # Small vibration while the impact is happening
            if progress < 0.35:
                vibration = int(
                    5 * (1 - progress / 0.35)
                )

                ship_x += random.randint(
                    -vibration,
                    vibration
                )

                ship_y += random.randint(
                    -vibration,
                    vibration
                )

            ship_collision_rect = spacer.get_rect(
                center=(
                    int(ship_x + shake_x),
                    int(ship_y + shake_y)
                )
            )

            # --------------------------------------------------
            # Draw ship
            # --------------------------------------------------
            screen.blit(
                spacer,
                ship_collision_rect
            )

            # --------------------------------------------------
            # Draw the ACTUAL asteroid that hit the ship
            # --------------------------------------------------
            if collision_asteroid is not None:

                # Asteroid moves slightly through the collision
                asteroid_progress = min(progress / 0.45, 1)

                asteroid_x = (
                    collision_asteroid_start_x +
                    collision_direction_x *
                    asteroid_progress * 45
                )

                asteroid_y = (
                    collision_asteroid_start_y +
                    collision_direction_y *
                    asteroid_progress * 45
                )

                # Continue rotating the asteroid
                asteroid_angle = (
                    collision_asteroid_angle +
                    collision_asteroid_rotation *
                    collision_elapsed / 16
                )

                asteroid_rot = pygame.transform.rotate(
                    collision_asteroid,
                    asteroid_angle
                )

                asteroid_collision_rect = asteroid_rot.get_rect(
                    center=(
                        int(asteroid_x + shake_x),
                        int(asteroid_y + shake_y)
                    )
                )

                screen.blit(
                    asteroid_rot,
                    asteroid_collision_rect
                )

            # --------------------------------------------------
            # Small impact sparks
            # --------------------------------------------------
            if progress < 0.45:

                spark_progress = progress / 0.45
                spark_alpha = int(
                    255 * (1 - spark_progress)
                )

                for i in range(8):
                    angle = (i * 45) * 3.14159 / 180

                    spark_distance = 15 + (
                        spark_progress * 45
                    )

                    spark_x = int(
                        collision_x +
                        pygame.math.Vector2(
                            1, 0
                        ).rotate(i * 45).x *
                        spark_distance
                    )

                    spark_y = int(
                        collision_y +
                        pygame.math.Vector2(
                            1, 0
                        ).rotate(i * 45).y *
                        spark_distance
                    )

                    spark_surface = pygame.Surface(
                        (8, 8),
                        pygame.SRCALPHA
                    )

                    pygame.draw.circle(
                        spark_surface,
                        (255, 210, 70, spark_alpha),
                        (4, 4),
                        3
                    )

                    screen.blit(
                        spark_surface,
                        (
                            spark_x - 4 + shake_x,
                            spark_y - 4 + shake_y
                        )
                    )

            pygame.display.update()
            clock.tick(60)

        else:
            # Collision animation finished.
            collision_active = False
            game_active = False

            # Make absolutely sure music is stopped.
            pygame.mixer.music.stop()

        continue

    # Opening screen
    if opening:
        screen.fill((5, 5, 12))

        # Moving space background
        bg_v1 += bg_speed

        if bg_v1 >= 500:
            bg_v1 = 0

        screen.blit(space_back, (0, bg_v1))
        screen.blit(space_back, (0, bg_v1 - 500))

        # Title
        title_rect = title_text.get_rect(center=(325, 180))
        screen.blit(title_text, title_rect)

        # Subtitle
        subtitle_rect = subtitle_text.get_rect(center=(325, 240))
        screen.blit(subtitle_text, subtitle_rect)

        # Start message
        start_rect = start_text.get_rect(center=(325, 330))
        screen.blit(start_text, start_rect)

    elif game_active:
        screen.fill((5, 5, 12))

        # LEVEL
        cur_time = int(pygame.time.get_ticks() / 1000) - start_time
        level = (cur_time // 10) + 1

        # Speed increases with level
        speed_multiplier = 1 + ((level - 1) * 0.20)

        current_ast1_vy = ast1_vy * speed_multiplier
        current_ast2_vy = ast2_vy * speed_multiplier
        current_ast3_vy = ast3_vy * speed_multiplier
        current_ast4_vy = ast4_vy * speed_multiplier
        current_ast5_vy = ast5_vy * speed_multiplier

        current_bg_speed = bg_speed * speed_multiplier

        current_planet_speed = planet_speed * speed_multiplier

        planet_float_y += current_planet_speed
        planets_rect.y = int(planet_float_y)

        if planets_rect.top > 500:
            if not avaliable_plan:
                avaliable_plan = planet_keys.copy()
                random.shuffle(avaliable_plan)

            cur_planet = avaliable_plan.pop(0)
            planet_size = random.randint(450, 700)

            planet_speed = 0.3 + (planet_size / 600.0) * 0.35

            planet_x = random.choice([
                random.randint(-max_clip, -20),
                random.randint(
                    650 - planet_size + 20,
                    650 - planet_size + max_clip
                )
            ])

            planet_float_x = float(planet_x)
            planet_float_y = -float(planet_size)

            cur_planet_surf = pygame.transform.smoothscale(
                planets[cur_planet],
                (planet_size, planet_size)
            )

            planets_rect = cur_planet_surf.get_rect(
                topleft=(int(planet_float_x), int(planet_float_y))
            )

        bg_v1 += current_bg_speed

        if bg_v1 >= 500:
            bg_v1 = 0

        screen.blit(space_back, (0, bg_v1))
        screen.blit(space_back, (0, bg_v1 - 500))

        screen.blit(cur_planet_surf, planets_rect)

        if earth_rect.top < 500:
            earth_rect.y += 1
            screen.blit(earth, earth_rect)

        screen.blit(spacer, spacer_rect)
        spacer_box = spacer_rect.inflate(-45, -50)

        scoring()
        level_display()

        angle1 += -1
        angle2 += 1
        angle3 += -1
        angle4 += 1
        angle5 += -1

        asteroid_col()

        # Asteroid 1
        ast1_rect.x += ast1_vx
        ast1_rect.top += current_ast1_vy

        if ast1_rect.left <= 0 or ast1_rect.right >= 650:
            ast1_vx *= -1

        if ast1_rect.bottom >= 549:
            ast1_rect.top = random.randint(-450, -120)
            ast1_rect.x = random.randint(0, 250 - ast1_rect.width)
            ast1_vx = 0

        ast1_rot = pygame.transform.rotate(ast1, angle1)
        screen.blit(
            ast1_rot,
            ast1_rot.get_rect(center=ast1_rect.center)
        )

        # Asteroid 2
        ast2_rect.x += ast2_vx
        ast2_rect.top += current_ast2_vy

        if ast2_rect.left <= 0 or ast2_rect.right >= 650:
            ast2_vx *= -1

        if ast2_rect.bottom >= 569:
            ast2_rect.top = random.randint(-200, -100)
            ast2_rect.x = random.randint(
                200,
                450 - ast2_rect.width
            )
            ast2_vx = 0

        ast2_rot = pygame.transform.rotate(ast2, angle2)
        screen.blit(
            ast2_rot,
            ast2_rot.get_rect(center=ast2_rect.center)
        )

        # Asteroid 3
        ast3_rect.x += ast3_vx
        ast3_rect.top += current_ast3_vy

        if ast3_rect.left <= 0 or ast3_rect.right >= 650:
            ast3_vx *= -1

        if ast3_rect.bottom >= 649:
            ast3_rect.top = random.randint(-150, -40)
            ast3_rect.x = random.randint(
                400,
                650 - ast3_rect.width
            )
            ast3_vx = 0

        ast3_rot = pygame.transform.rotate(ast3, angle3)
        screen.blit(
            ast3_rot,
            ast3_rot.get_rect(center=ast3_rect.center)
        )

        # Asteroid 4
        ast4_rect.x += ast4_vx
        ast4_rect.top += current_ast4_vy

        if ast4_rect.left <= 0 or ast4_rect.right >= 650:
            ast4_vx *= -1

        if ast4_rect.bottom >= 649:
            ast4_rect.top = random.randint(-300, -150)
            ast4_rect.x = random.randint(
                0,
                650 - ast4_rect.width
            )
            ast4_vx = 0

        ast4_rot = pygame.transform.rotate(ast4, angle4)
        screen.blit(
            ast4_rot,
            ast4_rot.get_rect(center=ast4_rect.center)
        )

        # Asteroid 5
        ast5_rect.x += ast5_vx
        ast5_rect.top += current_ast5_vy

        if ast5_rect.left <= 0 or ast5_rect.right >= 650:
            ast5_vx *= -1

        if ast5_rect.bottom >= 649:
            ast5_rect.top = random.randint(-500, -300)
            ast5_rect.x = random.randint(
                0,
                650 - ast5_rect.width
            )
            ast5_vx = 0

        ast5_rot = pygame.transform.rotate(ast5, angle5)
        screen.blit(
            ast5_rot,
            ast5_rot.get_rect(center=ast5_rect.center)
        )

        # Keys movement
        if keys[pygame.K_a] and spacer_rect.left > -2:
            spacer_rect.x -= 3

        if keys[pygame.K_d] and spacer_rect.right < 650:
            spacer_rect.x += 3

        if keys[pygame.K_w] and spacer_rect.top > 0:
            spacer_rect.y -= 3

        if keys[pygame.K_s] and spacer_rect.bottom < 500:
            spacer_rect.y += 3

        # ======================================================
        # Collision with Player Check
        # ======================================================

        collided_asteroid = None
        collided_angle = 0

        if spacer_box.colliderect(ast1_rect):
            collided_asteroid = ast1
            collided_angle = angle1
            collision_asteroid_rect = ast1_rect

        elif spacer_box.colliderect(ast2_rect):
            collided_asteroid = ast2
            collided_angle = angle2
            collision_asteroid_rect = ast2_rect

        elif spacer_box.colliderect(ast3_rect):
            collided_asteroid = ast3
            collided_angle = angle3
            collision_asteroid_rect = ast3_rect

        elif spacer_box.colliderect(ast4_rect):
            collided_asteroid = ast4
            collided_angle = angle4
            collision_asteroid_rect = ast4_rect

        elif spacer_box.colliderect(ast5_rect):
            collided_asteroid = ast5
            collided_angle = angle5
            collision_asteroid_rect = ast5_rect

        if collided_asteroid is not None:

            # Save collision position
            collision_x = spacer_rect.centerx
            collision_y = spacer_rect.centery

            # Save the REAL asteroid that hit the ship
            collision_asteroid = collided_asteroid
            collision_asteroid_angle = collided_angle

            collision_asteroid_start_x = collision_asteroid_rect.centerx
            collision_asteroid_start_y = collision_asteroid_rect.centery

            # Work out which direction the asteroid came from.
            dx = (
                collision_asteroid_start_x -
                collision_x
            )

            dy = (
                collision_asteroid_start_y -
                collision_y
            )

            # Normalize direction
            distance = max(
                1,
                (dx * dx + dy * dy) ** 0.5
            )

            collision_direction_x = dx / distance
            collision_direction_y = dy / distance

            # Make the asteroid push away from the ship
            if abs(collision_direction_x) < 0.1:
                collision_direction_x = 0

            if abs(collision_direction_y) < 0.1:
                collision_direction_y = -1

            # Collision rotation direction
            collision_asteroid_rotation = random.choice([
                -0.8,
                0.8
            ])

            # Play impact sound ONCE
            impact_sound.stop()
            impact_sound.play()

            # Stop background music immediately
            pygame.mixer.music.stop()

            # Start collision animation
            collision_active = True
            collision_start_time = pygame.time.get_ticks()

            # Stop the actual game
            game_active = False

    else:
        # Game Over screen
        screen.fill('Black')
        screen.blit(spacer, (270, 200))
        screen.blit(game_over_text, (225, 290))
        screen.blit(game_restart_text, (205, 324))

    pygame.display.update()
    clock.tick(60)

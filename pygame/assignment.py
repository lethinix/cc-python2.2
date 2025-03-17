import pygame
import os
import random

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Battle")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
STAR_COLOR = (255, 255, 153)  # Light yellow for twinkling stars

FPS = 60
VEL = 5
BULLET_VEL = 7
MAX_BULLETS = 3
ENEMY_VEL = 2

SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

# Load images
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png')) 
YELLOW_SPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), -90)

RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_red.png')) 
RED_SPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), -270)

# Load sounds
shoot_sound = pygame.mixer.Sound(os.path.join('Assets', 'shoot.wav'))
explosion_sound = pygame.mixer.Sound(os.path.join('Assets', 'explosion.mp3'))

# Generate stars for the night sky
NUM_STARS = 100
stars = [(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(NUM_STARS)]

class Enemy:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
        self.vel = ENEMY_VEL
    
    def update(self):
        self.rect.x -= self.vel
        
    def draw(self, window):
        window.blit(RED_SPACESHIP, (self.rect.x, self.rect.y))
    
    def is_off_screen(self):
        return self.rect.x < -SPACESHIP_WIDTH

def draw_window(yellow, yellow_bullets, enemies):
    WIN.fill(BLACK)  # Night sky background

    # Draw twinkling stars
    for star in stars:
        if random.random() > 0.5:  # Random flicker effect
            pygame.draw.circle(WIN, STAR_COLOR, star, 2)

    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))

    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)

    for enemy in enemies:
        enemy.draw(WIN)

    pygame.display.update()

def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_LEFT] and yellow.x - VEL > 0: 
        yellow.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and yellow.x + VEL + yellow.width < WIDTH: 
        yellow.x += VEL
    if keys_pressed[pygame.K_UP] and yellow.y - VEL > 0: 
        yellow.y -= VEL
    if keys_pressed[pygame.K_DOWN] and yellow.y + VEL + yellow.height < HEIGHT: 
        yellow.y += VEL

def handle_bullets(yellow_bullets, enemies):
    for bullet in yellow_bullets[:]:
        bullet.x += BULLET_VEL
        if bullet.x > WIDTH:
            yellow_bullets.remove(bullet)
            continue
        
        for enemy in enemies[:]:
            if bullet.colliderect(enemy.rect):
                explosion_sound.play()  # Play explosion sound
                yellow_bullets.remove(bullet)
                enemies.remove(enemy)
                break 

def main():
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow_bullets = []
    enemies = []

    enemy_spawn_timer = 0
    enemy_spawn_delay = 120  

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS) 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2 - 2, 10, 5)
                    yellow_bullets.append(bullet)
                    shoot_sound.play()  # Play shooting sound
        
        enemy_spawn_timer += 1
        if enemy_spawn_timer >= enemy_spawn_delay:
            new_enemy = Enemy(WIDTH, random.randint(50, HEIGHT - SPACESHIP_HEIGHT - 50))
            enemies.append(new_enemy)
            enemy_spawn_timer = 0

        for enemy in enemies[:]:
            enemy.update()
            if enemy.is_off_screen():
                enemies.remove(enemy)

        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        handle_bullets(yellow_bullets, enemies)
        draw_window(yellow, yellow_bullets, enemies)
        
    pygame.quit() 

if __name__ == "__main__": 
    main()

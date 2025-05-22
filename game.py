# flappy_dilay.py
# Flappy Dilay - Python/Pygame ile Flappy Bird klonu
# Kullanım:
# 1. pip install pygame
# 2. assets klasörüne dilay_bird.png, background.png, pipe.png, ground.png ekleyin
# 3. python flappy_dilay.py

import pygame
import sys
import random

# --- Sabitler ---
WIDTH, HEIGHT = 400, 600
FPS = 60
GRAVITY = 0.5
FLAP_POWER = -10
PIPE_GAP = 150
PIPE_INTERVAL = 1500  # ms aralıklarla

# --- Başlat ---
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Flappy Dilay")

# --- Asset Yükleme ---
bird_img = pygame.image.load("assets/dilay_bird.png").convert_alpha()
bg_img = pygame.image.load("assets/background.png").convert()
pipe_img = pygame.image.load("assets/pipe.png").convert_alpha()
ground_img = pygame.image.load("assets/ground.png").convert()

# --- Font ---
font = pygame.font.SysFont(None, 48)

# --- Oyun Değişkenleri ---
bird_rect = bird_img.get_rect(center=(WIDTH//4, HEIGHT//2))
bird_vel = 0
pipes = []
SPAWN_PIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWN_PIPE, PIPE_INTERVAL)
score = 0

# --- Fonksiyonlar ---
def reset_game():
    global bird_rect, bird_vel, pipes, score
    bird_rect.center = (WIDTH//4, HEIGHT//2)
    bird_vel = 0
    pipes.clear()
    score = 0

# --- Ana Döngü ---
running = True
while running:
    dt = clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_vel = FLAP_POWER
        if event.type == SPAWN_PIPE:
            y = random.randint(100, HEIGHT - 200)
            top = pipe_img.get_rect(midbottom=(WIDTH+50, y - PIPE_GAP//2))
            bottom = pipe_img.get_rect(midtop=(WIDTH+50, y + PIPE_GAP//2))
            pipes.append((top, bottom))

    # --- Fizik ---
    bird_vel += GRAVITY
    bird_rect.centery += bird_vel

    # --- Boruları Hareket Ettir ---
    for top, bottom in pipes:
        top.centerx -= 3
        bottom.centerx -= 3
    pipes = [(t, b) for t, b in pipes if t.right > -50]

    # --- Çarpışma ---
    if bird_rect.top <= 0 or bird_rect.bottom >= HEIGHT - ground_img.get_height():
        reset_game()
    for top, bottom in pipes:
        if bird_rect.colliderect(top) or bird_rect.colliderect(bottom):
            reset_game()

    # --- Skor ---
    for t, b in pipes:
        # skoru boru tam geçtiğinde bir kez arttır
        if t.centerx == bird_rect.centerx:
            score += 1

    # --- Çizimler ---
    screen.blit(bg_img, (0, 0))
    for top, bottom in pipes:
        screen.blit(pipe_img, top)
        # alt boru için düşey çevirme
        screen.blit(pipe_img, bottom)
    screen.blit(ground_img, (0, HEIGHT - ground_img.get_height()))
    screen.blit(bird_img, bird_rect)
    
    # Skor yazdır
    score_surf = font.render(str(score), True, (255, 255, 255))
    screen.blit(score_surf, (WIDTH//2 - score_surf.get_width()//2, 20))

    pygame.display.update()

pygame.quit()
sys.exit()

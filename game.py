import pygame
import sys
import random

# Game Constants
WIDTH, HEIGHT = 400, 600
FPS = 60
GRAVITY = 0.5
FLAP_STRENGTH = -10
PIPE_GAP = 150
PIPE_FREQ = 1500  # milliseconds

# Initialize Pygame
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Flappy Dilay")

    # Load Assets
    bird_img = pygame.image.load('assets/dilay_bird.png').convert_alpha()
    bg_img = pygame.image.load('assets/background.png').convert()
    pipe_img = pygame.image.load('assets/pipe.png').convert_alpha()
    ground_img = pygame.image.load('assets/ground.png').convert()

    # Bird
    bird_rect = bird_img.get_rect(center=(WIDTH//4, HEIGHT//2))
    bird_vel = 0

    # Pipes
    pipes = []
    SPAWNPIPE = pygame.USEREVENT
    pygame.time.set_timer(SPAWNPIPE, PIPE_FREQ)

    score = 0
    font = pygame.font.SysFont(None, 36)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                bird_vel = FLAP_STRENGTH
            if event.type == SPAWNPIPE:
                pipe_height = random.randint(100, HEIGHT - 200)
                top_pipe = pipe_img.get_rect(midbottom=(WIDTH + 50, pipe_height - PIPE_GAP//2))
                bottom_pipe = pipe_img.get_rect(midtop=(WIDTH + 50, pipe_height + PIPE_GAP//2))
                pipes.append(top_pipe)
                pipes.append(bottom_pipe)

        # Bird physics
        bird_vel += GRAVITY
        bird_rect.centery += bird_vel

        # Move pipes
        for pipe in pipes:
            pipe.centerx -= 3
        pipes = [p for p in pipes if p.right > -50]

        # Collision
        if bird_rect.top <= 0 or bird_rect.bottom >= HEIGHT-100:
            running = False
        for pipe in pipes:
            if bird_rect.colliderect(pipe):
                running = False

        # Score
        for pipe in pipes:
            if pipe.centerx == bird_rect.centerx:
                score += 0.5  # each pair counts as 1

        # Draw
        screen.blit(bg_img, (0, 0))
        for pipe in pipes:
            if pipe.bottom >= HEIGHT:
                screen.blit(pipe_img, pipe)
            else:
                flip_pipe = pygame.transform.flip(pipe_img, False, True)
                screen.blit(flip_pipe, pipe)
        screen.blit(ground_img, (0, HEIGHT-100))
        screen.blit(bird_img, bird_rect)

        score_surf = font.render(f"Score: {int(score)}", True, (255, 255, 255))
        screen.blit(score_surf, (10, 10))

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()

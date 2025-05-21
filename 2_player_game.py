import pygame
import random


PIKACHU = "/home/dwipendu/Desktop/Pygame/player_pics/pikachu.png"
MEOWTH = "/home/dwipendu/Desktop/Pygame/player_pics/avatar.png"
POKEBALL = "/home/dwipendu/Desktop/Pygame/player_pics/POKEBALL.png"
MUSIC = "/home/dwipendu/Desktop/Pygame/music/pokemon_go.mp3"

pygame.mixer.init()
pygame.mixer.music.load(MUSIC)
pygame.mixer.music.play(-1)


# initialize the pygame
pygame.init()

# screen height and width and create a screen
height, width = 900, 1900
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Dwip's game")

# speed of 2 players:
plane_speed = 10

# player1:
player = pygame.image.load(PIKACHU)
player = pygame.transform.scale(player, (100, 100))
p1_x_axis = width//2-100
p1_y_axis = height//2-100
p1_score = 0

# player2:
player2 = pygame.image.load(MEOWTH)
player2 = pygame.transform.scale(player2, (100, 100))
p2_x_axis = width//2-100
p2_y_axis = height//2-100
p2_score = 0

# pokeball:
pokeball = pygame.image.load(POKEBALL)
pokeball = pygame.transform.scale(pokeball, (100, 100))
ball_x_axis = random.randint(0, width-100)
ball_y_axis = random.randint(0, height-100)


# player1:
def player_1(x, y):
    screen.blit(player, (x, y))


# player2:
def player_2(x, y):
    screen.blit(player2, (x, y))

# ball:


def pokeball_bug(x, y):
    screen.blit(pokeball, (x, y))


# run the game loop here
run = 1
while run:
    # take screen color here
    screen.fill((250, 0, 100))
    x_change = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = 0

    # player1:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and p1_x_axis > 0:
        p1_x_axis -= plane_speed
    if keys[pygame.K_RIGHT] and p1_x_axis < width-100:
        p1_x_axis += plane_speed
    if keys[pygame.K_UP] and p1_y_axis > 0:
        p1_y_axis -= plane_speed
    if keys[pygame.K_DOWN] and p1_y_axis < height-100:
        p1_y_axis += plane_speed

    # player2:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and p2_x_axis > 0:
        p2_x_axis -= plane_speed
    if keys[pygame.K_d] and p2_x_axis < width-100:
        p2_x_axis += plane_speed
    if keys[pygame.K_w] and p2_y_axis > 0:
        p2_y_axis -= plane_speed
    if keys[pygame.K_s] and p2_y_axis < height-100:
        p2_y_axis += plane_speed

    # take player functions here
    player_1(p1_x_axis, p1_y_axis)
    player_2(p2_x_axis, p2_y_axis)
    pokeball_bug(ball_x_axis, ball_y_axis)

    # collision detection
    p1_rect = pygame.Rect(p1_x_axis, p1_y_axis, 100, 100)
    p2_rect = pygame.Rect(p2_x_axis, p2_y_axis, 100, 100)
    ball_rect = pygame.Rect(ball_x_axis, ball_y_axis, 100, 100)

    # Collision for player 1
    if p1_rect.colliderect(ball_rect):
        p1_score += 1
        ball_x_axis = random.randint(0, width - 100)
        ball_y_axis = random.randint(0, height - 100)

    # Collision for player 2
    if p2_rect.colliderect(ball_rect):
        p2_score += 1
        ball_x_axis = random.randint(0, width - 100)
        ball_y_axis = random.randint(0, height - 100)

    # winner print:
    if p1_score >= 20 or p2_score >= 20:
        if p1_score >= 20:
            winner = "Pikachu Wins!"
        else:
            winner = "Meowth Wins!"
        font = pygame.font.SysFont(None, 100)
        text = font.render(winner, True, (255, 255, 255))
        screen.blit(text, (width // 2 - 300, height // 2 - 50))
        pygame.display.update()
        pygame.time.delay(3000)  # Show result for 3 seconds
        run = 0

    # score
    player1_icon = pygame.transform.scale(player, (50, 50))
    player2_icon = pygame.transform.scale(player2, (50, 50))
    font = pygame.font.SysFont(None, 50)
    screen.blit(player1_icon, (20, 20))
    p1_score_text = font.render(f"{p1_score}", True, (255, 255, 255))
    screen.blit(p1_score_text, (80, 25))

    screen.blit(player2_icon, (width - 120, 20))
    p2_score_text = font.render(f"{p2_score}", True, (255, 255, 255))
    screen.blit(p2_score_text, (width - 60, 25))

    pygame.display.update()
pygame.quit()
exit()

import random
import time
import pygame

pygame.init()

clock = pygame.time.Clock()
gd = pygame.display.set_mode((800, 600))
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
light_green = (0, 155, 255)
gray = (119, 118, 110)
gif_surface = pygame.image.load('r.gif')
car_image = pygame.image.load("car-clipart-sprite-sheet-14.jpg")
car_image = pygame.transform.scale(car_image, (100, 100))
bgImg = pygame.image.load("background1.jpg")
grass = pygame.image.load("download12.jpg")
enymy = pygame.image.load("enymy.png")
enymy = pygame.transform.scale(enymy, (100, 100))
screen_info = pygame.display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h
gif_x = 0
gif_y = 0
gif_width = screen_width
gif_height = screen_height
gif_surface = pygame.transform.scale(gif_surface, (gif_width, gif_height))


def text(size, mess, x_pos, y_pos):
    font = pygame.font.SysFont(None, size)
    render = font.render(mess, True, white)
    gd.blit(render, (x_pos, y_pos))


def button(x_button, y_button, mess_b):
    pygame.draw.rect(gd, green, [x_button, y_button, 100, 30])
    text(50, mess_b, x_button, y_button)
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x_button < mouse[0] < x_button+100 and y_button < mouse[1] < y_button+30:

        pygame.draw.rect(gd, light_green, [x_button, y_button, 100, 30])
        text(50, mess_b, x_button, y_button)
        if click == (1, 0, 0) and mess_b == "PLAY":
            pygame.mixer.music.load("go-kart-racing-33647.mp3")
            pygame.mixer.music.play()
            game_loop()
        elif click == (1, 0, 0) and mess_b == "QUIT":

            pygame.quit()
            quit()


def car(x, y):
    gd.blit(car_image, (x, y))
    gd.blit(grass, (0, 0))
    gd.blit(grass, (700, 0))
    if 0 < x < 90 or 700 < x+100:
        text(100, "Game Over", 200, 200)
        pygame.mixer.music.load("crashed.mp3")
        pygame.mixer.music.play()
        pygame.display.update()
        clock.tick(0.5)
        game_intro()


def enymy_car(x_r, y_r):
    gd.blit(enymy, (x_r, y_r))


def game_intro():
    intro = False
    while intro == False:
        gd.blit(bgImg, (0, 0))
        button(100, 300, "PLAY")
        button(600, 300, "QUIT")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:

                pygame.quit()
                quit()
        pygame.display.update()


def car_crash(x, x_r, y, y_r):
    if x_r < x < x_r+80 and y_r < y < y_r+80 or x_r < x+80 < x_r+80 and y_r < y < y_r+90:
        pygame.mixer.music.load("crashed.mp3")
        pygame.mixer.music.play()
        text(100, "Crashed!", 200, 200)
        pygame.display.update()
        time.sleep(1)

        game_intro()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


def score(count):
    font = pygame.font.SysFont(None, 30)
    screen_text = font.render("Score :" + str(count), True, white)
    gd.blit(screen_text, (0, 0))


def hiscore(hiscore):
    font = pygame.font.SysFont(None, 30)
    screen_text = font.render("Hi Score :" + str(hiscore), True, white)
    gd.blit(screen_text, (650, 0))


def level(level):
    font = pygame.font.SysFont(None, 30)
    screen_text = font.render("level :" + str(level), True, white)
    gd.blit(screen_text, (350, 0))


def game_loop():
    global count
    with open("socre.txt", "r") as f:
        content = f.read()
    count = 0
    hi = int(content)
    x = 300
    y = 490
    x_r = random.randrange(100, 600)
    y_r = 0
    x_change = 0
    y_change = 0
    speed = 50
    le = 1

    pygame.display.update()
    loop = False
    while loop == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                with open("socre.txt", "w") as scorefile:
                    scorefile.write(f"{count}")
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = +10
                elif event.key == pygame.K_RIGHT:
                    x_change = -10
                    pygame.display.update()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                    y_change = 0

        gd.fill(gray)
        gd.blit(gif_surface, (gif_x, gif_y, gif_width, gif_height))
        car(x, y,)
        score(count)
        hiscore(hi)
        level(le)
        enymy_car(x_r, y_r)
        y_r += 10
        if y_r == 500:
            x_r = random.randrange(100, 600)
            y_r = 0
            count += 1
        if count > hi:
            with open("socre.txt", "w") as scorefile:
                scorefile.write(f"{count}")
        if count > 10:
            le = 2
            speed = 60
        if count > 20:
            le = 3
            speed = 80
        if count > 30:
            le = 3
            speed = 90
        if count > 40:
            le = 4
            speed = 100
        if count > 50:
            le = 5
            speed = 105
        if count > 60:
            le = 6
            speed = 106
        car_crash(x, x_r, y, y_r)
        x = x-x_change
        y = y-y_change
        clock.tick(speed)
        pygame.display.update()


game_intro()
game_loop()
pygame.display.update()

pygame.quit()
quit()

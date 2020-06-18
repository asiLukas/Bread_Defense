import pygame, sys, json
import random
from pygame.locals import *

pygame.init()

# Screen and variables
dis_size = (752, 400)
winX = 1920
winY = 1080
pygame.display.set_caption('Bread Defense')
icon = pygame.image.load('everything/idling/icon.png')
pygame.display.set_icon(icon)
monitor_size = [pygame.display.Info().current_w, pygame.display.Info().current_h]
screen = pygame.display.set_mode(monitor_size)
display = pygame.Surface(dis_size)
clock = pygame.time.Clock()
dusk = (37.3, 65.9, 82)
skyblue = (145, 206, 235)
nightsky = (1, 2, 20)
darkblue = (6, 8, 45)
dark_blue = (43, 47, 119)
white = (255, 255, 255)
grey = (200, 200, 200)
# Sound and variables
enemy_dead_sound = pygame.mixer.Sound('everything/sound/dead.wav')
jump_sound = pygame.mixer.Sound('everything/sound/jump.wav')
bullet_sound = pygame.mixer.Sound('everything/sound/bullet_sound.wav')
grass_sound = [pygame.mixer.Sound('everything/sound/grass0.wav'), pygame.mixer.Sound('everything/sound/grass1.wav')]
pygame.mixer.music.load('everything/sound/main_music.wav')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.04)
pygame.mixer.set_num_channels(64)
grass_sound[0].set_volume(0.08)
grass_sound[1].set_volume(0.08)
jump_sound.set_volume(0.5)
bullet_sound.set_volume(0.1)
enemy_dead_sound.set_volume(0.5)

# Sprites and pictures in general
bullet = pygame.image.load('everything/map_images/maybe_bullet.png').convert_alpha()
cannon_right = pygame.image.load('everything/cannon/cannon_right.png').convert_alpha()
cannon_left = pygame.image.load('everything/cannon/cannon_left.png').convert_alpha()
rock = pygame.image.load('everything/map_images/rocks.png').convert_alpha()
fire = [pygame.image.load('everything/map_images/fire0.png').convert_alpha(),
        pygame.image.load('everything/map_images/fire1.png').convert_alpha(),
        pygame.image.load('everything/map_images/fire2.png').convert_alpha(),
        pygame.image.load('everything/map_images/fire3.png').convert_alpha()]
tree1 = pygame.image.load('everything/map_images/tree1.png').convert_alpha()
tree2 = pygame.image.load('everything/map_images/tree2.png').convert_alpha()
tree3 = pygame.image.load('everything/map_images/tree3.png').convert_alpha()
plant = pygame.image.load('everything/map_images/plant.png').convert_alpha()
cloud = pygame.image.load('everything/map_images/cloudd.png').convert_alpha()
cloud2 = pygame.image.load('everything/map_images/cloudd2.png').convert_alpha()
cloud3 = pygame.image.load('everything/map_images/cloudd3.png').convert_alpha()
cloud00 = pygame.image.load('everything/map_images/cloudss21.png').convert_alpha()
cloud02 = pygame.image.load('everything/map_images/cloudss23.png').convert_alpha()
cloud03 = pygame.image.load('everything/map_images/clouds24.png').convert_alpha()
sun = pygame.image.load('everything/map_images/sluncoo.png').convert_alpha()
moon = pygame.image.load('everything/map_images/moon.png').convert_alpha()

menu_bg = pygame.image.load('everything/map_images/menu_bg.png').convert_alpha()
bg = pygame.image.load('everything/map_images/bg.png').convert_alpha()
grasstile = pygame.image.load('everything/map_images/grasstile1.png').convert_alpha()
dirttile = pygame.image.load('everything/map_images/dirtt.png').convert_alpha()
block = pygame.image.load('everything/map_images/block.png').convert_alpha()

idle = pygame.image.load('everything/idling/idle00.png').convert_alpha()
big_enemy3 = [pygame.image.load('everything/enemy3/big_enemy30.png').convert_alpha(),
              pygame.image.load('everything/enemy3/big_enemy31.png').convert_alpha(),
              pygame.image.load('everything/enemy3/big_enemy32.png').convert_alpha(),
              pygame.image.load('everything/enemy3/big_enemy33.png').convert_alpha()]
big_enemy1 = [pygame.image.load('everything/enemy1/big_enemy10.png').convert_alpha(),
              pygame.image.load('everything/enemy1/big_enemy11.png').convert_alpha(),
              pygame.image.load('everything/enemy1/big_enemy12.png').convert_alpha(),
              pygame.image.load('everything/enemy1/big_enemy13.png').convert_alpha()]
enemy1 = [pygame.image.load('everything/enemy1/enemy10.png').convert_alpha(),
          pygame.image.load('everything/enemy1/enemy11.png').convert_alpha(),
          pygame.image.load('everything/enemy1/enemy12.png').convert_alpha(),
          pygame.image.load('everything/enemy1/enemy13.png').convert_alpha()]
enemy2 = [pygame.image.load('everything/enemy2/enemy20.png').convert_alpha(),
          pygame.image.load('everything/enemy2/enemy21.png').convert_alpha(),
          pygame.image.load('everything/enemy2/enemy22.png').convert_alpha(),
          pygame.image.load('everything/enemy2/enemy23.png').convert_alpha(),
          pygame.image.load('everything/enemy2/enemy24.png').convert_alpha()]
enemy3 = [pygame.image.load('everything/enemy3/enemy30.png').convert_alpha(),
          pygame.image.load('everything/enemy3/enemy31.png').convert_alpha(),
          pygame.image.load('everything/enemy3/enemy32.png').convert_alpha(),
          pygame.image.load('everything/enemy3/enemy33.png').convert_alpha()]
enemy4 = [pygame.image.load('everything/enemy4/enemy40.png').convert_alpha(),
          pygame.image.load('everything/enemy4/enemy41.png').convert_alpha(),
          pygame.image.load('everything/enemy4/enemy42.png').convert_alpha(),
          pygame.image.load('everything/enemy4/enemy43.png').convert_alpha()]
enemy11 = [pygame.image.load('everything/enemy1/enemy_flip10.png').convert_alpha(),
           pygame.image.load('everything/enemy1/enemy_flip11.png').convert_alpha(),
           pygame.image.load('everything/enemy1/enemy_flip12.png').convert_alpha(),
           pygame.image.load('everything/enemy1/enemy_flip13.png').convert_alpha()]
enemy22 = [pygame.image.load('everything/enemy2/enemy_flip20.png').convert_alpha(),
           pygame.image.load('everything/enemy2/enemy_flip21.png').convert_alpha(),
           pygame.image.load('everything/enemy2/enemy_flip22.png').convert_alpha(),
           pygame.image.load('everything/enemy2/enemy_flip23.png').convert_alpha(),
           pygame.image.load('everything/enemy2/enemy_flip24.png').convert_alpha()]
enemy33 = [pygame.image.load('everything/enemy3/enemy_flip30.png').convert_alpha(),
           pygame.image.load('everything/enemy3/enemy_flip31.png').convert_alpha(),
           pygame.image.load('everything/enemy3/enemy_flip32.png').convert_alpha(),
           pygame.image.load('everything/enemy3/enemy_flip33.png').convert_alpha()]
enemy44 = [pygame.image.load('everything/enemy4/enemy_flip40.png').convert_alpha(),
           pygame.image.load('everything/enemy4/enemy_flip41.png').convert_alpha(),
           pygame.image.load('everything/enemy4/enemy_flip42.png').convert_alpha(),
           pygame.image.load('everything/enemy4/enemy_flip43.png').convert_alpha()]

run_r = [pygame.image.load('everything/running/run00.png').convert_alpha(),
         pygame.image.load('everything/running/run01.png').convert_alpha(),
         pygame.image.load('everything/running/run02.png').convert_alpha(),
         pygame.image.load('everything/running/run03.png').convert_alpha(),
         pygame.image.load('everything/running/run04.png').convert_alpha(),
         pygame.image.load('everything/running/run05.png').convert_alpha()]
run_l = [pygame.image.load('everything/running/beh_0.png').convert_alpha(),
         pygame.image.load('everything/running/beh_1.png').convert_alpha(),
         pygame.image.load('everything/running/beh_2.png').convert_alpha(),
         pygame.image.load('everything/running/beh_3.png').convert_alpha(),
         pygame.image.load('everything/running/beh_4.png').convert_alpha(),
         pygame.image.load('everything/running/beh_5.png').convert_alpha()]


class Enemies:
    def __init__(self, image, x, y, w, h, movement_speed, enemy_health):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.movement_speed = movement_speed
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.image = image
        self.enemycount = 0
        self.enemy_health = enemy_health
        self.live = True

    def draw(self):
        if self.live:
            if self.enemycount + 1 >= 18:
                self.enemycount = 0
            display.blit(self.image[self.enemycount // 5],
                         (self.rect[0] - int(scroll[0]), self.rect[1] - int(scroll[1])))
            self.enemycount += 1
        if not self.live:
            self.rect = pygame.Rect(0, 0, self.w, self.h)

    def collision(self, bulletrect, l_bulletrect, r_bulletrect):
        global healthbar, coins, damage_decreaser
        if days == 3:
            damage_decreaser = 0.9
        if days == 5:
            damage_decreaser = 0.8
        if days == 7:
            damage_decreaser = 0.7
        if days == 9:
            damage_decreaser = 0.65
        if days == 11:
            damage_decreaser = 0.55
        if days == 16:
            damage_decreaser = 0.45
        if days == 19:
            damage_decreaser = 0.4
        if self.rect.colliderect(bulletrect):
            self.enemy_health -= 2 * upgrade_p * damage_decreaser
        if self.rect.colliderect(l_bulletrect):
            self.enemy_health -= 2 * upgrade_l * damage_decreaser
        if self.rect.colliderect(r_bulletrect):
            self.enemy_health -= 2 * upgrade_r * damage_decreaser
        if self.enemy_health <= 5:
            self.live = False
            if 6 > self.enemy_health > -14:
                coins += 1
                enemy_dead_sound.play()
            self.enemy_health = -50
        if time == 0:
            self.enemy_health = self.enemy_health
        if self.rect.colliderect(player_rect):
            healthbar -= 1

    def moving(self):
        self.rect[0] += self.movement_speed


def map_reader(path):
    f = open(path + '.txt', 'r')
    read = f.read()
    f.close()
    read = read.split('\n')
    mapp = []
    for row in read:
        mapp.append(list(row))
    return mapp


def collision(rect, tiles):
    hit = []
    global healthbar
    for tile in tiles:
        if rect.colliderect(tile):
            hit.append(tile)

        if healthbar <= 0:
            healthbar = 100

    return hit


# Collisions with tiles, moving player
def move(rect, tiles, location):
    col_type = {'top': False, 'bottom': False, 'left': False, 'right': False}
    rect.x += location[0]
    hit = collision(rect, tiles)
    for tile in hit:
        if location[0] > 0:
            rect.right = tile.left
            col_type['right'] = True
        elif location[0] < 0:
            rect.left = tile.right
            col_type['left'] = True
    rect.y += round(location[1])
    hit = collision(rect, tiles)
    for tile in hit:
        if location[1] > 0:
            rect.bottom = tile.top
            col_type['bottom'] = True
        elif location[1] < 0:
            rect.top = tile.bottom
            col_type['top'] = True
    return rect, col_type


def health_bar():
    if healthbar == 1:
        pygame.draw.rect(display, white, (0, 387, 2, 13))
    if 1 < healthbar <= 10:
        pygame.draw.rect(display, white, (0, 387, 10, 13))
    if 10 < healthbar <= 20:
        pygame.draw.rect(display, white, (0, 387, 20, 13))
    if 20 < healthbar <= 30:
        pygame.draw.rect(display, white, (0, 387, 30, 13))
    if 30 < healthbar <= 40:
        pygame.draw.rect(display, white, (0, 387, 40, 13))
    if 40 < healthbar <= 50:
        pygame.draw.rect(display, white, (0, 387, 50, 13))
    if 50 < healthbar <= 60:
        pygame.draw.rect(display, white, (0, 387, 60, 13))
    if 60 < healthbar <= 70:
        pygame.draw.rect(display, white, (0, 387, 70, 13))

    if 70 < healthbar <= 80:
        pygame.draw.rect(display, white, (0, 387, 80, 13))

    if 80 < healthbar <= 90:
        pygame.draw.rect(display, white, (0, 387, 90, 13))

    if 90 < healthbar <= 100:
        pygame.draw.rect(display, white, (0, 387, 100, 13))


def game_time():
    global time, days, night, day
    time += 1
    if time <= 1500:
        display.fill(skyblue)
        day = True
        night = False
    elif 1500 < time <= 3000:
        display.fill(dusk)
        day = True
        night = False
    elif 3000 < time <= 4000:
        display.fill(darkblue)
        night = True
        day = False
    elif 4000 < time <= 6000:
        display.fill(nightsky)
        night = True
        day = False
    else:
        display.fill(white)
        night = False
        day = False
    if time == 6000:
        time = 0
        days += 1
    if night:
        display.blit(moon, (80 - int(scroll[0] * 0.02), round(-45 - int(scroll[1]) * 0.04)))
    if day:
        display.blit(sun, (700 - int(scroll[0] * 0.02), 10 - int(scroll[1] * 0.04)))

    if time == 1500:
        enemy_objects.extend(
            (Enemies(enemy1, 4600, 225, 32, 32, -0.5, 70), Enemies(enemy1, 4700, 225, 32, 32, -0.6, 70)))
    if time == 2000:
        enemy_objects.extend((Enemies(enemy2, 5600, 225, 32, 32, -1.3, 40),
                              Enemies(enemy3, 5500, 225, 32, 32, -0.9, 50)))
    if time == 3000:
        enemy_objects.append(Enemies(enemy2, 5300, 225, 32, 32, -1.3, 50))
    if time == 3500:
        enemy_objects.append(Enemies(enemy4, 5600, 225, 32, 32, -1.1, 50))
    if time == 3000:
        enemy_objects.append(Enemies(enemy11, -600, 225, 32, 32, 1.5, 90))
    if time == 4600:
        enemy_objects.append(Enemies(enemy22, -760, 225, 32, 32, 2, 50))
    if time == 4300:
        enemy_objects.append(Enemies(enemy33, -750, 225, 32, 32, 1.6, 60))

    if days >= 2:
        if time == 1500:
            enemy_objects.extend(
                (Enemies(enemy1, 4000, 225, 32, 32, -0.6, 90), Enemies(enemy1, 4300, 225, 32, 32, -0.6, 90)))
        if time == 2000:
            enemy_objects.append(Enemies(enemy33, -750, 225, 32, 32, 1.6, 50))
    if days >= 3:
        if time == 2600:
            enemy_objects.extend((Enemies(enemy2, 5800, 225, 32, 32, -1.4, 50),
                                  Enemies(enemy1, 5400, 225, 32, 32, -0.5, 90)))
        if time == 3000:
            enemy_objects.extend(
                (Enemies(enemy22, -760, 225, 32, 32, 2, 50), Enemies(enemy33, -750, 225, 32, 32, 1.6, 60)))
    if days >= 4:
        if time == 3500:
            enemy_objects.extend(
                (Enemies(enemy2, 5400, 225, 32, 32, -1.4, 40), Enemies(enemy44, -700, 225, 32, 32, 1.9, 60),
                 Enemies(enemy33, -750, 225, 32, 32, 1.6, 60)))
    if days >= 6:
        if time == 1550:
            enemy_objects.extend(
                (Enemies(enemy1, 4400, 225, 32, 32, -0.7, 90), Enemies(enemy2, 5000, 225, 32, 32, -1, 60)))
        if time == 4100:
            enemy_objects.append(Enemies(enemy4, 5600, 225, 32, 32, -1.1, 70))
        if time == 3300:
            enemy_objects.append(Enemies(enemy11, -700, 225, 32, 32, 1.8, 100))
        if time == 3000:
            enemy_objects.append(Enemies(enemy11, -680, 225, 32, 32, 1.5, 100))
        if time == 2500:
            enemy_objects.append(Enemies(enemy22, -760, 225, 32, 32, 2, 50))
        if time == 4300:
            enemy_objects.append(Enemies(enemy44, -750, 225, 32, 32, 1.6, 60))
    if days >= 7:
        if time == 1400:
            enemy_objects.extend(
                (Enemies(enemy22, -700, 225, 32, 32, 2.2, 50), Enemies(enemy22, -500, 225, 32, 32, 2.1, 50)))
        if time == 3000:
            enemy_objects.append(Enemies(enemy11, -700, 225, 32, 32, 1.8, 90))
        if time == 2800:
            enemy_objects.append(Enemies(enemy11, -680, 225, 32, 32, 1.5, 90))
        if time == 2300:
            enemy_objects.append(Enemies(enemy22, -760, 225, 32, 32, 2.3, 50))
        if time == 4100:
            enemy_objects.append(Enemies(enemy44, -750, 225, 32, 32, 1.6, 60))
    if days >= 8:
        if time == 1600:
            enemy_objects.extend(
                (Enemies(enemy44, -700, 225, 32, 32, 2, 60), Enemies(enemy3, 5100, 225, 32, 32, -1, 60)))
        if time == 1900:
            enemy_objects.extend(
                (Enemies(enemy22, -640, 225, 32, 32, 2, 60), Enemies(enemy2, 5000, 225, 32, 32, -1.3, 50)))
    if days >= 9:
        if time == 2100:
            enemy_objects.extend(
                (Enemies(enemy44, -700, 225, 32, 32, 2.1, 60), Enemies(enemy1, 5000, 225, 32, 32, -0.8, 100),
                 Enemies(enemy1, 5100, 225, 32, 32, -0.7, 110), Enemies(enemy3, 5100, 225, 32, 32, -1.1, 80),
                 Enemies(enemy4, 4900, 225, 32, 32, -1, 80)))
    if days == 10:
        if time == 2000:
            enemy_objects.append(Enemies(big_enemy3, 5000, 60, 100, 200, -0.4, 700))
    if days == 11:
        if time == 2000:
            enemy_objects.append(Enemies(big_enemy1, -600, 115, 100, 200, 1, 700))
    if days >= 14:
        if time == 1400:
            enemy_objects.extend(
                (Enemies(enemy33, -640, 225, 32, 32, 2, 60), Enemies(enemy1, 5000, 225, 32, 32, -1, 100)))
    if days == 15:
        if time == 1500:
            enemy_objects.append(Enemies(big_enemy3, 5000, 60, 128, 200, -0.4, 700))
        if time == 2000:
            enemy_objects.append(Enemies(big_enemy1, -600, 115, 128, 200, 1, 700))
    if days >= 16:
        if time == 1500:
            enemy_objects.extend(
                (Enemies(enemy22, -640, 225, 32, 32, 2.5, 60), Enemies(enemy2, 5000, 225, 32, 32, -1.5, 60),
                 Enemies(enemy3, 4800, 225, 32, 32, -1, 110), Enemies(enemy11, -400, 225, 32, 32, 1, 110)))
    if days >= 17:
        if time == 1500:
            enemy_objects.extend(
                (Enemies(enemy1, 5000, 225, 128, 200, -0.7, 130), Enemies(enemy2, 4400, 225, 128, 200, -1.2, 60)))
        if time == 3500:
            enemy_objects.extend(
                (Enemies(enemy11, -500, 225, 128, 200, 1.2, 120), Enemies(enemy11, -400, 225, 128, 200, 1.2, 130)))
    if days >= 18:
        if time == 3050:
            enemy_objects.extend(
                (Enemies(enemy2, 5000, 225, 128, 200, -1.7, 60), Enemies(enemy3, 4400, 225, 128, 200, -2, 70)))
        if time == 3500:
            enemy_objects.extend(
                (Enemies(enemy44, -400, 225, 128, 200, 1.2, 70), Enemies(enemy22, -300, 225, 128, 200, 1, 50)))
    if days >= 21:
        if time == 1500:
            enemy_objects.append(Enemies(big_enemy3, 5000, 60, 128, 200, -0.4, 700))
        if time == 2000:
            enemy_objects.append(Enemies(big_enemy1, -600, 115, 128, 200, 1, 700))

    if time == 1450:
        enemy_objects.clear()

    if time == 1420:
        with open('everything/saves/previous_save.txt', 'w') as previous_save:
            json.dump(
                (player_rect.x, player_rect.y, time, coins, days, upgrade_r, upgrade_l, upgrade_p, turret1, turret2,
                 damage_decreaser, healthbar), previous_save)
    if days <= 1:
        if time == 100:
            enemy_objects.clear()


def text_reader(text, fontt, colorr, surface, x, y):
    text_object = fontt.render(text, 1, colorr)
    textrect = text_object.get_rect()
    textrect.topleft = (round(x), round(y))
    surface.blit(text_object, textrect)


def main_menu():
    menu = True

    while menu:
        screen.blit(menu_bg, (0, 0))
        text_reader('MAIN MENU', large_font, white, screen, screen.get_width() / 2 - 100, 20)

        mx, my = pygame.mouse.get_pos()

        button1 = pygame.Rect(round(screen.get_width() / 3 - 100), 700, 200, 50)
        button2 = pygame.Rect(round(screen.get_width() / 2 - 100), 700, 200, 50)
        button3 = pygame.Rect(round(screen.get_width() / 1.5 - 100), 700, 200, 50)

        pygame.draw.rect(screen, white, button1)
        pygame.draw.rect(screen, white, button2)
        pygame.draw.rect(screen, white, button3)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                menu = False

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if button1.collidepoint(mx, my):
            pygame.draw.rect(screen, grey, button1)
            if click:
                mainloop()
        if button2.collidepoint(mx, my):
            pygame.draw.rect(screen, grey, button2)
            if click:
                options_menu()
        if button3.collidepoint(mx, my):
            pygame.draw.rect(screen, grey, button3)
            if click:
                pygame.quit()
                sys.exit()

        text_reader('PLAY', font, (0, 0, 0), screen, button1[0] + 85, button1[1] + 10)
        text_reader('OPTIONS', font, (0, 0, 0), screen, button2[0] + 80, button2[1] + 10)
        text_reader('QUIT', font, (0, 0, 0), screen, button3[0] + 85, button3[1] + 10)

        pygame.display.update()
        clock.tick(60)


def options_menu():
    options = True

    while options:
        screen.blit(menu_bg, (0, 0))
        text_reader('OPTIONS', large_font, white, screen, screen.get_width() / 2 - 100, 20)
        mx, my = pygame.mouse.get_pos()

        button1 = pygame.Rect(round(screen.get_width() / 3 - 100), 700, 200, 50)
        button2 = pygame.Rect(round(screen.get_width() / 1.5 - 100), 700, 200, 50)
        button3 = pygame.Rect(round(screen.get_width() / 2 - 100), 700, 200, 50)
        button4 = pygame.Rect(round(screen.get_width() / 2 - 100), 600, 200, 50)
        pygame.draw.rect(screen, white, button1)
        pygame.draw.rect(screen, white, button2)
        pygame.draw.rect(screen, white, button3)
        pygame.draw.rect(screen, white, button4)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                options = False

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if button1.collidepoint(mx, my):
            pygame.draw.rect(screen, grey, button1)
            if click:
                controls_menu()

        if button2.collidepoint(mx, my):
            pygame.draw.rect(screen, grey, button2)
            if click:
                main_menu()
        if button3.collidepoint(mx, my):
            pygame.draw.rect(screen, grey, button3)
            if click:
                audio_menu()
        if button4.collidepoint(mx, my):
            pygame.draw.rect(screen, grey, button4)
            if click:
                credits_menu()

        text_reader('CONTROLS', font, (0, 0, 0), screen, button1[0] + 70, button1[1] + 10)
        text_reader('BACK', font, (0, 0, 0), screen, button2[0] + 80, button2[1] + 10)
        text_reader('AUDIO', font, (0, 0, 0), screen, button3[0] + 80, button3[1] + 10)
        text_reader('CREDITS', font, (0, 0, 0), screen, button4[0] + 80, button4[1] + 10)

        pygame.display.update()
        clock.tick(60)


def controls_menu():
    controls = True
    button_color = white

    while controls:

        screen.blit(menu_bg, (0, 0))
        text_reader('CONTROLS', large_font, white, screen, screen.get_width() / 2 - 100, 20)
        mx, my = pygame.mouse.get_pos()

        button1 = pygame.Rect(round(screen.get_width() / 2 - 100), 700, 200, 50)
        pygame.draw.rect(screen, button_color, button1)
        text_reader('BACK', font, (0, 0, 0), screen, button1[0] + 80, button1[1] + 10)
        text_reader('Left: A', medium_font, white, screen, 100, 200)
        text_reader('Right: D', medium_font, white, screen, 100, 300)
        text_reader('Jump: SPACE', medium_font, white, screen, 100, 400)
        text_reader('Sprint: SHIFT + A / SHIFT + D', medium_font, white, screen, 100, 500)
        text_reader('Pause: ESC', medium_font, white, screen, 100, 600)
        text_reader('Attack: E', medium_font, white, screen, 100, 700)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                controls = False

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if button1.collidepoint(mx, my):
            button_color = grey
            if click:
                options_menu()
        else:
            button_color = white

        pygame.display.update()
        clock.tick(60)


def audio_menu():
    audio = True

    while audio:
        screen.blit(menu_bg, (0, 0))

        text_reader('AUDIO', large_font, white, screen, screen.get_width() / 2 - 100, 20)
        mx, my = pygame.mouse.get_pos()

        button1 = pygame.Rect(round(screen.get_width() / 2 - 100), 700, 200, 50)
        audio_off = pygame.Rect(210, 210, 20, 20)
        audio_medium = pygame.Rect(250, 210, 20, 20)
        audio_loud = pygame.Rect(290, 210, 20, 20)
        audio_optimized = pygame.Rect(330, 210, 20, 20)

        pygame.draw.rect(screen, white, button1)
        pygame.draw.circle(screen, white, (220, 220), 15, 2)
        pygame.draw.circle(screen, white, (260, 220), 15, 2)
        pygame.draw.circle(screen, white, (300, 220), 15, 2)
        pygame.draw.circle(screen, white, (340, 220), 15, 2)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                audio = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if audio_optimized.collidepoint(mx, my):
            pygame.draw.circle(screen, white, (340, 220), 15)
            if click:
                grass_sound[0].set_volume(0.08)
                grass_sound[1].set_volume(0.08)
                jump_sound.set_volume(0.5)
                pygame.mixer.music.set_volume(0.04)
                bullet_sound.set_volume(0.1)
                enemy_dead_sound.set_volume(0.5)

        if audio_loud.collidepoint(mx, my):
            pygame.draw.circle(screen, white, (300, 220), 15)
            if click:
                pygame.mixer.music.set_volume(1)
                grass_sound[0].set_volume(1)
                grass_sound[1].set_volume(1)
                jump_sound.set_volume(1)
                bullet_sound.set_volume(1)
                enemy_dead_sound.set_volume(1)

        if audio_medium.collidepoint(mx, my):
            pygame.draw.circle(screen, white, (260, 220), 15)
            if click:
                pygame.mixer.music.set_volume(0.1)
                grass_sound[0].set_volume(0.3)
                grass_sound[1].set_volume(0.3)
                jump_sound.set_volume(0.8)
                bullet_sound.set_volume(0.5)
                enemy_dead_sound.set_volume(0.8)

        if audio_off.collidepoint(mx, my):
            pygame.draw.circle(screen, white, (220, 220), 15)
            if click:
                pygame.mixer.music.set_volume(0)
                grass_sound[0].set_volume(0)
                grass_sound[1].set_volume(0)
                jump_sound.set_volume(0)
                bullet_sound.set_volume(0)
                enemy_dead_sound.set_volume(0)

        if button1.collidepoint(mx, my):
            pygame.draw.rect(screen, grey, button1)
            if click:
                options_menu()

        text_reader('BACK', font, (0, 0, 0), screen, button1[0] + 80, button1[1] + 10)
        text_reader('Master', medium_font, white, screen, 100, 200)
        text_reader('  OFF     MEDIUM   MAX   LOW   ', font, white, screen, 200, 170)

        pygame.display.update()
        clock.tick(60)


def credits_menu():
    credit = True

    while credit:
        screen.blit(menu_bg, (0, 0))
        text_reader('CREDITS', large_font, white, screen, screen.get_width() / 2 - 100, 20)
        mx, my = pygame.mouse.get_pos()

        button1 = pygame.Rect(round(screen.get_width() / 2 - 100), 700, 200, 50)
        pygame.draw.rect(screen, white, button1)

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                credit = False

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        if button1.collidepoint(mx, my):
            pygame.draw.rect(screen, grey, button1)
            if click:
                options_menu()

        text_reader('BACK', font, (0, 0, 0), screen, button1[0] + 80, button1[1] + 10)
        text_reader('Music: Schmauz', medium_font, white, screen, 100, 300)
        text_reader('Enemy art: Bonchilo', medium_font, white, screen, 100, 400)
        text_reader('Help with code for Enemies: Tempest', medium_font, white, screen, 100, 500)
        text_reader('Code: asi Lukas', medium_font, white, screen, 100, 600)
        pygame.display.update()
        clock.tick(60)


def pause():
    global player_rect, time, coins, days, upgrade_r, upgrade_l, upgrade_p, turret1, turret2, damage_decreaser, healthbar
    now_pause = True

    while now_pause:
        screen.blit(menu_bg, (0, 0))

        text_reader('PAUSE', large_font, white, screen, screen.get_width() / 2 - 70, 20)
        text_reader('press ESC to resume', large_font, white, screen, screen.get_width() / 2 - 160, 60)
        mx, my = pygame.mouse.get_pos()

        button2 = pygame.Rect(screen.get_width() / 2 - 100, 500, 200, 50)
        button1 = pygame.Rect(screen.get_width() / 2 - 100, 200, 200, 50)
        button3 = pygame.Rect(screen.get_width() / 2 - 100, 800, 200, 50)

        pygame.draw.rect(screen, white, button1)
        pygame.draw.rect(screen, white, button2)
        pygame.draw.rect(screen, white, button3)

        click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                now_pause = False

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    mainloop()

        if button1.collidepoint(mx, my):
            pygame.draw.rect(screen, grey, button1)
            if click:
                with open('everything/saves/new_save.txt') as new_save:
                    player_rect.x, player_rect.y, time, coins, days, upgrade_r, upgrade_l, upgrade_p, turret1, turret2, damage_decreaser, healthbar = json.load(
                        new_save)
                mainloop()
        if button2.collidepoint(mx, my):
            pygame.draw.rect(screen, grey, button2)
            if click:
                with open('everything/saves/previous_save.txt') as last_save:
                    player_rect.x, player_rect.y, time, coins, days, upgrade_r, upgrade_l, upgrade_p, turret1, turret2, damage_decreaser, healthbar = json.load(
                        last_save)
                mainloop()
        if button3.collidepoint(mx, my):
            pygame.draw.rect(screen, grey, button3)
            if click:
                main_menu()

        text_reader('LOAD NEW SAVE', font, (0, 0, 0), screen, button1[0] + 50, button1[1] + 10)
        text_reader('LOAD LAST SAVE', font, (0, 0, 0), screen, button2[0] + 50, button2[1] + 10)
        text_reader('MAIN MENU', font, (0, 0, 0), screen, button3[0] + 65, button3[1] + 10)

        pygame.display.update()
        clock.tick(60)


def end_screen():
    global player_rect, time, coins, days, upgrade_r, upgrade_l, upgrade_p, turret1, turret2, damage_decreaser, healthbar
    end = True

    while end:
        screen.blit(menu_bg, (0, 0))
        text_reader('MAYBE TRY AGAIN?', large_font, white, screen, screen.get_width() / 2 - 150, 100)

        mx, my = pygame.mouse.get_pos()
        button2 = pygame.Rect(screen.get_width() / 2 - 100, 500, 200, 50)
        button1 = pygame.Rect(screen.get_width() / 2 - 100, 200, 200, 50)
        button3 = pygame.Rect(screen.get_width() / 2 - 100, 800, 200, 50)

        pygame.draw.rect(screen, white, button1)
        pygame.draw.rect(screen, white, button2)
        pygame.draw.rect(screen, white, button3)

        click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = False

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if button1.collidepoint(mx, my):
            pygame.draw.rect(screen, grey, button1)
            if click:
                with open('everything/saves/new_save.txt') as new_save:
                    player_rect.x, player_rect.y, time, coins, days, upgrade_r, upgrade_l, upgrade_p, turret1, turret2, damage_decreaser, healthbar = json.load(
                        new_save)
                mainloop()

        if button2.collidepoint(mx, my):
            pygame.draw.rect(screen, grey, button2)
            if click:
                with open('everything/saves/previous_save.txt') as last_save:
                    player_rect.x, player_rect.y, time, coins, days, upgrade_r, upgrade_l, upgrade_p, turret1, turret2, damage_decreaser, healthbar = json.load(
                        last_save)
                mainloop()
        if button3.collidepoint(mx, my):
            pygame.draw.rect(screen, grey, button3)
            if click:
                pygame.quit()
                sys.exit()

        text_reader('TRY AGAIN', font, (0, 0, 0), screen, button1[0] + 70, button1[1] + 10)
        text_reader('LOAD LAST SAVE', font, (0, 0, 0), screen, button2[0] + 50, button2[1] + 10)
        text_reader('QUIT', font, (0, 0, 0), screen, button3[0] + 80, button3[1] + 10)

        pygame.display.update()
        clock.tick(60)


# Variables for main_loop
scroll = [0, 0]
moving = [0, 0]
randomX = random.randint(150, 900)
randomX1 = random.randint(130, 500)
randomX2 = random.randint(110, 950)
randomY = random.randint(20, 110)
randomY1 = random.randint(30, 100)
randomY2 = random.randint(10, 150)
font = pygame.font.Font("everything/font/Pixeled.ttf", 8)
large_font = pygame.font.Font("everything/font/Pixeled.ttf", 20)
medium_font = pygame.font.Font('everything/font/Pixeled.ttf', 15)
small_font = pygame.font.Font('everything/font/Pixeled.ttf', 5)
mapa = map_reader('everything/map')
healthbar = 100
time = 0
days = 1
coins = 0
player_rect = pygame.Rect(bg.get_width(), 120, 28, 16)
vel = 8
night = False
day = False
enemy_objects = []
upgrade_p = 1
upgrade_l = 1
upgrade_r = 1
turret1 = False
turret2 = False
damage_decreaser = 1
escape_price = 150


# --------------------------------------------------- Main game loop ---------------------------------------------------
def mainloop():
    global player_rect, screen, coins, upgrade_p, upgrade_l, upgrade_r, healthbar
    global turret1, turret2
    runcount = 0
    firecount = 0

    bullet_rect = pygame.Rect(0, 0, 6, 6)
    bullet_side = 0

    grass_sound_timer = 0
    shift_grass_sound_timer = 0

    bullet_state = 'ready'
    l_cannon_rect = pygame.Rect(bg.get_width() - 100, 225, 32, 32)
    r_cannon_rect = pygame.Rect(bg.get_width() + 100, 225, 32, 32)
    l_bullet_rect = pygame.Rect(l_cannon_rect.x - 150, l_cannon_rect.y + 15, 6, 6)
    r_bullet_rect = pygame.Rect(r_cannon_rect.x + 165, r_cannon_rect.y + 15, 6, 6)
    cannon_price = 2
    upgrade_price = 15
    player_upgrade = 20
    player_health = 5

    game_end = False
    moving_r = False
    moving_l = False
    moving_shift = False
    moving_shift_d = False
    moving_shift_a = False
    run = True
    i = 'idle'

    air_time = 0
    player_y_loc = 0

    while run:
        game_time()
        # Paralax bg
        display.blit(bg, (-80 - int(scroll[0] * 0.09), 60 - int(scroll[1] * 0.15)))
        moving[0] += 0.1
        moving[1] += 0.1
        scroll[0] += (player_rect.x - scroll[0] - 376) / 20
        scroll[1] += (player_rect.y - scroll[1] - 320) / 20

        if grass_sound_timer > 0:
            grass_sound_timer -= 1

        tile_rects = []
        y = 0
        for row in mapa:
            x = -50
            for tile in row:
                if tile == '1':
                    display.blit(dirttile, (x * 16 - int(scroll[0]), y * 16 - int(scroll[1])))
                if tile == '3':
                    display.blit(grasstile, (x * 16 - int(scroll[0]), y * 16 - int(scroll[1])))
                if not game_end:
                    if tile == '4':
                        display.blit(block, (x * 16 - int(scroll[0]), y * 16 - int(scroll[1])))
                if game_end:
                    tile_rects.clear()
                if tile == '5':
                    display.blit(plant, (x * 16 - int(scroll[0]), y * 16 - int(scroll[1])))
                if tile == '6':
                    display.blit(tree1, (x * 16 - int(scroll[0]), y + 185 - int(scroll[1])))
                if tile == '7':
                    display.blit(tree2, (x * 16 - int(scroll[0]), y + 171 - int(scroll[1])))
                if tile == '8':
                    display.blit(fire[firecount // 5], (x * 16 - 5 - int(scroll[0]), y + 220 - int(scroll[1])))
                    firecount += 1
                if tile == '9':
                    display.blit(rock, (x * 16 - 3 - int(scroll[0]), y + 230 - int(scroll[1])))
                if tile == '!':
                    display.blit(tree3, (x * 16 - 20 - int(scroll[0]), y + 100 - int(scroll[1])))
                if tile != '0' and tile != '5' and tile != '6' and tile != '7' and tile != '8' and tile != '9' and tile != '!':
                    tile_rects.append(pygame.Rect(x * 16, y * 16, 16, 16))

                x += 1
            y += 1

        display.blit(cloud3, (650 - int(scroll[0] * 0.12) - int(moving[0] * 0.09), 10 - int(scroll[1] * 0.12)))
        display.blit(cloud, (400 - int(scroll[0] * 0.16) - int(moving[0] * 0.2), 40 - int(scroll[1] * 0.16)))
        display.blit(cloud2, (350 - int(scroll[0] * 0.2) - int(moving[0] * 0.14), 80 - int(scroll[1] * 0.2)))
        display.blit(cloud2, (100 - int(scroll[0] * 0.2) - int(moving[0] * 0.13), 50 - int(scroll[1] * 0.2)))
        display.blit(cloud3, (100 - int(scroll[0] * 0.1) - int(moving[0] * 0.11), 100 - int(scroll[1] * 0.1)))
        display.blit(cloud, (400 - int(scroll[0] * 0.16) - int(moving[0] * 0.19), 40 - int(scroll[1] * 0.16)))
        display.blit(cloud3, (750 - int(scroll[0] * 0.12) - int(moving[0] * 0.09), 20 - int(scroll[1] * 0.12)))
        display.blit(cloud, (1250 - int(scroll[0] * 0.16) - int(moving[0] * 0.2), 30 - int(scroll[1] * 0.16)))
        display.blit(cloud2, (1000 - int(scroll[0] * 0.2) - int(moving[0] * 0.14), 90 - int(scroll[1] * 0.2)))
        display.blit(cloud2, (700 - int(scroll[0] * 0.2) - int(moving[0] * 0.13), 40 - int(scroll[1] * 0.2)))
        display.blit(cloud3, (1300 - int(scroll[0] * 0.17) - int(moving[0] * 0.11), 90 - int(scroll[1] * 0.1)))
        display.blit(cloud, (1200 - int(scroll[0] * 0.16) - int(moving[0] * 0.19), 50 - int(scroll[1] * 0.16)))
        display.blit(cloud03,
                     (randomX - int(scroll[0] * 0.13) - int(moving[0] * 0.12), randomY - int(scroll[1] * 0.13)))
        display.blit(cloud00,
                     (randomX1 - int(scroll[0] * 0.14) - int(moving[0] * 0.14),
                      randomY1 - int(scroll[1] * 0.15)))
        display.blit(cloud02,
                     (1000 - int(scroll[0] * 0.1) - int(moving[0] * 0.15), randomY2 - int(scroll[1] * 0.1)))
        display.blit(cloud03,
                     (1500 - int(scroll[0] * 0.13) - int(moving[0] * 0.12), randomY - int(scroll[1] * 0.13)))
        display.blit(cloud00,
                     (500 - int(scroll[0] * 0.14) - int(moving[0] * 0.14),
                      60 - int(scroll[1] * 0.15)))
        display.blit(cloud03,
                     (1100 - int(scroll[0] * 0.1) - int(moving[0] * 0.15), randomY2 - int(scroll[1] * 0.1)))
        display.blit(cannon_right, (r_cannon_rect.x + 140 - int(scroll[0]), r_cannon_rect.y - int(scroll[1])))
        display.blit(cannon_left, (l_cannon_rect.x - 150 - int(scroll[0]), l_cannon_rect.y - int(scroll[1])))

        player_loc = [0, 0]

        if moving_l:
            player_loc[0] -= 3
        if moving_r:
            player_loc[0] += 3
        if moving_shift_d and moving_shift:
            player_loc[0] += 1
        if moving_shift_a and moving_shift:
            player_loc[0] -= 1

        player_loc[1] += player_y_loc
        player_y_loc += 0.2
        if player_y_loc > 3:
            player_y_loc = 3

        player_rect, collisions = move(player_rect, tile_rects, player_loc)

        if shift_grass_sound_timer > 0:
            shift_grass_sound_timer -= 1
        if collisions['bottom']:
            air_time = 0
            player_y_loc = 0
            if moving_l or moving_r:
                if grass_sound_timer == 0:
                    grass_sound_timer = 50
                    random.choice(grass_sound).play()
            if moving_shift and moving_shift_d or moving_shift and moving_shift_a:
                if shift_grass_sound_timer == 0:
                    shift_grass_sound_timer = 30
                    random.choice(grass_sound).play()
        else:
            air_time += 1

        if runcount + 1 >= 18:
            runcount = 0
        if firecount + 1 >= 21:
            firecount = 0

        if i == 0:
            if moving_r:
                display.blit(run_r[runcount // 3], (player_rect.x - int(scroll[0]), player_rect.y - int(scroll[1])))
                runcount += 1
            elif moving_l:
                display.blit(run_l[runcount // 3], (player_rect.x - int(scroll[0]), player_rect.y - int(scroll[1])))
                runcount += 1

        if i == 'left':
            display.blit(run_l[0], (player_rect.x - int(scroll[0]), player_rect.y - int(scroll[1])))
        if i == 'right':
            display.blit(run_r[0], (player_rect.x - int(scroll[0]), player_rect.y - int(scroll[1])))
        if i == 'idle':
            display.blit(idle, (player_rect.x - int(scroll[0]), player_rect.y - int(scroll[1])))

        if bullet_state == 'ready':
            bullet_rect = pygame.Rect(0, -1000, 6, 6)
            l_bullet_rect[1] -= 1000
            r_bullet_rect[1] -= 1000
            if i == 'left':
                bullet_rect = pygame.Rect(player_rect.x + 15, player_rect.y + 3, 6, 6)
            if i == 'right':
                bullet_rect = pygame.Rect(player_rect.x, player_rect.y + 3, 6, 6)

        if bullet_state == 'fire':
            display.blit(bullet, (bullet_rect[0] - int(scroll[0]), bullet_rect[1] - int(scroll[1])))
            display.blit(bullet, (l_bullet_rect[0] - int(scroll[0]), l_bullet_rect[1] - int(scroll[1])))
            display.blit(bullet, (r_bullet_rect[0] - int(scroll[0]), r_bullet_rect[1] - int(scroll[1])))
            if i == 'left' or moving_l:
                bullet_side = -1

            if i == 'right' or moving_r:
                bullet_side = 1

            if player_rect.x + 85 > bullet_rect.x > player_rect.x - 70:
                bullet_rect.x += vel * bullet_side
                r_bullet_rect.x += vel
                l_bullet_rect.x -= vel
            else:
                bullet_rect = pygame.Rect(0, -1000, 6, 6)
                l_bullet_rect = pygame.Rect(0, 0, 6, 6)
                r_bullet_rect = pygame.Rect(0, 0, 6, 6)
                bullet_state = 'ready'

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == KEYDOWN:
                if event.key == K_f and coins >= escape_price:
                    coins -= escape_price
                    game_end = True
                if event.key == K_DOWN:
                    if coins >= player_health:
                        coins -= player_health
                        healthbar += 100 - healthbar
                if event.key == K_UP:
                    if coins >= player_upgrade:
                        coins -= player_upgrade
                        upgrade_p += 1
                if event.key == K_LEFT and not turret1:
                    if coins >= cannon_price:
                        turret1 = True
                        coins -= cannon_price
                if event.key == K_j and turret1:
                    if coins >= upgrade_price:
                        coins -= upgrade_price
                        upgrade_l += 1
                if event.key == K_RIGHT and not turret2:
                    if coins >= cannon_price:
                        turret2 = True
                        coins -= cannon_price
                if event.key == K_l and turret2:
                    if coins >= upgrade_price:
                        coins -= upgrade_price
                        upgrade_r += 1
                if event.key == K_e:
                    bullet_sound.play()
                    if turret1:
                        l_bullet_rect = pygame.Rect(l_cannon_rect.x - 150, l_cannon_rect.y + 15, 6, 6)
                    if turret2:
                        r_bullet_rect = pygame.Rect(r_cannon_rect.x + 165, r_cannon_rect.y + 15, 6, 6)
                    bullet_state = 'fire'
                if event.key == K_ESCAPE:
                    pause()
                if event.key == K_LSHIFT:
                    moving_shift = True
                if event.key == K_d:
                    moving_r = True
                    moving_shift_d = True
                    i = 0
                if event.key == K_a:
                    moving_l = True
                    moving_shift_a = True
                    i = 0
                if event.key == K_SPACE:
                    if air_time < 6:
                        jump_sound.play()
                        player_y_loc = -3.7

            if event.type == KEYUP:
                if event.key == K_LSHIFT:
                    moving_shift = False
                    moving_shift_a = False
                    moving_shift_d = False
                if event.key == K_d:
                    moving_shift_d = False
                    moving_r = False
                    i = 'right'
                if event.key == K_a:
                    moving_shift_a = False
                    moving_l = False
                    i = 'left'

        for objectt in enemy_objects:
            objectt.draw()
            objectt.moving()
            objectt.collision(bullet_rect, r_bullet_rect, l_bullet_rect)

        if healthbar <= 1:
            end_screen()
        text = font.render('Health: ' + str(healthbar), 10, white)
        text2 = font.render('Day: ' + str(days), 10, white)
        text3 = font.render('Coins: ' + str(coins), 10, white)
        text4 = small_font.render('You need ' + str(cannon_price - coins) + ' more coins to repair that', 1, white)
        text5 = small_font.render('You need ' + str(cannon_price - coins) + ' more coins to repair that', 1, white)
        text6 = small_font.render('You need ' + str(player_upgrade - coins) + ' more coins to upgrade your weapon', 1,
                                  white)
        text7 = small_font.render('You need ' + str(player_health - coins) + ' more coins to fill your health', 1,
                                  white)
        text8 = medium_font.render('So you made it through my game huh? ', 1, (0, 0, 0))
        text9 = medium_font.render('Well, that is nice, but what about the bread?', 1, (0, 0, 0))
        text10 = medium_font.render('Will he ever land somewhere? I do not know.', 1, (0, 0, 0))
        if days == 1 or days == 5 or days == 10 or days == 15 or days >= 20:
            text11 = small_font.render('You need 150 coins to beat the game', 1, white)
            display.blit(text11, (600, 380))

        health_bar()
        display.blit(text, (1, 365))
        display.blit(text2, (1, 350))
        display.blit(text3, (1, 335))
        if game_end:
            display.blit(text8, (50, 100))
            display.blit(text9, (50, 150))
            display.blit(text10, (50, 200))
        if coins >= escape_price:
            text11 = small_font.render('Press F to finish the game', 1, (0, 0, 0))
            display.blit(text11, (620, 387))

        if coins >= cannon_price:
            text4 = small_font.render('Press left arrow key to repair that', 1, white)
            text5 = small_font.render('Press right arrow key to repair that', 1, white)
        if coins >= player_health:
            text7 = small_font.render('Press down arrow key to fill your health', 1, white)
        if coins >= player_upgrade:
            text6 = small_font.render('Press up arrow key to upgrade your weapon', 1, white)
        if turret1:
            text4 = small_font.render('You need ' + str(upgrade_price - coins) + ' more coins to upgrade cannon', 1,
                                      white)
            if coins >= upgrade_price:
                text4 = small_font.render('Press J to upgrade cannon', 1,
                                          white)

        if turret2:
            text5 = small_font.render('You need ' + str(upgrade_price - coins) + ' more coins to upgrade cannon', 1,
                                      white)
            if coins >= upgrade_price:
                text5 = small_font.render('Press L to upgrade cannon', 1,
                                          white)

        display.blit(text6, (round(bg.get_width() - 60 - int(scroll[0])), 255 - int(scroll[1])))
        display.blit(text7, (round(bg.get_width() - 60 - int(scroll[0])), 270 - int(scroll[1])))
        display.blit(text4, (round(l_cannon_rect.x - 200 - int(scroll[0])), l_cannon_rect.y + 30 - int(scroll[1])))
        display.blit(text5, (round(r_cannon_rect.x + 100 - int(scroll[0])), r_cannon_rect.y + 30 - int(scroll[1])))
        screen.blit(pygame.transform.scale(display, (monitor_size[0], monitor_size[1])), (0, 0))
        pygame.display.update()
        clock.tick(60)


main_menu()
mainloop()

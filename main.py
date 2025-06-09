import random
import pygame
import time
from pygame.locals import *

width = 900
height = 700

pygame.init()

pygame.display.set_caption("Recycle Game")
screen = pygame.display.set_mode((width, height))

def changeBackground(img):
    background = pygame.image.load(img)
    bg = pygame.transform.scale(background,(width,height))
    screen.blit(bg, (0,0))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images\\bin.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(40,60))
        self.rect = self.image.get_rect()

class Recycle(pygame.sprite.Sprite):
    def __init__(self, img):
        super().__init__()
        self.image = pygame.image.load(img).convert_alpha()
        self.image = pygame.transform.scale(self.image,(30,30))
        self.rect = self.image.get_rect()

class Non_Recycleable(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images\\bag.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (40,40))
        self.rect = self.image.get_rect()

images = ["images\paper.png","images\pencil.png","images\\box.png"]
item_list = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
plastic_list = pygame.sprite.Group()
for i in range(50):
    item = Recycle(random.choice(images))
    item.rect.x = random.randrange(width)
    item.rect.y = random.randrange(height)
    item_list.add(item)
    all_sprites.add(item)
for i in range(20):
    plastic = Non_Recycleable()
    plastic.rect.x = random.randrange(width)
    plastic.rect.y = random.randrange(height)
    plastic_list.add(plastic)
    all_sprites.add(plastic)
    
bin = Player()
all_sprites.add(bin)
white = (255,255,255)
red = (255,0,0)
playing = True
score = 0
clock = pygame.time.Clock()
start_time = time.time()
my_font = pygame.font.SysFont("Arial",20)
time_font = pygame.font.SysFont("Times New Roman",20)
text = my_font.render("Score = " + str(0),True,white)
while playing:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
    time_elapsed = time.time() - start_time
    if time_elapsed >= 60:
        if score > 50:
            text = my_font.render("Bin Loot Successful",True,red)
            changeBackground("images\win_screen.jpg")
        else:
            text = my_font.render("Better Luck Next Time",True, white)
            changeBackground("images\lose_screen.jpg")
        screen.blit(text,(250,40))
    else:
        changeBackground("images\\bg.png")
        countdown = time_font.render("Time left"+str(60-int(time_elapsed)),True,white)
        screen.blit(countdown,(20,10))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            if bin.rect.y > 0:
                bin.rect.y -= 5
        if keys[pygame.K_DOWN]:
            if bin.rect.y < 650:
                bin.rect.y += 5
        if keys[pygame.K_RIGHT]:
            if bin.rect.x < 850:
                bin.rect.x += 5
        if keys[pygame.K_LEFT]:
            if bin.rect.x > 0:
                bin.rect.x -= 5
        item_hit_list = pygame.sprite.spritecollide(bin,item_list,True)
        plastic_hit_list = pygame.sprite.spritecollide(bin,plastic_list,True)
        for item in item_hit_list:
            score += 1
            text = my_font.render("Score = " + str(score),True,white)
        for plastic in plastic_hit_list:
            score -= 5
            text = my_font.render("Score = " + str(score),True,white)
        screen.blit(text,(20,50))
        all_sprites.draw(screen)
    pygame.display.update()



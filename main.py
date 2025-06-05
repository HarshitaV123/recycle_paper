import random
import pygame
import time
from pygame.locals import *

width = 900
height = 700

pygame.init()

pygame.display.set_caption("Recycle Game")
screen = pygame.display.set_mode(width, height)

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

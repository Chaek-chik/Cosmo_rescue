import pygame as pg
from random import randint

class Bullet(pg.sprite.Sprite):
    def __init__(self, x, y, width = 0, height = 0, color = (255, 0, 0), speed_x = 0, speed_y = 0):
        super().__init__()
        self.width = width
        self.height = height
        self.color = color
        
        
        self.image = pg.Surface((self.width, self.height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed_x = speed_x
        self.speed_y = speed_y

    def change_size(self, width, height, image = ''):
        self.width = width
        self.height = height
        self.image = image
        if self.image:
            self.image = pg.transform.scale(
                pg.image.load(self.image),
                (self.width, self.height))
            self.rect = self.image.get_rect()

    
    def update(self):

        self.rect.y += self.speed_y 
        self.rect.x += self.speed_x
        
    
    


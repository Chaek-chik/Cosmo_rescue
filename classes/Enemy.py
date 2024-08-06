# класс врагов

import pygame as pg

import random

class Enemy(pg.sprite.Sprite):
    def __init__(self, x, y, screen, width = 20, height = 20, speed = 2, image = ''):
        super().__init__()
        self.width = width
        self.height = height
        self.scr = screen
        self.speed = speed
        self.scr_width = self.scr.get_width()
        self.scr_height = self.scr.get_height()
        self.image = image
        # self.image = pg.Surface([self.width, self.height])
        # self.image.fill((255, 0, 0))
        self.image = pg.transform.scale(pg.image.load(self.image),
                                        (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.change_x = random.uniform(-self.speed, self.speed)
        self.change_y = random.uniform(-self.speed, self.speed)

    # изменение скорости
    def change_speed(self, speed):
        self.speed += speed
    
    # изменение размера
    def change_view(self, width, height, image = ''):
        self.width = width
        self.height = height
        self.image = image
        if self.image:
            self.image = pg.transform.scale(
                pg.image.load(self.image),
                (self.width, self.height))
            self.rect = self.image.get_rect()

    # обновление позиции
    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        if self.rect.left < 0 or self.rect.right > self.scr_width:
            self.change_x *= -1
        if self.rect.top < 0 or self.rect.bottom > self.scr_height:
            self.change_y *= -1



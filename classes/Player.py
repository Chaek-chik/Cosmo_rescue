# класс игрока

import pygame as pg

class Player(pg.sprite.Sprite):

    def __init__(self, screen, width = 20, height = 20, speed  = 5, image = ''):
        super().__init__()
        self.width = width
        self.height = height
        self.scr = screen
        self.scr_width = self.scr.get_width()
        self.scr_height = self.scr.get_height()
        self.speed = speed
        self.image = image
        # self.image = pg.Surface([self.width, self.height])
        # self.image.fill((255, 255, 255))
        self.image = pg.transform.scale(
            pg.image.load(self.image),
            (self.width, self.height))

        self.rect = self.image.get_rect()
        self.rect.center = (self.scr_width // 2, self.scr_height - self.height // 2)
        self.change_x = 0
        self.change_y = 0

    # изменение размера rect
    def change_view(self, width, height, image = ''):
        self.width = width
        self.height = height
        self.image = image
        if self.image:
            self.image = pg.transform.scale(
                pg.image.load(self.image),
                (self.width, self.height))
            self.rect = self.image.get_rect()

    # изменение скорости игрока
    def chsnge_speed(self, speed):
        self.speed += speed

    # обновление позиции
    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > self.scr_width:
            self.rect.right = self.scr_width
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > self.scr_height:
            self.rect.bottom = self.scr_height

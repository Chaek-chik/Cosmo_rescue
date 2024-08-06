import pygame as pg
import random

class Boss(pg.sprite.Sprite):
    def __init__(self, x, y, screen,  width = 60, height = 60, speed = 5, image = '', weapons = []):
        super().__init__()
        self.width = width
        self.height = height
        self.speed = speed
        self.weapons = weapons
        self.boss_live = 100
        self.x = x
        self.y = y
        self.scr = screen
        self.scr_width = self.scr.get_width()
        self.scr_height = self.scr.get_height()
        self.image = image

        # self.image = pg.Surface([self.width, self.height])
        # self.image.fill((255, 0, 0))
        self.image = pg.transform.scale(pg.image.load(self.image),
                                         (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
    
        self.change_x = random.uniform(-self.speed, self.speed)
        self.change_y = random.uniform(-self.speed, self.speed)
        self.create_weapons(self.weapons)

    def change_view(self, width, height, image = ''):
        self.width = width
        self.height = height
        self.image = image
        if self.image:
            self.image = pg.transform.scale(pg.image.load(self.image),
                                            (self.width, self.height))
            self.rect = self.image.get_rect()
        # self.rect.center = (self.x, self.y)

    def create_weapons(self, weapons):
        # self.__dict__.update(args)
        for i in weapons:
            self.__dict__[i[0]] = (self.rect.centerx + i[1][0], self.rect.centery + i[1][1])
            self.__dict__[f'pos{i[0][-1]}'] = i[1]

        self.__dict__.pop('weapons')
            

    # def print_info(self):
    #     for key, value in self.__dict__.items():
    #         if 'weapon' in key:
    #             print(key, value)

    def check_position(self, screen):
        if self.rect.left < 0 or self.rect.right > self.scr_width:
            self.change_x *= -1
        if self.rect.top < 0 or self.rect.bottom > self.scr_height:
            self.change_y *= -1

    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        
        self.check_position(self.scr)
        self.weapon_update()
    
    def weapon_update(self):
        for key, value in self.__dict__.items():
            if 'weapon' in key:
                self.__dict__[key] = (self.rect.centerx + self.__dict__[f'pos{key[-1]}'][0], self.rect.centery + self.__dict__[f'pos{key[-1]}'][1])



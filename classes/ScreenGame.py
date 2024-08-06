import pygame as pg

# pg.init()

class ScreenGame:
   
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pg.display.set_mode((self.width, self.height))
        self.caption = pg.display.set_caption('')
        self.background = pg.image.load('images/background.png').convert()
        self.background = pg.transform.scale(self.background, (self.width, self.height))
        self.scroll = 0
        self.background_rect = self.background.get_rect()
        self.background_size = self.background.get_size()

    def transform_background(self):
        self.background = pg.transform.scale(self.background, (self.width, self.height))
        return self.background

    def change_caption(self, score = 0, live = 0, level = 0, boss_live = 0, boss = False):
        if not boss:
            self.caption = pg.display.set_caption(f'Космический бой.  Уничтожено: {str(score)}.  Жизней: {live}.  Уровень: {str(level)}.  Пауза: F2  Новая игра: F5  Правила: F1')
        else:
            self.caption = pg.display.set_caption(f'Космический бой.  Уничтожено: {str(score)}.  Жизней: {live}.  Уровень: {str(level)}.  Босс: жизней {str(boss_live)}.  Пауза: F2  Новая игра: F5  Правила: F1')

    def change_background(self, speed = 0):
        self.background_rect.y -= speed
        self.screen.blit(self.background, (self.background_rect.x, self.background_rect.y))
        # self.background_rect = self.new_background_rect
        if self.background_rect.y < self.height - self.height:
            self.screen.blit(self.background, (self.background_rect.bottomleft[0], self.background_rect.bottomleft[1]))
        if self.background_rect.bottom <= 0:
            self.background_rect.y = 0


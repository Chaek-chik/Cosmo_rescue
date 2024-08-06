# import pygame as pg

# pg.init()

# class ScreenGame:
#     def __init__(self):
#         self.width = 1024
#         self.height = 768
#         self.screen = pg.display.set_mode((self.width, self.height))
#         self.caption = pg.display.set_caption('')
#         self.background = pg.image.load('images/background.png').convert()
#         self.background = pg.transform.scale(self.background, (self.width, self.height))
#         self.scroll = 0
#         self.background_rect = self.background.get_rect()
#         self.background_size = self.background.get_size()

#     def transform_background(self):
#         self.background = pg.transform.scale(self.background, (self.width, self.height))
#         return self.background

#     def change_caption(self, score = 0, live = 0, level = 0, boss_live = 0, boss = False):
#         if not boss:
#             self.caption = pg.display.set_caption(f'Космический бой.  Уничтожено: {str(score)}.  Жизней: {live}.  Уровень: {str(level)}.  Пауза: F2  Новая игра: F5  Правила: F1')
#         else:
#             self.caption = pg.display.set_caption(f'Космический бой.  Уничтожено: {str(score)}.  Жизней: {live}.  Уровень: {str(level)}.  Босс: жизней {str(boss_live)}.  Пауза: F2  Новая игра: F5  Правила: F1')

#     def change_background(self, speed = 0):
#         self.background_rect.y -= speed
#         self.screen.blit(self.background, (self.background_rect.x, self.background_rect.y))
#         # self.background_rect = self.new_background_rect
#         if self.background_rect.y < self.height - self.height:
#             self.screen.blit(self.background, (self.background_rect.bottomleft[0], self.background_rect.bottomleft[1]))
#         if self.background_rect.bottom <= 0:
#             self.background_rect.y = 0

# # sg = ScreenGame()

# class Fonts:
#     def __init__(self):
#         self.heading = pg.font.SysFont('arial', 38)
#         self.text = pg.font.SysFont('arial', 24)
#         self.textFiles = pg.font.SysFont('arial', 18)
#         self.headingColor = (255, 255, 0)
#         self.textColor = (255, 255, 255)
#         self.textFilesColor = (255, 255, 255)
        

#     def txtObjects(self, text, font, color):
#         surf = font.render(text, True, color)
#         return surf, surf.get_rect()

# # fonts = Fonts()

# class SpriteSize:
#     def __init__(self):
#         self.player = 20
#         self.enemy = 20
#         self.boss = 60

# # sprite_size = SpriteSize()

# class SpriteSpeed:
#     def __init__(self):
#         self.player = 5
#         self.enemy = 2
#         self.player_bullet = 8
#         self.enemy_bullet = 5
#         self.boss = 5
#         self.boss_bullet = 50

# # sprite_speed = SpriteSpeed()

# class LevelsGame:
#     def __init__(self):
#         self.old_score = 0
#         self.live = 5
#         self.level = 0
#         self.enemies = 10
#         self.boss = 0

#     def change_levels(self, score = 0):
#         if score - self.old_score == 50:
#             self.live += 1
#             self.enemies += 2
#             self.level += 1
#             self.old_score = score
#         if score // 250 > self.boss:
#             self.boss += 1   

# # levels_game = LevelsGame()

# class Fps:
#     def __init__(self, tick):
#         self.tick = tick

#     def chahge_tick(self, tick):
#         self.tick = tick

# # fps = Fps(60)


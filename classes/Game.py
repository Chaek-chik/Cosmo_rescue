import pygame as pg
from pygame.locals import *
import random
from classes.Player import Player
from classes.Enemy import Enemy
from classes.Bullet import Bullet
from classes.Boss import Boss
from initialization import screenGame, fps, levelsGame, showText, bossWeapon, shots

screenGame.change_caption(0, levelsGame.live_player)


class Game:

    def __init__(self):
        pg.init()
        self.screen = screenGame.screen
        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()
        self.clock = pg.time.Clock()

        self.all_sprites = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.bullets_player = pg.sprite.Group()
        self.bullets_enemy = pg.sprite.Group()

        self.score = 0
        self.pause = False
        self.NewGame = False
        self.rules = False
        self.boss_level = True
        self.showText = showText.showText
        self.shots = shots

    def setup(self, player = True):

        if player:
            self.player = Player(width = 20,
                                 height = 20,
                                 screen = self.screen,
                                 speed = 8, image = 'images/player.png')
            self.all_sprites.add(self.player)

        if not self.boss_level:
            for _ in range(levelsGame.enemies):
                enemy = Enemy(x = random.uniform(20, self.screen_width),
                              y = random.uniform(20, self.screen_height - 20 * 10),
                              screen = self.screen,
                              speed = 2,
                              width = 20,
                              height = 20, image = 'images/enemy.png')
                self.enemies.add(enemy)
                self.all_sprites.add(enemy)

        elif self.boss_level:
            self.boss = Boss(x = random.uniform(20, self.screen_width),
                             y = random.uniform(20, self.screen_height - 20 * 15),
                             screen = self.screen, width = 60, height = 60, speed = 5,
                             weapons = bossWeapon.boss_level_1, image = 'images/boss1.png')

            screenGame.change_caption(self.score,
                                      levelsGame.live_player,
                                      levelsGame.level_game,
                                      self.boss.boss_live,
                                      boss = True)
            self.enemies.add(self.boss)
            self.all_sprites.add(self.boss)

    def hotKey(self, event = None):
        match event:
            case 'pause' | 'rules':
                self.pause = True if self.pause == False else False
                if self.pause:
                    if event == 'pause':
                        self.showText(
                            text_heading = 'Пауза',
                            text_basic = 'Для снятия с паузы нажмите F2')
                        self.top_window()

                    elif event == 'rules':
                        with open('rules_game.txt', 'r',
                                  encoding="UTF-8") as rg_file:
                            rules_list = []
                            for row in rg_file:
                                rules_list.append(row[:-1])
                        self.showText(
                            text_heading = 'Правила',
                            text_basic = 'Для продолжения игры нажмите F1',
                            text_file = rules_list,
                            position = 'top')
                        self.top_window()

            case 'NewGame':
                self.NewGame = True if self.NewGame == False else False
                if self.NewGame:
                    levelsGame.live_player = 5
                    levelsGame.enemies = 10
                    levelsGame.level_game = 0
                    self.score = 0
                    screenGame.change_caption(0, levelsGame.live_player)
                    self.showText(
                        text_heading='Новая игра',
                        text_basic='Для начала новой игры нажмите F5')
                    self.top_window()
                    self.all_sprites.empty()
                    self.enemies.empty()
                    self.setup()
        
    def top_window(self):
        top_screen = pg.Surface((self.screen_width, self.screen_height),
                                pg.SRCALPHA)
        top_screen.fill((0, 0, 255, 50))
        self.screen.blit(top_screen, (0, 0))
        pg.display.update()

    def run(self):
        self.setup()

        running = True

        while running:

            self.clock.tick(fps.tick)

            for event in pg.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == KEYDOWN:

                    if event.key == K_F1:
                        if not self.NewGame:
                            self.hotKey('rules')

                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_F5:
                        self.hotKey('NewGame')

                    if not self.NewGame:
                        if event.key == K_F2:
                            self.hotKey('pause')

                    if not self.pause and not self.NewGame:
                        if event.key == K_LEFT and not self.pause:
                            self.player.change_x = -self.player.speed

                        elif event.key == K_RIGHT and not self.pause:
                            self.player.change_x = self.player.speed

                        elif event.key == K_UP and not self.pause:
                            self.player.change_y = -self.player.speed

                        elif event.key == K_DOWN and not self.pause:
                            self.player.change_y = self.player.speed

                        elif event.key == K_c and not self.pause:
                            bullet_player = Bullet(x = self.player.rect.centerx,
                                                   y = self.player.rect.centery,
                                                   width = 2,
                                                   height = 10,
                                                   color = (255, 0, 0),
                                                   speed_y =-8)

                            self.bullets_player.add(bullet_player)
                            self.all_sprites.add(bullet_player)

                elif event.type == KEYUP:
                    if event.key == K_LEFT or event.key == K_RIGHT:
                        self.player.change_x = 0

                    elif event.key == K_UP or event.key == K_DOWN:
                        self.player.change_y = 0

            if not self.pause and not self.NewGame:

                self.all_sprites.update()

                for enemy in self.enemies:
                    # if enemy.rect.y < self.player.rect.y:
                    if enemy.rect.x <= self.player.rect.x <= enemy.rect.topright[
                            0] or enemy.rect.x <= self.player.rect.topright[
                            0] <= enemy.rect.topright[0] or enemy.rect.x <= self.player.rect.centerx <= enemy.rect.topright[0]:

                        if not self.boss_level:
                            shot_true = round(self.shots.boss_shot / 2)
                            shot_true = 1 if shot_true == 0 else 1
                            if random.randint(1, self.shots.enemy_shot) == shot_true:
                                
                                enemy_bullet = Bullet(x = enemy.rect.centerx,
                                                    y = enemy.rect.centery,
                                                    width = 2,
                                                    height = 10,
                                                    color = (255, 255, 0),
                                                    speed_y = 5)
                            
                                self.bullets_enemy.add(enemy_bullet)
                                self.all_sprites.add(enemy_bullet)

                        elif self.boss_level:
                            shot_true = round(self.shots.boss_shot / 2)
                            shot_true = 1 if shot_true == 0 else 1
                            if random.randint(1, self.shots.boss_shot) == shot_true:

                                for key, value in self.boss.__dict__.items():
                                    if 'weapon' in key:
                                        enemy_bullet = Bullet(x = value[0],
                                                            y = value[1],
                                                            width = 2,
                                                            height = 10,
                                                            color = (255, 255, 0),
                                                            speed_y = 10)

                                        self.bullets_enemy.add(enemy_bullet)
                                        self.all_sprites.add(enemy_bullet)

                hit_player_bullet = pg.sprite.spritecollide(
                    self.player, self.bullets_enemy, False)
                if hit_player_bullet:

                    for hit in hit_player_bullet:
                        if hit:
                            hit.kill()
                        if hit.rect.y > self.screen_height:
                            hit.kill()
                    levelsGame.live_player -= 1
                    screenGame.change_caption(self.score,
                                              levelsGame.live_player)

                hit_player = pg.sprite.spritecollide(self.player, self.enemies,
                                                     False)
                if hit_player:
                    levelsGame.live_player -= 1
                    screenGame.change_caption(self.score,
                                              levelsGame.live_player,
                                              levelsGame.level_game)
                    for hit in hit_player:
                        hit.change_x *= -1
                        hit.change_y *= -1
                        self.player.change_x *= -1
                        self.player.change_y *= -1

                if levelsGame.live_player <= 0:
                    self.player.kill()
                    self.boss_level = False
                    self.hotKey('NewGame')

                if not self.NewGame:

                    for player_bullet in self.bullets_player:
                        if not self.boss_level:
                            hit_enemies = pg.sprite.spritecollide(
                                player_bullet, self.enemies, True)
                        elif self.boss_level:
                            hit_enemies = pg.sprite.spritecollide(
                                player_bullet, self.enemies, False)

                        if hit_enemies:
                            player_bullet.kill()
                            if not self.boss_level:
                                self.score += 1
                                screenGame.change_caption(
                                    self.score, levelsGame.live_player,
                                    levelsGame.level_game)
                            elif self.boss_level:
                                self.boss.boss_live -= 1
                                screenGame.change_caption(
                                    self.score,
                                    levelsGame.live_player,
                                    levelsGame.level_game,
                                    self.boss.boss_live,
                                    boss = True)
                                if self.boss.boss_live <= 0:
                                    self.boss.kill()
                                    self.boss_level = False
                                    levelsGame.live_player += 5
                                    self.all_sprites.empty()
                                    self.enemies.empty()
                                    self.setup(True)

                        if player_bullet.rect.y < 0:
                            player_bullet.kill()


                    levelsGame.change_levels(self.score)

                    if levelsGame.old_boss < levelsGame.boss:
                        self.boss_level = True
                        levelsGame.old_boss = levelsGame.boss
                        self.all_sprites.empty()
                        self.enemies.empty()
                        self.setup(True)

                    if len(self.enemies) == 0 and not self.boss_level:
                        self.setup(False)
                    

                    screenGame.change_background(1)
                    # self.screen.blit(self.background, (0, 0))
                    self.all_sprites.draw(self.screen)

                pg.display.update()

        pg.quit()

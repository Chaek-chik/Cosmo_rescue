#модуль инициализации. вызов импортов модулей и создание всех классов для программы

import random
from classes.ScreenGame import ScreenGame
from classes.LevelsGame import LevelsGame
from classes.Fps import Fps
from classes.ShowText import ShowText
from classes.Shots import Shots

from boss_weapon_list import BossWeapon

screenGame = ScreenGame(1024, 768)
levelsGame = LevelsGame()
fps = Fps(60)
bossWeapon = BossWeapon()
shots = Shots()
showText = ShowText(screenGame.screen)

ENEMY_SHOT = 1
BOSS_SHOT = 1

shots.change_freq(enemy_shot = ENEMY_SHOT, boss_shot = BOSS_SHOT)


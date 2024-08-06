from random import randint

class Shots:
    def __init__(self, enemy_shot = 1, boss_shot = 1):
        self.enemy_shot = enemy_shot
        self.boss_shot = boss_shot

    def change_freq(self, enemy_shot, boss_shot):
        self.enemy_shot = enemy_shot
        self.boss_shot = boss_shot
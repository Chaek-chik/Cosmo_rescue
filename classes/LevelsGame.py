class LevelsGame:
    def __init__(self):
        self.old_score = 0
        self.live_player = 5
        self.level_game = 0
        self.enemies = 10
        self.boss = 0
        self.old_boss = 0

    def change_levels(self, score = 0):
        if score - self.old_score == 10:
            self.live_player += 1
            self.enemies += 2
            self.level_game += 1
            self.old_score = score
        if score // 50 > self.boss:
            self.boss += 1   
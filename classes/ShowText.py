# класс для работы с текстом. Для вывода текста на экране паузы, новой игры, и правил игры

import pygame as pg

pg.init()

class ShowText:

    def __init__(self, screen):
        self.scr = screen
        self.width = self.scr.get_width()
        self.height = self.scr.get_height()

        # определение необходимых фонтов для проги
        self.heading = pg.font.SysFont('arial', 38)
        self.text = pg.font.SysFont('arial', 24)
        self.textFiles = pg.font.SysFont('arial', 18)
        self.headingColor = (255, 255, 0)
        self.textColor = (255, 255, 255)
        self.textFilesColor = (255, 255, 255)

    # определение области с фонтами и цветом для вывода на экран
    def txtObjects(self, text, font, color):
        surf = font.render(text, True, color)
        return surf, surf.get_rect()

    # сам текст и его оформление в суфейсе для экрана
    def showText(self,
                 text_heading,
                 text_basic = None,
                 text_file = None,
                 position = 'center'):
        
        # заголовочный текст
        headingSurf, headingRect = self.txtObjects(
            text_heading, self.heading, self.headingColor)
        
        # позиция, топ, центр
        if position == 'top':
            headingRect.center = ((self.width / 2), (50))
        
        elif position == 'center':
            headingRect.center = ((self.width / 2), (self.height / 2))
        self.scr.blit(headingSurf, headingRect)

        if text_basic:
            basicSurf, basicRect = self.txtObjects(
                text_basic, self.text, self.textColor)
            
            if position == 'top':
                basicRect.center = ((self.width / 2), (100))
            
            elif position == 'center':
                basicRect.center = ((self.width / 2), (self.height / 2) + 100)

            self.scr.blit(basicSurf, basicRect)

        # для вывода текста из файла
        if text_file:
            y_pos = 0
            for lines in text_file:
                linesSurf, linesRect = self.txtObjects(
                    lines, self.textFiles, self.textFilesColor)
                linesRect.x = 20
                linesRect.y = 150 + y_pos
                self.scr.blit(linesSurf, linesRect)
                y_pos += 30

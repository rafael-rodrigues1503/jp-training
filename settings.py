import pygame as pg


class Settings:

    def __init__(self):

        self.screen_res = (1360, 768)
        self.card_res = (self.screen_res[0] / 8, self.screen_res[1] / 4)

        # Color settings
        self.color_palette = {
            'screen_bg':         (128,  64,   0),
            'flashcard_normal':  (  0, 128, 255),
            'flashcard_wrong':   (255,   0,   0),
            'flashcard_correct': (128, 255,   0),
            'card_text':         (245, 245, 245),
            'card_input_box':    ( 40,  40,  40)
        }
        self.fonts = {
            'kana':  pg.font.SysFont('Meiryo', 48),
            'input': pg.font.SysFont('Meiryo', 32)
        }

import pygame as pg
from jp_converter import romaji, hiragana


class Flashcard:

    def __init__(self, screen, settings, kana, x, y):
        self.screen = screen
        self.settings = settings
        self.kana = kana
        self.answer = romaji[hiragana.index(kana)]

        self.screen_rect = self.screen.get_rect()
        self.flashcard_state = 'normal'

        # Card
        self.card_rect = pg.Rect(0, 0, self.settings.card_res[0], self.settings.card_res[1])
        self.card_rect.x = x
        self.card_rect.y = y

        # Kana
        self.kana_render = self.settings.fonts['kana'].render(kana, True, self.settings.color_palette['card_text'])
        self.kana_rect = self.kana_render.get_rect()
        self.kana_rect.centerx = self.card_rect.centerx
        self.kana_rect.centery = self.card_rect.y + (self.card_rect.height / 3)

        # Input box
        self.input_box_width = self.settings.card_res[0] - 10
        self.input_box_height = (self.settings.card_res[1] / 3) - 10
        self.input_rect = pg.Rect(0, 0, self.input_box_width, self.input_box_height)
        self.input_rect.centerx = self.card_rect.centerx
        self.input_rect.centery = self.card_rect.y + (self.card_rect.height * 5 / 6)

        # Input text
        self.input_text_active = False
        self.input_text = ''
        self.input_text_render = self.settings.fonts['input'].render(self.input_text,
                                                                     True,
                                                                     self.settings.color_palette['card_text'])
        self.input_text_rect = self.input_text_render.get_rect()
        self.input_text_rect.center = self.input_rect.center

    def write_input(self, char='', backspace=False):
        if backspace:
            self.input_text = self.input_text[:-1]
        elif len(self.input_text) == 3 or self.flashcard_state == 'correct':
            return
        elif char:
            self.input_text += char
        self.input_text_render = self.settings.fonts['input'].render(self.input_text,
                                                                     True,
                                                                     self.settings.color_palette['card_text'])
        self.input_text_rect = self.input_text_render.get_rect()
        self.input_text_rect.center = self.input_rect.center

    def check_valid(self):
        if self.input_text:
            if self.input_text == self.answer:
                self.flashcard_state = 'correct'
            else:
                self.flashcard_state = 'wrong'

    def draw_flashcard(self):
        self.screen.fill(self.settings.color_palette['flashcard_' + self.flashcard_state], self.card_rect)
        self.screen.blit(self.kana_render, self.kana_rect)
        self.screen.fill(self.settings.color_palette['card_input_box'], self.input_rect)
        self.screen.blit(self.input_text_render, self.input_text_rect)

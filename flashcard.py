import pygame as pg
from pygame.sprite import Sprite


class Flashcard(Sprite):

    def __init__(self, screen, settings, kana):
        super().__init__()

        self.screen = screen
        self.settings = settings
        self.screen_rect = self.screen.get_rect()
        self.flashcard_state = 'normal'

        # Card
        self.card_width, self.card_height = self.settings.screen_width / 8, self.settings.screen_height / 4
        self.card_rect = pg.Rect(0, 0, self.card_width, self.card_height)
        self.card_rect.centerx = self.screen_rect.centerx / 8
        self.card_rect.centery = self.screen_rect.centery / 3

        # Kana
        self.kana_render = self.settings.fonts['kana'].render(kana, True, self.settings.color_palette['card_text'])
        self.kana_rect = self.kana_render.get_rect()
        self.kana_rect.centerx = self.card_rect.centerx
        self.kana_rect.centery = self.card_rect.y + (self.card_rect.height / 3)

        # Input box
        self.input_box_width, self.input_box_height = self.card_width - 10, (self.card_height / 3) - 10
        self.input_rect = pg.Rect(0, 0, self.input_box_width, self.input_box_height)
        self.input_rect.centerx = self.card_rect.centerx
        self.input_rect.centery = self.card_rect.y + (self.card_rect.height * 5 / 6)

        # Input text
        self.text_input_active = False
        self.input_text = ''
        self.input_text_render = self.settings.fonts['input'].render(self.input_text, True, self.settings.color_palette['card_text'])
        self.input_text_rect = self.input_text_render.get_rect()
        self.input_text_rect.center = self.input_rect.center

    def move_card(self, x_move=0, y_move=0):
        for rect in self.card_rect, self.kana_rect, self.input_rect, self.input_text_rect:
            rect.x += x_move
            rect.y += y_move

    def write_input(self, char):
        self.input_text += char
        self.input_text_render = self.settings.fonts['input'].render(self.input_text, True, self.settings.color_palette['card_text'])
        self.input_text_rect = self.input_text_render.get_rect()
        self.input_text_rect.center = self.input_rect.center

    def draw_flashcard(self):
        self.screen.fill(self.settings.color_palette['flashcard_' + self.flashcard_state], self.card_rect)
        self.screen.blit(self.kana_render, self.kana_rect)
        self.screen.fill(self.settings.color_palette['card_input_box'], self.input_rect)
        self.screen.blit(self.input_text_render, self.input_text_rect)

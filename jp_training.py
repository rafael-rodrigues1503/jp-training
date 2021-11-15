import pygame as pg
import sys
from settings import Settings
from jp_converter import convert
from flashcard import Flashcard


class JpTraining:

    def __init__(self):
        pg.init()
        self.settings = Settings()

        self.screen = pg.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pg.display.set_caption("JP Training")

        self.flashcards = pg.sprite.Group()
        n = 0
        d = {'あ': 'a', 'い': 'i', 'う': 'u', 'え': 'e', 'お': 'o'}
        for kana in d:
            flashcard = Flashcard(self.screen, self.settings, kana)
            flashcard.write_input(d[kana])
            flashcard.move_card((n + 1) * (flashcard.card_width + 15))
            self.flashcards.add(flashcard)
            n += 1


    def run_game(self):
        while True:
            self.check_events()
            self.update_screen()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = pg.mouse.get_pos()

                for flashcard in self.flashcards:
                    if flashcard.input_rect.collidepoint(mouse_pos):
                        flashcard.text_input_active = True
                        break

    def update_screen(self):
        self.screen.fill(self.settings.color_palette['screen_bg'])
        for flashcard in self.flashcards:
            flashcard.draw_flashcard()
        pg.display.flip()


if __name__ == '__main__':
    jpt = JpTraining()
    jpt.run_game()

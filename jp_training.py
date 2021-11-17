import pygame
import pygame as pg
import sys
from settings import Settings
from flashcard import Flashcard
import random
from jp_converter import hiragana


class JpTraining:

    def __init__(self):
        pg.init()
        self.settings = Settings()

        self.screen = pg.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pg.display.set_caption("JP Training")

        self.flashcards = pg.sprite.Group()
        self.active_flashcard = None

        self.create_cards()

    def run_game(self):
        while True:
            self.check_events()
            self.update_screen()

    def check_events(self):
        # TODO: Make Tab/Shift+Tab move to next/previous card, respectively

        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()

            elif self.active_flashcard:
                if event.type == pg.MOUSEBUTTONDOWN:
                    mouse_pos = pg.mouse.get_pos()

                    if not self.active_flashcard.input_rect.collidepoint(mouse_pos):
                        self.active_flashcard.check_valid()
                        self.active_flashcard.text_input_active = False
                        self.active_flashcard = None

                        for flashcard in self.flashcards:
                            if flashcard.input_rect.collidepoint(mouse_pos):
                                self.active_flashcard = flashcard
                                flashcard.text_input_active = True
                                break

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                        self.active_flashcard.check_valid()
                        self.active_flashcard.text_input_active = False
                        self.active_flashcard = None
                    elif event.key == pygame.K_BACKSPACE:
                        self.active_flashcard.write_input('')
                    else:
                        self.active_flashcard.write_input(event.unicode)

            elif event.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = pg.mouse.get_pos()

                for flashcard in self.flashcards:
                    if flashcard.input_rect.collidepoint(mouse_pos):
                        self.active_flashcard = flashcard
                        flashcard.text_input_active = True
                        break

    def update_screen(self):
        self.screen.fill(self.settings.color_palette['screen_bg'])
        for flashcard in self.flashcards:
            flashcard.draw_flashcard()
        pg.display.flip()

    def create_cards(self):
        available_space_x = self.settings.screen_width * 0.95
        num_cards_x = int(available_space_x // (self.settings.card_width + 20))

        available_space_y = self.settings.screen_height * 0.95
        num_cards_y = int(available_space_y // (self.settings.card_height + 20))

        hira = random.sample(hiragana, num_cards_x * num_cards_y)
        for row in range(num_cards_y):
            for col in range(num_cards_x):
                card_x = 50 + (self.settings.card_width + 50) * col
                card_y = 50 + (self.settings.card_height + 50) * row

                chosen_hira = hira.pop()
                card = Flashcard(self.screen, self.settings, chosen_hira, card_x, card_y)
                self.flashcards.add(card)


if __name__ == '__main__':
    jpt = JpTraining()
    jpt.run_game()

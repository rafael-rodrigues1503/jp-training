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

        self.screen = pg.display.set_mode(self.settings.screen_res)
        pg.display.set_caption("JP Training")

        self.flashcards = []
        self.active_flashcard = None
        self.create_cards()

        self.run_game()

    def run_game(self):
        while True:
            self.check_events()
            self.update_screen()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()

            elif self.active_flashcard:
                if event.type == pg.MOUSEBUTTONDOWN:
                    mouse_pos = pg.mouse.get_pos()

                    if not self.active_flashcard.input_rect.collidepoint(mouse_pos):
                        self.active_flashcard.check_valid()
                        self.active_flashcard = None

                        for flashcard in self.flashcards:
                            if flashcard.input_rect.collidepoint(mouse_pos):
                                self.active_flashcard = flashcard
                                break

                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN or event.key == pg.K_KP_ENTER:
                        self.active_flashcard.check_valid()
                        self.active_flashcard = None
                    elif event.key == pg.K_TAB:
                        card_states = [False if card.flashcard_state == 'correct' else True for card in self.flashcards]
                        self.active_flashcard.check_valid()

                        i = self.flashcards.index(self.active_flashcard)
                        if pg.key.get_pressed()[pg.K_LSHIFT]:
                            while i != 0:
                                i -= 1
                                if card_states[i]:
                                    break
                        else:
                            while i != len(card_states) - 1:
                                i += 1
                                if card_states[i]:
                                    break

                        self.active_flashcard = self.flashcards[i]

                    elif event.key == pg.K_BACKSPACE:
                        self.active_flashcard.write_input(backspace=True)
                    else:
                        self.active_flashcard.write_input(char=event.unicode)

            elif event.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = pg.mouse.get_pos()

                for flashcard in self.flashcards:
                    if flashcard.input_rect.collidepoint(mouse_pos):
                        self.active_flashcard = flashcard
                        break

    def update_screen(self):
        self.screen.fill(self.settings.color_palette['screen_bg'])
        for flashcard in self.flashcards:
            flashcard.draw_flashcard()
        pg.display.flip()

    def create_cards(self):
        num_cards_x = int((self.settings.screen_res[0] - 100) // (self.settings.card_res[0] + 20))
        num_cards_y = int((self.settings.screen_res[1] - 100) // (self.settings.card_res[1] + 20))

        space_x = 35
        space_y = 60
        x_start = 0.5 * (self.settings.screen_res[0] - num_cards_x * (self.settings.card_res[0] + space_x) + space_x)
        y_start = 0.5 * (self.settings.screen_res[1] - num_cards_y * (self.settings.card_res[1] + space_y) + space_y)

        hira = random.sample(hiragana, num_cards_x * num_cards_y)
        card_index = 0

        for row in range(num_cards_y):
            card_y = y_start + (self.settings.card_res[1] + space_y) * row

            for col in range(num_cards_x):
                card_x = x_start + (self.settings.card_res[0] + space_x) * col

                chosen_hira = hira.pop()
                card = Flashcard(self.screen, self.settings, chosen_hira, card_x, card_y)
                self.flashcards.append(card)

                card_index += 1


if __name__ == '__main__':
    JpTraining()

# TODO: Let player choose which kana will appear
# TODO: Implement katakana
# TODO: Add scrolling up/down

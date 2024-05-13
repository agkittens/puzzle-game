
import pygame as pg
from constants import *


class Window:
    def __init__(self):
        pg.init()

        self.window_size = (WIDTH, HEIGHT)
        self.window = pg.display.set_mode(self.window_size)
        pg.display.set_caption("Sliding Puzzles")

        self.bg_image = pg.image.load(BACKGROUND)
        self.bg_image = pg.transform.scale(self.bg_image, self.window_size)

        self.buttons = {}
        self.view = 'menu'
        self.slider_active = False
        self.imgs = []

    def draw_buttons(self, rect: pg.Rect, name = 'Start'):
        pg.draw.rect(self.window,BUTTON_COLOR,rect, border_radius=10)
        font = pg.font.Font(None, 28)
        text_surface = font.render(name, True, 'white')
        text_rect = text_surface.get_rect(center=rect.center)
        self.window.blit(text_surface, text_rect)

    def create_buttons(self):
        start_button = pg.Rect(310, 400, 150, 45)
        self.buttons['start'] = [start_button, False]

        collection_button = pg.Rect(310, 480, 150, 45)
        self.buttons['collection'] = [collection_button, False]

        exit_button = pg.Rect(310, 560, 150, 45)
        self.buttons['exit'] = [exit_button, False]

    def create_collection_options(self):
        load_image = pg.Rect(550,250,100,100)
        self.buttons['load'] = [load_image, False]

        X_button = pg.Rect(700,20,30,30)
        self.buttons['x'] = [X_button, False]

        puzzle1 = pg.image.load(PUZZLE1)
        puzzle1 = pg.transform.scale(puzzle1, (100, 100))
        puzzle1_button = pg.Rect(100,250,100,100)
        self.buttons['puzzle1'] = [puzzle1_button, False]

        puzzle2 = pg.image.load(PUZZLE2)
        puzzle2 = pg.transform.scale(puzzle2, (100, 100))
        puzzle2_button = pg.Rect(250,250,100,100)
        self.buttons['puzzle2'] = [puzzle2_button, False]

        puzzle3 = pg.image.load(PUZZLE3)
        puzzle3 = pg.transform.scale(puzzle3, (100, 100))
        puzzle3_button = pg.Rect(400,250,100,100)
        self.buttons['puzzle3'] = [puzzle3_button, False]

        puzzle4 = pg.image.load(PUZZLE4)
        puzzle4 = pg.transform.scale(puzzle4, (100, 100))
        puzzle4_button = pg.Rect(100,400,100,100)
        self.buttons['puzzle4'] = [puzzle4_button, False]

        puzzle5 = pg.image.load(PUZZLE5)
        puzzle5 = pg.transform.scale(puzzle5, (100, 100))
        puzzle5_button = pg.Rect(250,400,100,100)
        self.buttons['puzzle5'] = [puzzle5_button, False]

        puzzle6 = pg.image.load(PUZZLE6)
        puzzle6 = pg.transform.scale(puzzle6, (100, 100))
        puzzle6_button = pg.Rect(400,400,100,100)
        self.buttons['puzzle6'] = [puzzle6_button, False]

        self.imgs = [puzzle1, puzzle2, puzzle3, puzzle4, puzzle5, puzzle6]

    def display_menu_buttons(self):
        self.deactivate_buttons()
        self.activate_buttons(['start', 'collection', 'exit'])
        self.draw_buttons(self.buttons['start'][0])
        self.draw_buttons(self.buttons['collection'][0], name = 'Collection')
        self.draw_buttons(self.buttons['exit'][0], name = 'Exit')

    def display_collection_buttons(self):
        self.deactivate_buttons()
        self.activate_buttons(['load', 'x', 'puzzle1','puzzle2',
                               'puzzle3','puzzle4','puzzle5','puzzle6'])

        self.draw_buttons(self.buttons['load'][0], name = 'Load')
        self.draw_buttons(self.buttons['x'][0], name = 'X')

        self.draw_buttons(self.buttons['puzzle1'][0], name='')
        self.window.blit(self.imgs[0], self.buttons['puzzle1'][0])

        self.draw_buttons(self.buttons['puzzle2'][0], name='')
        self.window.blit(self.imgs[1], self.buttons['puzzle2'][0])

        self.draw_buttons(self.buttons['puzzle3'][0], name='')
        self.window.blit(self.imgs[2], self.buttons['puzzle3'][0])

        self.draw_buttons(self.buttons['puzzle4'][0], name='')
        self.window.blit(self.imgs[3], self.buttons['puzzle4'][0])

        self.draw_buttons(self.buttons['puzzle5'][0], name='')
        self.window.blit(self.imgs[4], self.buttons['puzzle5'][0])

        self.draw_buttons(self.buttons['puzzle6'][0], name='')
        self.window.blit(self.imgs[5], self.buttons['puzzle6'][0])

    def display_game_buttons(self):
        self.deactivate_buttons()
        self.activate_buttons(['x'])
        self.draw_buttons(self.buttons['x'][0], name = 'X')

    def activate_buttons(self, keys: list):
        for key in keys:
            if key in self.buttons.keys():
                self.buttons[key][1] = True

    def deactivate_buttons(self):
        for button in self.buttons.values():
            button[1] = False

    @staticmethod
    def add_rounded_corners(surface, radius):
        width, height = surface.get_size()
        mask = pg.Surface((width, height), pg.SRCALPHA)
        mask.fill((0, 0, 0, 0))
        pg.draw.rect(mask, (255, 255, 255, 255), (0, 0, width, height), border_radius=radius)
        surface.blit(mask, (0, 0), special_flags=pg.BLEND_RGBA_MIN)

    def check_condition(self, key, pos):
        if self.buttons[key][0].collidepoint(pos) and self.buttons[key][1]:
            return True

        else:
            return False

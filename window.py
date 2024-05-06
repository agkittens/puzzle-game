
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
        self.view = 'start'
        self.slider_active = False
        self.selected_img = None

    def draw_buttons(self, rect, name = 'Start'):
        pg.draw.rect(self.window,BUTTON_COLOR,rect, border_radius=10)
        font = pg.font.Font(None, 28)
        text_surface = font.render(name, True, 'white')
        text_rect = text_surface.get_rect(center=rect.center)
        self.window.blit(text_surface, text_rect)

    def create_buttons(self):
        start_button = pg.Rect(310, 400, 150, 45)
        self.buttons['start'] = start_button
        self.draw_buttons(start_button)

        collection_button = pg.Rect(310, 480, 150, 45)
        self.buttons['collection'] = collection_button
        self.draw_buttons(collection_button, name = 'Collection')

        exit_button = pg.Rect(310, 560, 150, 45)
        self.buttons['exit'] = exit_button
        self.draw_buttons(exit_button, name = 'Exit')

    def create_collection_options(self):
        load_image = pg.Rect(550,250,100,100)
        self.buttons['load'] = load_image
        self.draw_buttons(load_image, name = 'Load')

        X_button = pg.Rect(700,20,30,30)
        self.buttons['x'] = X_button
        self.draw_buttons(X_button, name = 'X')

        puzzle1 = pg.image.load(PUZZLE)
        puzzle1 = pg.transform.scale(puzzle1, (100, 100))
        puzzle1_button = pg.Rect(100,250,100,100)
        self.buttons['puzzle1'] = puzzle1_button
        self.draw_buttons(puzzle1_button, name='')
        self.window.blit(puzzle1, puzzle1_button)

        puzzle2 = pg.image.load(PUZZLE)
        puzzle2 = pg.transform.scale(puzzle2, (100, 100))
        puzzle2_button = pg.Rect(250,250,100,100)
        self.buttons['puzzle2'] = puzzle2_button
        self.draw_buttons(puzzle2_button, name='')
        self.window.blit(puzzle2, puzzle2_button)

        puzzle3 = pg.image.load(PUZZLE)
        puzzle3 = pg.transform.scale(puzzle3, (100, 100))
        puzzle3_button = pg.Rect(400,250,100,100)
        self.buttons['puzzle3'] = puzzle3_button
        self.draw_buttons(puzzle3_button, name='')
        self.window.blit(puzzle3, puzzle3_button)

import pygame as pg
import tkinter as tk
from constants import *
from tkinter import filedialog


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
        self.imgs = []
        self.surfaces = []

        self.slider_active = False

        self.font = pg.font.Font(None, 38)
        self.timer_status = False
        self.start_time = 0
        self.time_limit = 15 * 60 * 1000

        self.selected_img = None
        self.create_buttons()
        self.create_collection_options()

    def display_title(self):
        title = pg.image.load(TITLE)
        title_rect = pg.Rect(140, 5, *B_C_SIZE)
        self.window.blit(title, (title_rect.x, title_rect.y))

    def create_buttons(self):
        start_button = pg.Rect(310, 400, *B_M_SIZE)
        self.buttons['start'] = [start_button, False]

        collection_button = pg.Rect(310, 480, *B_M_SIZE)
        self.buttons['collection'] = [collection_button, False]

        exit_button = pg.Rect(310, 560, *B_M_SIZE)
        self.buttons['exit'] = [exit_button, False]

    def create_collection_options(self):
        load_image = pg.Rect(550, 250, *B_C_SIZE)
        self.buttons['load'] = [load_image, False]

        X_button = pg.Rect(700, 20, 30, 30)
        self.buttons['x'] = [X_button, False]

        self.process_image(PUZZLE1)
        self.process_image(PUZZLE2)
        self.process_image(PUZZLE3)
        self.process_image(PUZZLE4)
        self.process_image(PUZZLE5)
        self.process_image(PUZZLE6)

        puzzle1_button = pg.Rect(100, 250, *B_C_SIZE)
        self.buttons['puzzle1'] = [puzzle1_button, False]

        puzzle2_button = pg.Rect(250, 250, *B_C_SIZE)
        self.buttons['puzzle2'] = [puzzle2_button, False]

        puzzle3_button = pg.Rect(400, 250, *B_C_SIZE)
        self.buttons['puzzle3'] = [puzzle3_button, False]

        puzzle4_button = pg.Rect(100, 400, *B_C_SIZE)
        self.buttons['puzzle4'] = [puzzle4_button, False]

        puzzle5_button = pg.Rect(250, 400, *B_C_SIZE)
        self.buttons['puzzle5'] = [puzzle5_button, False]

        puzzle6_button = pg.Rect(400, 400, *B_C_SIZE)
        self.buttons['puzzle6'] = [puzzle6_button, False]

        self.create_slider()

    def process_image(self, name: str):
        puzzle = pg.image.load(name)
        puzzle = pg.transform.scale(puzzle, B_C_SIZE)
        self.imgs.append(puzzle)

    def draw_buttons(self, rect: pg.Rect, name='Start', radius=10, color=BUTTON_COLOR):
        pg.draw.rect(self.window, color, rect, border_radius=radius)
        font = pg.font.Font(None, 28)
        text_surface = font.render(name, True, 'white')
        text_rect = text_surface.get_rect(center=rect.center)
        self.window.blit(text_surface, text_rect)

    def display_menu_buttons(self):
        self.deactivate_buttons()
        self.activate_buttons(['start', 'collection', 'exit'])
        self.draw_buttons(self.buttons['start'][0])
        self.draw_buttons(self.buttons['collection'][0], name='Collection')
        self.draw_buttons(self.buttons['exit'][0], name='Exit')

    def display_collection_buttons(self):
        self.deactivate_buttons()
        self.activate_buttons(['load', 'x', 'puzzle1', 'puzzle2',
                               'puzzle3', 'puzzle4', 'puzzle5', 'puzzle6'])

        self.draw_buttons(self.buttons['load'][0], name='Load')
        self.draw_buttons(self.buttons['x'][0], name='X')

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

        self.draw_buttons(self.buttons['slider'][0], name='', color=SLIDER_COLOR)
        self.draw_buttons(self.buttons['circle'][0], name='', radius=30, color=SLIDER_DOT_COLOR)

    def process_img_display(self, surface, rect):
        mask_rect = surface.get_rect(center=rect.center)
        self.window.blit(surface, mask_rect.topleft)

    def display_game_buttons(self):
        self.deactivate_buttons()
        self.activate_buttons(['x'])
        self.draw_buttons(self.buttons['x'][0], name='X')

    def activate_buttons(self, keys: list):
        for key in keys:
            if key in self.buttons.keys():
                self.buttons[key][1] = True

    def deactivate_buttons(self):
        for button in self.buttons.values():
            button[1] = False

    def check_condition(self, key: str, pos: tuple):
        if self.buttons[key][0].collidepoint(pos) and self.buttons[key][1]:
            return True
        else:
            return False

    def update_pieces(self, puzzle):
        for piece in puzzle.pieces.values():
            self.window.blit(piece[0],
                             (130 + piece[1].left + puzzle.spacing // 2, 130 + piece[1].top + puzzle.spacing // 2))

    def create_slider(self):
        slider = pg.Rect(160, 120, 430, 30)
        self.buttons['slider'] = [slider, False]

        circle = pg.Rect(160, 120, 30, 30)
        self.buttons['circle'] = [circle, False]

    def move_slider_dot(self, pos: tuple):
        if pos[0] in range(160, 430 + 130):
            self.buttons['circle'][0].update((pos[0], 120), (30, 30))

    def define_size(self):
        x = self.buttons['circle'][0].left
        min = 160
        max = 560
        steps = 60

        if x <= min + 20:
            size = 3
        elif x == max:
            size = 9

        else:
            size = x // steps

        return size

    def display_puzzle_icons(self, number: str or None, puzzle):
        if number is not None:
            temp = pg.image.load(number)
            temp = pg.transform.scale(temp, SIZE)
            self.selected_img = temp

        size = self.define_size()
        puzzle.load_puzzle(self.selected_img, size)

    def display_load_window(self, font: pg.font.Font, puzzle):
        folder_window = tk.Tk()
        folder_window.withdraw()
        path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
        if path:
            image = pg.image.load(path)
            folder_window.destroy()
            status = font.render('Loaded', True, 'white')

            image = pg.transform.scale(image, SIZE)
            size = self.define_size()
            puzzle.load_puzzle(image, size)

        else:
            status = font.render('', True, 'white')

        return status

    def display_timer(self, elapsed_time: int):
        remaining_time = max(0, (self.time_limit - elapsed_time) // 1000)
        timer_text = self.font.render(f"Time left: {remaining_time // 60:02}:{remaining_time % 60:02}",
                                      True,
                                      '#e13aed')

        self.window.blit(timer_text, (280, 50))

    def display_size_info(self, size: int):
        size_text = self.font.render(f"Size: {size}x{size}", True, '#e13aed')
        self.window.blit(size_text, (320, 70))

    def display_win_info(self, size: tuple):
        win_rect = pg.Rect(100, 100, *size)
        self.draw_buttons(win_rect, 'You won!', 20, BG_SURFACE_COLOR)

    @staticmethod
    def add_rounded_corners(surface: pg.Surface, radius: int):
        width, height = surface.get_size()
        mask = pg.Surface((width, height), pg.SRCALPHA)
        mask.fill((0, 0, 0, 0))
        pg.draw.rect(mask, (255, 255, 255, 255), (0, 0, width, height), border_radius=radius)
        surface.blit(mask, (0, 0), special_flags=pg.BLEND_RGBA_MIN)

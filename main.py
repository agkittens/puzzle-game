from tkinter import filedialog
import sys
import tkinter as tk
from window import *
from puzzle import *

temp = pg.image.load(PUZZLE1)
temp = pg.transform.scale(temp, (500, 500))

window = Window()
puzzle = Puzzle(temp, 3)
font = pg.font.Font(None, 28)
status = font.render('', True, 'white')

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

        elif event.type == pg.MOUSEBUTTONDOWN:

            if window.check_condition('start', event.pos):
                window.view = 'game'

            elif window.check_condition('collection', event.pos):
                window.view = 'collection'

            elif window.check_condition('exit', event.pos):
                pg.quit()
                sys.exit()

            elif window.check_condition('x', event.pos):
                window.view = 'menu'
                status = font.render('', True, 'white')

            elif window.check_condition('load', event.pos):
                folder_window = tk.Tk()
                folder_window.withdraw()
                path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
                if path:
                    image = pg.image.load(path)
                    folder_window.destroy()
                    status = font.render('Loaded', True, 'white')

                    image = pg.transform.scale(image, (500, 500))
                    puzzle.load_puzzle(image)

                else:
                    status = font.render('', True, 'white')

            elif window.check_condition('puzzle1', event.pos):
                temp = pg.image.load(PUZZLE1)
                temp = pg.transform.scale(temp, (500, 500))
                puzzle.load_puzzle(temp)

            elif window.check_condition('puzzle2', event.pos):
                temp = pg.image.load(PUZZLE2)
                temp = pg.transform.scale(temp, (500, 500))
                puzzle.load_puzzle(temp)

            elif window.check_condition('puzzle3', event.pos):
                temp = pg.image.load(PUZZLE3)
                temp = pg.transform.scale(temp, (500, 500))
                puzzle.load_puzzle(temp)

            elif window.check_condition('puzzle4', event.pos):
                temp = pg.image.load(PUZZLE4)
                temp = pg.transform.scale(temp, (500, 500))
                puzzle.load_puzzle(temp)

            elif window.check_condition('puzzle5', event.pos):
                temp = pg.image.load(PUZZLE5)
                temp = pg.transform.scale(temp, (500, 500))
                puzzle.load_puzzle(temp)

            elif window.check_condition('puzzle6', event.pos):
                temp = pg.image.load(PUZZLE6)
                temp = pg.transform.scale(temp, (500, 500))
                puzzle.load_puzzle(temp)

            if window.view == 'game':
                puzzle.click_piece(event.pos)

    window.window.blit(window.bg_image, (0, 0))
    window.create_buttons()
    window.create_collection_options()

    # buttons
    if window.view == 'menu':
        window.display_menu_buttons()
        window.display_title()

    elif window.view == 'game':
        window.display_game_buttons()
        colored_surface = pg.Surface((puzzle.puzzle_w_h * 3 + puzzle.spacing * 3 + 37,
                                      puzzle.puzzle_w_h * 3 + puzzle.spacing * 3 + 37), pg.SRCALPHA)

        colored_surface.fill((61, 155, 179))
        window.add_rounded_corners(colored_surface, 20)
        window.window.blit(colored_surface, (100, 100))

        window.update_pieces(puzzle)

    elif window.view == 'collection':
        window.display_collection_buttons()
        window.window.blit(status, (565, 360))

    pg.display.update()

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
            if window.buttons['start'].collidepoint(event.pos):
                window.view = 'game'

            elif window.buttons['collection'].collidepoint(event.pos):
                window.view = 'collection'

            elif window.buttons['exit'].collidepoint(event.pos):
                pg.quit()
                sys.exit()

            elif window.buttons['x'].collidepoint(event.pos):
                window.view = 'menu'
                status = font.render('', True, 'white')

            elif window.buttons['load'].collidepoint(event.pos):
                folder_window = tk.Tk()
                folder_window.withdraw()
                path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
                if path:
                    image = pg.image.load(path)
                    window.selected_img = image
                    folder_window.destroy()
                    status = font.render('Loaded', True, 'white')

                else: status = font.render('', True, 'white')

            elif window.buttons['puzzle1'].collidepoint(event.pos):
                temp = pg.image.load(PUZZLE1)
                temp = pg.transform.scale(temp, (500, 500))
                puzzle.load_puzzle(temp)

            elif window.buttons['puzzle2'].collidepoint(event.pos):
                temp = pg.image.load(PUZZLE2)
                temp = pg.transform.scale(temp, (500, 500))
                puzzle.load_puzzle(temp)

            elif window.buttons['puzzle3'].collidepoint(event.pos):
                temp = pg.image.load(PUZZLE3)
                temp = pg.transform.scale(temp, (500, 500))
                puzzle.load_puzzle(temp)

            elif window.buttons['puzzle4'].collidepoint(event.pos):
                temp = pg.image.load(PUZZLE4)
                temp = pg.transform.scale(temp, (500, 500))
                puzzle.load_puzzle(temp)

            elif window.buttons['puzzle5'].collidepoint(event.pos):
                temp = pg.image.load(PUZZLE5)
                temp = pg.transform.scale(temp, (500, 500))
                puzzle.load_puzzle(temp)

            elif window.buttons['puzzle6'].collidepoint(event.pos):
                temp = pg.image.load(PUZZLE6)
                temp = pg.transform.scale(temp, (500, 500))
                puzzle.load_puzzle(temp)


    window.window.blit(window.bg_image, (0,0))

    #buttons
    if window.view == 'menu':
        window.create_buttons()

    elif window.view == 'game':
        window.create_game_buttons()
        colored_surface = pg.Surface((puzzle.puzzle_w_h*3+puzzle.spacing*3+37,
                                      puzzle.puzzle_w_h*3+puzzle.spacing*3+37))

        colored_surface.fill((25, 34, 51))
        window.window.blit(colored_surface, (100, 100))

        for piece in puzzle.pieces:
            window.window.blit(piece[0],
                        (130+ piece[1].left + puzzle.spacing // 2, 130 +piece[1].top + puzzle.spacing // 2))



    elif window.view == 'collection':
        window.create_collection_options()
        window.window.blit(status, (565, 360))

    pg.display.update()

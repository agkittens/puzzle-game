import sys
from window import *
from puzzle import *

temp = pg.image.load(PUZZLE1)
temp = pg.transform.scale(temp, (500, 500))

window = Window()
window.selected_img = temp
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
                status = window.display_load_window(font, puzzle)

            elif window.check_condition('puzzle1', event.pos):
                window.display_puzzle_icons(PUZZLE1, puzzle)

            elif window.check_condition('puzzle2', event.pos):
                window.display_puzzle_icons(PUZZLE2, puzzle)

            elif window.check_condition('puzzle3', event.pos):
                window.display_puzzle_icons(PUZZLE3, puzzle)

            elif window.check_condition('puzzle4', event.pos):
                window.display_puzzle_icons(PUZZLE4, puzzle)

            elif window.check_condition('puzzle5', event.pos):
                window.display_puzzle_icons(PUZZLE5, puzzle)

            elif window.check_condition('puzzle6', event.pos):
                window.display_puzzle_icons(PUZZLE6, puzzle)

            if window.view == 'game':
                puzzle.click_piece(event.pos)

            if window.view == 'collection':
                if window.buttons['circle'][0].collidepoint(event.pos):
                    window.slider_active = True


        elif event.type == pg.MOUSEBUTTONUP:
            if window.view == 'collection':
                window.slider_active = False
                window.display_puzzle_icons(None, puzzle)

        elif event.type == pg.MOUSEMOTION:
            if window.view == 'collection':
                if window.slider_active:
                    window.move_slider_dot(event.pos)


    window.window.blit(window.bg_image, (0, 0))

    # buttons
    if window.view == 'menu':
        window.display_menu_buttons()
        window.display_title()

    elif window.view == 'game':
        window.display_game_buttons()
        colored_surface = pg.Surface((puzzle.puzzle_w_h * puzzle.size + puzzle.spacing * puzzle.size,
                                      puzzle.puzzle_w_h * puzzle.size + puzzle.spacing * puzzle.size),
                                      pg.SRCALPHA)

        colored_surface.fill((61, 155, 179))
        window.add_rounded_corners(colored_surface, 20)
        window.window.blit(colored_surface, (100, 100))

        window.update_pieces(puzzle)

    elif window.view == 'collection':
        window.display_collection_buttons()
        window.window.blit(status, (565, 360))

    pg.display.update()

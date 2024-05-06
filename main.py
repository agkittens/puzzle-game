from tkinter import filedialog
import sys
import tkinter as tk
from window import *


window = Window()
font = pg.font.Font(None, 28)
status = font.render('', True, 'white')

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        elif event.type == pg.MOUSEBUTTONDOWN:
            if window.buttons['start'].collidepoint(event.pos):pass

            elif window.buttons['collection'].collidepoint(event.pos):
                window.view = 'collection'

            elif window.buttons['exit'].collidepoint(event.pos):
                pg.quit()
                sys.exit()

            elif window.buttons['x'].collidepoint(event.pos):
                window.view = 'start'
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


    window.window.blit(window.bg_image, (0,0))

    #buttons
    if window.view == 'start':
        window.create_buttons()

    elif window.view == 'collection':
        window.create_collection_options()
        window.window.blit(status, (565, 360))

    pg.display.update()

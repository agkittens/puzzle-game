import pygame as pg


class Puzzle:
    def __init__(self,img, size):
        self.object = img
        self.size = size
        self.puzzle_w_h = self.object.get_width() // self.size
        self.spacing = 7

        self.pieces = self.cut_to_pieces()

    def load_puzzle(self,img):
        self.object = img

    def cut_to_pieces(self):
        pieces = []

        width = height = self.puzzle_w_h

        for i in range(self.size):
            for j in range(self.size):
                piece_rect = pg.Rect(j * width, i * height, width,
                                     height)
                piece_surface = pg.Surface((width - self.spacing, height - self.spacing))
                piece_surface.blit(self.object, (0, 0), piece_rect)
                pieces.append((piece_surface, piece_rect))
        return pieces

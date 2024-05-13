import random

import pygame as pg


class Puzzle:
    def __init__(self,img, size):
        self.object = img
        self.size = size
        self.puzzle_w_h = self.object.get_width() // self.size
        self.spacing = 7

        self.pieces = self.cut_to_pieces()
        self.prev_puzzle = None
        self.next_puzzle = None

    def load_puzzle(self,img):
        self.object = img
        self.pieces = self.cut_to_pieces()

    def cut_to_pieces(self):
        pieces = []
        rects = []
        img_pieces = []
        width = height = self.puzzle_w_h
        surfaces = [pg.Surface((width - self.spacing, height - self.spacing)) for _ in range(9)]

        for i in range(self.size):
            for j in range(self.size):
                piece_rect = pg.Rect(j * width, i * height, width, height)
                rects.append(piece_rect)
                img_pieces.append(self.object.subsurface(piece_rect))

        random.shuffle(rects)
        random.shuffle(img_pieces)

        for idx, rect in enumerate(rects):
            surfaces[idx].blit(img_pieces[idx],(0,0))
            pieces.append((surfaces[idx], rect))

        return pieces

    def check_click(self, pos):
        for idx, piece in enumerate(self.pieces):
            if piece[1].collidepoint(pos):
                return True, idx
        return False, None

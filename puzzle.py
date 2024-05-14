import random

import pygame as pg


class Puzzle:
    def __init__(self, img, size: int):
        self.object = img
        self.size = size
        self.puzzle_w_h = self.object.get_width() // self.size
        self.spacing = 7
        self.offset = 130

        self.img_pieces = []
        self.pieces = self.cut_to_pieces()
        self.selected_puzzle = None
        self.next_puzzle = None


    def load_puzzle(self, img,size):
        self.object = img
        self.img_pieces = []
        self.update_size_params(size)
        self.selected_puzzle = None
        self.next_puzzle = None
        self.pieces = self.cut_to_pieces()

    def update_size_params(self,size):
        self.size = size
        self.puzzle_w_h = self.object.get_width() // self.size

    def cut_to_pieces(self):
        pieces = {}
        rects = []
        width = height = self.puzzle_w_h
        surfaces = [pg.Surface((width - self.spacing, height - self.spacing)) for _ in range(self.size**2)]
        for i in range(self.size):
            for j in range(self.size):
                piece_rect = pg.Rect(j * width, i * height, width, height)
                rects.append(piece_rect)

                self.img_pieces.append(self.object.subsurface(piece_rect))

        random.shuffle(self.img_pieces)

        for idx, rect in enumerate(rects):
            column = idx % self.size
            row = idx // self.size
            surfaces[idx].blit(self.img_pieces[idx], (0, 0))
            pieces[idx] = [surfaces[idx], rect, [row, column]]

        return pieces

    def click_piece(self, pos: tuple):
        if self.selected_puzzle is None:
            self.selected_puzzle = self.remember_piece(pos)
            self.next_puzzle = None

        elif self.selected_puzzle is not None:
            self.next_puzzle = self.remember_piece(pos)

        if self.selected_puzzle is not None and self.next_puzzle is not None:
            self.move_pieces()
            self.selected_puzzle = None

    def remember_piece(self, pos: tuple):
        for key, piece in self.pieces.items():
            if piece[1].collidepoint(pos[0] - self.offset, pos[1] - self.offset):
                return piece[2], key

    def move_pieces(self):
        key_s = self.selected_puzzle[1]
        key_n = self.next_puzzle[1]

        row_s, col_s = self.selected_puzzle[0]
        row_n, col_n = self.next_puzzle[0]

        if abs(row_s - row_n) + abs(col_s - col_n) == 1:

            temp = self.img_pieces[key_s]
            self.pieces[key_s][0].blit(self.img_pieces[key_n], (0, 0))
            self.pieces[key_n][0].blit(self.img_pieces[key_s], (0, 0))

            self.img_pieces[key_s] = self.img_pieces[key_n]
            self.img_pieces[key_n] = temp


# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 21:36:38 2024

@author: the great Arpita
"""

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

# src/game.py
import numpy as np

class Game2048:
    def __init__(self):
        self.board = np.zeros((4, 4), dtype=int)
        self.score = 0
        self.add_new_tile()
        self.add_new_tile()

    def add_new_tile(self):
        empty_tiles = [(i, j) for i in range(4) for j in range(4) if self.board[i, j] == 0]
        if empty_tiles:
            i, j = empty_tiles[np.random.randint(0, len(empty_tiles))]
            self.board[i, j] = 2 if np.random.rand() < 0.9 else 4

    def move_left(self):
        moved = False
        for i in range(4):
            new_row = [x for x in self.board[i] if x != 0]
            new_row += [0] * (4 - len(new_row))
            for j in range(3):
                if new_row[j] == new_row[j + 1] and new_row[j] != 0:
                    new_row[j] *= 2
                    new_row[j + 1] = 0
                    self.score += new_row[j]
                    moved = True
            new_row = [x for x in new_row if x != 0]
            new_row += [0] * (4 - len(new_row))
            if not np.array_equal(self.board[i], new_row):
                moved = True
            self.board[i] = new_row
        if moved:
            self.add_new_tile()
        return moved

    def move_right(self):
        self.board = np.fliplr(self.board)
        moved = self.move_left()
        self.board = np.fliplr(self.board)
        return moved

    def move_up(self):
        self.board = self.board.T
        moved = self.move_left()
        self.board = self.board.T
        return moved

    def move_down(self):
        self.board = np.flipud(self.board.T)
        moved = self.move_left()
        self.board = np.flipud(self.board.T)
        return moved

    def is_game_over(self):
        if not any(0 in row for row in self.board):
            for i in range(4):
                for j in range(3):
                    if self.board[i][j] == self.board[i][j + 1] or self.board[j][i] == self.board[j + 1][i]:
                        return False
            return True
        return False

    def get_valid_moves(self):
        moves = []
        if self.move_left():
            moves.append('left')
            self.move_right()  # revert
        if self.move_right():
            moves.append('right')
            self.move_left()  # revert
        if self.move_up():
            moves.append('up')
            self.move_down()  # revert
        if self.move_down():
            moves.append('down')
            self.move_up()  # revert
        return moves

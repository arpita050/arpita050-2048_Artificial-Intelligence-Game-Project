# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 21:36:48 2024

@author: the great Arpita
"""

# src/alpha_beta.py
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

import copy
from game import Game2048

class AlphaBetaAI:
    def __init__(self, game):
        self.game = game

    def get_best_move(self, depth):
        def max_value(board, alpha, beta, depth):
            if depth == 0 or board.is_game_over():
                return self.evaluate(board)
            v = float('-inf')
            for move in board.get_valid_moves():
                new_board = copy.deepcopy(board)
                getattr(new_board, f"move_{move}")()
                v = max(v, min_value(new_board, alpha, beta, depth - 1))
                if v >= beta:
                    return v
                alpha = max(alpha, v)
            return v

        def min_value(board, alpha, beta, depth):
            if depth == 0 or board.is_game_over():
                return self.evaluate(board)
            v = float('inf')
            for move in board.get_valid_moves():
                new_board = copy.deepcopy(board)
                getattr(new_board, f"move_{move}")()
                v = min(v, max_value(new_board, alpha, beta, depth - 1))
                if v <= alpha:
                    return v
                beta = min(beta, v)
            return v

        best_score = float('-inf')
        best_move = None
        for move in self.game.get_valid_moves():
            new_board = copy.deepcopy(self.game)
            getattr(new_board, f"move_{move}")()
            score = min_value(new_board, float('-inf'), float('inf'), depth - 1)
            if score > best_score:
                best_score = score
                best_move = move
        return best_move

    def evaluate(self, board):
        # Implement a heuristic evaluation function for the board state
        return np.sum(board.board)

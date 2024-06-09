# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 21:36:57 2024

@author: the great Arpita
"""
# src/fuzzy_logic.py
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from game import Game2048

class FuzzyLogicAI:
    def __init__(self, game):
        self.game = game

    def get_best_move(self):
        # Implement fuzzy logic for decision making
        # For simplicity, we'll use a very basic rule-based approach
        def evaluate(board):
            score = 0
            for i in range(4):
                for j in range(4):
                    if board.board[i][j] != 0:
                        score += board.board[i][j]
            return score

        best_score = float('-inf')
        best_move = None
        for move in self.game.get_valid_moves():
            new_board = copy.deepcopy(self.game)
            getattr(new_board, f"move_{move}")()
            score = evaluate(new_board)
            if score > best_score:
                best_score = score
                best_move = move
        return best_move

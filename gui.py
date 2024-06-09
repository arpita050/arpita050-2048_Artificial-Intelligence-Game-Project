# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 21:37:13 2024

@author: the great Arpita
"""

import pygame
from game import Game2048

class GUI:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((400, 500))
        self.game = Game2048()
        self.font = pygame.font.Font(None, 36)
        self.colors = {0: (205, 193, 180), 2: (238, 228, 218), 4: (237, 224, 200),
                       8: (242, 177, 121), 16: (245, 149, 99), 32: (246, 124, 95),
                       64: (246, 94, 59), 128: (237, 207, 114), 256: (237, 204, 97),
                       512: (237, 200, 80), 1024: (237, 197, 63), 2048: (237, 194, 46)}
        self.background = pygame.transform.scale(pygame.image.load("background.jpeg"), (400, 500))  # Load and scale background image

    def draw_board(self):
        self.screen.fill((187, 173, 160))
        for i in range(4):
            for j in range(4):
                value = self.game.board[i][j]
                color = self.colors.get(value, (60, 58, 50))
                pygame.draw.rect(self.screen, color, (j * 100 + 10, i * 100 + 10, 80, 80))
                if value != 0:
                    text = self.font.render(str(value), True, (0, 0, 0))
                    text_rect = text.get_rect(center=(j * 100 + 50, i * 100 + 50))
                    self.screen.blit(text, text_rect)

    def draw_menu(self):
        self.screen.blit(self.background, (0, 0))  # Draw background image

        modes = [("A", "Alpha-Beta Pruning"), ("F", "Fuzzy Logic"), ("G", "Genetic Algorithm")]
        colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
        positions = [(200, 100), (200, 250), (200, 400)]  # Adjust the positions for vertical layout

        for (key, mode), color, pos in zip(modes, colors, positions):
            text_surface = self.font.render(key, True, (255, 255, 255))
            desc_surface = self.font.render(mode, True, (255, 255, 255))
            
            width = max(text_surface.get_width(), desc_surface.get_width()) + 20
            height = text_surface.get_height() + desc_surface.get_height() + 20

            pygame.draw.rect(self.screen, color, (pos[0] - width // 2, pos[1], width, height))
            
            text_rect = text_surface.get_rect(center=(pos[0], pos[1] + text_surface.get_height() // 2 + 5))
            self.screen.blit(text_surface, text_rect)

            desc_rect = desc_surface.get_rect(center=(pos[0], pos[1] + text_surface.get_height() + desc_surface.get_height() // 2 + 10))
            self.screen.blit(desc_surface, desc_rect)

        pygame.display.flip()

    def get_user_choice(self):
        self.draw_menu()
        choice = None
        while choice is None:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if 100 <= x <= 300 and 100 <= y <= 200:
                        choice = 'easy'
                    elif 100 <= x <= 300 and 250 <= y <= 350:
                        choice = 'moderate'
                    elif 100 <= x <= 300 and 400 <= y <= 500:
                        choice = 'difficult'
        return choice

    def run_ai(self, mode):
        if mode == 'easy':
            from alpha_beta import AlphaBetaAI
            ai = AlphaBetaAI(self.game)
            move = ai.get_best_move(depth=4)
        elif mode == 'moderate':
            from fuzzy_logic import FuzzyLogicAI
            ai = FuzzyLogicAI(self.game)
            move = ai.get_best_move()
        elif mode == 'difficult':
            from genetic_algorithm import GeneticAlgorithmAI
            ai = GeneticAlgorithmAI(self.game)
            move = ai.get_best_move()
        if move:
            getattr(self.game, f"move_{move}")()

    def run(self):
        mode = self.get_user_choice()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.game.move_left()
                    elif event.key == pygame.K_RIGHT:
                        self.game.move_right()
                    elif event.key == pygame.K_UP:
                        self.game.move_up()
                    elif event.key == pygame.K_DOWN:
                        self.game.move_down()
                    elif event.key == pygame.K_SPACE:
                        self.run_ai(mode)

            self.draw_board()
            pygame.display.flip()

        pygame.quit()

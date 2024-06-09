# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 21:37:07 2024

@author: the great Arpita
"""

# src/genetic_algorithm.py
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

import copy
import random
import numpy as np
from game import Game2048

class GeneticAlgorithmAI:
    def __init__(self, game, population_size=50, mutation_rate=0.1, generations=100):
        self.game = game
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.generations = generations

    def evolve(self):
        population = self.initialize_population()
        for _ in range(self.generations):
            population = self.next_generation(population)
        best_individual = max(population, key=lambda ind: ind['fitness'])
        return best_individual['moves'][0]

    def initialize_population(self):
        population = []
        for _ in range(self.population_size):
            moves = [random.choice(['left', 'right', 'up', 'down']) for _ in range(10)]
            fitness = self.evaluate_fitness(moves)
            population.append({'moves': moves, 'fitness': fitness})
        return population

    def evaluate_fitness(self, moves):
        board = copy.deepcopy(self.game)
        for move in moves:
            getattr(board, f"move_{move}")()
        return np.sum(board.board)

    def select_parents(self, population):
        population = sorted(population, key=lambda ind: ind['fitness'], reverse=True)
        return population[:self.population_size // 2]

    def crossover(self, parent1, parent2):
        point = random.randint(1, len(parent1['moves']) - 1)
        child1 = parent1['moves'][:point] + parent2['moves'][point:]
        child2 = parent2['moves'][:point] + parent1['moves'][point:]
        return child1, child2

    def mutate(self, individual):
        for i in range(len(individual)):
            if random.random() < self.mutation_rate:
                individual[i] = random.choice(['left', 'right', 'up', 'down'])
        return individual

    def next_generation(self, population):
        parents = self.select_parents(population)
        next_generation = []
        for i in range(0, len(parents), 2):
            parent1, parent2 = parents[i], parents[i + 1]
            child1_moves, child2_moves = self.crossover(parent1, parent2)
            child1_moves = self.mutate(child1_moves)
            child2_moves = self.mutate(child2_moves)
            child1_fitness = self.evaluate_fitness(child1_moves)
            child2_fitness = self.evaluate_fitness(child2_moves)
            next_generation.append({'moves': child1_moves, 'fitness': child1_fitness})
            next_generation.append({'moves': child2_moves, 'fitness': child2_fitness})
        return next_generation

    def get_best_move(self):
        return self.evolve()

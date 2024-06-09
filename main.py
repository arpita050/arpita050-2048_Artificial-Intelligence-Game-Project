# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 21:36:29 2024

@author: the great Arpita
"""

# src/main.py
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from gui import GUI

def main():
    gui = GUI()
    gui.run()

if __name__ == "__main__":
    main()

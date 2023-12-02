"""!@file solve_sudoku.py
@brief This file contains the main sudoku solving code. .

@details Using functions from modules ...,
it takes in a sudoku in txt format (with specific formatting),
solves it using ...,
and returns the solved sudoku in the same format as the input.
@author Created by T.Breitburd on 19/11/2023
"""

import sys
import configparser as cfg
import numpy as np
import pandas as pd
import preprocessing as preproc
import solver_tools as st

input_file = sys.argv[1]

config = cfg.ConfigParser()
config.read(input_file)

sudoku = preproc.load_sudoku(config["Input"]["sudoku1"])

markup_0 = st.markup(sudoku)
markup_1 = pd.DataFrame(index=range(9), columns=range(9))

while not np.array_equal(markup_0.values, markup_1.values):
    markup_0 = st.markup(sudoku)
    for row in range(9):
        for col in range(9):
            if len(markup_0[col][row]) == 1:
                print(markup_0[col][row][0])
                sudoku[row][col] = markup_0[col][row][0]
    markup_1 = st.markup(sudoku)

print(sudoku)

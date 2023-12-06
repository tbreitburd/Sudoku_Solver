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
from . import preprocessing as preproc
from . import solver_tools as st

input_file = sys.argv[1]

config = cfg.ConfigParser()
config.read(input_file)

sudoku = preproc.load_sudoku(config["Input"]["sudoku2"])

markup_0 = st.markup(sudoku)
markup_1 = pd.DataFrame(index=range(9), columns=range(9))

while not np.array_equal(markup_0.values, markup_1.values):
    markup_0 = st.markup(sudoku)
    for row in range(9):
        for col in range(9):
            if len(markup_0[col][row]) == 1:
                sudoku[row][col] = markup_0[col][row][0]
    if all(x != 0 for x in np.ravel(sudoku[:][:])):
        break
    markup_1 = st.markup(sudoku)

# get the indices of markup cells that still have more than one possible value
backtrack_cells = np.where(markup_1.map(len) > 1)
# put those in a 2D array
backtrack_cells = np.array([backtrack_cells[1], backtrack_cells[0]]).T


if st.backtrack_alg(sudoku, markup_1, backtrack_cells, 0):
    solved_sudoku_str = preproc.sudoku_to_output_format(sudoku)
    print(solved_sudoku_str)
else:
    print("Something went wrong")


output_file = config["Output"]["sudoku2"]  # Specify the output file path

# Write the solved sudoku to the output file
with open(output_file, "w") as file:
    file.write(solved_sudoku_str)

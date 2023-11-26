# test preprocessing.py
from src import preprocessing
import numpy as np
import unittest


def test_preproc():
    assert preprocessing.test(2) == 3


def test_load_sudoku():
    np.array_equal(
        preprocessing.load_sudoku("sudokus/sudoku1.txt"),
        [
            [0, 0, 0, 0, 0, 7, 0, 0, 0],
            [0, 0, 0, 0, 0, 9, 5, 0, 4],
            [0, 0, 0, 0, 5, 0, 1, 6, 9],
            [0, 8, 0, 0, 0, 0, 3, 0, 5],
            [0, 7, 5, 0, 0, 0, 2, 9, 0],
            [4, 0, 6, 0, 0, 0, 0, 8, 0],
            [7, 6, 2, 0, 8, 0, 0, 0, 0],
            [1, 0, 3, 9, 0, 0, 0, 0, 0],
            [0, 0, 0, 6, 0, 0, 0, 0, 0],
        ],
    )


def test_load_sudoku_2():
    with unittest.TestCase().assertRaises(ValueError):
        preprocessing.load_sudoku("sudokus/bad_format_sudoku.txt")


sudoku = [
    [0, 0, 0, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 0, 9, 5, 0, 4],
    [0, 0, 0, 0, 5, 0, 1, 6, 9],
    [0, 8, 0, 0, 0, 0, 3, 0, 5],
    [0, 7, 5, 0, 0, 0, 2, 9, 0],
    [4, 0, 6, 0, 0, 0, 0, 8, 0],
    [7, 6, 2, 0, 8, 0, 0, 0, 0],
    [1, 0, 3, 9, 0, 0, 0, 0, 0],
    [0, 0, 0, 6, 0, 0, 0, 0, 0],
]


def test_box():
    assert preprocessing.box(sudoku, 1, 2) == [[0, 0, 7], [0, 0, 9], [0, 5, 0]]

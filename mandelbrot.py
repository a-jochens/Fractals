#!/usr/bin/env python3

# Picturing the Mandelbrot set
# Algorithm as in Make Your Own Mandelbrot by Tariq Rashid, section The Recipe
# Implementation by Arne Jochens

import numpy as np


def initialize_grid(frame, n_points_x, n_points_y):
    """ Return a 2d NumPy array of points in the complex plane """

    bottom_left, top_right = frame
    x_start = bottom_left.real
    x_stop = top_right.real
    y_start = bottom_left.imag
    y_stop = top_right.imag

    grid = np.empty(shape=[n_points_x, n_points_y], dtype='complex')

    for j, y in enumerate(np.linspace(y_start, y_stop, n_points_y)):
        for i, x in enumerate(np.linspace(x_start, x_stop, n_points_x)):
            grid[n_points_y - j - 1, i] = complex(x, y)

    return grid



def picture_mandelbrot(frame=[complex(-2.25, -1.5), complex(0.75, 1.5)],
                       n_points_x=3, n_points_y=3):
    """ Picture the Mandelbrot set
        within the frame given as [bottom left corner, top right corner]
        with a resolution of n_points_x times n_points_y pixels
    """

    grid = initialize_grid(frame=frame, n_points_x=n_points_x, n_points_y=n_points_y)

    print(grid)



picture_mandelbrot()
#!/usr/bin/env python3

# Picturing the Mandelbrot set
# Algorithm as in Make Your Own Mandelbrot by Tariq Rashid, section The Recipe
# Implementation by Arne Jochens

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def transform(z, c):
    """ Function to iterate for every point c within the frame. 
        Works with single complex input numbers as well as with complex arrays.
    """ 
    return z**2 + c


def plot_counts(iter_counts):
    """ Plot NumPy array of integer values as heatmap. 
    """
    cmap = sns.color_palette('mako', as_cmap=True)
    plt.imshow(np.log(iter_counts + 1), cmap=cmap)
    plt.show()


def initialize_grid(frame, n_points_x, n_points_y):
    """ Return a 2d NumPy array of points in the complex plane. 
    """
    bottom_left, top_right = frame
    x_start = bottom_left.real
    x_stop = top_right.real
    y_start = bottom_left.imag
    y_stop = top_right.imag

    grid = np.zeros(shape=[n_points_y, n_points_x], dtype='complex')

    for j, y in enumerate(np.linspace(y_start, y_stop, n_points_y)):
        for i, x in enumerate(np.linspace(x_start, x_stop, n_points_x)):
            grid[n_points_y - j - 1, i] = complex(x, y)

    return grid


def count_iterations(grid, n_iter):
    """ Iterate the complex function n_iter times on the grid numbers.
        Return a Boolean array indicating the numbers of iterations until divergence.
    """
    z = np.zeros(shape=grid.shape, dtype='complex')
    diverged = np.zeros(shape=grid.shape, dtype='bool') 
    iter_counts = np.zeros(shape=grid.shape, dtype='int') 

    for i in range(n_iter):
        z = transform(z * (~diverged).astype(int), grid)
        diverged = diverged | (np.absolute(z) > 4)
        iter_counts[~diverged] += 1

    return iter_counts


def picture_mandelbrot(frame=[complex(-2.25, -1.5), complex(0.75, 1.5)],
                       n_points_x=1_000, n_points_y=1_000, n_iter=100):
    """ Picture the Mandelbrot set
        within the frame given as [bottom left corner, top right corner]
        with a resolution of n_points_x times n_points_y pixels.
    """
    grid = initialize_grid(frame=frame, n_points_x=n_points_x, n_points_y=n_points_y)
    iter_counts = count_iterations(grid, n_iter)
    plot_counts(iter_counts)
    

if __name__ == "__main__":
    picture_mandelbrot()

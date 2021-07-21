# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 12:43:07 2021

@author: Andycyca

Original writeup: The Curlicue Fractal (place) by Oolong

URL: https://everything2.com/user/Oolong/writeups/The+Curlicue+Fractal
"""

import numpy as np
import matplotlib.pyplot as plt
import math

plt.style.use('fivethirtyeight')

#%% Plot everything


def plot_curlicue(seed, my_ax, rounds=5000):
    """
    Plot a curlicue fractal with 5000 iterations.

    Parameters
    ----------
    seed : float
        A float that will describe how much "turn" to make at every step.
        Can be larger than 1, but only the decimal part will be used.
    my_ax : matplotlib axis
        The easiest way is to generate one with plt.subplots()
    rounds : int, optional
        Number of iterations to draw. The default is 5000.

    Returns
    -------
    None.

    """

    x0 = np.array([0])
    y0 = np.array([0])
    f = 0
    for i in range(rounds):
        # Use only the decimal part of the seed
        f += math.modf(seed)[0] * 2 * np.pi
        x0 = np.append(x0, x0[-1] + np.cos(f**2))
        y0 = np.append(y0, y0[-1] + np.sin(f**2))
    my_ax.grid(False)
    my_ax.set_xticks([])
    my_ax.set_yticks([])
    my_ax.plot(x0, y0, lw=1)
    my_ax.set_title("Seed = %f" % seed)
    pass

#%% Plotting


n = 101  # Works good with larger numbers, integers preferred
values = (1/n, 2/n, 3/n, 4/n, 5/n, 6/n)
fig, axs = plt.subplots(2, 3)
fig.suptitle("Curlicue fractals")

for i in (0, 1):
    for j in (0, 1, 2):
        plot_curlicue(values[3*i + j], axs[i, j])

plt.savefig('curlicuefractal.png')
plt.show()

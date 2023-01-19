#!/usr/bin/python

import os
import numpy as np
import matplotlib.pyplot as plt
import cv2
import pdb


def colormapArray(X, colors):
    """
    Basically plt.imsave but return a matrix instead

    Given:
        a HxW matrix X
        a Nx3 color map of colors in [0,1] [R,G,B]
    Outputs:
        a HxW uint8 image using the given colormap. See the Bewares
    """

    N = len(colors)
    vmin = np.min(X)
    vmax = np.max(X)

    new_X = ((N - 1) * (X - vmin)) / (vmax - vmin)
    # print(new_X)
    new_X = np.uint8(new_X)
    # print(new_X.shape)
    return new_X


if __name__ == "__main__":
    colors = np.load("mysterydata/colors.npy")
    data = np.load("mysterydata/mysterydata4.npy")
    colored = colormapArray(data, colors)
    for i in range(9):
        plt.imsave("changed_vis4_%d.png" % i, colored[:, :, i])

    X = np.load("mysterydata/mysterydata.npy")
    for i in range(9):
        plt.imsave("vis_%d.png" % i, X[:, :, i])
    X = np.load("mysterydata/mysterydata2.npy")
    for i in range(9):
        plt.imsave("vis2_%d.png" % i, X[:, :, i])
    A = np.log1p(X)
    for i in range(9):
        plt.imsave("changed_vis2_%d.png" % i, A[:, :, i])

    X = np.load("mysterydata/mysterydata3.npy")
    for i in range(9):
        plt.imsave("vis3_%d.png" % i, X[:, :, i])
    vmin = np.nanmin(X)
    vmax = np.nanmax(X)
    for i in range(9):
        plt.imsave("changed_vis3_%d.png" % i, X[:, :, i], vmin=vmin, vmax=vmax)
    # pdb.set_trace()

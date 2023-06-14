#!/usr/bin/env python

"""This is the visualisation.py module. This module contains code required to visualise various stages in the
placenta model generation process
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

#def plot_skeleton_3d


def plot_vasculature_3d(nodes, elems, colour, radii,x_dim,y_dim,z_dim):
    ######
    # Function: Creates a 3D plot of branching tree
    # Inputs: nodes - an M x 3 array giving cartesian coordinates (x,y,z) for the node locations in the tree
    #         elems - an N x 3 array, the first colum in the element number, the second two columns are the index of the start and end node
    #         colour - an N x 1 array where value determines colour of corresponding element
    #         Nc - the maximum number of elements connected at a single node
    # Outputs: 3D plot of tree, with radius proportional to radii and colour depending on the input array
    ######

    # initialize arrays
    Ne = len(elems)
    elems = elems[:, 1:3]
    x = np.zeros([Ne, 2])
    y = np.zeros([Ne, 2])
    z = np.zeros([Ne, 2])

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.set_xlim(left=0,right=x_dim)
    ax.set_ylim(bottom=0, top=y_dim)
    ax.set_zlim(bottom=0,top=z_dim)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z (slices)")
    # scale colour and radii
    colour = (colour - min(colour)) / max(colour) * 255
    radii = radii / max(radii) * 3

    for i in range(0, Ne):
        # get start and end node
        nN1 = int(elems[i, 0])
        nN2 = int(elems[i, 1])

        # get coordinates of nodes
        x[i, 0] = nodes[nN1, 0]
        y[i, 0] = nodes[nN1, 1]
        z[i, 0] = nodes[nN1, 2]
        x[i, 1] = nodes[nN2, 0]
        y[i, 1] = nodes[nN2, 1]
        z[i, 1] = nodes[nN2, 2]

        colour_value = np.asarray(cm.jet(int(colour[i])))
        ax.plot(np.squeeze(x[i, :]), np.squeeze(y[i, :]), np.squeeze(z[i, :]), c=colour_value[0:3], linewidth=2.)#*radii[i])
    plt.show()

def image_show(nda, figurenum=1,  title=None, margin=0.05, dpi=40,colormap="gray",normalise=None ,exportto=None):
    #spacing = nda.GetSpacing()
    figsize = (1 + margin) * nda.shape[0] / dpi, (1 + margin) * nda.shape[1] / dpi
    #extent = (0, nda.shape[1] * spacing[1], nda.shape[0] * spacing[0], 0)
    fig = plt.figure(num=figurenum,figsize=figsize, dpi=dpi)
    ax = fig.add_axes([margin, margin, 1 - 2 * margin, 1 - 2 * margin])

    plt.set_cmap(colormap)

    pcm = ax.imshow(nda,norm=normalise)#, extent=extent, interpolation=None)
    plt.colorbar(pcm,ax=ax)
    if title:
        plt.title(title)

    plt.show()
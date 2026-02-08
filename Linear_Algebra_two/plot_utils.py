import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_vectors(vectors, colors):
    """
    Plot one or more vectors in a 2D plane, specifying a color for each.

    Arguments
    ---------
    vectors: list of lists or of arrays
        Coordinates of the vectors to plot. For example, [[1, 3], [2, 2]]
        contains two vectors to plot, [1, 3] and [2, 2].
    colors: list
        Colors of the vectors. For instance: ['red', 'blue'] will display the
        first vector in red and the second in blue.

    Example
    -------
    plot_vectors([[1, 3], [2, 2]], ['red', 'blue'])
    plt.xlim(-1, 4)
    plt.ylim(-1, 4)
    """
    
    plt.close('all')        # kill old figures
    
    plt.figure()
    plt.axvline(x=0, color='lightgray')
    plt.axhline(y=0, color='lightgray')

    # for i in range(len(vectors)):
    #     x = np.concatenate([[0,0],vectors[i]])
    #     plt.quiver([x[0]], [x[1]], [x[2]], [x[3]],
    #                angles='xy', scale_units='xy', scale=1, color=colors[i],)
    
    for i, v in enumerate(vectors):
        # Convert torch tensor -> numpy if needed
        if hasattr(v, "detach"):
            v = v.detach().cpu().numpy()
        else:
            v = np.asarray(v)

        x = np.array([0, 0, v[0], v[1]])

        plt.quiver(
            x[0], x[1],
            x[2], x[3],
            angles='xy',
            scale_units='xy',
            scale=1,
            color=colors[i]
        )
        
        
def plot_vectors_3d(vectors, colors):
    """
    Plot one or more vectors in 3D, specifying a color for each.

    Arguments
    ---------
    vectors: list of lists / numpy arrays / torch tensors (shape: (3,))
    colors: list of colors (same length as vectors)
    """

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Axes through origin
    ax.plot([-1, 1], [0, 0], [0, 0], color='lightgray')
    ax.plot([0, 0], [-1, 1], [0, 0], color='lightgray')
    ax.plot([0, 0], [0, 0], [-1, 1], color='lightgray')

    for i, v in enumerate(vectors):
        if hasattr(v, "detach"):
            v = v.detach().cpu().numpy()
        else:
            v = np.asarray(v)

        ax.quiver(
            0, 0, 0,
            v[0], v[1], v[2],
            color=colors[i],
            arrow_length_ratio=0.1,
            linewidth=2
        )

    return fig, ax

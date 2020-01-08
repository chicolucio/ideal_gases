from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from scipy import constants
import pathlib


def grid_points(volume_array,
                temperature_array,
                n_mol=1,
                R=constants.gas_constant):
    """Creates grid points to a 3D plot pressure x volume x temperatura.
    The pressure data are calculated with ideal gas formula from volume
    and temperature arrays.

    The R value is taken from SciPy constants by default. So the values are
    considered to be in SI units. The user can change the parameter R to use
    another unit system.

    Parameters
    ----------
    volume_array : array
        volume array
    temperature_array : array
        volume array
    n_mol : int, optional
        number of moles of gas, by default 1
    R : float, optional
        ideal gas constante, by default constants.gas_constant

    Returns
    -------
    tuple
        volume, temperature and pressure matrices
    """
    volume_matrix, temperature_matrix = np.meshgrid(
        volume_array, temperature_array)

    pressure_matrix = n_mol * R * temperature_matrix / volume_matrix

    return volume_matrix, temperature_matrix, pressure_matrix


def plot_3d(volume_matrix,
            temperature_matrix,
            pressure_matrix,
            labels=['Volume / m3', 'Temperature / K', 'Pressure / Pa'],
            save_fig=True,
            save_angle=30):
    """3D plot for pressure, volume and temperature of an ideal gas.

    Parameters
    ----------
    volume_matrix : ndarray
        volume matrix
    temperature_matrix : ndarray
        temperature matrix
    pressure_matrix : ndarray
        pressure matrix
    labels : list, optional
        Axes labels, by default ['Volume / m3', 'Temperature / K', 'Pressure / Pa']
    save_fig : bool, optional
        If the plot should be saved periodically (an 'images' folder
        will be created if not exists), by default True
    save_angle : int, optional
        The angle interval to save the plot, by default 30
    """
    fig = plt.figure(1, figsize=(10, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_wireframe(volume_matrix, temperature_matrix,
                      pressure_matrix, rstride=50, cstride=50)
    ax.set_xlabel(labels[0])
    ax.set_ylabel(labels[1])
    ax.set_zlabel(labels[2])

    for angle in range(0, 361):
        ax.view_init(30, angle)
        plt.draw()
        plt.pause(.001)
        if (angle % save_angle == 0) and save_fig:
            pathlib.Path('images').mkdir(parents=False, exist_ok=True)
            plt.savefig('images/pvt_plot_{}.png'.format(angle),
                        bbox_inches='tight')


if __name__ == "__main__":
    vol = np.linspace(1, 50, 500)
    temp = np.linspace(1, 300, 500)

    v, t, p = grid_points(vol, temp)

    plot_3d(v, t, p)

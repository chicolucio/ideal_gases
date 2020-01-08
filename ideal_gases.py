from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from scipy import constants
import pathlib


def grid_points(volume_array,
                temperature_array,
                n_mol=1,
                R=constants.gas_constant):
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

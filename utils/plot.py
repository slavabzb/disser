import os

import matplotlib.pyplot as plt

from data import *


def plot():
    for point in zip(cores2, cores4, cores8):
        plt.plot([2, 4, 8], point)
    plt.xticks([2, 4, 8])
    plt.title("График параллельных координат")
    plt.xlabel('Количество потоков')
    plt.ylabel('Ускорение')
    plt.savefig(os.path.join("plots", "parallel.png"), dpi=480)
    plt.show()

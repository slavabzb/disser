import os

import matplotlib.pyplot as plt

from data import cores2, cores4, cores8
from utils import normalize


def plot():
    ncores = [2, 4, 8]
    for point in zip(cores2, cores4, cores8):
        plt.plot(ncores, point)
    plt.xticks(ncores)
    plt.xlabel("Количество потоков")
    plt.ylabel("Ускорение")
    plt.savefig(os.path.join("plots", "parallel.png"), dpi=480)

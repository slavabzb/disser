from functools import reduce
from random import uniform

import numpy as np


def geomean(vs):
    return round((reduce(lambda x, y: x * y, vs)) ** (1.0 / len(vs)), 2)


def mean(vs):
    return round(sum(vs) / len(vs), 2)


def normalize(vs):
    scale = np.mean(vs)
    return [v / scale for v in vs]


def trans(vs):
    return [round(v + uniform(-0.07, 0.0), 2) for v in vs]

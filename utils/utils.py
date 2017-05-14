import functools
import random

def geomean(nums):
    return round((functools.reduce(lambda x, y: x*y, nums))**(1.0/len(nums)), 2)

def mean(vals):
    return round(sum(vals)/len(vals), 2)

def trans(vals):
    return [round(v + random.uniform(-0.07, 0.0), 2) for v in vals]
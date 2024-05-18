import numpy as np


def dejong1(solution):
    return np.sum(solution ** 2)


def dejong2(solution):
    return np.sum(np.abs(solution))


def schweffel(solution):
    return -np.sum(solution * np.sin(np.sqrt(np.abs(solution))))

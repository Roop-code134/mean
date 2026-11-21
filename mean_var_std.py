import numpy as np


def calculate(lst):
    if len(lst) != 9:
        raise ValueError("List must contain nine numbers.")

    matrix = np.array(lst).reshape(3, 3)

    def stats(func):
        return [
            func(matrix, axis=0).tolist(),  # axis 1: down each column
            func(matrix, axis=1).tolist(),  # axis 2: across each row
            func(matrix.flatten()).item(),  # flattened matrix
        ]

    return {
        'mean': stats(np.mean),
        'variance': stats(np.var),
        'standard deviation': stats(np.std),
        'max': stats(np.max),
        'min': stats(np.min),
        'sum': stats(np.sum),
    }

import numpy as np


def reshape_rows(values: list[float], width: int) -> list[list[float]]:
    if width <= 0 or len(values) % width != 0:
        return []
    arr = np.asarray(values, dtype=float).reshape(-1, width)
    return arr.tolist()


def block(matrix: list[list[float]], rows: list[int], columns: list[int]) -> list[list[float]]:
    arr = np.asarray(matrix, dtype=float)
    return arr[np.ix_(rows, columns)].tolist()


def column_means(matrix: list[list[float]]) -> list[float]:
    if len(matrix) == 0:
        return []
    arr = np.asarray(matrix, dtype=float)
    return [round(float(m), 6) for m in arr.mean(axis=0)]


def column_range(matrix: list[list[float]], column: int) -> float:
    if len(matrix) == 0:
        return 0.0
    arr = np.asarray(matrix, dtype=float)
    col = arr[:, column]
    return round(float(col.max() - col.min()), 6)
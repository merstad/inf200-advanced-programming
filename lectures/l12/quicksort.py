"""
Example for profiling.
"""

__author__ = "Hans Ekkehard Plesser / NMBU"

import numpy as np


def quicksort(data):
    _quicksort(data, 0, len(data))


def _quicksort(data, left, right):
    if right - left < 2:
        return

    pivot_idx = _partition(data, left, right)
    _quicksort(data, left, pivot_idx)
    _quicksort(data, pivot_idx + 1, right)


def _partition(data, left, right):
    if not left < right:
        return None

    right -= 1
    pivot_idx = left
    pivot_val = data[pivot_idx]

    data[pivot_idx], data[right] = data[right], data[pivot_idx]
    store_idx = left

    for i in range(left, right):
        if data[i] < pivot_val:
            data[i], data[store_idx] = data[store_idx], data[i]
            store_idx += 1
    data[store_idx], data[right] = data[right], data[store_idx]

    return store_idx


if __name__ == "__main__":
    data = np.random.random(100000)
    quicksort(data.copy())

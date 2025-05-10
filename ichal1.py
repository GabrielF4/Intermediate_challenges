#Challenge 1: Shifting an array

from typing import List

def shift_array_left(arr: List[int], shifts: int) -> List[int]:
    for _ in range(shifts):
        first, *rest = arr
        arr = rest
        arr.append(first)
    return arr

def shift_array_right(arr: List[int], shifts: int) -> List[int]:
    for _ in range(shifts):
        *arr, last = arr
        arr.insert(0, last)
    return arr

arr = [1, 2, 3, 4, 5]
print(arr)
arr = shift_array_left(arr, 2)
print(arr)
arr = shift_array_right(arr, 3)
print(arr)
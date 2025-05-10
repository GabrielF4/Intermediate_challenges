#Challenge 2: Two Sum Problem

from typing import List

def find_sum(arr: List[int], sum: int):
    for i in arr:
        for j in arr:
            if i != j and i + j == sum:
                return i, j
    return False, False

arr: List[int] = [2, 3, 5, 7, 11, 13]

print(arr)

while True:
    user_input: str = input("What sum you want to find?: ")
    if user_input.isdigit():
        sum: int = int(user_input)
        break
    else:
        print("Invalid input")

a: int
b: int
a, b = find_sum(arr, sum)

if a and b:
    print(f"{a} + {b} = {sum}")
else:
    print("No sums found")
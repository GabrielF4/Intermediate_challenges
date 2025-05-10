#Challenge 6: Find Missing Number in Array

from typing import List

arr: List[int] = [4, 5, 6, 7, 3, 2, 1, 12, 10, 11, 9]

print(f"List to check for missing number: {arr}")

arr = sorted(arr)

missing_number_found: bool = False

for i in range(0, len(arr)):
    if i + 1 != arr[i]:
        print(f"Missing number: {i + 1}")
        missing_number_found = True
        break

if not missing_number_found:
    print("No missing number was found")

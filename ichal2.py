#Two Sum Problem

def find_sum(arr, sum):
    for i in arr:
        for j in arr:
            if i != j and i + j == sum:
                return i, j
    return "No sums found"

arr = [2, 3, 5, 7, 11, 13]

print(arr)
user_input = input("What sum you want to find?: ")
print(find_sum(arr, int(user_input)))
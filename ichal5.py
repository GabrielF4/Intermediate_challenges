#Challenge 5: Star pyramid

#Safe user input
while True:
    user_input: str = input("How many rows do you want the pyramid to have?: ")
    if user_input.isdigit():
        num: int = int(user_input)
        break
    else:
        print("Invalid input")

for i in range(1, num + 1):
    for j in range(num - i):
        print(" ", end="")
    for j in range(i):
        print("**", end="")
    print()
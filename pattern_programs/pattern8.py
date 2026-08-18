n = int(input("Enter a number: "))

for i in range(1, n + 1):
    spaces = " " * (n - i)

    if i == 1:
        print(spaces + "*")
    elif i == n:
        print("*" * (2 * n - 1))
    else:
        print(spaces + "*" + " " * (2 * i - 3) + "*")
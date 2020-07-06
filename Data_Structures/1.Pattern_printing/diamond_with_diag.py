"""
Print a diamond with both diagonals

"""


def rhombus_diag(row):
    for i in range(row):
        for j in range(row):
            if j == int(row / 2) or i == int(row / 2) or i + j == int(row / 2) \
                    or i + j == int(3 * row / 2) - 1 or i + j == int(row / 2) + 2 * i \
                    or i + j == int(row / 2) + 2 * j:
                print("*", end="")
            else:
                print(" ", end="")
        print()


rhombus_diag(15)

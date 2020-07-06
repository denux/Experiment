"""
solid and hollow rhombus
"""


def solid_rhombus(row):
    max_j = int(3 * row / 2) + 1
    for i in range(row):
        for j in range(max_j):
            if int(max_j / 2) <= j <= max_j - 1 - i or int(max_j / 2) - i <= j <= int(max_j / 2):
                print("*", end="")
            else:
                print(" ", end="")
        print()


def hollow_rhombus(row):
    max_j = int(3 * row / 2) + 1
    for i in range(row):
        for j in range(max_j):
            if int(max_j / 2) <= j <= max_j - 1 - i or int(max_j / 2) - i <= j <= int(max_j / 2):
                if i == 0 or i == row - 1 or j == max_j - 1 - i or int(max_j / 2) - i == j:
                    print("*", end="")
                else:
                    print(" ", end="")
            else:
                print(" ", end="")
        print()


hollow_rhombus(4)

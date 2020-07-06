"""
left and right arrow
"""


def right_arrow(row):
    for i in range(row):
        for j in range(row):
            if i == int(row / 2) or i + j == int(3 * row / 2) - 1 or j - i == int(row / 2):
                print("*", end="")
            else:
                print(" ", end="")
        print()


def left_arrow(row):
    for i in range(row):
        for j in range(row):
            if i == int(row / 2) or i + j == int(row / 2) - 1 or i - j == int(row / 2):
                print("*", end="")
            else:
                print(" ", end="")
        print()


left_arrow(7)

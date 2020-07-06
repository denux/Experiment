"""

Example 10: Floyd's Triangle.
1
2 3
4 5 6
7 8 9 10

"""


def floyds_triangle(row):
    count = 1
    for i in range(row):
        for j in range(i + 1):
            print(str(count) + " ", end="")
            count += 1
        print()

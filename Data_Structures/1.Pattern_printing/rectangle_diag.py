"""
Input : 7
Output :

    *******
    **   **
    * * * *
    *  *  *
    * * * *
    **   **
    *******

"""


def diagonal_code(row):
    for i in range(row):
        for j in range(row):
            if i == 0 or j == 0 or i == row - 1 or j == row - 1 or j == i or j == row - i - 1:
                print("*", end="")
            else:
                print(" ", end="")

        print()

diagonal_code(5)
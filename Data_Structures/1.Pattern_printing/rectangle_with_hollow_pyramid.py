"""
Diamond square star pattern using C programming

Input N: 5
Output

**********
****  ****
***    ***
**      **
*        *
*        *
**      **
***    ***
****  ****
**********

"""


def pattern(n):
    for i in range(n, 0, -1):
        for j1 in range(i, 0, -1):
            print("*", end="")
        for k1 in range(n - i):
            print(" ", end="")
        for k2 in range(n - i):
            print(" ", end="")
        for j1 in range(i, 0, -1):
            print("*", end="")
        print()
    for i in range(1, n + 1):
        for j1 in range(1, i + 1):
            print("*", end="")
        for k1 in range(n - i):
            print(" ", end="")
        for k2 in range(n - i):
            print(" ", end="")
        for j1 in range(1, i + 1):
            print("*", end="")
        print()


pattern(5)

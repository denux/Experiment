# practice to print the following pattern
# time taken : ~ 15 mins
"""
pattern 1 : Solid Rectangle

inputs:
 rows = x
 cols =y

****
****
****
****


pattern 2 : Hollow Rectangle

inputs:
 rows = x
 cols =y

****
*  *
*  *
****

"""


def solid_rectangle(row, col, character):
    for _ in range(row):
        for _ in range(col):
            print(character, end="")
        print()


def hollow_rectangle(row, col, character):
    for i in range(row):
        for j in range(col):
            if i == 0 or j == 0 or j == col - 1 or i == row - 1:
                print(character, end="")
            else:
                print(" ", end="")
        print()

# solid_rectangle(10,15, "*")
# hollow_rectangle(10,15, "*")

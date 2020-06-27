# practice to print the following pyramid pattern
# time taken : ~ 15 mins
"""
pattern 1 : Half Pyramid

inputs:
 rows = x

*
* *
* * *
* * * *
* * * * *
* * * * * *


pattern 2 : Inverted Half Pyramid

inputs:
 rows = x

* * * * * *
* * * * *
* * * *
* * *
* *
*


pattern 3 : Full Pyramid

inputs:
 rows = x

      *
     * *
    * * *
   * * * *
  * * * * *
 * * * * * *


pattern 4 : inverted Full Pyramid

inputs:
 rows = x

 * * * * * *
  * * * * *
   * * * *
    * * *
     * *
      *

pattern 5 : Hollow Pyramid

inputs:
 rows = x

           *
         *  *
       *      *
     *   *   *  *

pattern 6 : inverted half hollow Pyramid

inputs:
 rows = 5

* * * * *
*      *
*    *
*  *
*


pattern 6 : inverted full hollow Pyramid

Input rows: 6

Output:
###########
 #       #
  #     #
   #   #
    # #
     #

"""


# time taken : ~ 7 mins

def half_pyramid(row):
    for i in range(1, row + 1):
        for _ in range(i):
            print("*", end="")
        print()


# time taken : ~ 4 mins

def inverted_half_pyramid(row):
    for i in range(row, 0, -1):
        for _ in range(i):
            print("*", end="")
        print()


# time taken : 1+ hr (solutn n created my own soltn)

def full_pyramid(row):
    for i in range(1, row + 1):
        for j in range(1, row - i + 1):
            print(" ", end="")
        for k in range(1, i + 1):
            print("* ", end="")
        print()


# time taken : ~ 8 mins
def inverted_full_pyramid(row):
    for i in range(1, row + 1):
        for j in range(1, i):
            print(" ", end="")
        for k in range(row - i + 1, 0, -1):
            print("* ", end="")
        print()


# time taken : ~ 20 min
def hollow_pyramid(row):
    for i in range(1, row + 1):
        for j in range(row - i, 0, -1):
            print(" ", end="")
        for k in range(1, i + 1):
            if k == 1 or k == i or i == row:
                print("* ", end="")
            else:
                print("  ", end="")
        print()


# time taken : ~ 30 min
def inverted_half_hollow_pyramid(row):
    for i in range(row):
        for j in range(row - i):
            if j == 0 or j == row - i - 1 or i == 0:
                print("* ", end="")
            else:
                print("  ", end="")
        print()


# time taken : ~ 30 min
def inverted_full_holo_pyramid(row):
    for i in range(row):
        for j in range(i + 1):
            print(" ", end="")
        for k in range(i, 2 * row - 1 - i):
            if k == i or k == 2 * row - 1 - i - 1 or i == 0:
                print("#", end="")
            else:
                print(" ", end="")
        print()

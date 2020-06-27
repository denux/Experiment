"""
Half pyramid pattern using numbers

1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

"""


# TT : 4 mins
def halfp_num(row):
    for i in range(1, row + 1):
        for j in range(1, i + 1):
            print(j, end="")
        print()


""""
Inverted half pyramid pattern using numbers

1 2 3 4 5
1 2 3 4
1 2 3 
1 2
1

"""


# TT : 2 mins
def invhalfp_num(row):
    for i in range(row, 0, -1):
        for j in range(i, 0, -1):
            print(j, end="")
        print()


"""

Full pyramid pattern using numbers

        1
      2 3 2
    3 4 5 4 3
  4 5 6 7 6 5 4
 5 6 7 8 9 8 7 6 5

"""


# TT : ~ 20 min
def fullp_num(row):
    for i in range(row):
        for j in range(row - i - 1, 0, -1):
            print("  ", end="")
        for k in range(i + 1, 2 * i + 2):
            print(str(k) + " ", end="")
        for l in range(2 * i, i, -1):
            print(str(l) + " ", end="")
        print()


"""
Hollow half pyramid pattern using numbers

1
1 2
1   3
1     4
1 2 3 4 5

"""


# TT : ~ 5 mins
def hollowhp_num(row):
    for i in range(row):
        for j in range(1, i + 2):
            if j == 1 or j == i + 1 or i == row - 1:
                print(str(j) + " ", end=" ")
            else:
                print("  ", end="")
        print()


"""

Hollow Inverted Half Pyramid Pattern using numbers

1 2 3 4 5
2     5
3   5
4 5
5

"""


# TT : 10 mins
def holl_inv_hlf_pyr_num(row):
    for i in range(row):
        for j in range(i + 1, row + 1):
            if j == i + 1 or j == row or i == 0:
                print(str(j) + " ", end="")
            else:
                print("  ", end="")
        print()


"""

Hollow Full Pyramid Pattern using numbers

   1
  1 2
 1   3
1 2 3 4

"""

# TT : ~ 20 min
def holl_full_pyr_num(row):
    for i in range(row):
        for j in range(1, row - i):
            print(" ", end="")
        for k in range(1, i + 2):
            if k == 1 or k == i + 1 or i == row - 1:
                print(str(k) + " ", end="")
            else:
                print("  ", end="")
        print()


holl_full_pyr_num(5)

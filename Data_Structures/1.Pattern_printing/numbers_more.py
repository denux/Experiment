"""
Palindrome half pyramid pattern using numbers


Input:

5 (number of rows)



Output:

1

1  2  1

1  2  3  2  1

1  2  3  4  3  2  1

1  2  3  4  5  4  3  2  1

"""

import big_o


# time taken : 10 mins
def palindrome_half_pyramid(row):
    for i in range(row):
        for j in range(i + 1):
            print(j + 1, end="")
        for k in range(i, 0, -1):
            print(k, end="")
        print()


"""

Palindrome half pyramid pattern using alphabets


Input:

5 (number of rows)



Output:

A

A  B  A

A  B  C  B  A

A  B  C  D  C  B  A

A  B  C  D  E  D  C  B  A

"""


def pal_half_pyr_alpha(row):
    for i in range(row):
        for j in range(i + 1):
            print(chr(65 + j) + " ", end="")
        for k in range(i, 0, -1):
            print(chr(65 + k - 1) + " ", end="")
        print()


"""
Palindrome pyramid pattern using numbers

Input:

5(number of rows)

Output:
          1

      1  2  1

    1  2  3  2  1

  1  2  3  4  3  2  1

1  2  3  4  5  4  3  2  1

"""


def palindrome_pyramid_pattern(row):
    for i in range(row):
        for j in range(row - i + 1, 0, -1):
            print(" ", end="")
        for k in range(0, i + 1):
            print(str(k + 1) + " ", end="")
        for l in range(i, 0, -1):
            print(str(l) + " ", end="")
        print()



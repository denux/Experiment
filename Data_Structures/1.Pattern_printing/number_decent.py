"""
Half diamond pattern printing using numbers

Input:

3 4

Output:

3
44
555
6666
555
44
3

"""


def half_diamond_pattern_num(start, row):
    for i in range(row):
        for j in range(i + 1):
            print(i + start, end="")
        print()
    for i in range(row - 2, -1, -1):
        for j in range(i + 1, 0, -1):
            print(i + start, end="")
        print()


"""
Half diamond using numbers and stars
Input :
4

Output:

1
2*2
3*3*3
4*4*4*4
4*4*4*4
3*3*3
2*2
1

"""


def half_diamond_using_num_stars(row):
    for i in range(row):
        for j in range(i + 1):
            if j == 0:
                print(i + 1, end="")
            else:
                print("*" + str(i + 1), end="")
        print()
    for i in range(row, 0, -1):
        for j in range(i, 0, -1):
            if j == i:
                print(i, end="")
            else:
                print("*" + str(i), end="")
        print()


"""
Half diamond pattern using numbers and stars

Input: 4

Output:
1
2*3
4*5*6
7*8*9*10
7*8*9*10
4*5*6
2*3
1
"""


# nice one
def half_diamond_conti_using_num_stars(row):
    count = 1
    for i in range(row):
        for j in range(i + 1):
            if j == 0:
                print(count, end="")
                count += 1
            else:
                print("*" + str(count), end="")
                count += 1
        print()
    count = count - row
    for i in range(row, 0, -1):
        for j in range(i, 0, -1):
            if j == i:
                print(count, end="")
                count += 1
            else:
                print("*" + str(count), end="")
                count += 1
        count = (count + 1) - 2 * i
        print()


half_diamond_conti_using_num_stars(4)

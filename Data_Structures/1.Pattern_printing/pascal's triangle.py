"""
 fig : Pascal's Triange
n=6

1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1

"""


def pasacal_tri(n):
    outp = [1]
    temp = [0]
    for i in range(n):
        print(outp)
        outp = [l + r for l, r in zip(outp + temp, temp + outp)]


pasacal_tri(5)

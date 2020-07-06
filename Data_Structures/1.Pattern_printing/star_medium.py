"""
Solid Diamond pattern printing using stars


Input: 5



Output:

         *
       *  *
     *  *  *
   *  *  *  *
  *  *  *  *  *
    *  *  *  *
     *  *  *
      *  *
        *
"""


def solid_diamond_pattern(row):
    for i1 in range(row):
        for j1 in range(row - i1 - 1):
            print(" ", end="")
        for k1 in range(0, i1 + 1):
            print("* ", end="")
        print()
    for i2 in range(row - 1, 0, -1):
        for j2 in range(row - i2):
            print(" ", end="")
        for k2 in range(0, i2):
            print("* ", end="")
        print()


"""
Hollow diamond pattern printing using stars


Input: 5



Output:

     *
   *  * 
  *    *
 *      *  
*        *  
*        *
 *      *
  *    *  
   *  * 
     *
"""


def hollow_diamond_pattern(row):
    for i1 in range(row):
        for j1 in range(row - i1 - 1):
            print(" ", end="")
        for k1 in range(0, i1 + 1):
            if k1 == 0 or k1 == i1:
                print("* ", end="")
            else:
                print("  ", end="")
        print()
    for i2 in range(row - 1, 0, -1):
        for j2 in range(row - i2):
            print(" ", end="")
        for k2 in range(0, i2):
            if k2 == 0 or k2 == i2 - 1:
                print("* ", end="")
            else:
                print("  ", end="")
        print()


"""
Solid Half Diamond pattern printing using stars


Input:5



Output:
*
* *
* * *
* * * *
* * * * * 
* * * *
* * * 
* *
*
"""


def solid_half_diamond_pattern(row):
    for i in range(row):
        for j in range(i + 1):
            print("* ", end="")
        print()
    for i in range(row - 1, 0, -1):
        for j in range(i, 0, -1):
            print("* ", end="")
        print()

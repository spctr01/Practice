def triangle(r, c):
    if r == 0:
        return
    if c < r:
        print("*", end="")
        triangle(r, c + 1)

    else:
        print()
        triangle(r - 1, 0)


triangle(4, 0)

"""
output
****
***
**
*

"""

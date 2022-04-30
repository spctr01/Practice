# finding ceiling of number
"""
arr = [2,3,4,5,6,7,9,22]
target = 8

expected output = 9

"""

arr = [2, 3, 4, 5, 6, 7, 9, 22]
target = 8

left = 0
right = len(arr) - 1


def ceiling(left, right):

    # if element not found in array
    if target > arr[-1]:
        return -1

    # loop over until pointer(left , right) cross
    while left <= right:
        mid = (left + right) // 2

        if target < arr[mid]:
            mid = ceiling(left, mid - 1)

        if target > arr[mid]:
            mid = ceiling(mid + 1, right)

        # if we found that exact element (target) already exist in array
        return mid

    # pointer cross target lies between them
    # as they cross  left = right and right = left
    return left


number = ceiling(left, right)

if number != -1:
    print(arr[number])
else:
    print("not found")

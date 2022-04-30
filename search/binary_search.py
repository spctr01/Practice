arr = [1, 2, 4, 5, 6, 7, 9]
target = 6

left = 0
right = len(arr) - 1


def b(left, right):
    # loop until 2 pointer cross or at  same position
    while left <= right:
        mid = (left + right) // 2

        if target < arr[mid]:
            mid = b(left, mid - 1)

        if target > arr[mid]:
            mid = b(mid + 1, right)

        # return ans found (if not </> so ans found)
        return mid

    return -1


print(b(left, right))

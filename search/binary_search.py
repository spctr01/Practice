nums = [1, 2, 4, 5, 6, 7, 8, 9]
target = 8

left = 0
right = len(nums) - 1


def binary_search(left, right):

    # loop over until 2 pointer are equal or cross each other
    while left <= right:

        mid = (left + right) // 2

        # break condition (element not found if pointers cross)
        if left > right:
            return -1

        # move pointer accordingly
        else:
            if target < nums[mid]:
                mid = binary_search(left, mid - 1)

            if target > nums[mid]:
                mid = binary_search(mid + 1, right)

        return mid


print(binary_search(left, right))

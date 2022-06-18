# find first occurence

nums = [5, 7, 7, 8, 8, 10]
target = 7

left = 0
right = len(nums) - 1
ans = -1


def first_occur(left, right):
    ans = -1

    while left <= right:
        import pdb

        pdb.set_trace()

        mid = (left + right) // 2

        if target < nums[mid]:
            mid = first_occur(mid + 1, right)

        if target > nums[mid]:
            mid = first_occur(left, mid - 1)

        else:
            ans = mid
            right = mid - 1

    return ans


print(first_occur(left, right))

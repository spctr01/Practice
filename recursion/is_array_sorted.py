arr = [1, 3, 6]


def is_sorted(arr, curr):
    if curr == len(arr) - 1:
        return True

    else:
        return arr[curr] < arr[curr + 1] and is_sorted(arr, curr + 2)


print(is_sorted(arr, 0))

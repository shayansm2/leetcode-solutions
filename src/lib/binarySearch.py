def iterative_binary_search(array, target):
    low = 0  # inclusive
    high = len(array) - 1  # inclusive

    # Repeat until the pointers low and high meet each other
    while low <= high:

        mid = low + (high - low)//2

        if array[mid] == target:
            return mid

        elif array[mid] < target:
            low = mid + 1
            continue

        high = mid - 1

    return -1


# low and high are both inclusive
def recursive_binary_search(array, target, low, high):
    if high < low:
        return -1

    mid = low + (high - low)//2

    # If found at mid, then return it
    if array[mid] == target:
        return mid

    # Search the left half
    if array[mid] > target:
        return recursive_binary_search(array, target, low, mid - 1)

    # Search the right half
    return recursive_binary_search(array, target, mid + 1, high)

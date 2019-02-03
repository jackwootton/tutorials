"""Implement quick sort in Python.
Input a list.
Output a sorted list."""


def swap(array, left, right):
    array[left], array[right] = array[right], array[left]
    return array


def partition(array, first_index, last_index):
    """Partition array into two sublists."""
    pivot = array[first_index]
    left = first_index + 1
    right = last_index
    done = False

    while not done:
        while left <= right and array[left] <= pivot:
            left += 1

        while right >= left and array[right] >= pivot:
            right -= 1

        if right < left:
            done = True
        else:
            swap(array, left, right)

    swap(array, first_index, right)
    return right


def quicksort_helper(array, first, last):
    """Helper function kicks-off recursive calls."""
    if first < last:
        partition_index = partition(array, first, last)
        quicksort_helper(array, first, partition_index - 1)
        quicksort_helper(array, partition_index + 1, last)


def quicksort(array):
    quicksort_helper(array, 0, len(array) - 1)
    return array


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test)



def partition(l, start, end):
    print(l, start, end)
    """Partitions list into two sorted sub-lists and returns pivot."""
    pivot = l[start]
    left = start+1
    right = end-1
    done = False

    while not done:
        while left < end and l[left] < pivot:
            left += 1

        while right > 0 and l[right] > pivot:
            right -= 1

        if right > left:
            l[left], l[right] = l[right], l[left]
        else:
            # Swap pivot.
            l[start], l[right] = l[start], l[right]
            done = True

    return right


def quicksort(list_of_numbers):
    start = 0
    end = len(list_of_numbers)
    # Partition list into two sub-lists.
    index = partition(list_of_numbers, start, end)
    done = False

    while not done:
        # Everything to the LEFT of index is < list_of_numbers[pivot]
        partition(list_of_numbers, start, index)
        # Everything to the RIGHT of index is > list_of_numbers[pivot]
        partition(list_of_numbers, index, end)
        break


if __name__ == "__main__":
    list_of_numbers = [1, 7, 9, 2, 0, 5, 9, 4, 2, 5, 6]
    quicksort(list_of_numbers)

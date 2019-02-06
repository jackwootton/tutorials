

def merge_lists(my_list, alices_list):
    my_list_index = 0
    alices_list_index = 0
    done = False
    # O(n) space used.
    merged_list_size = len(my_list) + len(alices_list)
    merged_list = [None] * merged_list_size

    # O(n)
    while not done:
        is_my_list_exhausted = my_list_index == len(my_list)
        is_my_alices_exhausted = alices_list_index == len(alices_list)
        done = is_my_list_exhausted and is_my_alices_exhausted

        if not (is_my_list_exhausted or is_my_alices_exhausted):
            # Unmerged values remain in both lists.
            if my_list[my_list_index] < alices_list[alices_list_index]:
                merged_list.append(my_list[my_list_index])
                my_list_index += 1
            else:
                merged_list.append(alices_list[alices_list_index])
                alices_list_index += 1
            continue

        if not is_my_list_exhausted:
            merged_list.append(my_list[my_list_index])
            my_list_index += 1

        elif not is_my_alices_exhausted:
            merged_list.append(alices_list[alices_list_index])
            alices_list_index += 1

    return merged_list


if __name__ == "__main__":
    my_list = [3, 4, 6, 10, 11, 15]
    alices_list = [1, 5, 8, 12, 14, 19]

    # Prints [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
    print merge_lists(my_list, alices_list)

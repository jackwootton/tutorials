def highest_product_of_three(list_of_ints):
    min_of_1 = min(list_of_ints[0], list_of_ints[1])
    max_of_1 = max(list_of_ints[0], list_of_ints[1])

    min_of_2 = list_of_ints[0] * list_of_ints[1]
    max_of_2 = list_of_ints[0] * list_of_ints[1]

    max_of_3 = list_of_ints[0] * list_of_ints[1] * list_of_ints[2]

    for current_number in list_of_ints[2:]:

        # -> TEST and UPDATE max product of 3
        max_of_3 = max(max_of_2 * current_number,
                       min_of_2 * current_number,
                       max_of_3)

        # ----> TEST and UPDATE min product of 2
        min_of_2 = min(current_number * max_of_1,
                       current_number * min_of_1,
                       min_of_2)

        # ----> TEST and UPDATE max product of 2
        max_of_2 = max(current_number * max_of_1,
                       current_number * min_of_1,
                       max_of_2)

        # ----------------> TEST and UPDATE min
        min_of_1 = min(current_number, min_of_1)

        # ----------------> TEST and UPDATE max
        max_of_1 = max(current_number, max_of_1)

    return max_of_3


if __name__ == "__main__":
    t1 = [12, 0, -7, 9, 2, 1, 5, 9, 4, -1, -13, 10, 2, 5, -25]
    print(highest_product_of_three(t1))

    t2 = [1, -10, -10, 1, 3, 2]
    print(highest_product_of_three(t2))

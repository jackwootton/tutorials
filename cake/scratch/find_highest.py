

def _max_product_of_two(numbers):

    highest = max(numbers[0], numbers[1])
    lowest = min(numbers[0], numbers[1])
    max_product = numbers[0] * numbers[1]

    for number in numbers[2:]:
        # Try the current number *before* updating `highest`.
        possible_max_product = max(number * highest, number * lowest)
        max_product = max(possible_max_product, max_product)

        # Now update `highest`.
        highest = max(number, highest)
        lowest = min(number, lowest)

    return max_product


def _max_product_of_three(numbers):
    max_number = max(numbers[0], numbers[1])
    min_number = min(numbers[0], numbers[1])

    max_of_two = numbers[0] * numbers[1]
    min_of_two = numbers[0] * numbers[1]

    max_of_three = None

    for current_number in numbers[2:]:

        # -> TEST possible new max product of three.
        possible_max_of_three = max(
            max_of_two * current_number, min_of_two * current_number)

        # -> UPDATE max product of three.
        max_of_three = max(max_of_three, possible_max_of_three)

        # ----> TEST possible new min product of two.
        possible_min_of_two = min(current_number * max_number,
                                  current_number * min_number)
        # ----> UPDATE min product of two.
        min_of_two = min(possible_min_of_two, min_of_two)

        # ----> TEST possible new max product of two.
        possible_max_of_two = max(current_number * max_number,
                                  current_number * min_number)

        # ----> UPDATE max product of two.
        max_of_two = max(possible_max_of_two, max_of_two)

        # ----------------> TEST and UPDATE max
        max_number = max(current_number, max_number)

        # ----------------> TEST and UPDATE min
        min_number = min(current_number, min_number)

    return max_of_three


if __name__ == "__main__":
    t1 = [12, 0, -7, 9, 2, 1, 5, 9, 4, -1, -13, 10, 2, 5, -25]
    print(_max_product_of_three(t1))

    t2 = [1, -10, -10, 1, 3, 2]
    print(_max_product_of_three(t2))

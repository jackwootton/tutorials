

def product_of_other_numbers_slow(list_of_numbers):
    """O(n^2) implementation."""
    n = len(list_of_numbers)
    products = []

    for i in range(n):
        product = 1
        for k in range(n):
            if i != k:
                product *= list_of_numbers[k]

        products.append(product)
    return products


def product_of_other_numbers(list_of_numbers):
    n = len(list_of_numbers)

    before = [1]
    after = [1]
    before_product = 1
    after_product = 1

    b = 1
    a = 1

    for i in range(n):
        start = i
        end = n-1-i

        if start < n-1:
            a *= list_of_numbers[start]
        if end > 0:
            b *= list_of_numbers[end]
        print(a, b)

    # Up to last item, but not including it (from start of list)
    for i in range(n-1):
        before_product *= list_of_numbers[i]
        before.append(before_product)

    # Up to first item, not not including it (from end of list)
    for i in range(n-1, 0, -1):
        after_product *= list_of_numbers[i]
        after.append(after_product)

    products = []
    for i in range(n):
        end = n-1-i
        product = before[i]*after[end]
        products.append(product)

    return products


if __name__ == "__main__":
    # [120, 60, 40, 30, 24]
    product_of_other_numbers([1, 2, 3, 4, 5])

    # [540, 270, 90, 108, 60]
    # print product_of_other_numbers([1, 2, 6, 5, 9])

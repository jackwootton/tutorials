# reverse-string-in-place


def reverse_string(s):
    first = 0
    last = len(s)-1

    # If the number of chars is even, last swap, switches the two inner chars.
    # If odd, the final swap is skipped becayse first == last.
    while first < last:
        s[first], s[last] = s[last], s[first]
        first += 1
        last -= 1

    # Destructive function, so a return is not absolutely necessary.
    return s


if __name__ == "__main__":
    s1 = ['a', 'b', 'c', 'd']
    reverse_string(s1)
    print(s1)
    s2 = ['a', 'b', 'c', 'd', 'e']
    reverse_string(s2)
    print(s2)
    s3 = ['a']
    reverse_string(s3)
    print(s3)
    s4 = ['c', 'a', 'k', 'e', ' ',
               'p', 'o', 'u', 'n', 'd', ' ',
               's', 't', 'e', 'a', 'l']
    reverse_string(s4)
    print(s4)

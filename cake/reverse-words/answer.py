

def reverse_string(s, first=None, last=None):
    if first == None:
        first = 0

    if last == None:
        last = len(s)-1

    while first < last:
        s[first], s[last] = s[last], s[first]
        first += 1
        last -= 1

    return s


def rerverse_words(message):
    reverse_string(message)
    print message
    return
    first = 0
    last = 0

    for i, char in enumerate(message):
        last = i - 1
        if char == ' ':
            # Previous non-space character.
            reverse_string(message, first=first, last=last)
            # Next non-space character.
            first = i + 1

    # Swap final word.
    reverse_string(message, first=first, last=last+1)
    return message


if __name__ == "__main__":
    message = ['c', 'a', 'k', 'e', ' ',
               'p', 'o', 'u', 'n', 'd', ' ',
               's', 't', 'e', 'a', 'l']

    rerverse_words(message)
    # print(message)

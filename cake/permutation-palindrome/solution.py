def has_palindrome_permutation(the_string):
    # Track characters we've seen an odd number of times
    unpaired_characters = set()

    for char in the_string:
        if char in unpaired_characters:
            unpaired_characters.remove(char)
        else:
            unpaired_characters.add(char)

    # The string has a palindrome permutation if it
    # has one or zero characters without a pair
    return len(unpaired_characters) <= 1


if __name__ == "__main__":
    print has_palindrome_permutation('civic')
    print has_palindrome_permutation('ivicc')
    print has_palindrome_permutation('civil')
    print has_palindrome_permutation('livci')
    print has_palindrome_permutation('')
    print has_palindrome_permutation('a')



def has_palindrome_permutation(word):
    char_count = set()
    for char in word:
        if char in char_count:
            char_count.remove
        else:
            char_count[char] = 1

    have_odd_char_count = False
    for char in word:
        is_odd = char_count[char] % 2
        if is_odd and have_odd_char_count:
            # A palindrome can't have two odd character counts.
            return False

        if is_odd:
            have_odd_char_count = True

    return True


if __name__ == "__main__":
    print has_palindrome_permutation('civic')
    print has_palindrome_permutation('ivicc')
    print has_palindrome_permutation('civil')
    print has_palindrome_permutation('livci')
    print has_palindrome_permutation('')
    print has_palindrome_permutation('a')

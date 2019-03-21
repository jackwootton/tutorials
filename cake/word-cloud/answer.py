

def build_word_cloud(words):
    # Use a dictionary because we need to store a key and value.
    cloud = {}
    ignore = [',', '.', '\'', '"', ':', ';', '!',
              '@', '#', '$', '%', '^', '&', '*', '(', ')']

    # Default is to split on whitespace.
    # O(n) where n is the length of the string.
    tokens = words.split()
    for token in tokens:
        token = token.lower()

        first = token[0]
        if first in ignore:
            token = token[1:]

        last = token[-1]
        if last in ignore:
            token = token[:-1]

        if token not in cloud:
            cloud[token] = 0
        cloud[token] += 1

    return cloud


def build_word_cloud2(words):
    # Use a dictionary because we need to store a key and value.
    cloud = {}
    word = ''

    for char in words:
        if char == ' ':
            if word not in cloud:
                cloud[word] = 0
            cloud[word] += 1
            # Start a new word.
            word = ''
            continue

        if char.isalpha():
            word += char.lower()

    return cloud


if __name__ == "__main__":
    cloud = build_word_cloud2(
        'After beating the eggs, Dana read the next step: Add milk and eggs, then add flour and sugar.')
    print(cloud)
    cloud = build_word_cloud(
        'After beating the eggs, Dana read the next step: Add milk and eggs, then add flour and sugar.')
    print(cloud)

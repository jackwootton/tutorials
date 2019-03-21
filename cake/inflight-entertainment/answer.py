"""
Write a function that takes an integer flight_length(in minutes) and a list of integers movie_lengths(in minutes) and returns a boolean indicating whether there are two numbers in movie_lengths whose sum equals flight_length.

When building your function:

 - Assume your users will watch exactly two movies
 - Don't make your users watch the same movie twice
 - Optimize for runtime over memory
"""


def is_flight_length(flight_length, movie_lengths):

    # Should this be a set?
    seen_movie_lengths = {}

    for movie_length in movie_lengths:
        remaining = flight_length - movie_length
        if remaining in seen_movie_lengths:
            return True
        seen_movie_lengths[movie_length] = True
    print seen_movie_lengths

    return False


if __name__ == "__main__":
    flight_length = 184
    movie_lengths = [83, 178, 71, 164, 113, 108, 163, 74, 71, 160, 62, 24]
    print is_flight_length(flight_length, movie_lengths)

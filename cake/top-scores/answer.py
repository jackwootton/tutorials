

# Returns [91, 89, 65, 53, 41, 37]
def sort_scores(unsorted_scores, HIGHEST_POSSIBLE_SCORE):
    # Index of HIGHEST_POSSIBLE_SCORE is HIGHEST_POSSIBLE_SCORE-1
    # E.g. HIGHEST_POSSIBLE_SCORE = 10, score_counts[10] would be out of index.
    score_counts = [0]*HIGHEST_POSSIBLE_SCORE+1
    sorted_scores = []

    for score in unsorted_scores:
        score_counts[score] += 1

    for score, count in enumerate(score_counts):
        sorted_scores.extend([score]*count)

    return sorted_scores


if __name__ == "__main__":
    unsorted_scores = [37, 89, 41, 65, 91, 53, 53]
    HIGHEST_POSSIBLE_SCORE = 100
    results = sort_scores(unsorted_scores, HIGHEST_POSSIBLE_SCORE)
    print(results)

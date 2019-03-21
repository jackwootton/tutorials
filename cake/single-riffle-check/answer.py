

def is_riffle_shuffle(shuffled_deck, half1, half2):
    deck_index = 0
    half1_index = 0
    half2_index = 0
    num_cards = len(shuffled_deck)

    while deck_index < num_cards-1:
        current_card = shuffled_deck[deck_index]
        deck_index += 1

        if half1[half1_index] == current_card:
            half1_index += 1
            continue

        if half2[half2_index] == current_card:
            half2_index += 1
            continue

        return False

    return True


if __name__ == "__main__":
    is_riffle_shuffle()

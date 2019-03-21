

def get_random(floor, ceiling):
    import random
    return random.randint(floor, ceiling)


def shuffle(deck):
    card_count = len(deck)

    for i in range(card_count):
        card = get_random(0, card_count-1)
        print(i,  card)
        deck[i], deck[card] = deck[card], deck[i]

    return deck


if __name__ == "__main__":
    deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print shuffle(deck)

file = open("7/input.txt", "r")
input = file.readlines()

cards = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
# cards = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
card_types = {
    "five_of_a_kind": [],
    "four_of_a_kind": [],
    "full_house": [],
    "three_of_a_kind": [],
    "two_pair": [],
    "one_pair": [],
    "high_card": [],
}


def get_card_type(hand):
    label_counts = [hand.count(c) for c in cards]
    if 5 in label_counts:
        return "five_of_a_kind"
    if 4 in label_counts:
        return "four_of_a_kind"
    if 3 in label_counts:
        if 2 in label_counts:
            return "full_house"
        else:
            return "three_of_a_kind"
    if 2 in label_counts:
        if label_counts.count(2) > 1:
            return "two_pair"
        else:
            return "one_pair"
    return "high_card"


def part_one(input):
    score = 0
    for row in input:
        [hand, bid] = row.split(" ")
        type = get_card_type(hand)
        card_types[type].append((hand, int(bid)))

    mul = len(input)
    for card_collection in card_types.values():
        sorted_cards = sorted(
            card_collection,
            key=lambda h: (
                {c: i for i, c in enumerate(cards)}[h[0][0]],
                {c: i for i, c in enumerate(cards)}[h[0][1]],
                {c: i for i, c in enumerate(cards)}[h[0][2]],
                {c: i for i, c in enumerate(cards)}[h[0][3]],
                {c: i for i, c in enumerate(cards)}[h[0][4]],
            ),
        )
        for _, bid in sorted_cards:
            score += mul * bid
            mul -= 1

    return score


print(part_one(input))

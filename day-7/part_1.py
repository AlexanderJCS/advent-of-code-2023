CARD_STRENGTH = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]


class Hand:
    def __init__(self, hand: str, bet: int, card_strength_order: list[str]):
        self.hand = hand
        self.bid = bet
        self.card_strength = card_strength_order

    def get_hand_type(self) -> int:
        """
        :return: The hand type, where 1 is the weakest hand and 5 is the greatest hand
        """

        counted_cards = list(self.count_cards().values())
        counted_cards.sort(reverse=True)

        # Five of a kind
        if max(counted_cards) == 5:
            return 7

        # Four of a kind
        elif max(counted_cards) == 4:
            return 6

        # Full house
        elif max(counted_cards) == 3 and min(counted_cards) == 2:
            return 5

        # Three of a kind
        elif max(counted_cards) == 3 and min(counted_cards) == 1:
            return 4

        # Two pair
        elif counted_cards == [2, 2, 1]:
            return 3

        # One pair
        elif counted_cards == [2, 1, 1, 1]:
            return 2

        # High Card
        else:
            return 1

    def count_cards(self) -> dict[str, int]:
        """
        :return: A dictionary of how many of each card there is.
        """

        count_dict = {}

        for card in self.hand:
            if count_dict.get(card) is None:
                count_dict[card] = 1

            else:
                count_dict[card] += 1

        return count_dict

    def _compare(self, other) -> int:
        self_hand = self.get_hand_type()
        other_hand = other.get_hand_type()

        if self_hand != other_hand:
            return self_hand - other_hand

        for self_card, other_card in zip(self.hand, other.hand):
            self_card_index = self.card_strength.index(self_card)
            other_card_index = self.card_strength.index(other_card)

            if self_card_index < other_card_index:
                return 1

            if self_card_index > other_card_index:
                return -1

        return 0

    def __lt__(self, other):
        return self._compare(other) < 0

    def __le__(self, other):
        return self._compare(other) <= 0

    def __eq__(self, other):
        return self._compare(other) == 0

    def __ne__(self, other):
        return self._compare(other) != 0

    def __ge__(self, other):
        return self._compare(other) >= 0

    def __gt__(self, other):
        return self._compare(other) > 0


def main():
    with open("input.txt") as f:
        lines = f.read().splitlines()

    hands: list[Hand] = []

    for line in lines:
        hand, bid = line.split()
        bid = int(bid)

        hands.append(Hand(hand, bid, CARD_STRENGTH))

    total_points = 0

    for i, hand in enumerate(sorted(hands)):
        total_points += hand.bid * (i + 1)

    print(total_points)


if __name__ == "__main__":
    main()

import part_1

CARD_STRENGTH = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]


class JokerHand(part_1.Hand):
    def __init__(self, hand: str, bet: int, card_strength_order: list[str]):
        super().__init__(hand, bet, card_strength_order)

        self.joker_hand = hand
        self.hand = self.optimize_joker()

    def optimize_joker(self) -> str:
        max_card = None
        max_value = None

        for card in self.card_strength:
            if card == "J":
                continue

            self.hand = self.joker_hand.replace("J", card)
            hand_type = self.get_hand_type()

            if max_value is None or self.get_hand_type() > max_value:
                max_value = hand_type
                max_card = card

        return self.joker_hand.replace("J", max_card)

    def compare_cards(self, other) -> zip:
        return zip(self.joker_hand, other.joker_hand)


def main():
    with open("input.txt") as f:
        lines = f.read().splitlines()

    hands: list[JokerHand] = []

    for line in lines:
        hand, bid = line.split()
        bid = int(bid)

        hands.append(JokerHand(hand, bid, CARD_STRENGTH))

    total_points = 0

    for i, hand in enumerate(sorted(hands)):
        total_points += hand.bid * (i + 1)

    print(total_points)


if __name__ == "__main__":
    main()


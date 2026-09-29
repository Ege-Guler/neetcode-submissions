from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        count = Counter(hand)

        for x in sorted(count):
            c = count[x]
            if c == 0:
                continue

            for card in range(x, x + groupSize):
                if count[card] < c:
                    return False
                count[card] -= c
        
        return True
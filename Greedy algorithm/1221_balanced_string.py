class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count_L = 0
        count_R = 0
        pairs = 0
        for el in s:
            if el == 'L':
                count_L += 1
            elif el == 'R':
                count_R += 1
            if count_L == count_R:
                pairs += 1
        return pairs

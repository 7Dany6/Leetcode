class Solution:
    def intToRoman(self, num: int) -> str:
        possible_outcomes = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), (50, "L"),
                             (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
        result = []  # better than appending to a string, takes O(1)
        for k in possible_outcomes:
            while num >= k[0]:
                result.append(k[1])
                num -= k[0]
        return ''.join(result)

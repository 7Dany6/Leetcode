class Solution:
    def frequencySort(self, s: str) -> str:
        count = {}
        result = []
        for char in s:
            if char not in count:
                count[char] = 0
            count[char] += 1
        count = sorted(count.items(), key=lambda x: x[1], reverse=True)
        for key, value in count:
            result.extend([key] * value)
        return ''.join(result)

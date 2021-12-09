class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter

        count_occur = Counter(nums)
        count_occurs = sorted(count_occur.items(), key=lambda x: x[1], reverse=True)
        result = [el[0] for el in count_occurs]

        return result[:k]

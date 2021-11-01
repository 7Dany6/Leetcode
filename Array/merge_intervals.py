class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        last_range = None
        result = []
        for rng in intervals:
            if not last_range:
                last_range = rng
            elif rng[0] <= last_range[1]:
                last_range = (last_range[0], max(last_range[1], rng[1]))
            else:
                result.append(last_range)
                last_range = rng
        result.append(last_range)
        return result

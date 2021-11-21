class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        last_one = None
        max_dist = 0
        dist = 0
        for i in range(len(seats)):
            if seats[i] == 1:
                if last_one is None:
                    last_one = first_one = i
                dist = (i - last_one) // 2
                max_dist = max(max_dist, dist)
                last_one = i
        max_dist = max(max_dist, first_one - 0, len(seats) - 1 - last_one)
        return max_dist

"""
Well, though this problem might seen as complex, after drawing a solution everything becomes achievable.
We'll use two pointers. One will iterate through first array and another one - second array.
We're going to add a list to our result(which is a list) if both segments have an intersection.
It means that they must include each other at list with one element.
"""
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not firstList or not secondList:
            return []
        l = r = 0
        result = []
        while l < len(firstList) and r < len(secondList):
            if firstList[l][0] > secondList[r][1]:
                r += 1
            elif firstList[l][1] < secondList[r][0]:
                l += 1
            else:
                result.append([max(firstList[l][0], secondList[r][0]),
                               min(firstList[l][1], secondList[r][1])])
                if firstList[l][1] > secondList[r][1]:
                    r += 1
                else:
                    l += 1
        return result
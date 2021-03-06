class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        seen = {}
        l = 0
        maximum = 0
        for r in range(len(s)):
            if s[r] not in seen:
                maximum = max(maximum, r - l + 1)
            else:
                if seen[s[r]] < l:
                    maximum = max(maximum, r - l + 1)
                else:
                    l = seen[s[r]] + 1
            seen[s[r]] = r
        return maximum

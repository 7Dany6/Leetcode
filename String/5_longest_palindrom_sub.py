class Solution:
    def longestPalindrome(self, s: str) -> str:
        cur_length = 0

        for i in range(len(s)):
            l = r = i  # this is a case for substring which length is odd
            while l >= 0 and r <= len(s) - 1 and s[l] == s[
                r]:  # until letters are equal and we haven't gone beyond of boarders
                if (r - l + 1) > cur_length:
                    substring = s[l:r + 1]
                    cur_length = r - l + 1
                l -= 1
                r += 1

        for i in range(len(s)):
            l, r = i, i + 1  # this is a case for substring which length is odd: look we say that our second pointer should point at the following character and that's the only difference
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                if (r - l + 1) > cur_length:
                    substring = s[l:r + 1]
                    cur_length = r - l + 1
                l -= 1
                r += 1

        return substring

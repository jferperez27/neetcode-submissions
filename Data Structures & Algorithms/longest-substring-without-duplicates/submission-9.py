class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cMap = {}
        maxLen = 0
        l = 0

        for r in range(len(s)):
            if s[r] in cMap:
                l = max(cMap[s[r]] + 1, l)
            cMap[s[r]] = r
            maxLen = max(maxLen, r - l + 1)

        return maxLen
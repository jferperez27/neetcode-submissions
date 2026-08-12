class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l = 0
        output = 0
        cMap = {} # val -> freq
        maxFreqLen = 0

        for r in range(len(s)):
            val = s[r]
            if val in cMap:
                cMap[val] += 1
            else:
                cMap[val] = 1

            maxFreqLen = max(maxFreqLen, cMap[val])

            while (r - l + 1) - maxFreqLen > k:
                cMap[s[l]] -= 1
                l += 1

            output = max(output, r - l + 1)

        return output
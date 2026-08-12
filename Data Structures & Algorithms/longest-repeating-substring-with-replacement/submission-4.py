class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cMap = {} # val -> index
        l = 0
        uniqueCount = []
        maxCount = 0
        output = 0
        uniqueIndex = 0

        for r in range(len(s)):
            v = s[r]
            if v in cMap:
                i = cMap[v]
                uniqueCount[i] += 1
                maxCount = max(maxCount, uniqueCount[i])
            else:
                cMap[v] = uniqueIndex
                uniqueCount.append(1)
                maxCount = max(maxCount, uniqueCount[uniqueIndex])
                uniqueIndex += 1
            
            while (r - l + 1) - maxCount > k:
                uniqueCount[cMap[s[l]]] -= 1
                l += 1
            output = max(output, r - l + 1)

        return output
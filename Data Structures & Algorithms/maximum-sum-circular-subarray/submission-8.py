class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globalMax = nums[0]
        globalMin = nums[0]
        currMax = 0
        currMin = 0
        total = 0

        for n in nums:
            total += n

            #Handle max
            currMax = max(currMax + n, n)
            globalMax = max(globalMax, currMax)

            #Handle min
            currMin = min(currMin + n, n)
            globalMin = min(globalMin, currMin)

        return max(globalMax, total - globalMin) if globalMax > 0 else globalMax


        
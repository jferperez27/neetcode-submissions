class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L, currSum = 0, 0
        length = float('inf')

        for R in range(len(nums)):
            currSum += nums[R]
            while currSum >= target:
                length = min(length, R-L+1)
                currSum -= nums[L]
                L += 1
        
        return 0 if length == float('inf') else length

        
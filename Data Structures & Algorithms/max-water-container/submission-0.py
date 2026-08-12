class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxContainer = 0
        l, r = 0, len(heights) - 1

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            maxContainer = max(maxContainer, area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return maxContainer
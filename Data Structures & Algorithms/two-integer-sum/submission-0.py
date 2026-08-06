class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        count = 0
        for num in nums:
            need = target - num
            if need in visited:
                ans = sorted([count, visited[need]])
                return ans
            else:
                visited[num] = count
            count += 1
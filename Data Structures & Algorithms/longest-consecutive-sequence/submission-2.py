class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()

        prev = None
        count = 0
        max_count = 0
        print(nums)
        for num in nums:
            if prev == None: #starting count
                prev = num
                count += 1
            else:
                if prev == num:
                    continue
                elif num == prev + 1:
                    count += 1
                    prev = num
                else:
                    max_count = max(count, max_count)
                    count = 1
                    prev = num
        return max(count,max_count)
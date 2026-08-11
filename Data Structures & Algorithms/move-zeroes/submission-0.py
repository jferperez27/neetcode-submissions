class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        to_remove = []
        index = 0
        for n in nums:
            if n == 0:
                to_remove.append(index)
            index += 1
        
        offset = 0
        for i in to_remove:
            nums.pop(i - offset)
            offset += 1
            nums.append(0)
            
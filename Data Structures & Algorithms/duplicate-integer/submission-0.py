class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numset = set()

        for num in nums:
            curr_len = len(numset)
            numset.add(num)
            if curr_len == len(numset):
                return True
        return False
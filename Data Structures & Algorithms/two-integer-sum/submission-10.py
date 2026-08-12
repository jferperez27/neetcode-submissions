class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i_map = {}
        i = 0

        for n in nums:
            if target - n in i_map:
                return [i_map[target-n], i]
                
            if n in i_map:
                i_map[n].append(i)
            else:
                i_map[n] = i

            i += 1
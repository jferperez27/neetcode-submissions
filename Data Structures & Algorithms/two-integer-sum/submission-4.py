class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexMap = {}
        currIndex = 0

        for n in nums:
            if target - n in indexMap:
                return [indexMap[target - n], currIndex]
            else:
                indexMap[n] = currIndex
                currIndex += 1
        return []



        dict = {
            3 : 0
        }

        x = dict[3]
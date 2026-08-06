import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        items = {}
        freq = [[] for i in range(len(nums) + 1)]
        
        for n in nums:
            items[n] = 1 + items.get(n, 0)
        for n, c in items.items():
            freq[c].append(n)
        
        output = []
        for n in range(len(freq) - 1, 0, -1):
            for num in freq[n]:
                output.append(num)
                if len(output) == k:
                    return output
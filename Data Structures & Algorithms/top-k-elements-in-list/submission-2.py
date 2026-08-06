import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        pairs = {}

        for num in nums:
            if num in pairs.keys():
                curr = pairs.get(num)
                pairs[num] = curr + 1
            else:
                pairs[num] = 1
        
        for key, value in pairs.items():
            heapq.heappush(heap, (value, key))

        return [item[1] for item in heapq.nlargest(k, heap)]
        
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = [] #empty list representing max-heap
        freq = dict()

        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1  #increment freq 
        
        for key, val in freq.items():
            if len(ans) < k:
                heapq.heappush(ans, [val,key])
            else:
                heapq.heappushpop(ans,[val, key])
        
        return [key for value, key in ans]
        
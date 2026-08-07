class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        groups = {}
        for i in range(len(nums)):
            num = nums[i]
            if num in groups:
                groups[num] += 1
            else:
                groups[num] = 1
        buckets = [[] for _ in range(len(nums)+1)]
        for num, freq in groups.items():
            buckets[freq].append(num)
        
        result = []

        for freq in range(len(buckets)-1,0,-1):
            for num in buckets[freq]:
                result.append(num)
                if len(result) == k:
                    return result
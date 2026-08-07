class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        groups = {}
        for i in range(len(nums)):
            num = nums[i]
            if num in groups:
                groups[num] += 1
            else:
                groups[num] = 1
        sorted_groups = sorted(groups, key= lambda x: groups[x], reverse=True)
        return sorted_groups[:k]        




class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for c in nums:
            count[c] = count.get(c, 0) + 1
        return max(count, key=count.get)

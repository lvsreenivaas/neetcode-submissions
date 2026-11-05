class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        for c in nums:
            count[c] = count.get(c,0) + 1
        
        threshold = len(nums) // 3
        
        # Return all numbers that appear MORE than n // 3 times
        return [num for num, freq in count.items() if freq > threshold]
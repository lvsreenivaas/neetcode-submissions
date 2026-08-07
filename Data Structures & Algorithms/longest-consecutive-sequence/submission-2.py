class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        new_list = set(nums)
        longest = 0

        for num in new_list:
            if num-1 not in new_list:
                current = num
                length = 1

                while current + 1 in new_list:
                    current += 1
                    length += 1
                
                longest = max(longest, length)
        return longest
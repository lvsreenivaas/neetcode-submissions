class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {} #Create an empty dictionary
        for c in nums: #loop through the dictionary
            count[c] = count.get(c, 0) + 1 #Add the number of values
        return max(count, key=count.get) #Return whichever has the highest count easy peasy
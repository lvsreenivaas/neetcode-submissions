class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        j = 0
        i = 0
        max_frequency = 0
        length = 0
        while j < len(s):
            count[s[j]] = count.get(s[j],0) + 1
            max_frequency = max(max_frequency,count[s[j]])    
            while(j-i+1) - max_frequency > k:
                count[s[i]] -= 1
                i += 1
            length = max(length, j-i+1)
            j += 1
        return length
                

        


        

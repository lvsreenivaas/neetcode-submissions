class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        i = 0
        j = 0
        seen = set()
        while j < len(s):
            if s[j] not in seen:
                seen.add(s[j])
                length = max(length,j-i+1)
                j+=1
            else:
                seen.remove(s[i])
                i += 1
        return length


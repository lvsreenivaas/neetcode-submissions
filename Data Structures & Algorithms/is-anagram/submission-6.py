class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            list_s = list(s)
            list_t = list(t)
            if sorted(list_s) == sorted(list_t):
                return True
            else: return False
        else:
            return False
class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_word = ""
        for ch in s:
            if ch.isalnum():
                clean_word += ch.lower()
            
        return clean_word == clean_word[::-1]
class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")": "(",
        "]": "[",
        "}": "{"
        }
        stack = []
        for ch in s:
            if ch in "([{":
                stack.append(ch)
            else:
                if not stack:
                    return False
                if ch in ")]}":
                    if stack[-1] != pairs[ch]:
                        return False
                    else:
                        stack.pop()
        return not stack
            
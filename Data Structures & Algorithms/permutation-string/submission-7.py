class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        count_s1 = {}
        count_window = {}

        for c in s1:
            count_s1[c] = count_s1.get(c, 0) + 1

        for c in s2[:len(s1)]:
            count_window[c] = count_window.get(c, 0) + 1

        if count_window == count_s1:
            return True

        i = 0
        j = len(s1)

        while j < len(s2):

            count_window[s2[i]] -= 1

            if count_window[s2[i]] == 0:
                del count_window[s2[i]]

            count_window[s2[j]] = count_window.get(s2[j], 0) + 1

            i += 1
            j += 1

            if count_window == count_s1:
                return True

        return False
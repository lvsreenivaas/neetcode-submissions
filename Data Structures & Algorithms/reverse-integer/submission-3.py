class Solution:

    def reverse(self, x: int) -> int:

        if x < 0:
            sign = -1
            rev_num = int(str(abs(x))[::-1])
            result = sign * rev_num

        else:
            rev_num = int(str(x)[::-1])
            result = rev_num
        if result > 2**31 or result < -2**31:
            return 0
        else:
            return result
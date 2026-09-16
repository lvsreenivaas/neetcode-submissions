class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        new_num = int("".join(map(str, digits)))
        resulting_num = new_num + 1
        
        str_num = str(resulting_num)
        result = [int(c) for c in str_num]

        return result
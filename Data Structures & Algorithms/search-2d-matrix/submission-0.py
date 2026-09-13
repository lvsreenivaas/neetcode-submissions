import itertools

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flat_list = list(itertools.chain.from_iterable(matrix))
        for i in range(len(flat_list)):
            if flat_list[i] == target:
                return True
        else:
            return False        
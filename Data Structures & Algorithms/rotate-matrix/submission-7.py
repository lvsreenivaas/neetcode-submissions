class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        i = 0
        for v in zip(*matrix):
            matrix[i] = v[::-1]
            i+=1
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rotate(mat):
            mat.reverse()
            for i in range(len(mat)):
                for j in range(i):
                    mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
        for i in range(4):
            if mat==target:
                return True
            rotate(mat)
        return False
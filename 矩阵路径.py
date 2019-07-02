#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
题目描述
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。
如果一条路径经过了矩阵中的某一个格子，则之后不能再次进入这个格子。 
例如 abcesfcsadee这样的3 X 4 矩阵中包含一条字符串"bcced"的路径,但是矩阵中不包含"abcb"路径,
因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。

"""

#**************************此算法只能解决路径是否存在，无法计算路径条数****************************************
class Solution:
    def hasPath(self, matrix, rows, cols, path):

        if not matrix:
            return False
        if not path:
            return True
        x = [list(matrix[cols * i:cols * i + cols]) for i in range(rows)]
        print x
        for i in range(rows):
            for j in range(cols):
                if self.exist_helper(x, i, j, path):
                    return True
        return False

    def exist_helper(self, matrix, i, j, p):
        if matrix[i][j] == p[0]:
            if not p[1:]:
                return True
            matrix[i][j] = ''
            if i > 0 and self.exist_helper(matrix, i - 1, j, p[1:]):
                return True
            if i < len(matrix) - 1 and self.exist_helper(matrix, i + 1, j, p[1:]):
                return True
            if j > 0 and self.exist_helper(matrix, i, j - 1, p[1:]):
                return True
            if j < len(matrix[0]) - 1 and self.exist_helper(matrix, i, j + 1, p[1:]):
                return True
            matrix[i][j] = p[0]
            return False
        else:
            return False
        
        
if __name__ == "__main__":
    #t = Solution()
    #t.hasPath("ABCESFCEADED",3,4,"ABCCED")

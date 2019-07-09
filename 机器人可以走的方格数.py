#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，
但是不能进入行坐标和列坐标的数位之和大于k的格子。 例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。
但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？
"""


class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        #matrix = [range(i*cols, i*cols+cols+1) for i in range(rows)]
        
        stack = [(0, 0)]
        count = 0
        tmp = []
        while stack:
            tmp += stack
            x, y = stack.pop(-1)
            if sum([int(i) for i in list(str(x))]) + sum([int(j) for j in list(str(y))]) <= threshold:
                count += 1
                if x > 0:
                    if (x-1, y) not in tmp:
                        stack.append((x-1, y))
                if x < rows-1:
                    if (x+1, y) not in tmp:
                        stack.append((x+1, y))
                if y > 0:
                    if (x, y-1) not in tmp:
                        stack.append((x, y-1))
                if y < cols-1:
                    if (x, y+1) not in tmp:
                        stack.append((x, y+1))
        return count
        

if __name__ == '__main__':
    t = Soulution()
    t.movingCount()

#!/usr/bin/python
# -*- coding: utf-8 -*-


"""方法一【Fibonacci数列】"""
"""解决上楼梯问题【每次走1或2步】"""
def  Fibonacci(n):
    if n == 1:
        return 1
    v1 = 1
    v2 = 2
    for i in range(3, n+1):
        v1, v2= v2, v1 + v2
    return v2 

"""方法二【递归分两步走】"""
def  climb_Stairs(i, n):
    if i > n:
        return 0
    if i == n:
        return 1
    return  climb_Stairs(i+1, n) + climb_Stairs(i+2, n)

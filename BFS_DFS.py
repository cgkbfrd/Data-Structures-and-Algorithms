#!/usr/bin/env python
# -*- coding: utf-8 -*-


def test(start):
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'C', 'D'],
        'C': ['A', 'B', 'D', 'E'],
        'D': ['B', 'E', 'F'],
        'E': ['C', 'D'],
        'F': ['D']
    }
    queue = [start]
    tmp = []
    res = {start:None}  #记录上一级父节点
    while queue:
        node = queue.pop()
        tmp.append(node)
        for i in graph[node]:
            if i not in queue and i not in tmp:
                queue.append(i)
                res[i] = node

    endpoint = 'F' #假设要到达的节点为‘F’
    while endpoint:
        print endpoint
        endpoint = res[point]


if __name__ == "__main__":
    test('A')

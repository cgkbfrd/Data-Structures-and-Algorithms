#!/usr/bin/python
# -*- coding: utf-8 -*-


class Node(object):
    def __init__(self, elem = None):
        """构架节点"""
        self.elem = elem
        self.next = None
        
        
class Link_list(object):
    def __init__(self, head = None):
        """初始化头结点"""
        self.head = head
        
    def add(node):
    """添加节点"""
        pass
        
    def remove(elem)
        """删除节点"""
            pass
                                
    def reverse(head):
        """反转链表"""
        if head is None or head.next is None:
            return head
        p = reverse(head.next)
        head.next.next = head
        head.next = None
        return p

#!/usr/bin/python
# coding: utf-8
"""还有一种方法可以将两个链表的所有元素提取出来排序在生成新的链表"""

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = None
        cur_node = head
        while l1 and l2:
            if head is None:
                if l1.val <= l2.val:
                    head = ListNode(l1.val)
                    l1 = l1.next
                else:
                    head = ListNode(l2.val)
                    l2 = l2.next 
                cur_node = head
            if l1 and l2:
                if l1.val <= l2.val:
                    cur_node.next = ListNode(l1.val)
                    cur_node = cur_node.next
                    l1 = l1.next
                else:
                    cur_node.next = ListNode(l2.val)
                    cur_node = cur_node.next
                    l2 = l2.next 
        if l1:
            if head:
                cur_node.next = l1
            else:
                head = l1
            
        if l2:
            if head:
                cur_node.next = l2
            else:
                head = l2
        return head
        

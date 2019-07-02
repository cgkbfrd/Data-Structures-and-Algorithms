#!/usr/bin/env python
# -*- coding: utf-8 -*-

def test(ss, count, k):
    if count == k-1:
        return ss
    tmp = ss[:]
    for s in ss:
        s = s[:]
        v = 1
        for i in range(count+1, k):
            if s[i] not in s[count:count+v]:
                s[count], s[i] = s[i], s[count]
                tmp.append(s)
                s[count], s[i] = s[i], s[count]
                v += 1

    return test(tmp, count+1, k)


if __name__ == "__main__":
    #t = Solution()
    #t.hasPath("ABCESFCEADED",3,4,"ABCCED")
    con = [['a', 'b', 'c', 'b']]
    k = len(con[0])
    for i in test(con, 0, k):
        print i

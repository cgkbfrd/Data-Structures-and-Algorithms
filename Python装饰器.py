#!/usr/bin/python
# -*- coding: utf-8 -*-
from functools import wraps

def makeitalic(func):
    @wrapps(func)
    def wrapped(*args, **kwargs):
        ret = func(*args, **kwargs)
        return '<i>' + ret + '</i>'
    return wrapped

@makeitalic
def hello(name):
    return 'hello %s' % name

@makeitalic
def hello2(name1, name2):
    return 'hello %s, %s' % (name1, name2)
    

if __name == '__main__':
    a = hello  #此时返回的是函数wrapped
    b = hello("Python")  #此时将返回的函数wrapped进一步执行wrapped("Python")，相当于走了两步，b是返回函数wrapped执行的结果

# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 16:37:46 2020

@author: guguoqiang
"""
import heapq
def f(a,k):
    if a==None:
        return 'error'
    l=len(a)
    if k>l or k<=0:
        return 'error'
    heapq.heapify(a)
    m=0
    while a:
        t=heapq.heappop(a)
        if k==l:
            return t
        m+=1
        if m==l-k:
            break
    return heapq.heappop(a)
a=None
k=2
print(f(a,k))

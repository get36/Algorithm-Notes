# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 16:49:29 2020

@author: guguoqiang
"""

class heap():
    def __init__(self):
        self.temp=[]
    def get_parent_index(self,index):
        if index==0:
            return 0
        else:
            return (index-1)//2
    def swap(self,a,b):
        self.temp[a],self.temp[b]=self.temp[b],self.temp[a]
    def insert(self,num):
        self.temp.append(num)
        index=len(self.temp)-1
        parent_index=self.get_parent_index(index)
        while self.temp[index]>self.temp[parent_index]:
            self.swap(index,parent_index)
            index=parent_index
            parent_index=self.get_parent_index(index)
    def remove(self):
        t=self.temp[0]
        self.temp[0]=self.temp[-1]
        self.temp.pop()
        total_index=len(self.temp)-1
        index=0
        maxindex=0
        while True:
            maxindex=index
            maxindex1=index
            maxindex2=index
            if 2*index+1<=total_index and self.temp[2*index+1]>self.temp[index]:
                maxindex1=2*index+1
            if 2*index+2<=total_index and self.temp[2*index+2]>self.temp[index]:
                maxindex2=2*index+2
            maxindex=max(maxindex1,maxindex2)
            if index==maxindex:
                break
            self.swap(index,maxindex)
            index=maxindex
        return t
h=heap()
h.insert(3)
h.insert(5)
h.insert(1)
h.remove()
for i in h.temp:
    print(i)
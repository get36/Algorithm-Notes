# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def merge(s,left,mid,right):
    temp=[]
    i=left
    j=mid+1
    while i<=mid and j<=right:
        if s[i]<s[j]:
            temp.append(s[i])
            i+=1
        else:
            temp.append(s[j])
            j+=1
    while i<=mid:
        temp.append(s[i])
        i+=1
    while j<=right:
        temp.append(s[j])
        j+=1
    for i in range(left,right+1):
        s[i]=temp[i-left]
    return 
def mergesort(s,left,right):
    if left<0 or right>=len(s):
        return
    if right<=left:
        return
    elif right-left==1:
        if s[left]>s[right]:
            s[left],s[right]=s[right],s[left]
        return
    else:
        mergesort(s,left,(left+right)//2)
        mergesort(s,(left+right)//2+1,right)
        merge(s,left,(left+right)//2,right)
s=[2,0,4,1,5,3,7,6]
mergesort(s,0,7)
print(s)
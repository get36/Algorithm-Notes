# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def getnext(s):
    n=[0]*len(s)
    j=-1
    n[0]=-1
    for i in range(1,len(s),1):
        while s[j+1]!=s[i] and j!=-1:
            j=n[j]
        if j==-1 and s[j+1]==s[i]:
            n[i]=j+1
        if j==-1 and s[j+1]!=s[i]:
            n[i]=-1
        if j!=-1 and s[j+1]==s[i]:
            n[i]=j+1
        j=n[i]
    return n
def kmp(text,pattern,nex):
    n=len(text)
    m=len(pattern)
    j=-1
    for i in range(n):
        while text[i]!=pattern[j+1] and j!=-1:
            j=nex[j]
        if text[i]==pattern[j+1]:
            j+=1
            
        if j==m-1:
            return True
    return False
text="abababaabc"
pattern="ababaab"
nex=getnext(pattern)
print(nex)
print(kmp(text,pattern,nex))
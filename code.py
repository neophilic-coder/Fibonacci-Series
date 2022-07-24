#!/usr/bin/env python
# coding: utf-8

# In[9]:


#fibonacci series using for loop
n=int(input("Enter the number upto which you want the sequence: "))
fib=[0,1]

if n>2:
    for i in range (2,n):
        new = fib[i-1]+fib[i-2]
        fib.append(new)
print("Fibonacci series is:",fib)


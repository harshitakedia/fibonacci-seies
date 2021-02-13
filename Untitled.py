#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Function for fibonacci series
def fibo(n) :
    #check if n is valid
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return (fibo(n-1) + fibo(n-2))


# In[4]:


#driver program to print fibonacci series
n = int(input("enter a value : "))
print("fibonacci series: ", end = ' ')
for n in range(0,n):
    print(fibo(n),end = ' ')
    


# In[ ]:





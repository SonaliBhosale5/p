#!/usr/bin/env python
# coding: utf-8

# # write a program which will find all such no which are divisble by 7 but not multiple of 5,between 2000 and 3200.the no should  be printed in comma seperated sequence on a single line

# In[1]:


for i in range(2000, 3200):
    if(not i%7 and i%5):
        print(i, end=",")


# # write a python program to accept the users first & last name then getting them printed in the reverse order with space beween first & last name

# In[2]:


firstname = input("enter ur firstname:")


# In[3]:


lastname = input("enter ur lasttname:")


# In[5]:


print(firstname[::-1] + " " + lastname[::-1] )


# # write a prog o find the volume f a sphare with diameter 12cm

# In[9]:


pi = 3.1415926535897931
r= 6.0
V= 4.0/3.0*pi* r**3
print('The volume of the sphere is: ',V)


# # create below pattern using nested loop in python
# # *
# # **
# # ***
# # ****
# # *****
# # ****
# # ***
# # **
# # *

# In[10]:


n=5;
for i in range(n):
    for j in range(i):
        print ('* ', end="")
    print('')

for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')


# # write a prog to reverse a word after accepting the input from the user 

# In[11]:


word = input("Input a word to reverse: ")
for char in range(len(word) - 1, -1, -1):
  print(word[char], end="")
print("\n")


# In[15]:


print("WE, THE PEOPLE OF INDIA,\n\thaving solemnly resolved to constitute India into a SOVEREIGN,! \n\t\tSOCIALIST, SECULAR, DEMOCRATIC REPUBLIC \n\t\t and to secure to all its citizens")


# In[ ]:





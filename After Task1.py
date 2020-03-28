#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Task 2
str1 = "Welcome to Python"

print('to' in str1)


# In[3]:


#Task 3
# .count() method calculates total occurance of given elements inside the list
# syntax : list.count(elements)

char1 = ['a', 'a', 'b', 'c', 'd', 'a']

count1 = char1.count('a')

# print count
print('The count of a is:', count1)

# count element 'e'
count1 = char1.count('e')

# print count
print('The count of e is:', count1)


# In[5]:


# remove() method removed element that is mentioned using listname and element
# syntax : list.remove(element)

list1 = [2.3, 4.4, 3, 5.3, 1.0, 2.5]
print(list1)
list1.remove(3)
print(list1)


# In[6]:


# clear() method removes all items from the list 

list2 = [1,2,3,4,5]

list2.clear()
print('list2 : ', list2)


# In[7]:


# reverse() methodreverses the elements of a given list 
# syntax : list.reverse()

os = ['Windows', 'Macos', 'Linux', 'Ubuntu']

os.reverse()

print('Updated List : ', os)


# In[8]:


# sort() method sorts the element of given list 
# syntax : list.sort()

vowels = ['i', 'a', 'u', 'o', 'e']

vowels.sort()
print('Sorted List : ', vowels)


# In[11]:


# Task 4
# Using workaround 'add' or 'remove' values in Tuple
# add
tup1 = (1,2,3)
print(tup1)

#convert to list
list1 = list(tup1)
print(list1)

# change the value
list1.append(4)

# again change back to Tuple
tup1 = tuple(list1)
print(tup1)


# In[13]:


# remove
tup1 = (1,2,3,4)
print(tup1)

#convert to list
list2 = list(tup1)
print(list2)

# change the value
list2.remove(4)

# again change back to Tuple
tup1 = tuple(list2)
print(tup1)


# In[14]:


# Task 5
# difference() method in  sets returns set difference of two sets
# If A & B are two sets. The set difference of A & B is a set of elements that exist only in set A but not in B and vice versa

A = {'a', 'b', 'c', 'd'}
B = {'c', 'f', 'g'}

# Equivallent to A-B
print(A.difference(B))

# Equivallent to B-A
print(B.difference(A))


# In[16]:


# symmetric difference() method in sets return the smmetric difference of 2 sets

A = {'a', 'b', 'c', 'd'}
B = {'c', 'd', 'e'}

print(A.symmetric_difference(B))
print(B.symmetric_difference(A))


# In[21]:


# Task 6
# Calculator 

num1 = float(input("Enter Number 1 : "))
num2 = float(input("Enter Number 2 : "))

choice = input("Enter choice(1/2/3/4) : ")

add = num1 + num2
subtract = num1 - num2
multiply = num1 * num2
divide = num1 / num2

if choice == '1' : 
    print(num1, "+", num2, "=", add)
elif choice == '2' : 
    print(num1, "-", num2, "=", subtract)
elif choice == '3' : 
    print(num1, "*", num2, "=", multiply)
elif choice == '4' : 
    print(num1, "/", num2, "=", divide)
else :
    print("Invalid Syntax")


# In[24]:


# Task 7
# Use Recursion to print numbers from 1 to 10 without using loops

def my_func(i):
    i = i+1
    if(i>10):
        return
    else:
        print(i)
        my_func(i)

my_func(0)
        


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Task1
# some other methods in string
# isalnum() : returns True if all characters in string are alpha numeric else returns False

name = "Gautam345"
print(name.isalnum())

# contains whitespace
name = "M3onica G4stamb1d3 "
print(name.isalnum())

name = "Naman127"
print(name.isalnum())

name = "133"
print(name.isalnum())


# In[4]:


# isupper() method returns true if all the characters in the string are uppercase
# example string
string = "WELCOME TO PYTHON"
print(string.isupper());

# numbers in place of alphabets
string = "W3LC0ME T0 STRINGS"
print(string.isupper());

# lowercase string
string = "HOw ARE yOU DOING?" 
print(string.isupper());


# In[ ]:


# strip() removes leading and trailing white spaces from the string also we can remove characters using this method
string = ' Welcome to strip() method   '

# Leading whitepsace are removed
print(string.strip())

# Specifying what character to be removed

string = 'android is awesome'
print(string.strip('an'))


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# # Langdon Hatton
# 
# ## Cs-150-01
# 
# ## Chapter 3 in class notebook
# 
# ## Version 1
# 

# ## Chapter 3 Lists 
# * Lists are used to store multiple items in a single variable.
# 
# * Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are **Tuple, Set, and Dictionary**, all with different qualities and usage.
# 
# * Lists are created using square brackets
# 
# ![image.png](attachment:image.png)

# In[1]:


data="PROGRAMMING"
type(data)


# In[2]:


data_list=list(data)
data_list


# In[3]:


type(data_list)


# In[4]:


data_list[0]


# In[5]:


data_list[3]


# In[6]:


data_list[8]


# In[7]:


data_list[-1] #last index is -1 or you can count


# In[8]:


data_list[-2] #second to last -2 two and so on, or you can count and use positive. it starts with 0 on positive


# In[9]:


data_list[9]


# In[ ]:





# In[ ]:





# ### Lists do not have to contain only one data type. The example below contains both strings and integers.

# In[10]:


list_new=[12,34,67,68, 'Hello' , 'Class' , 67.88, 42.66]


# In[11]:


print(type(list_new[0]))
print(type(list_new[4]))
print(type(list_new[-2]))


# In[12]:


print('The printing statement is',list_new[-4])


# ## Practice 1
# ### Names: Store the names of a few of your friends in a list called names. Print each person’s name and a message to them by accessing each element in the list, one at a time.
# 

# In[13]:


names=['Braden', 'Dalton', 'Henry']


# In[14]:


print('What is up' , names[0], '?')


# In[15]:


print('Hi' , names[1])


# In[16]:


print('Hello' , names[-1])


# ## Changing, Adding, and Removing Elements

# #### Changing

# In[17]:


numbers=[12,45,67,89,32,65,100,99]


# In[18]:


#update the first number from 12 to 11 
numbers[0]=11


# In[19]:


print(numbers[0])


# In[20]:


numbers[-1]=100
print(numbers[-1])


# In[ ]:





# In[ ]:





# #### Adding
# * append

# In[21]:


numbers_new=[]
type(numbers_new)


# In[22]:


numbers_new.append(10)


# In[23]:


print(numbers_new)


# In[24]:


numbers_new.append(20)
numbers_new.append(30)
numbers_new.append(40)
numbers_new.append(50)
numbers_new.append(60)
print(numbers_new)


# In[25]:


car=[]
car.append('Toyota')
car.append('Honda')
car.append('Ford')
car.append('Mazda')
car


# In[ ]:





# #### Inserting Elements into a List
# * insert

# In[26]:


car.insert(0, 'Bmw')
car


# In[27]:


car.append('Audi')


# In[28]:


car #append goes to the end of the list but insert you put the place you want it to go


# #### Removing Elements from a List
# * del
# * pop
# * remove

# In[29]:


car


# In[30]:


del car[0]


# In[31]:


car


# In[32]:


del car[2]


# In[33]:


deleted_car= car.pop(2)
print('The deleted cars is' , deleted_car)


# In[34]:


car


# In[35]:


car.remove('Honda')


# In[36]:


car.remove('Toyota')
car.remove('Audi')


# In[37]:


car


# ### Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite?
# * Create an empty list called `Guest_list`.
# * Includes at least three people you’d like to invite to dinner using `append`. Then use your list to print a message to each person, inviting them to dinner.
# 

# In[38]:


Guest_list=[]


# In[39]:


Guest_list.append("Bob")
Guest_list.append('John')
Guest_list.append('Bill')
print('Would you like to attend my dinner,' , Guest_list[0], '?')
print('Please come to my dinner' ,Guest_list[1], '.')
print('Are you coming to my dinner', Guest_list[2], '.')


# In[ ]:





# In[ ]:





# In[ ]:





# ### Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.
# * Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
# * Print a second set of invitation messages, one for each person who is still in your list.
# * e.g. print("Hello" + guest_list[1] + "You are still invited" )

# In[40]:


Guest_list[0]='Billy'


# In[41]:


print('Hello' , Guest_list[0], 'you are invited to my dinner')


# In[42]:


print('Hello' , Guest_list[1], 'you are still invited.')


# In[43]:


print('Hello' , Guest_list[2], 'you are still invited.')


# ### More Guests: You just found a bigger dinner table, so now more space is available. Think of two more guests to invite to dinner.
# * Use insert() to add one new guest to the beginning of your list.
# * Use insert() to add one new guest to the middle of your list.
# * Use append() to add one new guest to the end of your list.
# * Print a new set of invitation messages, one for each person in your list.

# In[44]:


Guest_list.insert(0, 'Zach')
Guest_list.insert(2, 'Josiah')
Guest_list.append('Devin')


# In[45]:


Guest_list


# In[46]:


print('Hello, you,' ,Guest_list[0], 'are invited to my dinner')
print('Hello, you,' ,Guest_list[1], 'are invited to my dinner')
print('Hello, you,' ,Guest_list[2], 'are invited to my dinner')
print('Hello, you,' ,Guest_list[3], 'are invited to my dinner')
print('Hello, you,' ,Guest_list[4], 'are invited to my dinner')
print('Hello, you,' ,Guest_list[5], 'are invited to my dinner')


# In[47]:


Guest_list


# ### Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.
# * Add a new line that prints a message saying that you can invite only two people for dinner.
# * Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
# * Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.

# In[48]:


print('Sorry, but only two guest can come to dinner')


# In[ ]:





# In[49]:


name1=Guest_list.pop(0)
print("Sorry but there is no longer space for you, " + name1 + ' at dinner.')


# In[ ]:





# In[50]:


name2=Guest_list.pop(0)
print("Sorry but there is no longer space for you, " +name2 + ' at dinner')


# In[ ]:





# In[51]:


name3=Guest_list.pop(0)
print("Sorry but there is no longer space for you, " + name3 + ' at dinner.')


# In[ ]:





# In[52]:


name4=Guest_list.pop(0)
print("Sorry but there is no longer space for you, " + name4 + ' at dinner.')


# In[53]:


del Guest_list[0]


# In[54]:


del Guest_list[0]


# In[55]:


Guest_list


# In[ ]:





# ## Organizing a List

# ### Sorting a List Permanently with the sort() Method

# In[56]:


car.append('Honda')
car.append('Audi')
car.append('Mazda')


# In[57]:


car.sort()


# In[58]:


car


# In[59]:


car.sort(reverse=True)
car


# ### Sorting a List Temporarily with the sorted() Function

# In[60]:


car


# In[62]:


sorted(car)


# In[63]:


car


# ### Printing a List in Reverse Order

# In[64]:


car


# In[65]:


car.reverse()


# In[66]:


car


# In[ ]:





# ### Finding the Length of a List

# In[68]:


len(car)


# In[ ]:





# ### Slicing Lists
# Python provides several different ways to get "slices" of data from a list. That is, ways to extract particular elements from lists.

# In[69]:


numbers=[10,20,30,40,50,60,70,80,90,100]


# In[74]:


# select sequential elements from the list
numbers[0:4]
#the last element is not included, here it is just 0 , 1 , 2, 3


# In[76]:


#print all the elements from beginning to the seventh index
numbers[0:8]


# In[79]:


#print up to index -1
numbers[:11]


# In[78]:


#start at the beginning and print up to the end
numbers[7:]


# In[81]:


# replace the list with new data
numbers
numbers[:3]=[200,200,200]


# In[82]:


numbers


# In[84]:


#print elements in steps
numbers[::2]


# In[85]:


numbers[::3]


# In[86]:


numbers[3::3]


# In[87]:


#Create a list of names of six poeple then we will slice it
names=['Tom', 'Harry', 'Megan', 'Jess', 'Ron', 'Sam']


# In[89]:


#sort the list temporarilly
new_names=sorted(names)
new_names


# In[90]:


new_names[0:3]


# In[91]:


new_names[3:5]


# In[94]:


new_names[::2]


# In[ ]:





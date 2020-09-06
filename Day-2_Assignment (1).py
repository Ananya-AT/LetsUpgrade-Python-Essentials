#!/usr/bin/env python
# coding: utf-8

# # Lists

# In[1]:


lst = ["Krishna",5,10,25.5,[8,9,10]]


# In[2]:


lst


# In[3]:


lst.append("radha")


# In[4]:


lst


# In[5]:


lst.index(5)


# In[6]:


lst.copy()


# In[8]:


lst.count(10)


# In[12]:


lst.insert(4,11)


# In[13]:


lst


# In[14]:


abc=["mango","apple","orange"]
lst.extend(abc)


# In[15]:


lst


# In[16]:


lst.pop(2)


# In[17]:


lst


# In[18]:


lst.reverse()


# In[19]:


lst


# In[21]:


lst


# # Dictionary

# In[22]:


dit={"name":"Ananya","age":"19","rollno":317,"food":"pizza","game":"badminiton"}


# In[23]:


dit


# In[24]:


len(dit)


# In[25]:


str(dit)


# In[26]:


type(dit)


# In[27]:


dit.copy()


# In[28]:


dit.items()


# In[29]:


dit.keys()


# In[30]:


dit.values()


# In[31]:


dit.get('rollno')


# # Sets

# In[32]:


st = {"mohan","shyam","silicon",10,20,30,40,50,20,10,90,30}


# In[33]:


st


# In[34]:


st.add("apple")


# In[35]:


st


# In[36]:


st.discard("silicon")


# In[37]:


st


# In[38]:


st1={"ananya",2}


# In[39]:


st1


# In[40]:


st


# In[41]:


st1.issubset(st)


# In[42]:


st.pop()


# In[43]:


st


# In[44]:


st.copy()


# In[45]:


st


# # Tuple

# In[46]:


tup = ("rushav","is","a","good","boy")


# In[47]:


tup


# In[52]:


tup.count("is")


# In[53]:


tup.index("boy")


# In[56]:


len(tup)


# In[57]:


min(tup)


# In[58]:


max(tup)


# In[60]:


tup2=("ananya","is","a","friendly","girl")


# In[61]:


tup2


# # Strings

# In[63]:


txt = "hello, and welcome to LetsUpgrade"


# In[64]:


txt


# In[65]:


x= txt.capitalize()


# In[66]:


x


# In[69]:


x=txt.find("welcome")
print(x)


# In[70]:


x = txt.index("LetsUpgrade")


# In[71]:


x


# In[72]:


x= txt.lower()


# In[73]:


x


# In[76]:


x= txt.replace("LetsUpgrade","Python Course")


# In[77]:


x


# In[79]:


txt


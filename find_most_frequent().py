
# coding: utf-8

# In[13]:


def find_most_frequent(s):
    l = '' 
    l2 = [] 
    s = s.lower()
    
    for i in s:
        if i.isalnum() != True:
            l = l + " "
        else: l= l + i
    for i in l.split():
        if l.count(i)>1: 
            l2.append(i)
        elif len(l2) == 0: 
            return(l2)
        
    l={}
    for i in l2:
        if l2.count(i) not in l:
            l[l2.count(i)]=[i]
        elif l2.count(i) in l:
            l[l2.count(i)].append(i)
            
    try:
        l2 = set(l2)
        return(l2)
    
    except IndexError:
        return([])





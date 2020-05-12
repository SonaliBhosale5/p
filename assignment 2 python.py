#!/usr/bin/env python
# coding: utf-8

#  # write a python prog to implement ur own myreduce() fun which works exactly like pythons built in function reduce()

# 
# # write a python prog to implement ur own myfilter() fun which works exactly like pythons built in function filter()

# In[7]:



def myreduce(anyfunc, sequence):

  result = sequence[0]

  for item in sequence[1:]:
   result = anyfunc(result, item)

  return result


 
def myfilter(anyfunc, sequence):


 result = []

 for item in sequence:
  if anyfunc(item):
   result.append(item)


 return result


def sum(x,y): return x + y


def ispositive(x):
 if (x <= 0): 
  return False 
 else: 
  return True


print ("Sum on list [1,2,3] using custom reduce function "   + str(myreduce(sum, [1,2,3])) )
print ("Filter only positive Integers on list [0,1,-2,3,4,5] using custom filter function"  + str(myfilter(ispositive, [0,1,-2,3,4,5])))


# In[8]:


# implements list comprehensions to produce the followinglist write list compre to produce foolowing list
# ['A','C','A','D','G','I','L','D']
#['X','XX','XXX','XXXX','Y','YY','YYY','YYYY','Z','ZZ','ZZZ','ZZZZ']
#['x','y','z','xx','yy','zz','xxx','yyy','zzz']...


# In[9]:


word = "ACADGILD"
alphabet_list = [ alphabet for alphabet in word ]
print ("ACADGILD => " + str(alphabet_list))


# Compress above for loop into a single list comprehension using technique [i <Upper for condition> <lower for condition>]
input_list = ['x','y','z']
result = [ item*num for item in input_list for num in range(1,5)  ]
print("['x','y','z'] => " +   str(result))


input_list = ['x','y','z']
result = [ item*num for num in range(1,5) for item in input_list  ]
print("['x','y','z'] => " +   str(result))


input_list = [2,3,4]
result = [ [item+num] for item in input_list for num in range(0,3)]
print("[2,3,4] =>" +  str(result))


input_list = [2,3,4,5]
result = [ [item+num for item in input_list] for num in range(0,4)  ]
print("[2,3,4,5] =>" +  str(result))


input_list=[1,2,3]
result = [ (b,a) for a in input_list for b in input_list]
print("[1,2,3] =>" +  str(result))


# In[10]:


# implements fun longestword() that takes list of words and returns longest one


# In[17]:


def find_longest_word(words_list):
    word_len = []
    for n in words_list:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1][1]

print(find_longest_word(["python", "java", "datascience"]))


# In[18]:


# write a python prog with class concept to find area of triangle using below formula area=(s*(s-a)*(s-b)*(s-c)**0.5)


# In[20]:


a=int(input("Enter first side: "))
b=int(input("Enter second side: "))
c=int(input("Enter third side: "))
s=(a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print("Area of the triangle is: ",round(area,2))


# In[21]:


# write a function filter_long_words() that takes list of words and an integer n returns the list of words that are longer than n


# In[25]:


def filter_long_words(inputList,inputInteger):
 
    listOfWords = []
 
    for i in range(len(inputList)):
        if len(inputList[i]) > inputInteger:
            listOfWords.append(inputList[i])
 
    return listOfWords
 
inputListOfWords = ['wordOne','wordTwo','wordThree','wordFour','wordFive']
inputWordLength = 7
 
print (str(filter_long_words(inputListOfWords,inputWordLength)))


# In[26]:


# write a python function which takes a charchter (i.e string of length 1) and returns true if its is a vowel.false otherwise


# In[29]:


def is_vowel(char):
    all_vowels = 'aeiou'
    return char in all_vowels
print(is_vowel('c'))
print(is_vowel('e'))
    


# In[ ]:





---
redirect_from:
  - "/02-variables/exercise/questions"
interact_link: content/02_variables/exercise/questions.ipynb
kernel_name: python3
has_widgets: false
title: '02 variables'
prev_page:
  url: /01_intro/notebooks/trying_out_python.html
  title: 'Trying Out Python'
next_page:
  url: /02_variables/exercise/questions.html
  title: 'exercise'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-python/blob/master/content/02_variables/exercise/questions.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




# basic values and types
1. calculate `2+8` and put the result in tha variable `x`. 
   - print the value of `x`
     > hint: use the function `print()`
   - what is the type of `x`?
     > hint: use the function `type()`
2. calculate `5 / 2` and put the result in the variable `y`. print `y` and the type of `y`
3. put `"hello world"` into a variable named _`greeting`_. 
   - print the variable and the type of the variable
   - what is the `len` of _`greeting`_?
     > hint: use the function `len()`
4. put the values `1`, `2` and `3` into _`list1`_ and the values `"a"`, `"b"` and `"c"` into _`list2`_.
   - calcluate _`list1`_ + _`list2`_ and put the result into _`list3`_
    - print _`list3`_ 
    - print the `type` of _`list3`_
    - print the `len` of _`list3`_
    



# getting help
suppose we want to understand how to use a function. we can use the `help()` function for that!

1. let's try to use the function _`str.upper()`_, by copying this code below and running it:
```python
print( "hello".upper() )
```
2. lets see how to get help for a function. type the following code into a cell below. this will explain what the function _`str.upper`_ does
```python
help("hello".upper)
```





# some simple string functions
1. lets get help for __all__ the cool functions the type _`str`_ has. lets call `help(str)`. run the following code:
```python
help(str)
```

2. read the documentation you've just printed, for the following functions: 
`lower, upper, title, islower, isupper` and try to figure out what they do. you can try to use them, read the documentation again, google for them. anything that helps you understand.

3. convert this string to uppercase
`"the quick brown fox jumped over the lazy dog"`
> hint: use one of the functions you've learned in question #2

4. is the string `"I JusT mEt YoU, anD tHIs is CraaZy, sO CAll mE mayBe"` in lower case? can you convert it to lower case?
> hints :
> 1. there is a function that checks if a string is lower case
> 2. there is a function that converts a string to lower case



# help for str.split() function
print the `help` for the function _`str.split`_
> hint: use the `help()` function



# split a string

1. create the following string, and put it in a variable called `sent`
```
"the quick brown fox jumped over the lazy dog"
```

2.  then **split** it into a list 
    so that each word is an an element in the list. <br> 
    and put the result into another variable called `words`
    
   
3. print the variable `words`

expected ouput:
```
['the', 'quick', 'brown', 'fox', 'jumped', 'over', 'the', 'lazy', 'dog']
```



# str.join()

1. use the function `help` to read the documentation for the str.join function
1. read this code
```
mylist = ["one", "two", "three"]
result = " ".join(mylist)
print(result)
```
   1. can you guess what this code does ? 
   1. what is the function join?
   1. use help or documentation online if you can't guess
   1. copy this code to the cell below and run it to see if you were right




# using str.upper() and str.join()

1. split the sentence `"the quick brown fox jumped over the lazy dog"` into words using the function .split() 
   and put the result in a variable called `words` .
   

2. replace the the words "dog" and "fox" in the `words` list with *uppercase* "DOG" and "FOX" <br>

   HINTS:
   * use the .upper() function
   * use indexing like `words[3]` to acccess a particular word in the `words` list
   
   
3. use the function join to convert the list back into a string


4. print the result
   
expected output:
```
"the quick brown FOX jumped over the lazy DOG"
```



# 7 boom
use the following code, which puts an important string in a variable named _`song`_ 
```python
song = """
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
"""
```
now replace the 7th, 14th, 21st, 28th word with the word "boom"

print the result

[![This is important](https://cdn.instructables.com/FJI/WGSW/FPIUQQ3K/FJIWGSWFPIUQQ3K.LARGE.jpg?auto=webp&frame=1&width=320)](https://www.youtube.com/watch?v=dQw4w9WgXcQ "Everything Is AWESOME")



# Dictionary

1. create a dictionary that maps the name of cheeses to prices of 100mg of that cheese.

        gouda costs 4.99 
        Edam costs 2.45
        Camambert costs 7.75
        Bree costs 7.27
    
1. without using "head math", compute the costs of gouda, edam and camambert together 




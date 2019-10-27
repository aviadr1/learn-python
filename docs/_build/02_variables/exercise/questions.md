---
redirect_from:
  - "/02-variables/exercise/questions"
interact_link: content/02_variables/exercise/questions.ipynb
kernel_name: python3
has_widgets: false
title: 'Questions'
prev_page:
  url: /02_variables/exercise/questions.html
  title: 'exercise'
next_page:
  url: /02_variables/exercise/solutions.html
  title: 'Solutions'
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



# input from the user
run the following code to get input from the _user_ (you are the user!)
```python
name = input("what is your name: ")
print("hi", name)
```

your programs now have the power to ask questions!





# BMI: Body mass index
In health the BMI (body mass index) is defined as $$BMI=\frac{weight}{height^2}$$ 

where the weight is in kilograms, and the height is in meters.

for example for weight 80kg and height 2.0m the BMI is
$80 / (2^2) = 80 /4 = 20 $

1. put 97 into a variable called `weight`
2. put 1.84 into a variabled called `height`
3. write code to compute and print the bmi






# BMI with input from user
1. use the `input()` function to ask the user for his weight, put in variable `weight`
2. what is the type of the variable `weight`?
3. use the following code to convert the value to a `float`
```python
w = float(weight)
```
   what is the type of `w` now?
4. ask the user for his height and convert to float
5. compute and print the bmi



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



# 4 boom
in this exercise, we're going to take some song lyrics, and replace every 4th word of each line with the word "boom". and then print out the lyrics.
> NOTE: this exercise is simple but takes a lot of lines of code. 
> we _will_ learn loops __IN THE NEXT LESSON__. loops will help us write shorter solutions, but for now __YOU DONT NEED LOOPS__

use the following code, which puts an _important_ 😜 string in a variable named _`song`_ 
```python
song = """
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say good bye
Never gonna tell a lie and hurt you
"""
```
[![This is important](https://globalpremierbenefits.com/wp-content/uploads/2018/10/Click-Here-small-_0-300x107.jpg)](https://www.youtube.com/watch?v=dQw4w9WgXcQ "Everything Is AWESOME")


1. split this string into a list of lines. put it in variable called `lines`
   > hint: string have a function called `.splitlines()`
   
2. split the line 0 into words. put it in variable called words0
   - now also split line 1. put it into `words1`
   - repeat for line 2 ..., line 5, put each into word1, ... word5

   > hint: this should take you 6 simples lines.
   
3. replace the 4th word of line 1, line 2, ... line 6 with the word `"boom"``
   > hint: you __don't__ need loops. this again takes 6 lines
   
4. now join `words0`. put the result into variable boom0
   - continue to join `words1`, `words2` ... `words5` into `boom1`, `boom2` ... `boom5`
   
5. create a list that contains `boom0`, `boom1`, ... `boom5`, call it `boom`

6. join the lines in `boom` back into a string. put it into a variable called `result`
   > hint: use this code
   ```python
   result = "\n".join(boom)
   ```

7. print the result

[![This is important](https://cdn.instructables.com/FJI/WGSW/FPIUQQ3K/FJIWGSWFPIUQQ3K.LARGE.jpg?auto=webp&frame=1&width=320)](https://www.youtube.com/watch?v=dQw4w9WgXcQ "Everything Is AWESOME")


> expected output:
```
Never gonna give you boom
Never gonna let you boom
Never gonna run around boom desert you
Never gonna make you boom
Never gonna say good boom
Never gonna tell a boom and hurt you
```



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
### useful: data
song = """Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say good bye
Never gonna tell a lie and hurt you
"""

```
</div>

</div>



# Dictionary

1. create a dictionary that maps the name of cheeses to prices of 100mg of that cheese.

        gouda costs 4.99 
        Edam costs 2.45
        Camambert costs 7.75
        Bree costs 7.27
    
1. without using "head math", write simple code to compute the costs of gouda, edam and camambert together 
> hint: the solution is one simple but long line of code, which uses the `+` operator 3 times

1. add a new cheese to the dictionary: 
  `Cottage` cheese, which costs `3.2`
> hint: the solution takes just one very simple line of code

1. the government has added a new tax on milk products, now every cheese costs has increased by 27% ! can you update the costs in the dictionary?
> hint: the solution takes 5 (almost identical) lines of code

1. can you use the `round()` function to round the prices of cheese, so that it has costs in dollars and cents (Shekels and agorot)?
   > hint: what does the following code do?
    ```python
    pi = 3.14159265
    print(pi)
    pi_rounded = round(pi, 2)
    print(pi_rounded)
    ```






# len and indexing
```python
quote = "everything should be as simple as possible, but not simpler. Albert Einstein"
```

1. write code to check how many letters/characters are in this qoute.
> hint: use the function len()

2. split this qoute into words. how many words are in this quote?

3. write code to print:
   1. the 1st letter in the quote
   2. the 7th word
   3. the 1st letter of the 7th word
   4. the last letter in the quote
   5. the last letter of the 9th word

> hint: the function `len()` is useful to figuring out what is the last letter/word   



# len, indexing and input
1. what would the following code print? first try to answer yourself, then copy the code and run it to see if you guessed right

```
hi = "hello "
greeting = hi * 3
print(greeting)
```

2. use the `input()` function to ask the user for full name.

3. print the length of the name 

4. print the last letter of the name 100 times


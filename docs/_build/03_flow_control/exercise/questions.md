---
redirect_from:
  - "/03-flow-control/exercise/questions"
interact_link: content/03_flow_control/exercise/questions.ipynb
kernel_name: python3
has_widgets: false
title: 'Questions'
prev_page:
  url: /03_flow_control/exercise/questions.html
  title: 'exercise'
next_page:
  url: /03_flow_control/exercise/solutions.html
  title: 'Solutions'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-python/blob/master/content/03_flow_control/exercise/questions.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




# IMPORTANT

this is an incredibly crucial lesson. and requirs A LOT of excersizes to really get the hang of. please do all the excersizes, and if you found them challenging, keep doing more excersizes and even doing the same excersizes again and again until you can reliably solve them easily.

### Where to find more excercises?

For more exercizes on loops, see this [link](https://bit.ly/aviad-python-loops) which contains 44 exercises with solutions:



# for loops



### iterating over a word list with a `for` loop
Here's a line from [some old movie](https://www.youtube.com/watch?v=ZtYU87QNjPw)
```python
quote = "Strange women lying in ponds, distributing swords, is no basis for a system of government!"
```

1. use the .split() function to split it into a list of words. 
2. use the `for` loop to iterate over each word in the list
   - for each word, print the word and its `len()`

expected output:
```
Strange 7
women 5
lying 5
in 2
ponds, 6
distributing 12
swords, 7
is 2
no 2
basis 5
for 3
a 1
system 6
of 2
government! 11
```







### comments

> - Sometimes we want to write something that will explain the code we write, for this we can use comments.
> ``` python
> # this is a comment
> x = 10 + 90
> x = x * 2 # this is a comment at the end of a line 
> print(x) # will print 200
> ```
> 
> - comments start with the `#` character and continue until the end of the line
> - comments are just for reading by humans, the python interepreter completely ignores them

#### write helpful comments
copy this code to the answer below, and write short comments between the lines that explain the code
```python
hamburger = 59
pizza = 39
steak = 150
soup = 42
salad = 35
chips=18

dinner = [
    hamburger,
    hamburger,
    salad,
    chips
]

cost_of_dinner = 0
for food_item_cost in dinner:
    cost_of_dinner = cost_of_dinner + food_item_cost

print(cost_of_dinner)
```



### a nice dinner for two
1. copy this code below
```python
dinner = [
        # Sashimi plate
        60, 
        # some maki
        30, 35, 39,
        # agadashi 
        28,
        # miso
        18, 18,
        # lots of sake
        33, 39, 33,
        ]
```


1. use a `for` loop to calculate the cost of the dinner
   > this should take 3 lines

1. this is a dinner for two. what is the average cost per person for this dinner?
   > hint: divide by 2








### iterating over letters in a string
1. what does the following code do? try it
```python 
monty = "This is an ex parrot"
for letter in monty:
    print(letter, end=" ")
``` 
2. what does the `end=" "` part do? try to chage it to different values:
   - `" @ "` 
   - `""`
   - `" --- "` 
   - `"\n"`

3. can you write a loop that prints each letter twice?
   > expected output:
   ```
   TThhiiss  iiss  aann  eexx  ppaarrrroott
   ```




### range() - lists of numbers

1. run the following code
   ```python
   print(range(10))
   ```
   what does it print? 

1. the function `range(10)` __actually__ returns a _list-like_ object . iterate over all the elements of `range(10)` using a `for` loop and print each item in that list
   - repeat for `range(15)`
2. what does the function `range(10,20)` return ? print everything in that list 
   - repeat for `range(1,5)`
3. what does the function `range(0,10,2)` return? print everything in that list 
   - repeat for `range(0, 100, 10)`
   - repeat for `range(100, 0, -10)`

4. generally speaking, can you explain what function `range` does? 

5. 😵 can you solve this exercise with much fewer lines of code?
   > hint:
   > 1. put all the interesting ranges into a list of ranges
   > 2. iterate over the list of ranges with a `for` loop
   > 3. for each range in the list, use another _nested_/_inner_ `for` loop to print out all the elements of the list  






### sum of numbers

calculate the sum of the numbers between 0 and 1000
$$0 + 1 + 2 + 3 + 4 + ... + 997 + 998 +999$$ 

> hint: 
> - you dont need math or any formula ...
> - use the `range()` function and a `for` loop
> - to test your code you can see if it gets the right answer for numbers between 0 and 5 $$0+ 1+ 2+ 3+ 4 = 10$$




### average grades
here are some grades for students in a class. calculate the average grade

```python
grades = [ 60, 90, 70, 100, 65, 95, 80, 80, 80]
```

> hints:
> 1. use a for loop
> 2. $average = \frac{grade_1 + grade_2 + ... + grade_{n-1} + grade_n}{n}$





### printing asterics
1. what does the following code do?
```python
print('*', end="")
print('*', end="")
print('*', end="")
print('*', end="")
```

1. use a `for` loop, `range()` and `print('*', end="")` to print a line of 10 asterics
   > expected output:
   >   ```
   >   **********
   >   ```
   > hint: this takes just two lines




use a for loop



### squares

here's a square made of the `'*'` character with length 5

    *****
    *****
    *****
    *****
    *****

1. use the input() function to take a number from the user
   ```
   num = int(input('how big? '))
   ```
   
1. can you use for loop(s) to print such a square of length `num`?

hints: 
* use `print('*', end="")` to print a single `'*'` character
* you need more than one for loop



### triangles
here's a triangle made of the `'*'` character with length 5
   
     *
     **
     ***
     ****
     *****

can you use for loop(s) to print such a triangle of length 10?




### for loop - multiplication matrix
> - this question is slightly harder 🤯
> - multiplication matrix = לוח הכפל

this time, use `for` loop(s) and `range` to print the multiplication matrix
in the following way (total of 100 lines)

      1 x 1 = 1
      1 x 2 = 2
      ...
      1 x 10 = 10
      2 x 1 = 1
      2 x 2 = 2
      ...
      2 x 10 = 20
      ...
      ...
      10 x 1 = 10
      10 x 2 = 20
      ...
      10 x 10 = 100



### for loop - multiplication matrix with nice formatting
- > this question is harder 🤯🤯

1. copy your _for loop multiplication matrix_ solution  above 
   <br><br>
   
2. modify the solution so that it actually prints the multiplication table in table form <br>
      hint: 
        >> print(1,2,3, end="\t")
        >> print(4,5,6)
        1 2 3    4 5 6

expected output:

     1    2     3     4     5     6     7     8     9     10    
     2    4     6     8     10    12    14    16    18    20    
     3    6     9     12    15    18    21    24    27    30    
     4    8     12    16    20    24    28    32    36    40    
     5    10    15    20    25    30    35    40    45    50    
     6    12    18    24    30    36    42    48    54    60    
     7    14    21    28    35    42    49    56    63    70    
     8    16    24    32    40    48    56    64    72    80    
     9    18    27    36    45    54    63    72    81    90    
     10   20    30    40    50    60    70    80    90    100    




# conditionals and while loop



### if/elif/else - checking a password

1. use the input() function to take a password from the user
   <br><br>
   
1. check that the password is "good" according to the following criterions:
   1. the password length must be at least 4
   1. the password length must be no more than 12
   1. the password must not be just numbers
   1. the password must have both lowercase and uppercase letters
   <br><br>
   
1. if the password is good, print "excellent password". 
   otherwise, print the reason why the password was rejected
   <br><br>
   
HINTS:
* use the `len()`, `.isdigit()`, `.isupper()`, `.islower()` functions




### While loop - until we find a good password

1. copy the password testing code you wrote above
   <br> <br>
   
1. now use a while loop to continue asking for a new password
   until a password that passes all the tests is given



### While loop - password with maximum 3 attemps

1. copy your answer for the while loop above
   <br><br>
   
1. now modify the code such that no more than 3 attemps are possible
   after 3 failed attemps, the program should say "too many attemps, access denied"
   <br><br>




# while loop - numbers 0-100 divisible by 7

using a while loop, print all the numbers between 0 and 100 
that are divisible by 7

> **we say that x is divisible by 7 when `x%7 == 0`**




### for loop -  numbers 0-100 divisible by 7

> **Just like the question above, this time with a `for` loop**

print all the numbers between 0 and 100 that are divisible by 7
using a `for` loop and `range(100)`




### While loop - multiplication matrix
- > this question is harder 🤯🤯🤯
- > multiplication matrix = לוח הכפל

using while loop(s), print the multiplication matrix
in the following way (total of 100 lines)

      1 x 1 = 1
      1 x 2 = 2
      ...
      1 x 10 = 10
      2 x 1 = 1
      2 x 2 = 2
      ...
      2 x 10 = 20
      ...
      ...
      10 x 1 = 10
      10 x 2 = 20
      ...
      10 x 10 = 100



### loop to find long words

print all the words in the following sentence that are longer than 4 characters:
   
    "The quick brown fox jumped over the lazy dog"
   
expected output:
   
    quick
    brown
    jumped



### enumerate
1. split the string "the quick brown fox jumped over the lazy dog" into words
  using the .split() function, and put the list in the variable 'words'
  <br><br>

1. use the enumerate() function to print each word on its own line, 
   along with the index of the word in the 'words' variable
   <br><br>
   
       0 the
       1 quick
       2 brown
       3 fox
       4 jumped
       5 over
       6 the
       7 lazy
       8 dog

3. (harder) replace words that are longer than 4 characters to the string "too long"
   use enumerate() to do this with minimum number of code lines 

       ['the', 'too long', 'too long', 'fox', 'too long', 'over', 'the', 'lazy', 'dog'] 



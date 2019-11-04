---
redirect_from:
  - "/03-flow-control/exercise/solutions"
interact_link: content/03_flow_control/exercise/solutions.ipynb
kernel_name: python3
has_widgets: false
title: 'Solutions'
prev_page:
  url: /03_flow_control/exercise/questions.html
  title: 'Questions'
next_page:
  url: /03_flow_control/notebooks/1-100_multiplication_matrix_Luah_Kefel_.html
  title: 'notebooks'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-python/blob/master/content/03_flow_control/exercise/solutions.ipynb" target="_blank">
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







<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
quote = "Strange women lying in ponds, distributing swords, is no basis for a system of government!"
words = quote.split()
for word in words:
    print(word, len(word))

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
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
</div>
</div>
</div>



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



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# put the cost of each item in the menu in a variable
hamburger = 59
pizza = 39
steak = 150
soup = 42
salad = 35
chips=18
 
# create a list of all the item costs for a particular dinner
dinner = [
    hamburger,
    hamburger,
    salad,
    chips,
    steak,
    salad,
    soup
]

# calculate the cost of the dinner :
cost_of_dinner = 0 # before people ordered food, the cost of the dinner was 0
for food_item_cost in dinner: # now go through each item people ordered for dinner
    cost_of_dinner = cost_of_dinner + food_item_cost # add the cost of this item to the total cost

# now we have the full cost of the dinner, let's print it
print(cost_of_dinner)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
398
```
</div>
</div>
</div>



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








<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
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

cost_of_dinner = 0
for food_item_cost in dinner:
    # we use += because it is just a shorter way of writing
    # cost_of_dinner = cost_of_dinner + food_item_cost
    cost_of_dinner += food_item_cost

number_of_people = 2
average_per_person = cost_of_dinner/ number_of_people
print(average_per_person)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
166.5
```
</div>
</div>
</div>



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




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
monty = "This is an ex parrot"
for letter in monty:
    print(letter, end='')
    print(letter, end='')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
TThhiiss  iiss  aann  eexx  ppaarrrroott```
</div>
</div>
</div>



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






<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
###
### solution #1
### 
print(range(10))
for x in range(10):
   print(x, end=' ')

print("\n")
print(range(15))
for x in range(15):
   print(x, end=' ')

print("\n")
print(range(10, 20))
for x in range(10, 20):
   print(x, end=' ')

print("\n")
print(range(1, 5))
for x in range(1, 5):
   print(x, end=' ')

print("\n")
print(range(0, 10, 2))
for x in range(0, 10, 2):
   print(x, end=' ')

print("\n")
print(range(0, 100, 10))
for x in range(0, 100, 10):
   print(x, end=' ')

print("\n")
print(range(100, 0, -10))
for x in range(100, 0, -10):
   print(x, end=' ')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
range(0, 10)
0 1 2 3 4 5 6 7 8 9 

range(0, 15)
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 

range(10, 20)
10 11 12 13 14 15 16 17 18 19 

range(1, 5)
1 2 3 4 

range(0, 10, 2)
0 2 4 6 8 

range(0, 100, 10)
0 10 20 30 40 50 60 70 80 90 

range(100, 0, -10)
100 90 80 70 60 50 40 30 20 10 ```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
###
### solution #2
###
my_ranges = [range(10), range(15), range(10, 20), range(1, 5), range(0, 10, 2), range(0, 100, 10), range(100, 0, -10)]
for my_range in my_ranges:
    print("\n")
    print(my_range)
    for x in my_range:
        print(x, end=' ')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```


range(0, 10)
0 1 2 3 4 5 6 7 8 9 

range(0, 15)
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 

range(10, 20)
10 11 12 13 14 15 16 17 18 19 

range(1, 5)
1 2 3 4 

range(0, 10, 2)
0 2 4 6 8 

range(0, 100, 10)
0 10 20 30 40 50 60 70 80 90 

range(100, 0, -10)
100 90 80 70 60 50 40 30 20 10 ```
</div>
</div>
</div>



### sum of numbers

calculate the sum of the numbers between 0 and 1000
$$0 + 1 + 2 + 3 + 4 + ... + 997 + 998 +999$$ 

> hint: 
> - you dont need math or any formula ...
> - use the `range()` function and a `for` loop
> - to test your code you can see if it gets the right answer for numbers between 0 and 5 $$0+ 1+ 2+ 3+ 4 = 10$$




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
total = 0
for x in range(1000):
    total += x

print(total)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
499500
```
</div>
</div>
</div>



### average grades
here are some grades for students in a class. calculate the average grade

```python
grades = [ 60, 90, 70, 100, 65, 95, 80, 80, 80]
```

> hints:
> 1. use a for loop
> 2. $average = \frac{grade_1 + grade_2 + ... + grade_{n-1} + grade_n}{n}$





<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
grades = [ 60, 90, 70, 100, 65, 95, 80, 80, 80]
total = 0
for grade in grades:
    total += grade

print(total / len(grades))

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
80.0
```
</div>
</div>
</div>



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



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
for i in range(10):
    print('*', end="")

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
**********```
</div>
</div>
</div>



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



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
num = int(input('how big? '))
for row in range(num):
    for i in range(num):
        print('*', end="")
    print()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
how big? 10
**********
**********
**********
**********
**********
**********
**********
**********
**********
**********
```
</div>
</div>
</div>



### triangles
here's a triangle made of the `'*'` character with length 5
   
     *
     **
     ***
     ****
     *****

can you use for loop(s) to print such a triangle of length 10?




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
for row in range(10):
    for i in range(row+1):
        print('*', end="")
    print()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
*
**
***
****
*****
******
*******
********
*********
**********
```
</div>
</div>
</div>



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



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
for i in range(1,10+1):
    for j in range(1,10+1):
         print(i, '*', j, '=', i*j)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
1 * 1 = 1
1 * 2 = 2
1 * 3 = 3
1 * 4 = 4
1 * 5 = 5
1 * 6 = 6
1 * 7 = 7
1 * 8 = 8
1 * 9 = 9
1 * 10 = 10
2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
2 * 4 = 8
2 * 5 = 10
2 * 6 = 12
2 * 7 = 14
2 * 8 = 16
2 * 9 = 18
2 * 10 = 20
3 * 1 = 3
3 * 2 = 6
3 * 3 = 9
3 * 4 = 12
3 * 5 = 15
3 * 6 = 18
3 * 7 = 21
3 * 8 = 24
3 * 9 = 27
3 * 10 = 30
4 * 1 = 4
4 * 2 = 8
4 * 3 = 12
4 * 4 = 16
4 * 5 = 20
4 * 6 = 24
4 * 7 = 28
4 * 8 = 32
4 * 9 = 36
4 * 10 = 40
5 * 1 = 5
5 * 2 = 10
5 * 3 = 15
5 * 4 = 20
5 * 5 = 25
5 * 6 = 30
5 * 7 = 35
5 * 8 = 40
5 * 9 = 45
5 * 10 = 50
6 * 1 = 6
6 * 2 = 12
6 * 3 = 18
6 * 4 = 24
6 * 5 = 30
6 * 6 = 36
6 * 7 = 42
6 * 8 = 48
6 * 9 = 54
6 * 10 = 60
7 * 1 = 7
7 * 2 = 14
7 * 3 = 21
7 * 4 = 28
7 * 5 = 35
7 * 6 = 42
7 * 7 = 49
7 * 8 = 56
7 * 9 = 63
7 * 10 = 70
8 * 1 = 8
8 * 2 = 16
8 * 3 = 24
8 * 4 = 32
8 * 5 = 40
8 * 6 = 48
8 * 7 = 56
8 * 8 = 64
8 * 9 = 72
8 * 10 = 80
9 * 1 = 9
9 * 2 = 18
9 * 3 = 27
9 * 4 = 36
9 * 5 = 45
9 * 6 = 54
9 * 7 = 63
9 * 8 = 72
9 * 9 = 81
9 * 10 = 90
10 * 1 = 10
10 * 2 = 20
10 * 3 = 30
10 * 4 = 40
10 * 5 = 50
10 * 6 = 60
10 * 7 = 70
10 * 8 = 80
10 * 9 = 90
10 * 10 = 100
```
</div>
</div>
</div>



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




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
for i in range(1,10+1):
    for j in range(1,10+1):
        print( i*j, end="\t")
    print()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
1	2	3	4	5	6	7	8	9	10	
2	4	6	8	10	12	14	16	18	20	
3	6	9	12	15	18	21	24	27	30	
4	8	12	16	20	24	28	32	36	40	
5	10	15	20	25	30	35	40	45	50	
6	12	18	24	30	36	42	48	54	60	
7	14	21	28	35	42	49	56	63	70	
8	16	24	32	40	48	56	64	72	80	
9	18	27	36	45	54	63	72	81	90	
10	20	30	40	50	60	70	80	90	100	
```
</div>
</div>
</div>



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




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
p = input("your password, sir/madam? ")
if len(p) < 4:
    print("password too short")
elif len(p) > 12:
    print("password too long")
elif p.isdigit():
    print("cannot be just numbers")
elif p.islower():
    print("need uppercase letters")
elif p.isupper():
    print("need lowercase letters")
else:
    print("excellent password")
    finished = True

```
</div>

</div>



### While loop - until we find a good password

1. copy the password testing code you wrote above
   <br> <br>
   
1. now use a while loop to continue asking for a new password
   until a password that passes all the tests is given



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
finished = False
while not finished:
    p = input("your password, sir/madam? ")
    if len(p) < 4:
        print("password too short")
    elif len(p) > 12:
        print("password too long")
    elif p.isdigit():
        print("cannot be just numbers")
    elif p.islower():
        print("need uppercase letters")
    elif p.isupper():
        print("need lowercase letters")
    else:
        print("excellent password")
        finished = True

```
</div>

</div>



### While loop - password with maximum 3 attemps

1. copy your answer for the while loop above
   <br><br>
   
1. now modify the code such that no more than 3 attemps are possible
   after 3 failed attemps, the program should say "too many attemps, access denied"
   <br><br>




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
tries_left = 3
finished = False
while not finished and tries_left >0:
    tries_left = tries_left - 1
    p = input("your password, sir/madam? ")
    if len(p) < 4:
        print("password too short")   
    elif len(p) > 12:
        print("password too long")
    elif p.isdigit():
        print("cannot be just numbers")
    elif p.islower():
        print("need uppercase letters")
    elif p.isupper():
        print("need lowercase letters")
    else:
        print("excellent password")
        finished = True
        
if tries_left == 0 and not finished:
    print("too many attempts, access denied")

```
</div>

</div>



# while loop - numbers 0-100 divisible by 7

using a while loop, print all the numbers between 0 and 100 
that are divisible by 7

> **we say that x is divisible by 7 when `x%7 == 0`**




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
i=0
while i<=100:
    if i%7==0:
        print(i)
    i+=1

```
</div>

</div>



### for loop -  numbers 0-100 divisible by 7

> **Just like the question above, this time with a `for` loop**

print all the numbers between 0 and 100 that are divisible by 7
using a `for` loop and `range(100)`




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
for i in range(100):
    if i%7 ==0:
        print(i)

```
</div>

</div>



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



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
i=1
while i<=10:
    j=1
    while j<=10:
        print(i, '*', j, '=', i*j)
        j+=1
    i+=1
    

```
</div>

</div>



### loop to find long words

print all the words in the following sentence that are longer than 4 characters:
   
    "The quick brown fox jumped over the lazy dog"
   
expected output:
   
    quick
    brown
    jumped



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
sent = "the quick brown fox jumped over the lazy dog"
words = sent.split()
for word in words:
    if len(word) > 4:
        print(word)

```
</div>

</div>



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




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# a
words = "the quick brown fox jumped over the lazy dog".split()

# b 
for i, word in enumerate(words):
    print(i, word)
    
# c
for i, word in enumerate(words):
    if len(word) > 4:
        words[i] = "too long"
    
print(words)

```
</div>

</div>


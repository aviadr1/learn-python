---
redirect_from:
  - "/03-flow-control/exercise/questions"
interact_link: content/03_flow_control/exercise/questions.ipynb
kernel_name: python3
has_widgets: false
title: '03 flow control'
prev_page:
  url: /02_variables/notebooks/variables.html
  title: 'Variables'
next_page:
  url: /03_flow_control/exercise/questions.html
  title: 'exercise'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-python/blob/master/content/03_flow_control/exercise/questions.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




# For more exercizes on loops, see this link:
* [Python conditional statements and loops [44 exercises with solution]](bit.ly/aviad-python-loops)




# if/elif/else - checking a password

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

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
your password, sir/madam? blah
need uppercase letters
```
</div>
</div>
</div>



# While loop - until we find a good password

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

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
your password, sir/madam? BLAH
need lowercase letters
your password, sir/madam? blahBLAH
excellent password
```
</div>
</div>
</div>



# While loop - password with maximum 3 attemps

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

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
your password, sir/madam? 123
password too short
your password, sir/madam? 1242
cannot be just numbers
your password, sir/madam? blah
need uppercase letters
too many attempts, access denied
```
</div>
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

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
0
7
14
21
28
35
42
49
56
63
70
77
84
91
98
```
</div>
</div>
</div>



# for loop -  numbers 0-100 divisible by 7

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

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
0
7
14
21
28
35
42
49
56
63
70
77
84
91
98
```
</div>
</div>
</div>



# While loop - multiplication matrix

> multiplication matrix = ×œ×•×— ×”×›×¤×œ

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



# for loop - multiplication matrix

> multiplication matrix = ×œ×•×— ×”×›×¤×œ

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



# for loop - multiplication matrix with nice formatting

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



# loop to find long words

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

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
quick
brown
jumped
```
</div>
</div>
</div>



# squares

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
how big? 6
******
******
******
******
******
******
```
</div>
</div>
</div>



# triangles
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



# enumerate
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

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
0 the
1 quick
2 brown
3 fox
4 jumped
5 over
6 the
7 lazy
8 dog
['the', 'too long', 'too long', 'fox', 'too long', 'over', 'the', 'lazy', 'dog']
```
</div>
</div>
</div>


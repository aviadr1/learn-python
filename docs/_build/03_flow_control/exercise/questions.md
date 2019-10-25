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




# While loop - until we find a good password

1. copy the password testing code you wrote above
   <br> <br>
   
1. now use a while loop to continue asking for a new password
   until a password that passes all the tests is given



# While loop - password with maximum 3 attemps

1. copy your answer for the while loop above
   <br><br>
   
1. now modify the code such that no more than 3 attemps are possible
   after 3 failed attemps, the program should say "too many attemps, access denied"
   <br><br>




# while loop - numbers 0-100 divisible by 7

using a while loop, print all the numbers between 0 and 100 
that are divisible by 7

> **we say that x is divisible by 7 when `x%7 == 0`**




# for loop -  numbers 0-100 divisible by 7

> **Just like the question above, this time with a `for` loop**

print all the numbers between 0 and 100 that are divisible by 7
using a `for` loop and `range(100)`




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




# loop to find long words

print all the words in the following sentence that are longer than 4 characters:
   
    "The quick brown fox jumped over the lazy dog"
   
expected output:
   
    quick
    brown
    jumped



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



# triangles
here's a triangle made of the `'*'` character with length 5
   
     *
     **
     ***
     ****
     *****

can you use for loop(s) to print such a triangle of length 10?




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



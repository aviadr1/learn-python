---
redirect_from:
  - "/08-functions/exercise/questions"
interact_link: content/08_functions/exercise/questions.ipynb
kernel_name: python3
has_widgets: false
title: 'Questions'
prev_page:
  url: /08_functions/exercise/questions.html
  title: 'exercise'
next_page:
  url: /08_functions/exercise/solutions.html
  title: 'Solutions'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-python/blob/master/exercises/ex%2008%20-%20questions.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




# 1. write a multiply_by_10() function
create a function named 'multiply_by_10' that 
   - receives one parameter x
   - returns x multiplied by 10





# 2. triangles
we're going to write function to print triangles that look like this:
```
   *
   **
   ***
   ****
```

create a function called 'print_asterics' that 
- receives one parameter called n
- prints to screen one line with n asterics


```
>>> print_asterics(4)
****
>>> print_asterics(8)
********
```
   
use this function and a for loop to print a triangle having 10 lines




# 3. write print_char() function
create a new function called `print_char` that works 
similarly to print_asterics, 
- except it receives the character to print as an 
 additional parameter called 'c'
- the param c should have a default value of '*'

```
>>> print_char(4)
****
>>> print_char(8, '@')
@@@@@@@@ 
```

use this function to create this triangle with a loop
```
@
@@
@@@
@@@@
```




# 4. function print_trian()
create a function `print_trian` to print triangles like in #3 
it should receive two parameters:
- n determines how many lines the triangle would have
- c determines the character to use, with '*' as default

```
>>> print_trian(5, '$')
$
$$
$$$
$$$$
$$$$$
```

- hint: this function should use print_char internally




# 4.b write get_trian() function with return value

create a new function called `get_trian`, that is very similar to
`print_trian` from #4, but instead of printing the triangle
it returns the triangle as a string

```
>>> x = get_trian(5, '$')
>>> print(x)
$
$$
$$$
$$$$
$$$$$
```



#  `my_abs(x)` function

in this exercise we're going to implement a funtion that calculates the absolute value (×¢×¨×š ×ž×•×—×œ×˜) of a parameter x
and we're going to do it in 3 styles.

```
   x = my_abs(-10)
   print(x) # prints 10
```
```
   y = my_abs(12)
   print(y) # prints 12
```

> 1. write a function called `my_abs(x)` that calculates the absolute value (×¢×¨×š ×ž×•×—×œ×˜) of a parameter x




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
### useful: this tests your function
assert my_abs(0) == 0
assert my_abs(-10) == 10
assert my_abs(15) == 15


```
</div>

</div>



> 2. write a function called `my_abs2(x)` that does the same calculation as my_abs(x) <br>
   BUT use the __single line__ `if` variant: `exprssion1 if condition else expression2`




   
> 3. implement absolute value function using `lambda` syntax, put the result in a variable called my_abs3



# make_matrix() function

write a function called `make_matrix(nrows=10, ncols=10)` that returns a multiplication matrix (×œ×•×— ×›×¤×œ)
with `nrows` rows and `ncols` rows.

the function will return a list of lists that have the following property:
```
make_matrix()[i][j] == i*j
```

for example:
```
>>> from pprint import pprint
>>> x = make_matrix(5, 5)
>>> pprint(x)
[[0, 0, 0, 0, 0],
 [0, 1, 2, 3, 4],
 [0, 2, 4, 6, 8],
 [0, 3, 6, 9, 12],
 [0, 4, 8, 12, 16]]
```




# write maxitem() function
create a function called maxitem 
that finds and returns the maximum item in a list

```
>>> maxitem([1,2,3,4,3,1])
4
```



# sort_lists() - difficult

create a function called `sort_lists` that can sort a list of lists.
\[find hints on how to do it below.\]

it will work in the following way:
- we will sort lists according to which one has the maxmium item (like in #5)
- example:
```
>>> sort_lists([
 [1,2,3],
 [2,3,4],
 [1,1,1],
 [2]
 ])
[
[1,1,1],
[2],
[1,2,3],
[2,3,4
]
```

- hint: use the function `maxitem` from #5 
and the existing function `sorted`




# make_add_x - difficult
create a function called `make_add_x() `
that receives one parameter x
and returns an inner *function* ...
this inner function will receive one parameter y
and return `x+y`
```
>>> add7 = make_add_x(7)
>>> add7(3)
10
>>> add7(5)
12
>>> add10 = make_add_x(10)
>>> add10(100)
110
```



# myprint() - challenging

create a function called `myprint` that has similar properties to the built-in `print()` function:
- it is variadic: it can support 0,1,2,3 or more parameters (unlimited number)
- it supports the file, sep and end arguments

it differrs from print by prefering the character @
```
>>> myprint(1, 2, 3)
1 @ 2 @ 3 @
>>> myprint( [1, 2, 3], [4, 5, 6] )
[1, 2, 3] @ [4, 5, 6] @

>>> myprint(1, 2, 3, file=sys.stdout, sep=' ', end='\n')
1 2 3
```




# make_debuggable() - very difficult

create a function called make_debuggable(func) that:
- receives one paramter called func
- returns a new function that does the same thing as func, 

and can accept any argument that func accepts.

- but in addition the returned function also helps debugging by 
  printing out the parameters it received, and the return value it is about to return

hints:
- use a nested function that accepts variadic positional and keyword arguments



---
redirect_from:
  - "/08-functions/exercise/questions"
interact_link: content/08_functions/exercise/questions.ipynb
kernel_name: python3
has_widgets: false
title: '08 functions'
prev_page:
  url: /07_files/notebooks/pickle_example.html
  title: 'Pickle Example'
next_page:
  url: /08_functions/exercise/questions.html
  title: 'exercise'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-python/blob/master/content/08_functions/exercise/questions.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




# 1. write a multiply_by_10() function
create a function named 'multiply_by_10' that 
   - receives one parameter x
   - returns x multiplied by 10





<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def multiply_by_10(x):
    return x*10

multiply_by_10(3)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
30
```


</div>
</div>
</div>



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




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python

def print_asterics(n):
    line = '*' * n
    print(line)
    
for i in range(10):
    print_asterics(i+1)


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




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python

def print_char(n, c='*'):
    line = c * n
    print(line)
    
for i in range(5):
    print_char(i+1, '@')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
@
@@
@@@
@@@@
@@@@@
```
</div>
</div>
</div>



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




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def print_trian(n, c='*'):
    for i in range(n):
        print_char(i+1, c)
        
print_trian(5, '$')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
$
$$
$$$
$$$$
$$$$$
```
</div>
</div>
</div>



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



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def get_trian(n, c='*'):
    result = []
    for i in range(n):
        line = c * (i+1)
        result.append(line)
    
    return "\n".join(result)

x = get_trian(5, '@')
print(x)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
@
@@
@@@
@@@@
@@@@@
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# w

```
</div>

</div>



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
def my_abs(x):
  if x<0:
    return -x
  else:
    return x

```
</div>

</div>



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




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def my_abs2(x):
  return -x if x<0 else x

my_abs2(-10)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
10
```


</div>
</div>
</div>



   
> 3. implement absolute value function using `lambda` syntax, put the result in a variable called my_abs3



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
my_abs3 = lambda x: -x if x<0 else x

my_abs3(-10)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
10
```


</div>
</div>
</div>



# calculate VAT "מס ערך מוסף"

### a) write a function called `calc_vat` that takes a price and the VAT and calculates how much the price is after VAT

for instance:
```
>>> calc_vat(100, 17)
117
```

### b) make the vat a default parameter with value 17
```
>>> calc_vat(100)
117

>>> calc_vat(100, 15)
115
```





<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def calc_vat(price, vat=17):
    return price * (1 + vat/100.0)

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
### important: test your function
assert calc_vat(100, 17) == 117
assert calc_vat(200, 20) == 240
assert calc_vat(100) == 117

```
</div>

</div>



# zip-ing two lists together
1. create a list of fruits, put it in  a variable called `fruits`.

   example: ```['apple', 'guava', 'pineapple', 'pear', 'peach']```

1. create a list of prices for these fruits. it should have the same length as your list of fruits. put it in a variable called `prices`. 

   example: ```[10, 12, 20, 5, 8]```

1. use the `zip` function (look it up on google) to create a list of fruit/price pairs. 

   it could look like this: ```[('apple', 10), ('guava', 12), ('pineapple', 20), ('pear', 5), ('peach', 8)]``` 
   ```




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
fruits = ['apple', 'guava', 'pineapple', 'pear', 'peach']
fruits_prices = [10, 12, 20, 5, 8]
menu = dict(zip(fruits, fruits_prices))

def double_price(menu):
    return { name: price*2 for name, price in menu.items() }

print(double_price(menu))

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
{'apple': 20, 'guava': 24, 'pineapple': 40, 'pear': 10, 'peach': 16}
```
</div>
</div>
</div>



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




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
from pprint import pprint
def make_matrix(nrows=10, ncols=10):
    matrix = []
    for i in range(nrows):
        row = []
        matrix.append(row)
        for j in range(ncols):
            row.append(i*j)
        
    return matrix

x = make_matrix(5,5)
pprint(x)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
[[0, 0, 0, 0, 0],
 [0, 1, 2, 3, 4],
 [0, 2, 4, 6, 8],
 [0, 3, 6, 9, 12],
 [0, 4, 8, 12, 16]]
```
</div>
</div>
</div>



# write maxitem() function
create a function called maxitem 
that finds and returns the maximum item in a list

```
>>> maxitem([1,2,3,4,3,1])
4
```



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def maxitem(lst):
    themax = lst[0]
    for x in lst[1:]:
        if x > themax:
            themax = x
    return themax

maxitem([1,2,3,4,3,1])

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
4
```


</div>
</div>
</div>



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




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def sort_lists(lst):
    return sorted(lst, key=maxitem)

sort_lists([
         [1,2,3],
         [2,3,4],
         [1,1,1],
         [2]
        ])

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
[[1, 1, 1], [2], [1, 2, 3], [2, 3, 4]]
```


</div>
</div>
</div>



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



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python

def make_add_x(x):
    def add_x(y):
        return x+y
    return add_x

add7 = make_add_x(7)
print(add7(3)) # 10
print(add7(5)) # 12

add10 = make_add_x(10)
print(add10(100)) # 110

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
10
12
110
```
</div>
</div>
</div>



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




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python


import sys
def myprint(*args, sep=' @ ', end=' @\n', file=sys.stdout):
    return print(*args, sep=sep, end=end, file=file)

myprint(1, 2, 3)                #     1 @ 2 @ 3 @
myprint( [1, 2, 3], [4, 5, 6] ) #    [1, 2, 3] @ [4, 5, 6] @
myprint(1, 2, 3, file=sys.stdout, sep=' ', end='\n') # 1 2 3

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
1 @ 2 @ 3 @
[1, 2, 3] @ [4, 5, 6] @
1 2 3
```
</div>
</div>
</div>



# make_debuggable() - very difficult

create a function called make_debuggable(func) that:
- receives one paramter called func
- returns a new function that does the same thing as func, 

and can accept any argument that func accepts.

- but in addition the returned function also helps debugging by 
  printing out the parameters it received, and the return value it is about to return

hints:
- use a nested function that accepts variadic positional and keyword arguments




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def make_debuggable(func):
    def __get_signature(func, args, kwargs):
        fullargs = [str(a) for a in args] + [ f"{k}={v}" for k,v in kwargs.items()]
        return "{}({})".format(func.__name__, ', '.join(fullargs))
        
    def nested(*args, **kwargs):
        print(f"calling {__get_signature(func, args, kwargs)}")
        
        v = func(*args, **kwargs)
        
        print(f"{__get_signature(func, args, kwargs)} -->> {v}")
        return v
    
    return nested

import math
debug_sqrt = make_debuggable(math.sqrt)
debug_sqrt(100)
#debug_sqrt(-100)

print()

debug_print = make_debuggable(print)
debug_print(1,2,3, sep = ' @@@ ')


```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
calling sqrt(100)
sqrt(100) -->> 10.0

calling print(1, 2, 3, sep= @@@ )
1 @@@ 2 @@@ 3
print(1, 2, 3, sep= @@@ ) -->> None
```
</div>
</div>
</div>


---
redirect_from:
  - "/notebooks/lesson-12-exceptions"
interact_link: content/notebooks/lesson_12-exceptions.ipynb
kernel_name: python3
has_widgets: false
title: 'Lesson 12-exceptions'
prev_page:
  url: /notebooks/lesson_11-inheritance.html
  title: 'Lesson 11-inheritance'
next_page:
  url: /notebooks/lesson_12-raise_try_except_finally.html
  title: 'Lesson 12-raise Try Except Finally'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-python/blob/master/live%20class%20demonstrations/lesson%2012%20-%20exceptions.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
while True:
    x = input('give me a number: ')
    print(2 ** int(x))

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
give me a number: blah
```
</div>
</div>
<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_traceback_line}
```

    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-1-4d1e92aba1ff> in <module>
          1 while True:
          2     x = input('give me a number: ')
    ----> 3     print(2 ** int(x))
    

    ValueError: invalid literal for int() with base 10: 'blah'


```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
while True:
    try:
        x = input('give me a number: ')
        print(2 ** int(x))
        break
    except:
        pass

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
give me a number: asdf
give me a number: 8
256
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
while True:
    try:
        x = input('give me a number: ')
        print(2 ** int(x))
        break
    except ValueError:
        print('that wasnt a number, try again')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
give me a number: adfas
that wasnt a number, try again
give me a number: 8
256
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
while True:
    try:
        x = input('give me a number: ')
        print(2 ** int(x))
        break
    except Exception as ex:
        print('oops, that didnt work', ex, type(ex))

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
give me a number: sdf
oops, that didnt work invalid literal for int() with base 10: 'sdf' <class 'ValueError'>
give me a number: 8
256
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
raise ConnectionError('why not', 10, 20,30, True, {1:2})

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_traceback_line}
```

    ---------------------------------------------------------------------------

    ConnectionError                           Traceback (most recent call last)

    <ipython-input-6-ea9bb4ef90ec> in <module>
    ----> 1 raise ConnectionError('why not', 10, 20,30, True, {1:2})
    

    ConnectionError: ('why not', 10, 20, 30, True, {1: 2})


```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
class AviadError(AttributeError ):
    pass

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
x= 10
if x>0:
    raise AviadError('x is too big', x)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_traceback_line}
```

    ---------------------------------------------------------------------------

    AviadError                                Traceback (most recent call last)

    <ipython-input-8-9119bd55b181> in <module>
          1 x= 10
          2 if x>0:
    ----> 3     raise AviadError('x is too big', x)
    

    AviadError: ('x is too big', 10)


```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
assert x<5, 'x cannot be too big'

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_traceback_line}
```

    ---------------------------------------------------------------------------

    AssertionError                            Traceback (most recent call last)

    <ipython-input-11-e354469191d0> in <module>
    ----> 1 assert x<5, 'x cannot be too big'
    

    AssertionError: x cannot be too big


```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
assert x<5, 'x cannot be too big'

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_traceback_line}
```

    ---------------------------------------------------------------------------

    AssertionError                            Traceback (most recent call last)

    <ipython-input-16-e354469191d0> in <module>
    ----> 1 assert x<5, 'x cannot be too big'
    

    AssertionError: x cannot be too big


```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
bool( (False,  'x cannot be too big') )

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
True
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def mymax(seq):
    assert hasattr(seq[0], '__lt__'), 'seq is not comparable'
    return seq[0]

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
mymax([0,1])

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
class Test:
    pass

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
Test() < Test()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_traceback_line}
```

    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-21-94e876aeeec5> in <module>
    ----> 1 Test() < Test()
    

    TypeError: '<' not supported between instances of 'Test' and 'Test'


```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
mymax( [Test(), Test()] )

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
<__main__.Test at 0x23bc6c330b8>
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
seq = [Test(), Test()]
hasattr(seq[0], '__lt__')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
True
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
dir(seq[0])

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
['__class__',
 '__delattr__',
 '__dict__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__le__',
 '__lt__',
 '__module__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 '__weakref__']
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
seq[0].__lt__(1)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
NotImplemented
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
dir(object)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
['__class__',
 '__delattr__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__le__',
 '__lt__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__']
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
try:
    f = open('dir.txt')
    10/0
finally:
    f.close()
    


```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_traceback_line}
```

    ---------------------------------------------------------------------------

    ZeroDivisionError                         Traceback (most recent call last)

    <ipython-input-31-aa1385d06dcb> in <module>
          1 try:
          2     f = open('dir.txt')
    ----> 3     10/0
          4 finally:
          5     f.close()


    ZeroDivisionError: division by zero


```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
f.readline()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_traceback_line}
```

    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-32-7e1d2e12b839> in <module>
    ----> 1 f.readline()
    

    ValueError: I/O operation on closed file.


```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
f = open('dir.txt')
10/0

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_traceback_line}
```

    ---------------------------------------------------------------------------

    ZeroDivisionError                         Traceback (most recent call last)

    <ipython-input-33-d7df393567a9> in <module>
          1 f = open('dir.txt')
    ----> 2 10/0
    

    ZeroDivisionError: division by zero


```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
f.readline()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
' Volume in drive C has no label.\n'
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
import sys
def D(x):
    return 10/x

def C(x):
    return D(x)

def B(x):
    return C(x)

def A(x):
    return B(x) + B(x+1)

try:
    z = A(0)
    print(z)
except Exception as err:
    traceback.print_exc()


```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_traceback_line}
```

    ---------------------------------------------------------------------------

    ZeroDivisionError                         Traceback (most recent call last)

    <ipython-input-41-1c2351c36736> in <module>
         14 try:
    ---> 15     z = A(0)
         16     print(z)


    <ipython-input-41-1c2351c36736> in A(x)
         11 def A(x):
    ---> 12     return B(x) + B(x+1)
         13 


    <ipython-input-41-1c2351c36736> in B(x)
          8 def B(x):
    ----> 9     return C(x)
         10 


    <ipython-input-41-1c2351c36736> in C(x)
          5 def C(x):
    ----> 6     return D(x)
          7 


    <ipython-input-41-1c2351c36736> in D(x)
          2 def D(x):
    ----> 3     return 10/x
          4 


    ZeroDivisionError: division by zero

    
    During handling of the above exception, another exception occurred:


    NameError                                 Traceback (most recent call last)

    <ipython-input-41-1c2351c36736> in <module>
         16     print(z)
         17 except Exception as err:
    ---> 18     traceback.print_exc()
    

    NameError: name 'traceback' is not defined


```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
tb.tb_frame.f_trace

```
</div>

</div>


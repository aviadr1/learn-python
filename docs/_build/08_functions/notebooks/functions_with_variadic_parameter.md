---
redirect_from:
  - "/08-functions/notebooks/functions-with-variadic-parameter"
interact_link: content/08_functions/notebooks/functions_with_variadic_parameter.ipynb
kernel_name: python3
has_widgets: false
title: 'Functions With Variadic Parameter'
prev_page:
  url: /08_functions/notebooks/functions_calling_functions_shapes.html
  title: 'Functions Calling Functions Shapes'
next_page:
  url: /08_functions/notebooks/function_fundamentals.html
  title: 'Function Fundamentals'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-python/blob/master/content/08_functions/notebooks/functions_with_variadic_parameter.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def test_variadic_func(*args):
    print(type(args), len(args), args)
    
test_variadic_func()
test_variadic_func("one")
test_variadic_func("one", "two")
test_variadic_func("one", "two", "three", "four")

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
<class 'tuple'> 0 ()
<class 'tuple'> 1 ('one',)
<class 'tuple'> 2 ('one', 'two')
<class 'tuple'> 4 ('one', 'two', 'three', 'four')
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# packing
args = "one", "two", "three", "four"
print(args)

# unpacking
one, two, three, four = args
print(one,two,three, four)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
('one', 'two', 'three', 'four')
one two three four
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def myprint1(*args):
    print(*args) # unpacking
    # print(args[0], args[1], args[2], ... args[-1])

print("one", "two", "three")
myprint1("one", "two", "three")

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
one two three
one two three
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
import sys
def myprint2(*args, sep=" ", end="\n", file=sys.stdout):
    print(*args, sep=sep, end=end, file=file) # unpacking
    # print(args[0], args[1], args[2], ... args[-1])
    
print("one", "two", "three", sep=" @ ", end=" @\n")
myprint2("one", "two", "three", sep=" @ ", end=" @\n")

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
one @ two @ three @
one @ two @ three @
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def myprint2(*args, **kwargs):
    print(*args, **kwargs)
    
myprint2(1,2,3, sep=" @ ")
# myprint2(1,2,3, magic=" @ ")
    

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
1 @ 2 @ 3
```
</div>
</div>
<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_traceback_line}
```

    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-14-09f73822af3f> in <module>
          3 
          4 myprint2(1,2,3, sep=" @ ")
    ----> 5 myprint2(1,2,3, magic=" @ ")
          6 


    <ipython-input-14-09f73822af3f> in myprint2(*args, **kwargs)
          1 def myprint2(*args, **kwargs):
    ----> 2     print(*args, **kwargs)
          3 
          4 myprint2(1,2,3, sep=" @ ")
          5 myprint2(1,2,3, magic=" @ ")


    TypeError: 'magic' is an invalid keyword argument for print()


```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def test_variadic_func2(*args, **kwargs):
    print(type(args), len(args), args)
    print(type(kwargs), len(kwargs), kwargs)
    
test_variadic_func2(1,2,3, magic=" @ ", blah="blah")

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
<class 'tuple'> 3 (1, 2, 3)
<class 'dict'> 2 {'magic': ' @ ', 'blah': 'blah'}
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def very_important_function(a,b,c):
    print("very important", a, b, c)

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
very_important_function(10, 20, 30)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
very important 10 20 30
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def make_debug_function(func):
    def run(*args, **kwargs):
        print(func.__name__, " is about to run with", *args, **kwargs)
        result = func(*args, **kwargs)
        print(func.__name__, " finished running, returning", result)
        return result
    
    return run

very_important_function(10, 20, 30)
print()

debug_very_important_function = make_debug_function(very_important_function)
debug_very_important_function(10, 20, 30)
print()

very_important_function = debug_very_important_function
very_important_function(10, 20, 30)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
very important 10 20 30

very_important_function  is about to run with 10 20 30
very important 10 20 30
very_important_function  finished running, returning None

very_important_function  is about to run with 10 20 30
very important 10 20 30
very_important_function  finished running, returning None
```
</div>
</div>
</div>


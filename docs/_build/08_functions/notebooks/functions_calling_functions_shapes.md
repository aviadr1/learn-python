---
redirect_from:
  - "/08-functions/notebooks/functions-calling-functions-shapes"
interact_link: content/08_functions/notebooks/functions_calling_functions_shapes.ipynb
kernel_name: python3
has_widgets: false
title: 'Functions Calling Functions Shapes'
prev_page:
  url: /08_functions/notebooks/documentation.html
  title: 'Documentation'
next_page:
  url: /08_functions/notebooks/functions_with_variadic_parameter.html
  title: 'Functions With Variadic Parameter'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-python/blob/master/content/08_functions/notebooks/functions_calling_functions_shapes.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def get_line(n):
    result = ""
    for i in range(n):
        result += 'X'
    return result

x = get_line(5)
print(x)

def get_line(n):
    return 'X' * n

x = get_line(5)
print(x)


```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
XXXXX
XXXXX
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def get_square(n):
    result = ""
    for i in range(n):
        line = get_line(n)
        result += line + '\n'
        
    return result

x = get_square(5)
print(x)

def get_square(n):
    lines = [get_line(n)] * n
    return "\n".join(lines)

print(get_square(5))

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
XXXXX
XXXXX
XXXXX
XXXXX
XXXXX

XXXXX
XXXXX
XXXXX
XXXXX
XXXXX
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def get_triang(n):
    result = ""
    for i in range(1, n+1):
        line = get_line(i)
        result += line + '\n'
        
    return result

x = get_triang(5)
print(x)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
X
XX
XXX
XXXX
XXXXX

```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def reverse(lst):
    return lst[ : : -1]
    
def shape(n):
    return '\n'.join([
        get_triang(n), 
        get_square(n),
        reverse(get_triang(n))
    ])

print(shape(5))

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
X
XX
XXX
XXXX
XXXXX

XXXXX
XXXXX
XXXXX
XXXXX
XXXXX

XXXXX
XXXX
XXX
XX
X
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
x = get_triang(5)
x = x[::-1]
print(x)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```

XXXXX
XXXX
XXX
XX
X
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
x = ['one', 'two', 'three', 'four']
x[0]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'one'
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
x[-1]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'four'
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
x[0:2]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
['one', 'two']
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
x[:2]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
['one', 'two']
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
x[2:]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
['three', 'four']
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
x[0:4:2]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
['one', 'three']
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
x[3:0:-1]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
['four', 'three', 'two']
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
x[3:0:-2]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
['four', 'two']
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
x[ : :-2]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
['four', 'two']
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
help(len)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Help on built-in function len in module builtins:

len(obj, /)
    Return the number of items in a container.

```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
help(shape)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Help on function shape in module __main__:

shape(n)
    shape is an awesome function that draws something that looks like
    a double edged sword

```
</div>
</div>
</div>


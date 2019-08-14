---
redirect_from:
  - "/notebooks/lesson-08-variadic-functions"
interact_link: content/notebooks/lesson_08-variadic_functions.ipynb
kernel_name: python3
has_widgets: false
title: 'Lesson 08-variadic Functions'
prev_page:
  url: /notebooks/lesson_08-unpacking.html
  title: 'Lesson 08-unpacking'
next_page:
  url: /notebooks/lesson_08-variadic_functions_unpacking.html
  title: 'Lesson 08-variadic Functions Unpacking'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-python/blob/master/live%20class%20demonstrations/lesson%2008%20-%20variadic%20functions.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def oneparam(x):
    return x

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
oneparam(1,2,3)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_traceback_line}
```

    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-2-7af8d1116f6b> in <module>
    ----> 1 oneparam(1,2,3)
    

    TypeError: oneparam() takes 1 positional argument but 3 were given


```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def my_variadic_function_with_cool_name(*args, **kwargs):
    print("type(args)", type(args))
    print("args=", args)
    print("type(kwargs)", type(kwargs))
    print("kwargs=", kwargs)
    return "I am doing nothing"



```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
my_variadic_function_with_cool_name(1,2,3, "blah", first_named=1, second_named_param="blah2", whatever="blah3")

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
type(args) <class 'tuple'>
args= (1, 2, 3, 'blah')
type(kwargs) <class 'dict'>
kwargs= {'first_named': 1, 'second_named_param': 'blah2', 'whatever': 'blah3'}
```
</div>
</div>
<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'I am doing nothing'
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
my_variadic_function_with_cool_name()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
type(args) <class 'tuple'>
args= ()
type(kwargs) <class 'dict'>
kwargs= {}
```
</div>
</div>
<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'I am doing nothing'
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
my_variadic_function_with_cool_name(1,2,3)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
type(args) <class 'tuple'>
args= (1, 2, 3)
type(kwargs) <class 'dict'>
kwargs= {}
```
</div>
</div>
<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'I am doing nothing'
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
my_variadic_function_with_cool_name(a=1,b=2,c=3)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
type(args) <class 'tuple'>
args= ()
type(kwargs) <class 'dict'>
kwargs= {'a': 1, 'b': 2, 'c': 3}
```
</div>
</div>
<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'I am doing nothing'
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print(1,2,3,4,5,6,7,8,10,23432,234,234,234,23423,423,423,4324,234,234,234,23423,4234,234)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
1 2 3 4 5 6 7 8 10 23432 234 234 234 23423 423 423 4324 234 234 234 23423 4234 234
```
</div>
</div>
</div>


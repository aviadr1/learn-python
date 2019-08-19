---
redirect_from:
  - "/09-advanced-collections/notebooks/infinite-coroutine"
interact_link: content/09_advanced_collections/notebooks/infinite_coroutine.ipynb
kernel_name: python3
has_widgets: false
title: 'Infinite Coroutine'
prev_page:
  url: /09_advanced_collections/notebooks/generators_lazy_functions.html
  title: 'Generators Lazy Functions'
next_page:
  url: /09_advanced_collections/notebooks/lazy_lists_generators.html
  title: 'Lazy Lists Generators'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-python/blob/master/live%20class%20demonstrations/lesson%2009%20-%20infinite%20coroutine.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def infinite_memory_error():
    result = []
    i=0
    while True:
        result.append(i)
        i+=1
        
    return result


```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def infinite_but_really_just_0():
    i=0
    while True:
        return i
        i+=1


```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
infinite_but_really_just_0()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
0
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
infinite_but_really_just_0()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
0
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def infinite():
    i=0
    while True:
        yield i
        i+=1

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
infinite()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
<generator object infinite at 0x000002B7AE9BF0F8>
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
inf = infinite()

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
next(inf)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
7
```


</div>
</div>
</div>


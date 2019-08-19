---
redirect_from:
  - "/05-collections/notebooks/sorting-bitahon"
interact_link: content/05_collections/notebooks/sorting_bitahon.ipynb
kernel_name: python3
has_widgets: false
title: 'Sorting Bitahon'
prev_page:
  url: /05_collections/notebooks/sorting.html
  title: 'Sorting'
next_page:
  url: /05_collections/notebooks/unpacking.html
  title: 'Unpacking'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-python/blob/master/live%20class%20demonstrations/lesson%2005%20-%20sorting%20bitahon.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
num1  = 15
num2 = num1

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
help([].extend)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Help on built-in function extend:

extend(...) method of builtins.list instance
    L.extend(iterable) -> None -- extend list by appending elements from the iterable

```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
x = [4,5,6]

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
x.insert(0, [1,2,3])

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
len(x)

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



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
x

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
[[1, 2, 3], 4, 5, 6]
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
x = [4,5,6]
x = [1,2,3] + x

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
x

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
[1, 2, 3, 4, 5, 6]
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
["one", "two", "three"].remove("one")

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
x = ["one", "two", "three"]

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
x.remove("one")

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
x

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
['two', 'three']
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
stuff_to_do = [
    "buy milk",
    "cancel subscription",
    "go to work",
    "gym"
]

def do_stuff(work):
    print(work)

while stuff_to_do:
    work = stuff_to_do.pop()
    do_stuff(work)
    

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
gym
go to work
cancel subscription
buy milk
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
stuff_to_do = [
    "work",
    "live",
    "breath",
    "buy milk",
    "cancel subscription",
    "go to work",
    "gym",
    "try harder",
    "catch zzs"
]

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
stuff_to_do.pop(stuff_to_do.index('gym'))

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'gym'
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
stuff_to_do

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
['buy milk', 'cancel subscription', 'go to work']
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
for i in range(len(stuff_to_do)):
    for j in range(i, len(stuff_to_do)):
        if stuff_to_do[i] > stuff_to_do[j]:
            stuff_to_do[i], stuff_to_do[j] = stuff_to_do[j], stuff_to_do[i]

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
stuff_to_do

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
['breath',
 'buy milk',
 'cancel subscription',
 'catch zzs',
 'go to work',
 'gym',
 'live',
 'try harder',
 'work']
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
min = stuff_to_do[0]
for i in range(len(stuff_to_do[1:])):
    if min >  stuff_to_do[i]:
        min = stuff_to_do[i]
    
print(min)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
breath
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
for i in range(len(stuff_to_do)):
    
    min_j = i
    min = stuff_to_do[min_j]
    
    for j in range(i+1, len(stuff_to_do)):
        if min >  stuff_to_do[j]:
            min_j = j
            min = stuff_to_do[min_j]
    
    stuff_to_do[i], stuff_to_do[min_j] = stuff_to_do[min_j], stuff_to_do[i]
    

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print(stuff_to_do)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
['breath', 'buy milk', 'cancel subscription', 'catch zzs', 'go to work', 'gym', 'live', 'try harder', 'work']
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
sorted(stuff_to_do, reverse=True)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
['work',
 'try harder',
 'live',
 'gym',
 'go to work',
 'catch zzs',
 'cancel subscription',
 'buy milk',
 'breath']
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
lists = [
    [2, 2000],
    [1,1,1],
    [100, 75],
    [50, 50, 90],
    [10, 20, 30]
]

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
sorted(lists, key=len)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
[[2], [100], [50, 50], [1, 1, 1]]
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
sorted(lists, key=max)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
[[1, 1, 1], [2], [50, 50], [100]]
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
sorted(lists, key=min)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
[[1, 1, 1], [2, 2000], [10, 20, 30], [50, 50, 90], [100, 75]]
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
sorted(lists, key=max)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
[[1, 1, 1], [10, 20, 30], [50, 50, 90], [100, 75], [2, 2000]]
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
import math

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
help(math.pow)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Help on built-in function pow in module math:

pow(...)
    pow(x, y)
    
    Return x**y (x to the power of y).

```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
sorted(lists, key=str)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
[[1, 1, 1], [10, 20, 30], [100, 75], [2, 2000], [50, 50, 90]]
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
sorted(lists, key=sum)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
[[1, 1, 1], [10, 20, 30], [100, 75], [50, 50, 90], [2, 2000]]
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
help(sum)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Help on built-in function sum in module builtins:

sum(iterable, start=0, /)
    Return the sum of a 'start' value (default: 0) plus an iterable of numbers
    
    When the iterable is empty, return the start value.
    This function is intended specifically for use with numeric values and may
    reject non-numeric types.

```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
lists2 = [
    [10, 20, 30],
    [100, -100],
    [15, 75],
    [1000, 500, 200, 50]
]

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
sorted(lists2, key=min)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
[[100, -100], [10, 20, 30], [15, 75], [1000, 500, 200, 50]]
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
sorted(lists2, key=max)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
[[10, 20, 30], [15, 75], [100, -100], [1000, 500, 200, 50]]
```


</div>
</div>
</div>


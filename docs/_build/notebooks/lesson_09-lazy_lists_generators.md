---
redirect_from:
  - "/notebooks/lesson-09-lazy-lists-generators"
interact_link: content/notebooks/lesson_09-lazy_lists_generators.ipynb
kernel_name: python3
has_widgets: false
title: 'Lesson 09-lazy Lists Generators'
prev_page:
  url: /notebooks/lesson_09-infinite_coroutine.html
  title: 'Lesson 09-infinite Coroutine'
next_page:
  url: /notebooks/lesson_09-list_and_dictionary_comprehension_checkpoint.html
  title: 'Lesson 09-list And Dictionary Comprehension Checkpoint'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-python/blob/master/live%20class%20demonstrations/lesson%2009%20-%20lazy%20lists%20generators.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
nums = [4, 9, 16, 25, -9, -100, 10000]

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
import math
[math.sqrt(x) for x in nums if x>=0 ]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_traceback_line}
```

      File "<ipython-input-7-00a6234a803b>", line 2
        [math.sqrt(x) for x in nums if x>=0 else None]
                                               ^
    SyntaxError: invalid syntax



```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
[ math.sqrt(x)   for x in nums   ]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
[2.0, 3.0, 4.0, 5.0, None, None, 100.0]
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
x = 100


```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
10.0
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
list(reversed([1,2,3]))

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
[3, 2, 1]
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
f = open("green eggs and ham.txt")

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
f

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
<_io.TextIOWrapper name='green eggs and ham.txt' mode='r' encoding='cp1255'>
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
list(f)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
['I am Sam\n',
 'I am Sam\n',
 'Sam I am\n',
 'That Sam-I-am\n',
 'That Sam-I-am!\n',
 'I do not like\n',
 'That Sam-I-am\n',
 'Do you like\n',
 'Green eggs and ham\n',
 'I do not like them\n',
 'Sam-I-am\n',
 'I do not like\n',
 'Green eggs and ham\n',
 'Would you like them\n',
 'Here or there?\n',
 'I would not like them\n',
 'Here or there\n',
 'I would not like them\n',
 'Anywhere\n',
 'I do not like\n',
 'Green eggs and ham\n',
 'I do not like them\n',
 'Sam-I-am\n',
 'Would you like them\n',
 'In a house?\n',
 'Would you like them\n',
 'With a mouse?\n',
 'I do not like them\n',
 'In a house']
```


</div>
</div>
</div>


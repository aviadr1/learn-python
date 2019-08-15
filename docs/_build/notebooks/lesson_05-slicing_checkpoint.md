---
redirect_from:
  - "/notebooks/lesson-05-slicing-checkpoint"
interact_link: content/notebooks/lesson_05-slicing_checkpoint.ipynb
kernel_name: python3
has_widgets: false
title: 'Lesson 05-slicing Checkpoint'
prev_page:
  url: /notebooks/lesson_05-slicing_bitahon.html
  title: 'Lesson 05-slicing Bitahon'
next_page:
  url: /notebooks/lesson_05-sorting.html
  title: 'Lesson 05-sorting'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-python/blob/master/live%20class%20demonstrations/lesson%2005%20-%20slicing%20checkpoint.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
cheeses = ["adam", "bree", "cheddar", "gouda", "camambert"]

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
cheeses[::-1]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
['camambert', 'gouda', 'cheddar', 'bree', 'adam']
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
cheeses[::2]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
['adam', 'cheddar', 'camambert']
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
cheeses[3::]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
['gouda', 'camambert']
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
list(range(100))[::7]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
[0, 7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98]
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
list(range(0,100, 7))

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
[0, 7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98]
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
list(range(100 , 0, -7))

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
[100, 93, 86, 79, 72, 65, 58, 51, 44, 37, 30, 23, 16, 9, 2]
```


</div>
</div>
</div>


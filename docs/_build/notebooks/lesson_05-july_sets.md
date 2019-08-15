---
redirect_from:
  - "/notebooks/lesson-05-july-sets"
interact_link: content/notebooks/lesson_05-july_sets.ipynb
kernel_name: python3
has_widgets: false
title: 'Lesson 05-july Sets'
prev_page:
  url: /notebooks/lesson_05-july_fruits_sorting_dict_zip.html
  title: 'Lesson 05-july Fruits Sorting Dict Zip'
next_page:
  url: /notebooks/lesson_05-removing_from_lists.html
  title: 'Lesson 05-removing From Lists'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-python/blob/master/live%20class%20demonstrations/lesson%2005%20-%20july%20sets.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
all_tests = list(range(10))

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
alpha = {1,2,5,7,9}
beta = {0,2,3,4,5,9}

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
beta - alpha

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
{0, 3, 4}
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
alpha - beta

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
{1, 7}
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
alpha & beta

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
{2, 5, 9}
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
alpha | beta

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
{0, 1, 2, 3, 4, 5, 7, 9}
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
set(all_tests) - alpha - beta

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
{6, 8}
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
{1,1,1,1}

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
{1}
```


</div>
</div>
</div>


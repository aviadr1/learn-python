---
redirect_from:
  - "/notebooks/lesson-05-sets-checkpoint"
interact_link: content/notebooks/lesson_05-sets_checkpoint.ipynb
kernel_name: python3
has_widgets: false
title: 'Lesson 05-sets Checkpoint'
prev_page:
  url: /notebooks/lesson_05-reverse_dict_using_setdefault.html
  title: 'Lesson 05-reverse Dict Using Setdefault'
next_page:
  url: /notebooks/lesson_05-slicing.html
  title: 'Lesson 05-slicing'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-python/blob/master/live%20class%20demonstrations/lesson%2005%20-%20sets%20checkpoint.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
version1 = [ 1 , 7, 8, 10]
version2 = [1,2,3,8,9]


```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
succeeded_both = set(version1) & set(version2)
# succeeded_both = set(version1).intersection(set(version2))
print(succeeded_both)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
{8, 1}
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# suppose the total tests are named 0, 1, 2, ... 10
all_tests = set(range(11))
print("all tests:", all_tests)
failed1 = all_tests - set(version1)
failed2 = all_tests - set(version2)
print("failed version #1", failed1)
print("failed version #2", failed2)
print("failed both:", failed1 & failed2)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
all tests: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
failed version #1 {0, 2, 3, 4, 5, 6, 9}
failed version #2 {0, 4, 5, 6, 7, 10}
failed both: {0, 4, 5, 6}
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
improved =  set(version2) - set(version1)
print("tests fixed by version #2:", improved)

got_worse = set(version1) - set(version2)
print("tests that got worse by version #2:", got_worse)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
tests fixed by version #2: {9, 2, 3}
tests that got worse by version #2: {10, 7}
```
</div>
</div>
</div>


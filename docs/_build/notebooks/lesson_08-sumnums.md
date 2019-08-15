---
redirect_from:
  - "/notebooks/lesson-08-sumnums"
interact_link: content/notebooks/lesson_08-sumnums.ipynb
kernel_name: python3
has_widgets: false
title: 'Lesson 08-sumnums'
prev_page:
  url: /notebooks/lesson_08-soft_intro_to_functions.html
  title: 'Lesson 08-soft Intro To Functions'
next_page:
  url: /notebooks/lesson_08-unpacking.html
  title: 'Lesson 08-unpacking'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-python/blob/master/live%20class%20demonstrations/lesson%2008%20-%20sumnums.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
x=[52345,5,523,235,235,23553,35]


```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
total = 0
for num in x:
    total += num

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
total

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
76931
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def sumnums(dalist):
    total = 0
    for num in dalist:
        total = total + num
        
    return total

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
sumnums([52345,5,523,235,235,23553,35])

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
76931
```


</div>
</div>
</div>


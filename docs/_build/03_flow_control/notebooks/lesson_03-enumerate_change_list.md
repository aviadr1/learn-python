---
redirect_from:
  - "/03-flow-control/notebooks/lesson-03-enumerate-change-list"
interact_link: content/03_flow_control/notebooks/lesson_03-enumerate_change_list.ipynb
kernel_name: python3
has_widgets: false
title: 'Lesson 03-enumerate Change List'
prev_page:
  url: /03_flow_control/notebooks/lesson_03-enumerate.html
  title: 'Lesson 03-enumerate'
next_page:
  url: /03_flow_control/notebooks/lesson_03-for_loop.html
  title: 'Lesson 03-for Loop'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-python/blob/master/live%20class%20demonstrations/lesson%2003%20-%20enumerate%20change%20list.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
s = "the quick brown fox jumped over the lazy dog"
words = s.split()

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
result = []
for word in words:
    result.append(word.upper() if word in ['fox', 'dog'] else word)

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
result

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
['the', 'quick', 'brown', 'FOX', 'jumped', 'over', 'the', 'lazy', 'DOG']
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
for i, word in enumerate(words):
    if word in ['fox', 'dog']: words[i] = word.upper()

```
</div>

</div>


---
redirect_from:
  - "/03-flow-control/notebooks/lesson-03-enumerate"
interact_link: content/03_flow_control/notebooks/lesson_03-enumerate.ipynb
kernel_name: python3
has_widgets: false
title: 'Lesson 03-enumerate'
prev_page:
  url: /03_flow_control/notebooks/lesson_03-converting_to_bool.html
  title: 'Lesson 03-converting To Bool'
next_page:
  url: /03_flow_control/notebooks/lesson_03-enumerate_change_list.html
  title: 'Lesson 03-enumerate Change List'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-python/blob/master/live%20class%20demonstrations/lesson%2003%20-%20enumerate.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
cheeses = ['adam', 'bree', 'cheddar', 'stilton', 'gouda', 'cottage']

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
for i, cheese in enumerate(cheeses):
    if len(cheese) >= 5:
        cheese = "premium " + cheese
        print(cheese)
        cheeses[i] = cheese

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
premium cheddar
premium stilton
premium gouda
premium cottage
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
cheeses

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
['adam',
 'bree',
 'premium cheddar',
 'premium stilton',
 'premium gouda',
 'premium cottage']
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
list(enumerate(cheeses))

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
[(0, 'adam'),
 (1, 'bree'),
 (2, 'cheddar'),
 (3, 'stilton'),
 (4, 'gouda'),
 (5, 'cottage')]
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
i, cheese = (0, 'adam')
print(i)
print(cheese)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
0
adam
```
</div>
</div>
</div>


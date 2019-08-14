---
redirect_from:
  - "/notebooks/lesson-05-removing-from-lists"
interact_link: content/notebooks/lesson_05-removing_from_lists.ipynb
kernel_name: python3
has_widgets: false
title: 'Lesson 05-removing From Lists'
prev_page:
  url: /notebooks/lesson_05-july_sets.html
  title: 'Lesson 05-july Sets'
next_page:
  url: /notebooks/lesson_05-reverse_dictionary.html
  title: 'Lesson 05-reverse Dictionary'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-python/blob/master/live%20class%20demonstrations/lesson%2005%20-%20removing%20from%20lists.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
cheeses = ["adam", "bree", "cheDDar", "GOUDA", "camambert"]
print(cheeses)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
['adam', 'bree', 'cheDDar', 'GOUDA', 'camambert']
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
cheeses = ["adam", "bree", "cheDDar", "GOUDA", "camambert"]
del cheeses[3]
print(cheeses)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
['adam', 'bree', 'cheDDar', 'camambert']
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
cheeses = ["adam", "bree", "cheDDar", "GOUDA", "camambert"]
cheeses.pop(3)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'GOUDA'
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
cheeses = ["adam", "bree", "cheDDar", "GOUDA", "camambert"]
cheeses.remove("camambert")
#cheeses.pop(cheeses.index("camambert"))
print(cheeses)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
['adam', 'bree', 'cheDDar', 'GOUDA']
```
</div>
</div>
</div>


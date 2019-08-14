---
redirect_from:
  - "/notebooks/lesson-04-string-formatting"
interact_link: content/notebooks/lesson_04-string_formatting.ipynb
kernel_name: python3
has_widgets: false
title: 'Lesson 04-string Formatting'
prev_page:
  url: /notebooks/lesson_04-string_concatenation.html
  title: 'Lesson 04-string Concatenation'
next_page:
  url: /notebooks/lesson_04-string_formatting_checkpoint.html
  title: 'Lesson 04-string Formatting Checkpoint'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-python/blob/master/live%20class%20demonstrations/lesson%2004%20-%20string%20formatting.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
x = """
Item 1:      112.50$
item 2:        2.99$
VAT:          17.00%
VAT AMOUNT:    3.45$
TOTAL:        18.34$ 
"""

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print("{0: >20.2f}$".format(112))
print("{0: >20.2f}$".format(0.99))
print("{0: >20.2f}$".format((112 + 0.99) *0.17))

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
              112.00$
                0.99$
               19.21$
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print("""
{0: >20.2f}$ 
{1: >20.2f}$
{2: >20.2f}$
{0: >20.2f}$
""".format(112, 0.99, 119.21))


```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```

              112.00$                 0.99$
              119.21$
              112.00$

```
</div>
</div>
</div>


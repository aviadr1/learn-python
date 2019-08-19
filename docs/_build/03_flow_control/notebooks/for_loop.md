---
redirect_from:
  - "/03-flow-control/notebooks/for-loop"
interact_link: content/03_flow_control/notebooks/for_loop.ipynb
kernel_name: python3
has_widgets: false
title: 'For Loop'
prev_page:
  url: /03_flow_control/notebooks/enumerate_change_list.html
  title: 'Enumerate Change List'
next_page:
  url: /03_flow_control/notebooks/for_while_with_password_example.html
  title: 'For While With Password Example'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-python/blob/master/content/03_flow_control/notebooks/for_loop.ipynb" target="_blank">
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
'ADAM'.title()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'Adam'
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
for cheese in cheeses:
    print(cheese.title())

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Adam
Bree
Cheddar
Stilton
Gouda
Cottage
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
['adam', 'bree', 'cheddar', 'stilton', 'gouda', 'cottage']
```


</div>
</div>
</div>


---
redirect_from:
  - "/09-advanced-collections/notebooks/list-comprehension-order"
interact_link: content/09_advanced_collections/notebooks/list_comprehension_order.ipynb
kernel_name: python3
has_widgets: false
title: 'List Comprehension Order'
prev_page:
  url: /09_advanced_collections/notebooks/list_and_dictionary_comprehension_checkpoint.html
  title: 'List And Dictionary Comprehension Checkpoint'
next_page:
  url: /09_advanced_collections/notebooks/list_comprehension_sin.html
  title: 'List Comprehension Sin'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-python/blob/master/live%20class%20demonstrations/lesson%2009%20-%20list%20comprehension%20order.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
menu = {
    'steak' : 150,
    'pita' : 1.5,
    'hamburger' : 59,
    'chips' : 17,
    'shakshuka' : 32,
    'cake' : 25
}

order = ['steak', 'steak', 'chips', 'cake']


```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
total = 0
for item in order:
    price = menu[item]
    total += price
    
print(total)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
342
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
sum([menu[item] for item in order ])

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
342
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
cost_increase = 1.15

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
{ name:round(price*cost_increase) for name,price in menu.items() }

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
{'steak': 172,
 'pita': 2,
 'hamburger': 68,
 'chips': 20,
 'shakshuka': 37,
 'cake': 29}
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
menu.items()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
dict_items([('steak', 150), ('pita', 1.5), ('hamburger', 59), ('chips', 17), ('shakshuka', 32), ('cake', 25)])
```


</div>
</div>
</div>


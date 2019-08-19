---
redirect_from:
  - "/08-functions/notebooks/mul-pow"
interact_link: content/08_functions/notebooks/mul_pow.ipynb
kernel_name: python3
has_widgets: false
title: 'Mul Pow'
prev_page:
  url: /08_functions/notebooks/lambda_nested_functions_functional_programming.html
  title: 'Lambda Nested Functions Functional Programming'
next_page:
  url: /08_functions/notebooks/positional_and_named_arguments.html
  title: 'Positional And Named Arguments'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-python/blob/master/live%20class%20demonstrations/lesson%2008%20-%20mul%2C%20pow.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def mul(a,b):
    total = 0
    for iiii in range(b):
        total = total + a
    return total


```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
mul(10,20)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
200
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def pow(a,b):
    total = 1
    for iiii in range(b):
        #total = total * a
        total = mul(total, a)
    return total

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
pow(2,8)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
256
```


</div>
</div>
</div>


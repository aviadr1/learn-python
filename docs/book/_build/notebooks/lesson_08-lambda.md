---
redirect_from:
  - "/notebooks/lesson-08-lambda"
interact_link: content/notebooks/lesson_08-lambda.ipynb
kernel_name: python3
has_widgets: false
title: 'Lesson 08-lambda'
prev_page:
  url: /notebooks/lesson_08-function_fundamentals.html
  title: 'Lesson 08-function Fundamentals'
next_page:
  url: /notebooks/lesson_08-lambda_nested_functions_functional_programming.html
  title: 'Lesson 08-lambda Nested Functions Functional Programming'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-python/blob/master/live%20class%20demonstrations/lesson%2008%20-lambda.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
return100 = lambda : 100
return100()

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def sorted_bank_accounts(accounts):
    """
    (account_name, money)
    ("moshe", 1000)
    ("david", 500) 
    """
    def get_money(account):
        return account[1]
    
    return sorted(accounts, key=get_money) 

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def sorted_bank_accounts_lambda(accounts):
    get_money = lambda account: account[1]
    return sorted(accounts, key=get_money)

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def sorted_bank_accounts_lambda_shorter(accounts):
    return sorted(accounts, key=lambda account: account[1])

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
sorted_bank_accounts_lambda_shorter([
    ("moshe", 1000),
    ("david", 500),
    ("yana", 10000),
    ("simha", 9000),
    ("yocheved", 700),
    
])

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
[('david', 500),
 ('yocheved', 700),
 ('moshe', 1000),
 ('simha', 9000),
 ('yana', 10000)]
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
dir(int)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
['__abs__',
 '__add__',
 '__and__',
 '__bool__',
 '__ceil__',
 '__class__',
 '__delattr__',
 '__dir__',
 '__divmod__',
 '__doc__',
 '__eq__',
 '__float__',
 '__floor__',
 '__floordiv__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__getnewargs__',
 '__gt__',
 '__hash__',
 '__index__',
 '__init__',
 '__init_subclass__',
 '__int__',
 '__invert__',
 '__le__',
 '__lshift__',
 '__lt__',
 '__mod__',
 '__mul__',
 '__ne__',
 '__neg__',
 '__new__',
 '__or__',
 '__pos__',
 '__pow__',
 '__radd__',
 '__rand__',
 '__rdivmod__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__rfloordiv__',
 '__rlshift__',
 '__rmod__',
 '__rmul__',
 '__ror__',
 '__round__',
 '__rpow__',
 '__rrshift__',
 '__rshift__',
 '__rsub__',
 '__rtruediv__',
 '__rxor__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__sub__',
 '__subclasshook__',
 '__truediv__',
 '__trunc__',
 '__xor__',
 'bit_length',
 'conjugate',
 'denominator',
 'from_bytes',
 'imag',
 'numerator',
 'real',
 'to_bytes']
```


</div>
</div>
</div>


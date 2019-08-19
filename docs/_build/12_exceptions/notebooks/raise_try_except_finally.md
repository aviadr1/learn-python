---
redirect_from:
  - "/12-exceptions/notebooks/raise-try-except-finally"
interact_link: content/12_exceptions/notebooks/raise_try_except_finally.ipynb
kernel_name: python3
has_widgets: false
title: 'Raise Try Except Finally'
prev_page:
  url: /12_exceptions/notebooks/exceptions.html
  title: 'Exceptions'
next_page:
  url: /13_multiprocessing/notebooks/os_system_subprocess.html
  title: '13 multiprocessing'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-python/blob/master/live%20class%20demonstrations/lesson%2012%20-%20raise%2C%20try%2C%20except%2C%20finally.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def B(x):
    if x<0:
        raise LogicError("I dont like negative numbers", x)
    else:
        return x
    
def A(x):
    try:
        print(f"Starting A({x})")
        return B(x)
    finally:
        print(f"finished A({x})")

for i in [-1, 0, 1]:
    try:
        y=A(i)
        print(f"A({i})={y}")
    except Exception as x:
        print(f"failed running A({i}): ", )
        
        

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Starting A(-1)
finished A(-1)
failed running A(-1): 
Starting A(0)
finished A(0)
A(0)=0
Starting A(1)
finished A(1)
A(1)=1
```
</div>
</div>
</div>


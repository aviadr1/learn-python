---
redirect_from:
  - "/08-functions/notebooks/positional-and-named-arguments"
interact_link: content/08_functions/notebooks/positional_and_named_arguments.ipynb
kernel_name: python3
has_widgets: false
title: 'Positional And Named Arguments'
prev_page:
  url: /08_functions/notebooks/mul_pow.html
  title: 'Mul Pow'
next_page:
  url: /08_functions/notebooks/soft_intro_to_functions.html
  title: 'Soft Intro To Functions'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-python/blob/master/live%20class%20demonstrations/lesson%2008%20-%20positional%20and%20named%20arguments.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def annoying_print3(obj1, obj2="", obj3=""):
    print(obj1, obj2, obj3)

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
annoying_print3() # need at least 1 parameter for obj1 


```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_traceback_line}
```

    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-4-1f3fcb0f52bb> in <module>
    ----> 1 annoying_print3() # need at least 1 parameter for obj1
    

    TypeError: annoying_print3() missing 1 required positional argument: 'obj1'


```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
annoying_print3("hi") # hi
annoying_print3(1, 2) # 1 2
annoying_print3(1, 2, 3) # 1 2 3
annoying_print3(1, 2, 3, 4) # too many params

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
hi  
1 2 
1 2 3
```
</div>
</div>
<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_traceback_line}
```

    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-9-c886d9407ea9> in <module>
          2 annoying_print3(1, 2) # 1 2
          3 annoying_print3(1, 2, 3) # 1 2 3
    ----> 4 annoying_print3(1, 2, 3, 4) # too many params
    

    TypeError: annoying_print3() takes from 1 to 3 positional arguments but 4 were given


```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
annoying_print3(obj1=1) # 1
annoying_print3(obj1=1, obj2=2) # 1 2
annoying_print3(obj1=1, obj3=3) # 1  3
annoying_print3(obj2=2, obj1=1) # 1 2
annoying_print3(1, obj2=2) # 1 2
annoying_print3(1, obj3=3) # 1  3

 

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
1  
1 2 
1  3
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
annoying_print3(obj2=1) # needs value for obj1

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_traceback_line}
```

    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-12-8babd8f39c03> in <module>
    ----> 1 annoying_print3(obj2=1) # needs value for obj1
    

    TypeError: annoying_print3() missing 1 required positional argument: 'obj1'


```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# after named arguments cannot put positional arguments
annoying_print3(obj2=2, 1) 

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_traceback_line}
```

      File "<ipython-input-11-1f30a95c9611>", line 2
        annoying_print3(obj2=2, 1)
                               ^
    SyntaxError: positional argument follows keyword argument



```
</div>
</div>
</div>


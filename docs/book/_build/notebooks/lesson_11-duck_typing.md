---
redirect_from:
  - "/notebooks/lesson-11-duck-typing"
interact_link: content/notebooks/lesson_11-duck_typing.ipynb
kernel_name: python3
has_widgets: false
title: 'Lesson 11-duck Typing'
prev_page:
  url: /notebooks/lesson_11-basic_classes.html
  title: 'Lesson 11-basic Classes'
next_page:
  url: /notebooks/lesson_11-inheritance.html
  title: 'Lesson 11-inheritance'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-python/blob/master/live%20class%20demonstrations/lesson%2011%20-%20duck%20typing.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
class MobilePhone:
    def dial(self, phone):
        print("mobile phone dialed", phone)
        
class Fax:
    def dial(self, phone):
        print("fax dialed", phone)
        
class NotAPhone:
    pass

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
for obj in [MobilePhone(), Fax(), NotAPhone()]:
    obj.dial("053-55555")

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
mobile phone dialed 053-55555
fax dialed 053-55555
```
</div>
</div>
<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_traceback_line}
```

    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-6-12fa7657042c> in <module>
          1 for obj in [MobilePhone(), Fax(), NotAPhone()]:
    ----> 2     obj.dial("053-55555")
    

    AttributeError: 'NotAPhone' object has no attribute 'dial'


```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
numpy.dot

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_traceback_line}
```

    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-7-4b1a855c9c7d> in <module>
    ----> 1 numpy.dot
    

    NameError: name 'numpy' is not defined


```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
import math

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
math.sqrt(-100)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_traceback_line}
```

    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-9-b5dc45673dc3> in <module>
    ----> 1 math.sqrt(-100)
    

    ValueError: math domain error


```
</div>
</div>
</div>


---
redirect_from:
  - "/03-flow-control/notebooks/lesson-03-july-break-continue"
interact_link: content/03_flow_control/notebooks/lesson_03-july_break_continue.ipynb
kernel_name: python3
has_widgets: false
title: 'Lesson 03-july Break Continue'
prev_page:
  url: /03_flow_control/notebooks/lesson_03-if_else_password.html
  title: 'Lesson 03-if Else Password'
next_page:
  url: /03_flow_control/notebooks/lesson_03-july_enumerate_zip.html
  title: 'Lesson 03-july Enumerate Zip'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-python/blob/master/live%20class%20demonstrations/lesson%2003%20-%20july%20break%20continue.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
my_condition = False
if my_condition:
    # do something
    pass
    
print("end of example")

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
end of example
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
finished = False
while not finished:
    passw = input('?')
    if len(passw) < 4:
        print('too short')
    # more conditions
    # ...
    else:
        print('excellent')
        finished = True

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_traceback_line}
```

      File "<ipython-input-4-d52d0e26abd7>", line 6
        else:
             ^
    SyntaxError: unexpected EOF while parsing



```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
while True:
    passw = input('?')
    if len(passw) < 4:
        print('too short')
    # more conditions
    # ...
    else:
        print('excellent')
        break

```
</div>

</div>


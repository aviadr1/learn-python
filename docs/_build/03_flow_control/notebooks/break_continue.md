---
redirect_from:
  - "/03-flow-control/notebooks/break-continue"
interact_link: content/03_flow_control/notebooks/break_continue.ipynb
kernel_name: python3
has_widgets: false
title: 'Break Continue'
prev_page:
  url: /03_flow_control/notebooks/1-100_multiplication_matrix_Luah_Kefel_.html
  title: '1-100 Multiplication Matrix Luah Kefel '
next_page:
  url: /03_flow_control/notebooks/casting_objects_as_booleans.html
  title: 'Casting Objects As Booleans'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-python/blob/master/content/03_flow_control/notebooks/break_continue.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
while True:
    password = input("give me a password:")
    if len(password) <= 4 :
        print("too short")
    elif password.islower():
        print("please mix some uppercase letters")
    elif password.isupper():
        print("please mix some lowercase letters")
    else:
        print("great password")
        break
        print(1,2,3)

print("loop finished")

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
give me a password:BLAHblah
great password
loop finished
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
finished = False
while not finished:
    password = input("give me a password:")
    if len(password) <= 4 :
        print("too short")
        
    if password.islower():
        print("please mix some uppercase letters")
        
    if password.isupper():
        print("please mix some lowercase letters")
        
    else:
        print("great password")
        finished = True

print("loop finished")

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
give me a password:blah
too short
please mix some uppercase letters
great password
loop finished
```
</div>
</div>
</div>


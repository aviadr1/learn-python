---
redirect_from:
  - "/03-flow-control/notebooks/if-elif-else-with-password-checking"
interact_link: content/03_flow_control/notebooks/if_elif_else-with_password_checking.ipynb
kernel_name: python3
has_widgets: false
title: 'If Elif Else-with Password Checking'
prev_page:
  url: /03_flow_control/notebooks/for_while_with_password_example.html
  title: 'For While With Password Example'
next_page:
  url: /03_flow_control/notebooks/if_else_password.html
  title: 'If Else Password'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-python/blob/master/content/03_flow_control/notebooks/if_elif_else-with_password_checking.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
password = input("give me a password:")

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
give me a password:blah
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
if len(password) <= 4 :
    print("too short")

if password.islower():
    print("please mix some uppercase letters")

if password.isupper():
    print("please mix some lowercase letters")

else:
    

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
too short
please mix some uppercase letters
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
if len(password) <= 4 :
    print("too short")
elif password.islower():
    print("please mix some uppercase letters")
elif password.isupper():
    print("please mix some lowercase letters")
else:
    print("great password")


```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
great password
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
True and False

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
False
```


</div>
</div>
</div>


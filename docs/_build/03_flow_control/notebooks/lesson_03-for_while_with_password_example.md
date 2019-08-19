---
redirect_from:
  - "/03-flow-control/notebooks/lesson-03-for-while-with-password-example"
interact_link: content/03_flow_control/notebooks/lesson_03-for_while_with_password_example.ipynb
kernel_name: python3
has_widgets: false
title: 'Lesson 03-for While With Password Example'
prev_page:
  url: /03_flow_control/notebooks/lesson_03-for_loop.html
  title: 'Lesson 03-for Loop'
next_page:
  url: /03_flow_control/notebooks/lesson_03-if_elif_else-with_password_checking.html
  title: 'Lesson 03-if Elif Else-with Password Checking'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-python/blob/master/live%20class%20demonstrations/lesson%2003%20-%20for%2C%20while%2C%20with%20password%20example.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
password = input("gimme a new password: ")
if len(password) < 4 or len(password) > 6:
    print("your password must be betweeen 4-6 letters long")
elif password.islower() or password.isupper():
    print ("use a combination of lower and upper case letters")
elif '@' not in password:
    print("must use special characters like '@'")
else:
    print("awesome password")

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
gimme a new password: blAH
must use special characters like '@'
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
a = [1,2,3,4, "blah"]

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
if len(a) > 0:
    print(a.pop())
else:
    print("list is empty")

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
blah
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
a.pop()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
4
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
a = [1,2,3,4, "blah"]

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
while len(a) > 0:
    print(a.pop())
    
print("list is empty")

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
blah
4
3
2
1
list is empty
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
i=0
while i<10:
    print(i)
    i=i+1

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
0
1
2
3
4
5
6
7
8
9
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
for i in range(10):
    print(i)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
0
1
2
3
4
5
6
7
8
9
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
password = ""
while True:
    password = input("Gimme password: ")
    if len(password) < 6:
        print("too short")
        continue
        
    if password.islower() or password.isupper():
        print("need combination of upper and lower case")
        continue
        
    print("awesome password")
    break

print("break was called")

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Gimme password: blah
too short
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
import getpass


```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
getpass.getpass("properly ask for password :")

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
properly ask for password :········
```
</div>
</div>
<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'very secret password'
```


</div>
</div>
</div>


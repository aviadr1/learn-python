---
redirect_from:
  - "/04-strings/notebooks/formatting-bitahon"
interact_link: content/04_strings/notebooks/formatting_bitahon.ipynb
kernel_name: python3
has_widgets: false
title: 'Formatting Bitahon'
prev_page:
  url: /04_strings/notebooks/formatting_bitahon.html
  title: 'notebooks'
next_page:
  url: /04_strings/notebooks/print_parameters.html
  title: 'Print Parameters'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-python/blob/master/live%20class%20demonstrations/lesson%2004%20-%20formatting%20bitahon.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
"the quick brown fox jumped over the lazy dog".find("quick")

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
age = 30
height = 180
name = "ben"
score =85

"hi {}, happy {} birthday, your height is {}, your score is {}".format(name, age, height, score)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'hi ben, happy 30 birthday, your height is 180, your score is 85'
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
age = 30
height = 180
name = "ben"
score =85

"hi {2}, happy {0} birthday, your height is {1}, your score is {3}".format(age, height, name, score)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'hi ben, happy 30 birthday, your height is 180, your score is 85'
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
x= """hi {0}, 
{0} is a nice name
goodbye {0}
""".format(name, "this is not used")
print(x)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
hi ben, 
ben is a nice name
goodbye ben

```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
"{}".format(10/3)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'3.3333333333333335'
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
import math
math.sin(math.pi)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
1.2246467991473532e-16
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
"{:.2f}".format(math.sin(math.pi))

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'0.00'
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
"{:.20f}".format(math.sin(math.pi))

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'0.00000000000000012246'
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
ord(' ')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
32
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
"0x{:x}".format(ord(' '))

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'0x20'
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
"{:.2}".format(math.sin(math.pi))

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'1.2e-16'
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
"""
steak:                150.00 NIS
pita:                   1.50 NIS
shakshuka im thi na:   25.00 NIS
vat%                   17.00 %
vat:                   35.56
total:                222.40 NIS
"""

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'\nsteak:                150.00 NIS\npita:                   1.50 NIS\nshakshuka im thi na:   25.00 NIS\nvat%                   17.00 %\nvat:                   35.56\ntotal:                222.40 NIS\n'
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print("{:7.2f}".format(1.5))
print("{:7.2f}".format(222.49))
print("{:7.2f}".format(-10))

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
  +1.50
 222.49
 -10.00
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print("{:+7.2f}".format(1.5))
print("{:+7.2f}".format(222.49))
print("{:+7.2f}".format(-10))

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
  +1.50
+222.49
 -10.00
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print("{:^10.2f}".format(1.5))
print("{:^10.2f}".format(222.49))
print("{:^10.2f}".format(-10))

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
   1.50   
  222.49  
  -10.00  
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print("{:-^10.2f}".format(1.5))
print("{:-^10.2f}".format(222.49))
print("{:-^10.2f}".format(-10))

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
---1.50---
--222.49--
---10.00--
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print("{:#x}".format(32))
print("{:#o}".format(32))
print("{:#b}".format(32))
print("{:#d}".format(32))

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
0x20
0o40
0b100000
32
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
x= "hi {2}, happy {0} birthday, your height is {1}, your score is {3}".format(age, height, name, score)
print(x)

x = f"hi {name}, happy {age} birthday, your height is {height}, your score is {score}"
print(x)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
hi ben, happy 30 birthday, your height is 180, your score is 85
hi ben, happy 30 birthday, your height is 180, your score is 85
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print(f"""freedom is the right to say that {1}+{1} = {1+1}""")

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
freedom is the right to say that 1+1 = 2
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print(f"""{"the quick brown fox".upper().replace("FOX", "cat")}""")

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
THE QUICK BROWN cat
```
</div>
</div>
</div>


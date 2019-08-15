---
redirect_from:
  - "/notebooks/lesson-09-list-comprehension-sin"
interact_link: content/notebooks/lesson_09-list_comprehension_sin.ipynb
kernel_name: python3
has_widgets: false
title: 'Lesson 09-list Comprehension Sin'
prev_page:
  url: /notebooks/lesson_09-list_comprehension_order.html
  title: 'Lesson 09-list Comprehension Order'
next_page:
  url: /notebooks/lesson_09-shallow_copy_and_deep_copy.html
  title: 'Lesson 09-shallow Copy And Deep Copy'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-python/blob/master/live%20class%20demonstrations/lesson%2009%20-%20list%20comprehension%20sin.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
[2**x  for x in range(9)]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
[1, 2, 4, 8, 16, 32, 64, 128, 256]
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
list(range(9))

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
[0, 1, 2, 3, 4, 5, 6, 7, 8]
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
dalist = "the quick brown fox jumped over the lazy dog".split()

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
dalist

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
['the', 'quick', 'brown', 'fox', 'jumped', 'over', 'the', 'lazy', 'dog']
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
[word.title()   for word in dalist ]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
['The', 'Quick', 'Brown', 'Fox', 'Jumped', 'Over', 'The', 'Lazy', 'Dog']
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
[ [word.title(), len(word)]   for word in dalist ]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
[['The', 3],
 ['Quick', 5],
 ['Brown', 5],
 ['Fox', 3],
 ['Jumped', 6],
 ['Over', 4],
 ['The', 3],
 ['Lazy', 4],
 ['Dog', 3]]
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
[ len(word)   for word in dalist ]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
[3, 5, 5, 3, 6, 4, 3, 4, 3]
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def test1():
    return "OK"

def test2():
    return "FAIL"

def test3 ():
    return "OK"


```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
tests = [test1, test2, test3]

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
tests

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
[<function __main__.test1()>,
 <function __main__.test2()>,
 <function __main__.test3()>]
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
test_run = [t()    for t in tests]

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
test_run

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
['OK', 'FAIL', 'OK']
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
import re
def password_length_is_ok(passw):
    if 8<len(passw)<12:
        return "OK"
    else:
        return "Bad length"
    
def has_special_characters(paslensw):
    if re.match(r"[\@\#\$\%\^\&\*]", passw):
        return "OK"
    else:
        return "missing special characters"
    

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
password_checks = [password_length_is_ok, has_special_characters]

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
password = "1234567890"
password_checks_run = [check(password) for check in password_checks ]

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
password_checks_run

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
['OK', 'missing special characters']
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
password_checks_run = [ [check.__name__, check(password)] for check in password_checks ]

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
password_checks_run

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
[['password_length_is_ok', 'OK'],
 ['has_special_characters', 'missing special characters']]
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
len(password_checks)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
2
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
len(password_checks_run)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
2
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
deg = [0 , 30, 45, 60, 90]

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
import math
deg


```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
[0, 30, 45, 60, 90]
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
rad = [d * math.pi/180     for d in deg]

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
rad

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
[0.0,
 0.5235987755982988,
 0.7853981633974483,
 1.0471975511965976,
 1.5707963267948966]
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
results = [math.sin(r) for r in rad]

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
["{0:1.2f}".format(r) for r in results]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
['0.00', '0.50', '0.71', '0.87', '1.00']
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
["{0:1.2f}".format(x) for x in  [math.sin(rad) for rad in [ d * math.pi/180 for d in deg ] ]]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
['0.00', '0.50', '0.71', '0.87', '1.00']
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
["{0:1.2f}".format(math.sin(d*math.pi/180)) for d in deg]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
['0.00', '0.50', '0.71', '0.87', '1.00']
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
deg = [0,30, 45, 60]

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
[d + 90*i for i in range(4) for d in deg ]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
[0, 30, 45, 60, 90, 120, 135, 150, 180, 210, 225, 240, 270, 300, 315, 330]
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
deg

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
[0, 30, 45, 60]
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
deg2 = [d+90   for d  in deg]

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
deg2

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
[90, 120, 135, 150]
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
deg3 = [d+90   for d  in deg2]

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
deg4 =  [d+90   for d  in deg3]

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print(deg)
print(deg2)
print(deg3)
print(deg4)


```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
[0, 30, 45, 60]
[90, 120, 135, 150]
[180, 210, 225, 240]
[270, 300, 315, 330]
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
for i in range(4):
    for d in [0, 30, 45, 60]:
        print(d + i*90)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
0
30
45
60
90
120
135
150
180
210
225
240
270
300
315
330
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
deg360 = [ d + i*90 for i in range(4) for d in deg ]

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
deg360 = [ d + i*90  for d in deg  for i in range(4)]

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
deg360

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
[0, 30, 45, 60, 90, 120, 135, 150, 180, 210, 225, 240, 270, 300, 315, 330]
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
mydict = { d : "{0:1.2f}".format(math.sin(d*math.pi/180))   for d in deg360}

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
mydict

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
{0: '0.00',
 30: '0.50',
 45: '0.71',
 60: '0.87',
 90: '1.00',
 120: '0.87',
 135: '0.71',
 150: '0.50',
 180: '0.00',
 210: '-0.50',
 225: '-0.71',
 240: '-0.87',
 270: '-1.00',
 300: '-0.87',
 315: '-0.71',
 330: '-0.50'}
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
[key for key,value in mydict.items()]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
[0, 30, 45, 60, 90, 120, 135, 150, 180, 210, 225, 240, 270, 300, 315, 330]
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
[value for key,value in mydict.items()]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
['0.00',
 '0.50',
 '0.71',
 '0.87',
 '1.00',
 '0.87',
 '0.71',
 '0.50',
 '0.00',
 '-0.50',
 '-0.71',
 '-0.87',
 '-1.00',
 '-0.87',
 '-0.71',
 '-0.50']
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
thenums= [100, 10000, -9, 9 , -16, 16]

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
[math.sqrt(num) for num in thenums if num >= 0]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
[]
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
thenums

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
[100, 10000, -9, 9, -16, 16]
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
abs_thenums = [x if x>=0 else -x for x in thenums]

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
abs_thenums

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
[100, 10000, 9, 9, 16, 16]
```


</div>
</div>
</div>


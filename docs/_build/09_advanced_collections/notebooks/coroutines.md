---
redirect_from:
  - "/09-advanced-collections/notebooks/coroutines"
interact_link: content/09_advanced_collections/notebooks/coroutines.ipynb
kernel_name: python3
has_widgets: false
title: 'Coroutines'
prev_page:
  url: /09_advanced_collections/notebooks/coroutines.html
  title: 'notebooks'
next_page:
  url: /09_advanced_collections/notebooks/deepcopy_shallow_copy.html
  title: 'Deepcopy Shallow Copy'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-python/blob/master/live%20class%20demonstrations/lesson%2009%20-%20coroutines.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
f = open('dir.txt')
while not f.eof():
    line = f.readline()
    

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
for line in f.readlines():
    

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def line_reader(f):
    while not f.eof():
        line = f.readline()
        yield line


```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
for line in line_reader(f):
    

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def get_password():
    while True:
        p = input('give password')
        if len(p) <4:
            yield (False, 'Too short', p)
        elif p.islower():
            yield (False, 'need upper', p)
        else:
            break
    yield (True, ' ', p)
    
            

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
for newpass in get_password():
    if not newpass[0]:
        print(newpass[2], 'is not a good password because', newpass[1])
    else:
        print('hurray')
        break

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
give password1
1 is not a good password because Too short
give password2
2 is not a good password because Too short
give password3
3 is not a good password because Too short
give password4
4 is not a good password because Too short
give password234
234 is not a good password because Too short
give passwordblahBLAH
hurray
```
</div>
</div>
</div>


---
redirect_from:
  - "/09-advanced-collections/notebooks/template-for-list-comprehension"
interact_link: content/09_advanced_collections/notebooks/template_for_list_comprehension.ipynb
kernel_name: python3
has_widgets: false
title: 'Template For List Comprehension'
prev_page:
  url: /09_advanced_collections/notebooks/shallow_copy_and_deep_copy.html
  title: 'Shallow Copy And Deep Copy'
next_page:
  url: /10_modules/notebooks/modules.html
  title: '10 modules'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-python/blob/master/content/09_advanced_collections/notebooks/template_for_list_comprehension.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
first_list = ...

newlist = []
for item in first_list:
    newitem = ...
    newlist.append(newitem)
    
    
    

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
[2**x for x in range(16)]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
[1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768]
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
import pprint

first_list = range(16)

newlist = []
for item in first_list:
    newitem = 2**item
    newlist.append(newitem)
    
pprint.pprint(newlist)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
[1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768]
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
first_list = ...

newlist = []
for item in first_list:
    if ... :
        newitem = ...
        newlist.append(newitem)
    

```
</div>

</div>


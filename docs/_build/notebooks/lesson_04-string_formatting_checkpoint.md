---
redirect_from:
  - "/notebooks/lesson-04-string-formatting-checkpoint"
interact_link: content/notebooks/lesson_04-string_formatting_checkpoint.ipynb
kernel_name: python3
has_widgets: false
title: 'Lesson 04-string Formatting Checkpoint'
prev_page:
  url: /notebooks/lesson_04-string_formatting.html
  title: 'Lesson 04-string Formatting'
next_page:
  url: /notebooks/lesson_04-string_slicing.html
  title: 'Lesson 04-string Slicing'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-python/blob/master/live%20class%20demonstrations/lesson%2004%20-%20string%20formatting%20checkpoint.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




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
math.sin(0)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
0.0
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
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
"""
shakshuka:        10.99 NIS
break:             7.50 NIS
steak:           125.00 NIS
vat%              17.00%
vat:              15.82 NIS  
total:           142.67 NIS
"""

x = """
shakshuka: {:>10.2f} NIS
break:     {:>10.2f} NIS
steak:     {:>10x} NIS
vat%       {:>10.2f} %
vat:       {:>10.2f} NIS  
total:     {:>10.2f} NIS
""".format(10.99, 7.50, 125, 17, 15.82, 142.67)
print(x)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```

shakshuka:      10.99 NIS
break:           7.50 NIS
steak:            175 NIS
vat%            17.00 %
vat:            15.82 NIS  
total:         142.67 NIS

```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
"{:X}".format(255)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'FF'
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
shaksuha = 10.5
bread = 5
steak = 125
vatper = 17
x = f"""
shakshuka: {shaksuha:>10.2f} NIS
bread:     {bread:>10.2f} NIS
steak:     {steak:>10.2f} NIS
vat%:      {vatper:>10.2f} %
vat:       {(shaksuha+bread+steak)*vatper/100:>10.2f} NIS
"""
print(x)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```

shakshuka:      10.50 NIS
bread:           5.00 NIS
steak:         125.00 NIS
vat%:           17.00 %
vat:            23.89 NIS

```
</div>
</div>
</div>


---
redirect_from:
  - "/notebooks/lesson-07-pickle-checkpoint"
interact_link: content/notebooks/lesson_07-pickle_checkpoint.ipynb
kernel_name: python3
has_widgets: false
title: 'Lesson 07-pickle Checkpoint'
prev_page:
  url: /notebooks/lesson_07-pandas_and_csv.html
  title: 'Lesson 07-pandas And Csv'
next_page:
  url: /notebooks/lesson_08-documentation.html
  title: 'Lesson 08-documentation'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-python/blob/master/live%20class%20demonstrations/lesson%2007%20-pickle%20checkpoint.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
big_giant_data = [
    "my string",
    1,
    2,
    3,
    {
        "important" : [ [1,2], ["one", "two"] ],
        "blah" : { 1: "one", 2: "two"}
    }
]
big_giant_data

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
['my string',
 1,
 2,
 3,
 {'important': [[1, 2], ['one', 'two']], 'blah': {1: 'one', 2: 'two'}}]
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
import pickle
with open("mypicklefile.bin", "wb") as f:
    pickle.dump(big_giant_data, file=f)

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
del big_giant_data

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
big_giant_data

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_traceback_line}
```

    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-6-f55cfec9910d> in <module>
    ----> 1 big_giant_data
    

    NameError: name 'big_giant_data' is not defined


```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
with open("mypicklefile.bin", "rb") as f:
    big_giant_data2 = pickle.load(f)

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
big_giant_data2

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
['my string',
 1,
 2,
 3,
 {'important': [[1, 2], ['one', 'two']], 'blah': {1: 'one', 2: 'two'}}]
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
import json
with open("myobject.json.txt", "w") as f:
    json.dump(big_giant_data, fp=f)

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
["my string", 1, 2, 3, {"important": [[1, 2], ["one", "two"]], "blah": {"1": "one", "2": "two"}}]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
['my string',
 1,
 2,
 3,
 {'important': [[1, 2], ['one', 'two']], 'blah': {'1': 'one', '2': 'two'}}]
```


</div>
</div>
</div>


---
redirect_from:
  - "/02-variables/notebooks/lesson-02-lists"
interact_link: content/02-variables/notebooks/lesson_02-lists.ipynb
kernel_name: python3
has_widgets: false
title: 'Lesson 02-lists'
prev_page:
  url: /02-variables/notebooks/lesson_02-importing_math_printing_floats.html
  title: 'Lesson 02-importing Math Printing Floats'
next_page:
  url: /02-variables/notebooks/lesson_02-mutability_vs_immutability.html
  title: 'Lesson 02-mutability Vs Immutability'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-python/blob/master/live%20class%20demonstrations/lesson%2002%20-%20lists.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
x = ["one", "two", "three", "four"]

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
x[0]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'one'
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
x[1]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'two'
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
x[2]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'three'
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
len(x)

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
x[len(x) - 1]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'four'
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
x[-1]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'four'
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
x[-2]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'three'
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
x[-3]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'two'
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
x[-4]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'one'
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
x[3]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'four'
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
x[4]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_traceback_line}
```

    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-12-cedd7ac36334> in <module>
    ----> 1 x[4]
    

    IndexError: list index out of range


```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
x[-5]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_traceback_line}
```

    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-13-3f8aa68a9513> in <module>
    ----> 1 x[-5]
    

    IndexError: list index out of range


```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
x

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
['one', 'two', 'three', 'four']
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
x[-1] = 4

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
x

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
['one', 'two', 'three', 4]
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
type(x[-1])

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
int
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
type(x[0])

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
str
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
x[0] = x[0].upper()

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
x

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
['ONE', 'two', 'three', 4]
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
x[-1] = "four"

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
numbers = x

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
[num.upper() for num in numbers]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
['ONE', 'TWO', 'THREE', 'FOUR']
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
numbers[0]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'ONE'
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
numbers[0][0]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'O'
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
numbers[1][2]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'o'
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
numbers

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
['ONE', 'two', 'three', 'four']
```


</div>
</div>
</div>


---
redirect_from:
  - "/notebooks/lesson-03-july-enumerate-zip"
interact_link: content/notebooks/lesson_03-july_enumerate_zip.ipynb
kernel_name: python3
has_widgets: false
title: 'Lesson 03-july Enumerate Zip'
prev_page:
  url: /notebooks/lesson_03-july_break_continue.html
  title: 'Lesson 03-july Break Continue'
next_page:
  url: /notebooks/lesson_03-while_loop-password.html
  title: 'Lesson 03-while Loop-password'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-python/blob/master/live%20class%20demonstrations/lesson%2003%20-%20july%20enumerate%2C%20zip.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
song = """Yeah yeah yeah yeah yeah yeah
Yeah yeah yeah yeah yeah yeah
I think I did it again
I made you believe we're more than just friends
Oh baby
It might seem like a crush
But it doesn't mean that I'm serious
'Cause to lose all my senses
That is just so typically me
Oh baby, baby""".splitlines()


```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
song = ['Yeah yeah yeah yeah yeah yeah',
 'Yeah yeah yeah yeah yeah yeah',
 'I think I did it again',
 "I made you believe we're more than just friends",
 'Oh baby',
 'It might seem like a crush',
 "But it doesn't mean that I'm serious",
 "'Cause to lose all my senses",
 'That is just so typically me',
 'Oh baby, baby']

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
song

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
['Yeah yeah yeah yeah yeah yeah',
 'Yeah yeah yeah yeah yeah yeah',
 'I think I did it again',
 "I made you believe we're more than just friends",
 'Oh baby',
 'It might seem like a crush',
 "But it doesn't mean that I'm serious",
 "'Cause to lose all my senses",
 'That is just so typically me',
 'Oh baby, baby']
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
song_with_line_numbers = list(enumerate(song, 1))

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
song_with_line_numbers

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
[(1, 'Yeah yeah yeah yeah yeah yeah'),
 (2, 'Yeah yeah yeah yeah yeah yeah'),
 (3, 'I think I did it again'),
 (4, "I made you believe we're more than just friends"),
 (5, 'Oh baby'),
 (6, 'It might seem like a crush'),
 (7, "But it doesn't mean that I'm serious"),
 (8, "'Cause to lose all my senses"),
 (9, 'That is just so typically me'),
 (10, 'Oh baby, baby')]
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
i, item = (1, 'Yeah yeah yeah yeah yeah yeah')

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
i

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
1
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
item

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'Yeah yeah yeah yeah yeah yeah'
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
for i, item in enumerate(song):
    print(i, ':', item)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
0 : Yeah yeah yeah yeah yeah yeah
1 : Yeah yeah yeah yeah yeah yeah
2 : I think I did it again
3 : I made you believe we're more than just friends
4 : Oh baby
5 : It might seem like a crush
6 : But it doesn't mean that I'm serious
7 : 'Cause to lose all my senses
8 : That is just so typically me
9 : Oh baby, baby
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
words = "the quick brown fox jumped over the lazy dog".split()

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
for i, word in enumerate(words):
    words[i] = word.capitalize()

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
words

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
fruits = [
    'apple',
    'mango',
    'pear',
    'grapes'
]

prices = [
    14,
    7,
    8,
    25
]

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
list(zip(fruits, prices))

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
[('apple', 14), ('mango', 7), ('pear', 8), ('grapes', 25)]
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
for fruit, price in zip(fruits, prices):
    print(fruit, price)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
apple 14
mango 7
pear 8
grapes 25
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
dict (fruits, prices)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_traceback_line}
```

    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-27-f21d9a0d94b6> in <module>
    ----> 1 dict (fruits, prices)
    

    TypeError: dict expected at most 1 arguments, got 2


```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
dict(zip(fruits, prices))

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
{'apple': 14, 'mango': 7, 'pear': 8, 'grapes': 25}
```


</div>
</div>
</div>


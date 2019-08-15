---
redirect_from:
  - "/notebooks/lesson-09-dictionary-comprehension-generators-lazy-lists"
interact_link: content/notebooks/lesson_09-dictionary_comprehension_generators_lazy_lists.ipynb
kernel_name: python3
has_widgets: false
title: 'Lesson 09-dictionary Comprehension Generators Lazy Lists'
prev_page:
  url: /notebooks/lesson_09-deepcopy_shallow_copy.html
  title: 'Lesson 09-deepcopy Shallow Copy'
next_page:
  url: /notebooks/lesson_09-generators_lazy_functions.html
  title: 'Lesson 09-generators Lazy Functions'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-python/blob/master/live%20class%20demonstrations/lesson%2009%20-%20dictionary%20comprehension%2C%20generators%2C%20lazy%20lists.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
cheeses = ["adam", "bree", "cheddar", "rockfort"]
prices = [1.9, 2.45, 9.90, 6.60]

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
range(len(cheeses))

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
range(0, 4)
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
{cheeses[i] : prices[i]  for i in range(4)}

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
{'adam': 1.9, 'bree': 2.45, 'cheddar': 9.9, 'rockfort': 6.6}
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
nums = [2, -6, 4, 100, -9, 81]

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
import math
[math.sqrt(x) for x  in nums if x>=0]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
[1.4142135623730951, 2.0, 10.0, 9.0]
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
newlist = []
for i in range(1, 4):
    for j in range(1,4):
        newitem = f"{i} * {j} = {i*j}"
        newlist.append(newitem)
        
print(newlist)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
['1 * 1 = 1', '1 * 2 = 2', '1 * 3 = 3', '2 * 1 = 2', '2 * 2 = 4', '2 * 3 = 6', '3 * 1 = 3', '3 * 2 = 6', '3 * 3 = 9']
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
[f"{i} * {j} = {i*j}" for i in range(1,4) for j in range(1,4)]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
['1 * 1 = 1',
 '1 * 2 = 2',
 '1 * 3 = 3',
 '2 * 1 = 2',
 '2 * 2 = 4',
 '2 * 3 = 6',
 '3 * 1 = 3',
 '3 * 2 = 6',
 '3 * 3 = 9']
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
range(1000 * 1000 * 1000)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
range(0, 1000000000)
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
x = list(range(1000* 1000 * 10))

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
f = open("myfile.txt")

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print(f)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
<_io.TextIOWrapper name='myfile.txt' mode='r' encoding='cp1252'>
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
lines = f.readlines()

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
type(lines)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
list
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
gen = (2**i for i in range(8))

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
next(gen)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_traceback_line}
```

    ---------------------------------------------------------------------------

    StopIteration                             Traceback (most recent call last)

    <ipython-input-3-6e72e47198db> in <module>
    ----> 1 next(gen)
    

    StopIteration: 


```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
for i in gen:
    print(i)
    
    

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
1
2
4
8
16
32
64
128
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def infinite():
    i=0
    while True:
        #return i
        yield i
        i+=1


```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
x = infinite()
print(x)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
<generator object infinite at 0x05E8E7B0>
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
next(x)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
7
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def read_file_line_by_line_lazily(f):
    while True:
        line = f.readline().strip()
        yield line

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python

f = open("myfile.txt")
lines = read_file_line_by_line_lazily(f)
non_empty_lines = (line for line in lines if len(line.strip()) > 0)
print(lines)


```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
<generator object read_file_line_by_line_lazily at 0x0623A770>
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
for line in non_empty_lines:
    print(line)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
I am Daniel
I am Sam
Sam I am
That Sam-I-am
That Sam-I-am!
I do not like
That Sam-I-am
Do you like
Green eggs and ham
I do not like them,
Sam-I-am.
I do not like
Green eggs and ham.
Would you like them
Here or there?
I would not like them
Here or there.
I would not like them
Anywhere.
I do not like
Green eggs and ham.
I do not like them,
Sam-I-am
Would you like them
In a house?
Would you like them
With a mouse?
I do not like them
In a house.
I do not like them
With a mouse.
I do not like them
Here or there.
I do not like them
Anywhere.
I do not like green eggs and ham.
I do not like them, Sam-I-am.
Would you eat them
In a box?
Would you eat them
With a fox?
Not in a box.
Not with a fox.
Not in a house.
Not with a mouse.
I would not eat them here or there.
I would not eat them anywhere.
I would not eat green eggs and ham.
I do not like them, Sam-I-am.
Would you? Could you?
In a car?
Eat them! Eat them!
Here they are.
I woould not,
Could not,
In a car
You may like them.
You will see.
You may like them
In a tree?
I would not, could not in a tree.
Not in a car! You let me be.
I do not like them in a box.
I do not like them with a fox
I do not like them in a house
I do mot like them with a mouse
I do not like them here or there.
I do not like them anywhere.
I do not like green eggs and ham.
I do not like them, Sam-I-am.
A train! A train!
A train! A train!
Could you, would you
On a train?
Not on a train! Not in a tree!
Not in a car! Sam! Let me be!
I would not, could not, in a box.
I could not, would not, with a fox.
I will not eat them with a mouse
I will not eat them in a house.
I will not eat them here or there.
I will not eat them anywhere.
I do not like them, Sam-I-am.
Say!
In the dark?
Here in the dark!
Would you, could you, in the dark?
I would not, could not,
In the dark.
Would you, could you,
In the rain?
I would not, could not, in the rain.
Not in the dark. Not on a train,
Not in a car, Not in a tree.
I do not like them, Sam, you see.
Not in a house. Not in a box.
Not with a mouse. Not with a fox.
I will not eat them here or there.
I do not like them anywhere!
You do not like
Green eggs and ham?
I do not
Like them,
Sam-I-am.
Could you, would you,
With a goat?
I would not,
Could not.
With a goat!
Would you, could you,
On a boat?
```
</div>
</div>
</div>


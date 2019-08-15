---
redirect_from:
  - "/notebooks/lesson-05-unpacking"
interact_link: content/notebooks/lesson_05-unpacking.ipynb
kernel_name: python3
has_widgets: false
title: 'Lesson 05-unpacking'
prev_page:
  url: /notebooks/lesson_05-sorting_bitahon.html
  title: 'Lesson 05-sorting Bitahon'
next_page:
  url: /notebooks/lesson_05-unpacking_bitahon.html
  title: 'Lesson 05-unpacking Bitahon'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-python/blob/master/live%20class%20demonstrations/lesson%2005%20-%20unpacking.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
cheeses = ["adam", "bree", "cheDDar", "GOUDA", "camambert"]
# change the names to Title case

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
for i in range(len(cheeses)):
    cheeses[i] = cheeses[i].title()

print(cheeses)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
['Adam', 'Bree', 'Cheddar', 'Gouda', 'Camambert']
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
i=0
for cheese in cheeses:
    cheeses[i]= cheese.title()
    i+=1
    
print(cheeses)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
['Adam', 'Bree', 'Cheddar', 'Gouda', 'Camambert']
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
for i, cheese in enumerate(cheeses):
    cheeses[i] = cheese.title()
    
print(cheeses)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
['Adam', 'Bree', 'Cheddar', 'Gouda', 'Camambert']
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
list(enumerate(cheeses))

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
[(0, 'Adam'), (1, 'Bree'), (2, 'Cheddar'), (3, 'Gouda'), (4, 'Camambert')]
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
x= [1,2,3]
a=x[0]
b=x[1]
c=x[2]
print(a,b,c)

# unpacking
aa, bb, cc= x
print(aa, bb, cc)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
1 2 3
1 2 3
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# unpacking doesnt work with unbalanced left and right hand sides of '='
aa, bb, cc = [1,2,3,4]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_traceback_line}
```

    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-11-8b65758a2680> in <module>
          1 # unpacking doesnt work with unbalanced left and right hand sides of '='
    ----> 2 aa, bb, cc = [1,2,3,4]
    

    ValueError: too many values to unpack (expected 3)


```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
x = 10
y = 100

# classic swap
z = x
x = y
y = z

# swap using unpacking
x,y = [y,x] # list
x,y = (y,x) # tuple
x,y =  y,x  # tuple
print(x,y)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
10 100
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
(2+3)*4

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
20
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print( (10, 20, 30) )
print( (10, 20) )
print( (10, ) )
x= 10,  
print(x)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
(10, 20, 30)
(10, 20)
(10,)
(10,)
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
csv = """\
name, family, age, country
moshe, cohen, 20, israel
david, lev, 30, france
"""
lines= csv.splitlines()
print(lines)
header, *content = lines
#header, content= lines[0], lines[1:]
print(header)
print(content)
mosheline = content[0].split()
print(mosheline)
name, *eveything, country = mosheline
print(name, country, eveything)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
['name, family, age, country', 'moshe, cohen, 20, israel', 'david, lev, 30, france']
name, family, age, country
['moshe, cohen, 20, israel', 'david, lev, 30, france']
['moshe,', 'cohen,', '20,', 'israel']
moshe, israel ['cohen,', '20,']
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python



```
</div>

</div>


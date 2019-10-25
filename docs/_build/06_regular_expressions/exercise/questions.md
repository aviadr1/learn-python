---
redirect_from:
  - "/06-regular-expressions/exercise/questions"
interact_link: content/06_regular_expressions/exercise/questions.ipynb
kernel_name: python3
has_widgets: false
title: '06 regular expressions'
prev_page:
  url: /05_collections/notebooks/unpacking_bitahon.html
  title: 'Unpacking Bitahon'
next_page:
  url: /06_regular_expressions/exercise/questions.html
  title: 'exercise'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-python/blob/master/content/06_regular_expressions/exercise/questions.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/aviadr1/learn-python/)    



# regex to match positive integers
create and test a regex to:
match positive integer numbers





<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
### useful: test data
good_matches = [
   "1",
   "12",
   "65324",
   "0",
]

bad_matches = [
    "blah",
    "f123",
    "245fsd"
    "4-5",
    "4.0"
    "-10"
]

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
import re

regex = r"\b[0-9]+\b"
for test in good_matches:
    if not re.fullmatch(regex, test):
        print("failed:", test)

for test in bad_matches:
    if re.fullmatch(regex, test):
        print("failed:", test)

print(regex)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
\b[0-9]+\b
```
</div>
</div>
</div>



# regex for positive or negative integers
create and test a regex to:
 match positive or negative integers



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
### useful: test data
good_matches = [
   "1",
   "12",
   "65324",
   "+19",
   "-10",
   "0"
]

bad_matches = [
   "-0",
   "+0",
   "blah",
   "f123",
   "123you",
   "4-5",
   "4.0"
]


```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
regex = r"([+\-]?[1-9][0-9]*)|0"
for test in good_matches:
    if not re.fullmatch(regex, test):
        print("failed:", test)

for test in bad_matches:
    if re.fullmatch(regex, test):
        print("failed:", test)

print(regex)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
([+\-]?[1-9][0-9]*)|0
```
</div>
</div>
</div>



# decimal numbers `*`
create and test a regex to:
   match decimal numbers



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
### useful: test data
good_matches = [
       "1",
       "12",
       "123.4554",
       "0.43",
       "-10",
       "0",
       "+2.3",
       "-2.3"
   ]
   
bad_matches = [
   "-0",
   "+0",
   "blah",
   "f123",
   "123you",
   "4-5",
   "..34",
   ".34",
   "0.",
   "234."
]      

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
regex = r"([+-]?[0-9]+\.[0-9]+)|([+\-]?[1-9][0-9]*)|0"

for test in good_matches:
    if not re.fullmatch(regex, test):
        print("failed:", test)

for test in bad_matches:
    if re.fullmatch(regex, test):
        print("failed:", test)

print(regex)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
([+-]?[0-9]+\.[0-9]+)|([+\-]?[1-9][0-9]*)|0
```
</div>
</div>
</div>



# verbs
create and test a regex to:
   find words that look like verbs and end in '-ing'





<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
### useful: test data
good_matches = [
   "jumping",
   "eating",
   'sleeping',
   'ting',
   'bing',
   'zipziplinging'
]

bad_matches = [
   'jump',
   'ing',
   'jump ing',
   '_ing',
   '234ing'
]         

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
regex = r"[a-zA-Z]+ing"

for test in good_matches:
    if not re.fullmatch(regex, test):
        print("failed:", test)

for test in bad_matches:
    if re.fullmatch(regex, test):
        print("failed:", test)

print(regex)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
[a-zA-Z]+ing
```
</div>
</div>
</div>



# cats are awesome
create and test a regex to match:
lines that start with the word 'cats' and end with the words 'are awesome' 



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
### useful: test data
good_matches = [
   "cats are awesome",
   "cats that sleep are awesome",
   'cats that can count to 10 are awesome',
   'cats 1234567890-/.,gdf/.g, are awesome',
]

bad_matches = [
   'cat'
   'awesome',
   'cats are',
   'cats are awesome too',
   'my cats are awesome',
]

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
regex = r'cats.*are awesome'

for test in good_matches:
    if not re.fullmatch(regex, test):
        print("failed:", test)

for test in bad_matches:
    if re.fullmatch(regex, test):
        print("failed:", test)

print(regex)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
cats.*are awesome
```
</div>
</div>
</div>



# TODO
TODO: excersizes for iterall and match groups


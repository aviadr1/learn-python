---
redirect_from:
  - "/exercises/ex-06-questions"
interact_link: content/exercises/ex_06-questions.ipynb
kernel_name: python3
has_widgets: false
title: 'Ex 06-questions'
prev_page:
  url: /exercises/ex_05-solutions.html
  title: 'Ex 05-solutions'
next_page:
  url: /exercises/ex_06-solutions.html
  title: 'Ex 06-solutions'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-python/blob/master/exercises/ex%2006%20-%20questions.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




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



# TODO
TODO: excersizes for iterall and match groups


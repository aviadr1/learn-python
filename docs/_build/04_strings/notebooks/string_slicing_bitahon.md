---
redirect_from:
  - "/04-strings/notebooks/string-slicing-bitahon"
interact_link: content/04_strings/notebooks/string_slicing_bitahon.ipynb
kernel_name: python3
has_widgets: false
title: 'String Slicing Bitahon'
prev_page:
  url: /04_strings/notebooks/string_slicing.html
  title: 'String Slicing'
next_page:
  url: /04_strings/notebooks/string_tests.html
  title: 'String Tests'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-python/blob/master/content/04_strings/notebooks/string_slicing_bitahon.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
"the quick brown fox jumped over the lazy dog".split()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
['the', 'quick', 'brown', 'fox', 'jumped', 'over', 'the', 'lazy', 'dog']
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
"name, age, country".split(',')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
['name', 'age', 'country']
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
greeneggs = """\
Do you like
Green eggs and ham
I do not like them
Sam-I-am
I do not like
Green eggs and ham
Would you like them
Here or there?
I would not like them
Here or there
I would not like them
Anywhere
I do not like
Green eggs and ham
I do not like them
Sam-I-am
"""
greeneggs.splitlines()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
['Do you like',
 'Green eggs and ham',
 'I do not like them',
 'Sam-I-am',
 'I do not like',
 'Green eggs and ham',
 'Would you like them',
 'Here or there?',
 'I would not like them',
 'Here or there',
 'I would not like them',
 'Anywhere',
 'I do not like',
 'Green eggs and ham',
 'I do not like them',
 'Sam-I-am']
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
words = "the quick brown fox jumped over the lazy dog".split()
" ".join(words)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'the quick brown fox jumped over the lazy dog'
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
fields = "name, age, country".split(',')
", ".join(fields)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'name,  age,  country'
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
greeneggs[0]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'D'
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
greeneggs[20]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'g'
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
greeneggs[0:22]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'Do you like\nGreen eggs'
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
greeneggs[:22]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'Do you like\nGreen eggs'
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
x = greeneggs[22:len(greeneggs) -1]
print(x)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
 and ham
I do not like them
Sam-I-am
I do not like
Green eggs and ham
Would you like them
Here or there?
I would not like them
Here or there
I would not like them
Anywhere
I do not like
Green eggs and ham
I do not like them
Sam-I-am
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
x = greeneggs[22: -1]
print(x)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
 and ham
I do not like them
Sam-I-am
I do not like
Green eggs and ham
Would you like them
Here or there?
I would not like them
Here or there
I would not like them
Anywhere
I do not like
Green eggs and ham
I do not like them
Sam-I-am
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
x = greeneggs[22: ]
print(x)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
 and ham
I do not like them
Sam-I-am
I do not like
Green eggs and ham
Would you like them
Here or there?
I would not like them
Here or there
I would not like them
Anywhere
I do not like
Green eggs and ham
I do not like them
Sam-I-am

```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
x = greeneggs[: ]
print(x)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Do you like
Green eggs and ham
I do not like them
Sam-I-am
I do not like
Green eggs and ham
Would you like them
Here or there?
I would not like them
Here or there
I would not like them
Anywhere
I do not like
Green eggs and ham
I do not like them
Sam-I-am

```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
x = greeneggs[22:30 ]
print(x)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
 and ham
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
x = greeneggs[22:30:2 ]
print(x)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
 n a
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
x = greeneggs[22:30:1 ]
print(x)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
 and ham
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
x = greeneggs[::2 ]
print(x)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
D o ieGeneg n a
 ontlk hmSmIa
 ontlk
re gsadhmWudyulk hmHr rtee
 ol o iete
eeo hr
 ol o iete
nweeId o ieGeneg n a
 ontlk hmSmIa

```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
x = greeneggs[::-1]
print(x)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```

ma-I-maS
meht ekil ton od I
mah dna sgge neerG
ekil ton od I
erehwynA
meht ekil ton dluow I
ereht ro ereH
meht ekil ton dluow I
?ereht ro ereH
meht ekil uoy dluoW
mah dna sgge neerG
ekil ton od I
ma-I-maS
meht ekil ton od I
mah dna sgge neerG
ekil uoy oD
```
</div>
</div>
</div>


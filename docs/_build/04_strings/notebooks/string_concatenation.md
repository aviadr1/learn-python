---
redirect_from:
  - "/04-strings/notebooks/string-concatenation"
interact_link: content/04_strings/notebooks/string_concatenation.ipynb
kernel_name: python3
has_widgets: false
title: 'String Concatenation'
prev_page:
  url: /04_strings/notebooks/strings_multiline_strings_checkpoint.html
  title: 'Strings Multiline Strings Checkpoint'
next_page:
  url: /04_strings/notebooks/string_formatting.html
  title: 'String Formatting'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-python/blob/master/content/04_strings/notebooks/string_concatenation.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
greeneggs = "Do you like\n" + "Green eggs and ham\n" + "I do not like them\n" + "Sam-I-am\n"
print(greeneggs)

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

```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# literal strings do not need + to concatenate
greeneggs = "Do you like\n"  "Green eggs and ham\n"  "I do not like them\n"  "Sam-I-am\n"
print(greeneggs)

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

```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# use \ at end of lines to continue at the next line
greeneggs = \
    "Do you like\n"  \
    "Green eggs and ham\n"  \
    "I do not like them\n"  \
    "Sam-I-am\n"
print(greeneggs)

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

```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
greeneggs = """
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
print(greeneggs)

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
greeneggs = """Do you like
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
print(greeneggs)

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
print(r"""\n""")

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
\n
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
quoting_works_freely = """
I like "sarcasm"
and qouting smart people like this
'everything should be as simple as possible, but no simpler'
-- albert einstein
"""
print(quoting_works_freely)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```

I like "sarcasm"
and qouting smart people like this
'everything should be as simple as possible, but no simpler'
-- albert einstein

```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
repr("\n")

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
"'\\n'"
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
str("\n")

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'\n'
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
x= [3,2,1]
print(sorted(x))
print(x)
result = x.sort()
print(x)
print(result)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
[1, 2, 3]
[3, 2, 1]
[1, 2, 3]
None
```
</div>
</div>
</div>


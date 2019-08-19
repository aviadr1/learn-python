---
redirect_from:
  - "/04-strings/notebooks/split-join-csv"
interact_link: content/04_strings/notebooks/split_join_CSV.ipynb
kernel_name: python3
has_widgets: false
title: 'Split Join Csv'
prev_page:
  url: /04_strings/notebooks/split_join.html
  title: 'Split Join'
next_page:
  url: /04_strings/notebooks/strings_multiline_strings_checkpoint.html
  title: 'Strings Multiline Strings Checkpoint'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-python/blob/master/content/04_strings/notebooks/split_join_CSV.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
x = "the quick brown fox jumped over the lazy dog"
words = x.split()
print(words)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
['the', 'quick', 'brown', 'fox', 'jumped', 'over', 'the', 'lazy', 'dog']
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
words[3] = words[3].upper()
print(words)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
['the', 'quick', 'brown', 'FOX', 'jumped', 'over', 'the', 'lazy', 'dog']
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
" ".join(words)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'the quick brown FOX jumped over the lazy dog'
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
csv = """
name, family, age, country
moshe, cohen, 20, israel
david, lev, 30, france
"""

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
for line in csv.splitlines():
    fields = line.split(",")
    print(fields)
    

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
['']
['name', ' family', ' age', ' country']
['moshe', ' cohen', ' 20', ' israel']
['david', ' lev', ' 30', ' france']
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
fields
print(", ".join(fields)) # CSV line
print("\t".join(fields)) # TSV line

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
david,  lev,  30,  france
david	 lev	 30	 france
```
</div>
</div>
</div>


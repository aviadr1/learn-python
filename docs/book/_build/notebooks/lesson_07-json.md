---
redirect_from:
  - "/notebooks/lesson-07-json"
interact_link: content/notebooks/lesson_07-json.ipynb
kernel_name: python3
has_widgets: false
title: 'Lesson 07-json'
prev_page:
  url: /notebooks/lesson_07-file_open_write.html
  title: 'Lesson 07-file Open Write'
next_page:
  url: /notebooks/lesson_07-oops_i_did_it_again.html
  title: 'Lesson 07-oops I Did It Again'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-python/blob/master/live%20class%20demonstrations/lesson%2007%20-%20json.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
import json

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
very_complex_bank = { "customer1" : { "name" : "aviad, commas, just, for, the, hell, of, it", "account":1234, "money":200},
                     "accounts" : [1,2,3,4]
                     
                    }

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
json_repr = json.dumps(very_complex_bank)

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print(json_repr)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
{"customer1": {"name": "aviad", "account": 1234, "money": 200}, "accounts": [1, 2, 3, 4]}
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
blah = {"customer1": {"name": "aviad", "account": 1234, "money": 200}, "accounts": [1, 2, 3, 4]}

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
f = open("blah.json", "w")

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print(json_repr, file=f)

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
f.close()

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
f = open("blah.json")

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
bank = json.load(f)

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print(bank)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
{'customer1': {'name': 'aviad', 'account': 1234, 'money': 200}, 'accounts': [1, 2, 3, 4]}
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
f2 = open("blah.json", "w")

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
json.dump(bank, f2)

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
f2.close()

```
</div>

</div>


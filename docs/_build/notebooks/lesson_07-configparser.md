---
redirect_from:
  - "/notebooks/lesson-07-configparser"
interact_link: content/notebooks/lesson_07-configparser.ipynb
kernel_name: python3
has_widgets: false
title: 'Lesson 07-configparser'
prev_page:
  url: /notebooks/lesson_06-sub_python2-to-python3.html
  title: 'Lesson 06-sub Python2-to-python3'
next_page:
  url: /notebooks/lesson_07-files.html
  title: 'Lesson 07-files'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-python/blob/master/live%20class%20demonstrations/lesson%2007%20-%20configparser.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
import configparser


```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
x = configparser.ConfigParser()

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
x.read("config.ini")

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
['config.ini']
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
<configparser.ConfigParser at 0x163df2f7cc0>
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
for item in x.items():
    print(item)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
('DEFAULT', <Section: DEFAULT>)
('bitbucket.org', <Section: bitbucket.org>)
('topsecret.server.com', <Section: topsecret.server.com>)
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
x["DEFAULT"]["CompressionLevel"] = '11'

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
x["DEFAULT"]["CompressionLevel"]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'11'
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
f = open("config2.ini", "w")

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
x.write(f)

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


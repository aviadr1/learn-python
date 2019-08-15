---
redirect_from:
  - "/notebooks/lesson-13-os-system-subprocess-popen"
interact_link: content/notebooks/lesson_13-os_system_subprocess_popen.ipynb
kernel_name: python3
has_widgets: false
title: 'Lesson 13-os System Subprocess Popen'
prev_page:
  url: /notebooks/lesson_13-os_system_subprocess.html
  title: 'Lesson 13-os System Subprocess'
next_page:
  url: /notebooks/lesson_15-namedtuple.html
  title: 'Lesson 15-namedtuple'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-python/blob/master/live%20class%20demonstrations/lesson%2013%20-%20os.system%2C%20subprocess%2C%20popen.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
import os

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
os.system("del an_important_file.txt")

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
0
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
os.system("dir")

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
0
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
os.system("notepad an_important_file.txt")
print("finished")

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
finished
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
import subprocess

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
p = subprocess.Popen("notepad an_important_file.txt")
print("subprocess opened", p.pid)
print(p.wait())

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
subprocess opened 1776
0
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
p = subprocess.Popen("git add", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print("subprocess opened", p.pid)
print(p.wait())

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
subprocess opened 11412
128
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
p.stderr.readlines()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
[b'fatal: not a git repository (or any of the parent directories): .git\n']
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
for line in p.stderr:
    print(line)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
b'fatal: not a git repository (or any of the parent directories): .git\n'
```
</div>
</div>
</div>


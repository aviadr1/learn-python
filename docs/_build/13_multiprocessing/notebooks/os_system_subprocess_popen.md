---
redirect_from:
  - "/13-multiprocessing/notebooks/os-system-subprocess-popen"
interact_link: content/13_multiprocessing/notebooks/os_system_subprocess_popen.ipynb
kernel_name: python3
has_widgets: false
title: 'Os System Subprocess Popen'
prev_page:
  url: /13_multiprocessing/notebooks/os_system_subprocess.html
  title: 'Os System Subprocess'
next_page:
  url: /14_standard_library/notebooks/namedtuple.html
  title: '14 standard library'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-python/blob/master/content/13_multiprocessing/notebooks/os_system_subprocess_popen.ipynb" target="_blank">
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


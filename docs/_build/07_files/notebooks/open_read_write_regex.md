---
redirect_from:
  - "/07-files/notebooks/open-read-write-regex"
interact_link: content/07_files/notebooks/open_read_write_regex.ipynb
kernel_name: python3
has_widgets: false
title: 'Open Read Write Regex'
prev_page:
  url: /07_files/notebooks/oops_i_did_it_again.html
  title: 'Oops I Did It Again'
next_page:
  url: /07_files/notebooks/pandas_and_csv.html
  title: 'Pandas And Csv'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-python/blob/master/live%20class%20demonstrations/lesson%2007%20-%20open%2C%20read%2C%20write%2C%20regex.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
import re
regex = r"([ \t]*)print[ \t]+(.*)"
replacement = r"\1print(\2)"

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
f = open("test.py")
for line in f:
    
    result = re.sub(regex, replacement, line)
    print(result,end="")
f.close()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
print(1,2,3)
print("hello", "world")
if True:
	print(1,2,3)

	```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
f = open("test.py")
for line in f:
    
    result = re.sub(regex, replacement, line)
    if(result != line):
        print(result.rstrip(), "\t# <-- ", line, end="")
    else:
        print(result, end="")

f.close()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
print(1,2,3) 	# <--  print 1,2,3
print("hello", "world") 	# <--  print "hello", "world"
if True:
	print(1,2,3) 	# <--  	print 1,2,3

	```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
f = open("test.py")
f2 = open("test-py3.py", "w")
for line in f:
    
    result = re.sub(regex, replacement, line)
    print(result, end="", file=f2)

f.close()
f2.close()

newf2 = open("test-py3.py")
for line in newf2:
    print(line, end="")
newf2.close()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
print(1,2,3)
print("hello", "world")
if True:
	print(1,2,3)

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



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python



```
</div>

</div>


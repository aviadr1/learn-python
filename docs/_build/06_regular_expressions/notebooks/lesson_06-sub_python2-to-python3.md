---
redirect_from:
  - "/06-regular-expressions/notebooks/lesson-06-sub-python2-to-python3"
interact_link: content/06_regular_expressions/notebooks/lesson_06-sub_python2-to-python3.ipynb
kernel_name: python3
has_widgets: false
title: 'Lesson 06-sub Python2-to-python3'
prev_page:
  url: /06_regular_expressions/notebooks/lesson_06-sub_python2-to-python3.html
  title: 'notebooks'
next_page:
  url: /07_files/exercise/questions.html
  title: '07 files'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-python/blob/master/live%20class%20demonstrations/lesson%2006%20-%20sub%20python2-to-python3.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
import re

body = """
print       "hello", "world"
for i in range(10):
    print i
    
"""

regex = r"([ \t]*)print[ \t]+(.*)"
replacement = r"\1print(\2)"

result = re.sub(regex, replacement, body)
print(result)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```

print("hello", "world")
for i in range(10):
    print(i)
    

```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print(body)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```

print "hello", "world"
for i in range(10):
    print i
    

```
</div>
</div>
</div>


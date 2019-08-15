---
redirect_from:
  - "/notebooks/lesson-07-file-example"
interact_link: content/notebooks/lesson_07-file_example.ipynb
kernel_name: python3
has_widgets: false
title: 'Lesson 07-file Example'
prev_page:
  url: /notebooks/lesson_07-files.html
  title: 'Lesson 07-files'
next_page:
  url: /notebooks/lesson_07-file_open_write.html
  title: 'Lesson 07-file Open Write'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-python/blob/master/live%20class%20demonstrations/lesson%2007%20-%20file%20example.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
f=open("test.log")
lines = f.readlines()
f.close()

newline = input("give me more data: ")
lines.append(newline)


f=open("test.log", "w")
for line in lines:
    line=line.rstrip()
    print(line, file=f)
    print(line)

f.close()



```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
give me more data: line 4
asd
dsf
sdfdsf
sfdfdsfdsfds
line 4
```
</div>
</div>
</div>


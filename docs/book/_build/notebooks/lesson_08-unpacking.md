---
redirect_from:
  - "/notebooks/lesson-08-unpacking"
interact_link: content/notebooks/lesson_08-unpacking.ipynb
kernel_name: python3
has_widgets: false
title: 'Lesson 08-unpacking'
prev_page:
  url: /notebooks/lesson_08-sumnums.html
  title: 'Lesson 08-sumnums'
next_page:
  url: /notebooks/lesson_08-variadic_functions.html
  title: 'Lesson 08-variadic Functions'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-python/blob/master/live%20class%20demonstrations/lesson%2008%20-%20unpacking.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
params = {
    "sep" : " @ ",
    "end" : " @\n"
}
args = [1,2,3]

print(*args, **params) # 1 @ 2 @ 3 @

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
1 @ 2 @ 3 @
```
</div>
</div>
</div>


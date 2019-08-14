---
redirect_from:
  - "/notebooks/lesson-07-oops-i-did-it-again"
interact_link: content/notebooks/lesson_07-oops_i_did_it_again.ipynb
kernel_name: python3
has_widgets: false
title: 'Lesson 07-oops I Did It Again'
prev_page:
  url: /notebooks/lesson_07-json.html
  title: 'Lesson 07-json'
next_page:
  url: /notebooks/lesson_07-open_read_write_regex.html
  title: 'Lesson 07-open Read Write Regex'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-python/blob/master/live%20class%20demonstrations/lesson%2007%20-%20oops%20i%20did%20it%20again.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
oops = """\
oops I did it again
I played with your heart
got lost in the game
oh baby baby

oops you think I'm in love
that I'm sent from above
I'm not that innocent

oh baby baby
oh baby baby
oh
"""

fout = open('oops.txt', 'w')
print(oops, file=fout)
fout.close()

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
f = open('oops.txt')
fout = open('oops.double.txt', 'w')
for line in f:
    nextline = f.readline()
    print(line.strip(), '/', nextline.strip(), file=fout)

fout.close()

    

```
</div>

</div>


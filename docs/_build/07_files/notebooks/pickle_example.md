---
redirect_from:
  - "/07-files/notebooks/pickle-example"
interact_link: content/07_files/notebooks/pickle_example.ipynb
kernel_name: python3
has_widgets: false
title: 'Pickle Example'
prev_page:
  url: /07_files/notebooks/pickle_checkpoint.html
  title: 'Pickle Checkpoint'
next_page:
  url: /08_functions/exercise/questions.html
  title: '08 functions'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-python/blob/master/live%20class%20demonstrations/pickle%20example.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
import pickle

f= open("test.pickle", "wb")
pickle.dump([], f)

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
while True:
    r = input("(r)ead or (w)rite?")
    if r in ['w', 'r']:
        break

if r == 'r':
    f= open("test.pickle", "rb")
    db = pickle.load(f)
    print(db)
    
if r == 'w':
    f= open("test.pickle", "rb")
    db = pickle.load(f)
    new = input("what do you want to add?")
    db.append(new)
    f.close()
    f= open("test.pickle", "wb")
    pickle.dump(db, f)
    

```
</div>

</div>


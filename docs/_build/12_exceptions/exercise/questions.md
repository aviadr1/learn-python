---
redirect_from:
  - "/12-exceptions/exercise/questions"
interact_link: content/12_exceptions/exercise/questions.ipynb
kernel_name: python3
has_widgets: false
title: '12 exceptions'
prev_page:
  url: /11_classes_and_oop/notebooks/inheritance.html
  title: 'Inheritance'
next_page:
  url: /12_exceptions/exercise/questions.html
  title: 'exercise'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-python/blob/master/content/12_exceptions/exercise/questions.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




# convert to int
use a loop and the `int` function to find all the numbers embedded in the quote given below.
- hint: use `try/except` so that things which are not numbers wont stop your loop

expected outout:
```
[3, 3, 3, 4, 2, 3, 5]
```



# finally

we've provided an important function called `answer_to_universe_and_everything()`
1. open a file called `'answer.txt'` for writing
2. use a loop to call `answer_to_universe_and_everything()` a 100 times, and write the results to the file
3. use a `try/except` block to make sure that if answer_to_universe_and_everything() fails, we continue to call the function
4. if the function fails, write the fail message to the file
4. use a `try/finally` block to make sure we close the file
5. make sure the file indeed has exactly 100 lines



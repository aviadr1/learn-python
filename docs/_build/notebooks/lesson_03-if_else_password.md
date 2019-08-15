---
redirect_from:
  - "/notebooks/lesson-03-if-else-password"
interact_link: content/notebooks/lesson_03-if_else_password.ipynb
kernel_name: python3
has_widgets: false
title: 'Lesson 03-if Else Password'
prev_page:
  url: /notebooks/lesson_03-if_elif_else-with_password_checking.html
  title: 'Lesson 03-if Elif Else-with Password Checking'
next_page:
  url: /notebooks/lesson_03-july_break_continue.html
  title: 'Lesson 03-july Break Continue'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-python/blob/master/live%20class%20demonstrations/lesson%2003%20-%20if%2C%20else%2C%20password.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```password = input("gimme a new password: ")
if len(password) < 4 or len(password) > 6:
    print("your password must be betweeen 4-6 letters long")
else:
    print("awesome password")

```
</div>

</div>


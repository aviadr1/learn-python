---
redirect_from:
  - "/03-flow-control/notebooks/if-else-password"
interact_link: content/03_flow_control/notebooks/if_else_password.ipynb
kernel_name: python3
has_widgets: false
title: 'If Else Password'
prev_page:
  url: /03_flow_control/notebooks/if_elif_else-with_password_checking.html
  title: 'If Elif Else-with Password Checking'
next_page:
  url: /03_flow_control/notebooks/july_break_continue.html
  title: 'July Break Continue'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-python/blob/master/content/03_flow_control/notebooks/if_else_password.ipynb" target="_blank">
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


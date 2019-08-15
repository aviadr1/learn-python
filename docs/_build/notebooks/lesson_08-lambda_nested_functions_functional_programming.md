---
redirect_from:
  - "/notebooks/lesson-08-lambda-nested-functions-functional-programming"
interact_link: content/notebooks/lesson_08-lambda_nested_functions_functional_programming.ipynb
kernel_name: python3
has_widgets: false
title: 'Lesson 08-lambda Nested Functions Functional Programming'
prev_page:
  url: /notebooks/lesson_08-lambda.html
  title: 'Lesson 08-lambda'
next_page:
  url: /notebooks/lesson_08-mul_pow.html
  title: 'Lesson 08-mul Pow'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-python/blob/master/live%20class%20demonstrations/lesson%2008%20-%20lambda%2C%20nested%20functions%2C%20functional%20programming.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
bank = [
    {"name" : "avi", "money" : 100, "city" : "rehovot"},
    {"name" : "ben", "money" : -20, "city" : "raanana"},
    {"name" : "carrie", "money" : 500, "city" : "tel-aviv"},
    {"name" : "david", "money" : 250, "city" : "nes-ziona"},
    {"name" : "efrat", "money" : 1000, "city" : "beer-sheeva"},
    {"name" : "fred", "money" : 50, "city" : "yafo"},
]

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
import pprint


```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
pprint.pprint(bank)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
[{'city': 'rehovot', 'money': 100, 'name': 'avi'},
 {'city': 'raanana', 'money': -20, 'name': 'ben'},
 {'city': 'tel-aviv', 'money': 500, 'name': 'carrie'},
 {'city': 'nes-ziona', 'money': 250, 'name': 'david'},
 {'city': 'beer-sheeva', 'money': 1000, 'name': 'efrat'},
 {'city': 'yafo', 'money': 50, 'name': 'fred'}]
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def select_name(customer):
    return customer['name']

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def select_city(customer):
    return customer['city']

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def select_money(customer):
    return customer['money']

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
bank[0]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
{'name': 'avi', 'money': 100, 'city': 'rehovot'}
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print(bank[1])

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
{'name': 'ben', 'money': -20, 'city': 'raanana'}
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
select_name(bank[0])

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'avi'
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
select_money(bank[0])

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
100
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print(bank[1])
print(select_name(bank[1]))
print(select_money(bank[1]))


```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
{'name': 'ben', 'money': -20, 'city': 'raanana'}
ben
-20
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
bank[0] < bank[1]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_traceback_line}
```

    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-45-f526d7b9b849> in <module>
    ----> 1 bank[0] < bank[1]
    

    TypeError: '<' not supported between instances of 'dict' and 'dict'


```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
select_money(bank[0]) < select_money(bank[1])

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
False
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
sorted(bank)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_traceback_line}
```

    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-47-3335c59f163a> in <module>
    ----> 1 sorted(bank)
    

    TypeError: '<' not supported between instances of 'dict' and 'dict'


```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
sorted(bank, key=select_money)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
[{'name': 'ben', 'money': -20, 'city': 'raanana'},
 {'name': 'fred', 'money': 50, 'city': 'yafo'},
 {'name': 'avi', 'money': 100, 'city': 'rehovot'},
 {'name': 'david', 'money': 250, 'city': 'nes-ziona'},
 {'name': 'carrie', 'money': 500, 'city': 'tel-aviv'},
 {'name': 'efrat', 'money': 1000, 'city': 'beer-sheeva'}]
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
sorted(bank, key=select_name)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
[{'name': 'avi', 'money': 100, 'city': 'rehovot'},
 {'name': 'ben', 'money': -20, 'city': 'raanana'},
 {'name': 'carrie', 'money': 500, 'city': 'tel-aviv'},
 {'name': 'david', 'money': 250, 'city': 'nes-ziona'},
 {'name': 'efrat', 'money': 1000, 'city': 'beer-sheeva'},
 {'name': 'fred', 'money': 50, 'city': 'yafo'}]
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
sorted(bank, key=select_city)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
[{'name': 'efrat', 'money': 1000, 'city': 'beer-sheeva'},
 {'name': 'david', 'money': 250, 'city': 'nes-ziona'},
 {'name': 'ben', 'money': -20, 'city': 'raanana'},
 {'name': 'avi', 'money': 100, 'city': 'rehovot'},
 {'name': 'carrie', 'money': 500, 'city': 'tel-aviv'},
 {'name': 'fred', 'money': 50, 'city': 'yafo'}]
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
lambda_select_name = lambda customer : customer['name'] 

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
lambda_select_money = lambda customer : customer['money']

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print(bank[1])
print(lambda_select_name(bank[1]))
print(lambda_select_money(bank[1]))

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
{'name': 'ben', 'money': -20, 'city': 'raanana'}
ben
-20
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
sorted(bank, key=lambda_select_money)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
[{'name': 'ben', 'money': -20, 'city': 'raanana'},
 {'name': 'fred', 'money': 50, 'city': 'yafo'},
 {'name': 'avi', 'money': 100, 'city': 'rehovot'},
 {'name': 'david', 'money': 250, 'city': 'nes-ziona'},
 {'name': 'carrie', 'money': 500, 'city': 'tel-aviv'},
 {'name': 'efrat', 'money': 1000, 'city': 'beer-sheeva'}]
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
sorted(bank, key=lambda customer: customer['city'])

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
[{'name': 'efrat', 'money': 1000, 'city': 'beer-sheeva'},
 {'name': 'david', 'money': 250, 'city': 'nes-ziona'},
 {'name': 'ben', 'money': -20, 'city': 'raanana'},
 {'name': 'avi', 'money': 100, 'city': 'rehovot'},
 {'name': 'carrie', 'money': 500, 'city': 'tel-aviv'},
 {'name': 'fred', 'money': 50, 'city': 'yafo'}]
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def sort_the_bank(bank, mode="name"):
    def select_name2(customer):
        return customer['name']
    
    def select_money2(customer):
        return customer['money']
    
    def select_city2(customer):
        return customer['city']
    
    if(mode == "name"):
        return sorted(bank, key=select_name2)
    elif mode == "money":
        return sorted(bank, key=select_money2)
    elif mode == "city":
        return sorted(bank, key=select_city2)
    else:
        return "Error"
        

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
sort_the_bank(bank)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
[{'name': 'avi', 'money': 100, 'city': 'rehovot'},
 {'name': 'ben', 'money': -20, 'city': 'raanana'},
 {'name': 'carrie', 'money': 500, 'city': 'tel-aviv'},
 {'name': 'david', 'money': 250, 'city': 'nes-ziona'},
 {'name': 'efrat', 'money': 1000, 'city': 'beer-sheeva'},
 {'name': 'fred', 'money': 50, 'city': 'yafo'}]
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
sort_the_bank(bank, "money")

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
[{'name': 'ben', 'money': -20, 'city': 'raanana'},
 {'name': 'fred', 'money': 50, 'city': 'yafo'},
 {'name': 'avi', 'money': 100, 'city': 'rehovot'},
 {'name': 'david', 'money': 250, 'city': 'nes-ziona'},
 {'name': 'carrie', 'money': 500, 'city': 'tel-aviv'},
 {'name': 'efrat', 'money': 1000, 'city': 'beer-sheeva'}]
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
select_name2

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_traceback_line}
```

    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-65-a75fa71e9e21> in <module>
    ----> 1 select_name2
    

    NameError: name 'select_name2' is not defined


```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def sort_the_bank_lambda(bank, mode="name"):
    select_name2 = lambda customer: customer['name']
    select_money2 = lambda customer: customer['money']
    select_city2 = lambda customer: customer['city']
    
    if(mode == "name"):
        return sorted(bank, key=select_name2)
    elif mode == "money":
        return sorted(bank, key=select_money2)
    elif mode == "city":
        return sorted(bank, key=select_city2)
    else:
        return "Error"

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
sort_the_bank_lambda(bank)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
[{'name': 'avi', 'money': 100, 'city': 'rehovot'},
 {'name': 'ben', 'money': -20, 'city': 'raanana'},
 {'name': 'carrie', 'money': 500, 'city': 'tel-aviv'},
 {'name': 'david', 'money': 250, 'city': 'nes-ziona'},
 {'name': 'efrat', 'money': 1000, 'city': 'beer-sheeva'},
 {'name': 'fred', 'money': 50, 'city': 'yafo'}]
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def sort_the_bank_short(bank, mode="name"):
    def my_sorter(mode):
        return lambda customer: customer[mode]
 
    return sorted(bank, key=my_sorter(mode))

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
sort_the_bank_short(bank)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
[{'name': 'avi', 'money': 100, 'city': 'rehovot'},
 {'name': 'ben', 'money': -20, 'city': 'raanana'},
 {'name': 'carrie', 'money': 500, 'city': 'tel-aviv'},
 {'name': 'david', 'money': 250, 'city': 'nes-ziona'},
 {'name': 'efrat', 'money': 1000, 'city': 'beer-sheeva'},
 {'name': 'fred', 'money': 50, 'city': 'yafo'}]
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
sort_the_bank_short(bank, "money")

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
[{'name': 'ben', 'money': -20, 'city': 'raanana'},
 {'name': 'fred', 'money': 50, 'city': 'yafo'},
 {'name': 'avi', 'money': 100, 'city': 'rehovot'},
 {'name': 'david', 'money': 250, 'city': 'nes-ziona'},
 {'name': 'carrie', 'money': 500, 'city': 'tel-aviv'},
 {'name': 'efrat', 'money': 1000, 'city': 'beer-sheeva'}]
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def sort_the_bank_shorter(bank, mode="name"):
    return sorted(bank, key=lambda customer: customer[mode])

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
sort_the_bank_shorter(bank, "money")

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
[{'name': 'ben', 'money': -20, 'city': 'raanana'},
 {'name': 'fred', 'money': 50, 'city': 'yafo'},
 {'name': 'avi', 'money': 100, 'city': 'rehovot'},
 {'name': 'david', 'money': 250, 'city': 'nes-ziona'},
 {'name': 'carrie', 'money': 500, 'city': 'tel-aviv'},
 {'name': 'efrat', 'money': 1000, 'city': 'beer-sheeva'}]
```


</div>
</div>
</div>


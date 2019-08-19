---
redirect_from:
  - "/08-functions/notebooks/soft-intro-to-functions"
interact_link: content/08_functions/notebooks/soft_intro_to_functions.ipynb
kernel_name: python3
has_widgets: false
title: 'Soft Intro To Functions'
prev_page:
  url: /08_functions/notebooks/positional_and_named_arguments.html
  title: 'Positional And Named Arguments'
next_page:
  url: /08_functions/notebooks/sumnums.html
  title: 'Sumnums'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-python/blob/master/live%20class%20demonstrations/lesson%2008%20-%20soft%20intro%20to%20functions.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
3

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
3
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
3+4*5

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
23
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
'hello' + 'world'

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'helloworld'
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
'hello'.upper()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'HELLO'
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
'hello'.endswith('bye')

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
'hello'.endswith('llo')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
True
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
'hello'.endswith('hello')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
True
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
'hello'.endswith('!')

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
greeting = 'hello'

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
while greeting.islower():
    greeting = input('say hi: ')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
say hi: hi
say hi: hello
say hi: Hello
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
if greeting.isupper():
    print('too loud')

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
premium = []
cheeses = ['Edam', 'Brie', 'Camambert']
for cheese in cheeses:
    new_cheese = 'premium ' + cheese
    premium.append(new_cheese)

x = [10, 20, 0, 50, 50, 100]
soccer = ['maccabi ta', 'chelsea', 'real madrid', 'maccabi natanya', 'liverpool']

print(premium)
print(x)
print(soccer)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
['premium Edam', 'premium Brie', 'premium Camambert']
[10, 20, 0, 50, 50, 100]
['maccabi ta', 'chelsea', 'real madrid', 'maccabi natanya', 'liverpool']
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print()
for cheese in premium:
    print(cheese, end=',\n')
print()    

print()
for cheese in x:
    print(cheese, end=',\n')
print()

print()
for cheese in soccer:
    print(cheese, end=',\n')
print()


```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```

premium Edam,
premium Brie,
premium Camambert,


10,
20,
0,
50,
50,
100,


maccabi ta,
chelsea,
real madrid,
maccabi natanya,
liverpool,

```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def (thelist):
    print()
    for cheese in thelist:
        print(cheese, end=',\n')
    print()


```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
lineprint(premium)
lineprint(x)
lineprint(soccer)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```

premium Edam,
premium Brie,
premium Camambert,


10,
20,
0,
50,
50,
100,


maccabi ta,
chelsea,
real madrid,
maccabi natanya,
liverpool,

```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def printadd(x, y):
    print(x+y)
    
printadd(10, 5)
printadd('hello', ' world')
printadd([1,2], [3])

# write a function print_longer_list that receives two lists as parameters
# and prints only the longer list  
#    lets use len() function, and an if/else statement


```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
15
hello world
[1, 2, 3]
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def print_longer_list(list1, list2):
    if len(list1) <= len(list2):
        print(list2)
    else:
        print(list1)

x = print_longer_list(range(30), range(10, 20))
y = print_longer_list('encyclopedia', 'hello')        

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
range(0, 30)
encyclopedia
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print(y)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
None
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
x = len([1,2,3])

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
x

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
3
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def get_longer_list(list1, list2):
    if len(list1) <= len(list2):
        return list2
    else:
        return list1
    
x = get_longer_list(range(30), range(10, 20))
y = get_longer_list('encyclopedia', 'hello') 
z = get_longer_list([1,2,3,4,5,6], 'hello') 

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def make_david_happy():
     
    print('i made david', david)

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
make_david_happy()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
i made david happy
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
david = "ecstatic"
make_david_happy()
print('so now david is', david)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
i made david happy
so now david is ecstatic
```
</div>
</div>
</div>


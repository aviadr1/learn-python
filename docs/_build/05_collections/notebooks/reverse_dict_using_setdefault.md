---
redirect_from:
  - "/05-collections/notebooks/reverse-dict-using-setdefault"
interact_link: content/05_collections/notebooks/reverse_dict_using_setdefault.ipynb
kernel_name: python3
has_widgets: false
title: 'Reverse Dict Using Setdefault'
prev_page:
  url: /05_collections/notebooks/reverse_dictionary.html
  title: 'Reverse Dictionary'
next_page:
  url: /05_collections/notebooks/sets_checkpoint.html
  title: 'Sets Checkpoint'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-python/blob/master/content/05_collections/notebooks/reverse_dict_using_setdefault.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
menu = {
    'pita' : 1,
    'steak' : 150,
    'hamburger' : 59,
    'pizza' : 40,
    'cola' : 12
}

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
for item in menu.keys():
    price = menu[item]
    menu[item] = menu[item] * 1.1

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print(menu)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
{'pita': 1.1, 'steak': 165.0, 'hamburger': 64.9, 'pizza': 44.0, 'cola': 13.200000000000001}
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
for keyvalue in menu.items():
    item, price = keyvalue
    menu[item] = price * 1.1


```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
('pita', 1.1)
('steak', 165.0)
('hamburger', 64.9)
('pizza', 44.0)
('cola', 13.200000000000001)
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print(menu)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
{'pita': 1.2100000000000002, 'steak': 181.50000000000003, 'hamburger': 71.39000000000001, 'pizza': 48.400000000000006, 'cola': 14.520000000000003}
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
for item, price in menu.items():
    menu[item] = price * 1.1

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print(menu)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
{'pita': 1.3310000000000004, 'steak': 199.65000000000003, 'hamburger': 78.52900000000002, 'pizza': 53.24000000000001, 'cola': 15.972000000000005}
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
menu

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
{'pita': 1.3310000000000004,
 'steak': 199.65000000000003,
 'hamburger': 78.52900000000002,
 'pizza': 53.24000000000001,
 'cola': 15.972000000000005}
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
menu[0]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_traceback_line}
```

    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    <ipython-input-10-ca462d9b1d0b> in <module>
    ----> 1 menu[0]
    

    KeyError: 0


```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
menu['shkashuka'] = 100

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
menu

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
{'pita': 1.3310000000000004,
 'steak': 199.65000000000003,
 'hamburger': 78.52900000000002,
 'pizza': 53.24000000000001,
 'cola': 15.972000000000005,
 'shkashuka': 100}
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
menu.pop('cola')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
15.972000000000005
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
menu

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
{'pita': 1.3310000000000004,
 'steak': 199.65000000000003,
 'hamburger': 78.52900000000002,
 'pizza': 53.24000000000001,
 'shkashuka': 100}
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print(menu.get('cats', "Sorry not on menu"))

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Sorry not on menu
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
menu.get('pita', "Sorry not on menu")

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
1.3310000000000004
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
menu.setdefault('pita', "Sorry not on menu")

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
1.3310000000000004
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
menu

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
{'pita': 1.3310000000000004,
 'steak': 199.65000000000003,
 'hamburger': 78.52900000000002,
 'pizza': 53.24000000000001,
 'shkashuka': 100}
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
menu.setdefault('cats', "Sorry not on menu")

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'Sorry not on menu'
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
menu

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
{'pita': 1.3310000000000004,
 'steak': 199.65000000000003,
 'hamburger': 78.52900000000002,
 'pizza': 53.24000000000001,
 'shkashuka': 100,
 'cats': 'Sorry not on menu'}
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
p144 = {
    'avi' : 1,
    'ben' : 2,
    "gaddy" : 3,
    "david" : 4,
    "efrat" :4
    
}



```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
p441 = {}
for name, phone in p144.items():
    p441[phone] = name

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print(p441)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
{1: 'avi', 2: 'ben', 3: 'gaddy', 4: 'david'}
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
p441 = {}
for name, phone in p144.items():
    if phone in p441:
        list_of_names = p441[phone]
        list_of_names.append(name)
    else:
        p441[phone] = [ name ]

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
p441 = {}
for name, phone in p144.items():
    if phone in p441:
        p441[phone].append(name)
    else:
        p441[phone] = [ name ]

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
p441 = {}
for name, phone in p144.items():
    p441.setdefault(phone, []).append(name)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
p441={}, name=avi, phone=1
p441={1: ['avi']}, name=ben, phone=2
p441={1: ['avi'], 2: ['ben']}, name=gaddy, phone=3
p441={1: ['avi'], 2: ['ben'], 3: ['gaddy']}, name=david, phone=4
p441={1: ['avi'], 2: ['ben'], 3: ['gaddy'], 4: ['david']}, name=efrat, phone=4
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
p441

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
{1: ['avi'], 2: ['ben'], 3: ['gaddy'], 4: ['david', 'efrat']}
```


</div>
</div>
</div>


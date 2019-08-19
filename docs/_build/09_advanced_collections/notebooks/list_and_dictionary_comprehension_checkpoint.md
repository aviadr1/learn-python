---
redirect_from:
  - "/09-advanced-collections/notebooks/list-and-dictionary-comprehension-checkpoint"
interact_link: content/09_advanced_collections/notebooks/list_and_dictionary_comprehension_checkpoint.ipynb
kernel_name: python3
has_widgets: false
title: 'List And Dictionary Comprehension Checkpoint'
prev_page:
  url: /09_advanced_collections/notebooks/lazy_lists_generators.html
  title: 'Lazy Lists Generators'
next_page:
  url: /09_advanced_collections/notebooks/list_comprehension_order.html
  title: 'List Comprehension Order'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-python/blob/master/content/09_advanced_collections/notebooks/list_and_dictionary_comprehension_checkpoint.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
cheeses = ["adam", "bree", "camambert", "gouda", "grouyer"]

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
entitled_cheeses = []
i=0
while i<len(cheeses):
    entitled_cheeses.append(cheeses[i].title())
    i+=1
print(entitled_cheeses)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
['Adam', 'Bree', 'Camambert', 'Gouda', 'Grouyer']
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
entitled_cheeses = []
for cheese  in cheeses:
    entitled_cheeses.append(cheese.title())
print(entitled_cheeses)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
['Adam', 'Bree', 'Camambert', 'Gouda', 'Grouyer']
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
[cheese.title() for cheese in cheeses]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
['Adam', 'Bree', 'Camambert', 'Gouda', 'Grouyer']
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
[2**pow  for pow in range(16)]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
[1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768]
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
[len(cheese) for cheese in cheeses]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
[4, 4, 9, 5, 7]
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
cheese_prices = {
    'Adam' : 2,
    'Bree' : 3,
    'Camambert' : 4,
    'Gouda' : 5
}

missing = { 'Adam' }

buy = ['Adam', 'Bree']
# buy_prices = [ cheese_prices[item]   for item in buy]


```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
total = sum([ cheese_prices[item]   for item in buy])
print(total)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
5
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
total = sum([ cheese_prices[item] for item in buy if item not in missing])
print(total)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
3
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
item in missing

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_traceback_line}
```

      File "<ipython-input-18-8eff41c05ca1>", line 1
        in missing
         ^
    SyntaxError: invalid syntax



```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
new_prices = { 
    cheese: price*1.1    for cheese, price in cheese_prices.items() }
print(new_prices)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
{'Adam': 2.2, 'Bree': 3.3000000000000003, 'Camambert': 4.4, 'Gouda': 5.5}
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
d144 = { "avi" : "053",
            "ben" : "054",
            "gaddy" : "055"}
d441 = { phone:name      for name, phone in d144.items() } 

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print(d441)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
{'053': 'avi', '054': 'ben', '055': 'gaddy'}
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
d = {}
reverse_d = {value:key for key, value in d.items()}

```
</div>

</div>


---
redirect_from:
  - "/05-collections/notebooks/dictionaries-checkpoint"
interact_link: content/05_collections/notebooks/dictionaries_checkpoint.ipynb
kernel_name: python3
has_widgets: false
title: 'Dictionaries Checkpoint'
prev_page:
  url: /05_collections/notebooks/dictionaries_checkpoint.html
  title: 'notebooks'
next_page:
  url: /05_collections/notebooks/extending_lists.html
  title: 'Extending Lists'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-python/blob/master/content/05_collections/notebooks/dictionaries_checkpoint.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
prices = {
    "oranges" : 7.99,
    "tomatoes" : 2.9,
    "chicken" : 1
}

print(list(prices.items()))

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
[('oranges', 7.99), ('tomatoes', 2.9), ('chicken', 1)]
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# nice way
for product, price in prices.items():
    print("{} costs {:.2f} NIS".format(product, price))
print()

# crappy way
for product in prices.keys():
    print("{} costs {:.2f} NIS".format(product, prices[product]))

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
oranges costs 7.99 NIS
tomatoes costs 2.90 NIS
chicken costs 1.00 NIS

oranges costs 7.99 NIS
tomatoes costs 2.90 NIS
chicken costs 1.00 NIS
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
mydict = {'UK':['London','Wigan','Macclesfield','Bolton'], 
          'US':['Miami','Springfield','New York','Boston']}


```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
for country, city_list in mydict.items():
    print("{} has these major cities: {}".format(country, city_list))

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
UK has these major cities: ['London', 'Wigan', 'Macclesfield', 'Bolton']
US has these major cities: ['Miami', 'Springfield', 'New York', 'Boston']
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
prices["steak"] = 300
print(prices)

#discount
prices["steak"] = 200
print(prices)


```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
{'oranges': 7.99, 'tomatoes': 2.9, 'chicken': 1, 'steak': 300}
{'oranges': 7.99, 'tomatoes': 2.9, 'chicken': 1, 'steak': 200}
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
prices.pop("steak")
print(prices) # steak is gone

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
{'oranges': 7.99, 'tomatoes': 2.9, 'chicken': 1}
```
</div>
</div>
</div>


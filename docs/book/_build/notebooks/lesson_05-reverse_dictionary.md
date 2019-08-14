---
redirect_from:
  - "/notebooks/lesson-05-reverse-dictionary"
interact_link: content/notebooks/lesson_05-reverse_dictionary.ipynb
kernel_name: python3
has_widgets: false
title: 'Lesson 05-reverse Dictionary'
prev_page:
  url: /notebooks/lesson_05-removing_from_lists.html
  title: 'Lesson 05-removing From Lists'
next_page:
  url: /notebooks/lesson_05-reverse_dict_using_setdefault.html
  title: 'Lesson 05-reverse Dict Using Setdefault'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-python/blob/master/live%20class%20demonstrations/lesson%2005%20-%20reverse%20dictionary.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
countries = {
    "Israel" : "Jerusalem",
    "France" : "Paris",
    "UK" : "London"
}

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
countries["Finland"] = "Helsinki"

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print(countries)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
{'Israel': 'Jerusalem', 'France': 'Paris', 'UK': 'London', 'Finland': 'Helsinki'}
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
cities = {}

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
for land,city in countries.items():
    cities[city] = land

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print(cities)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
{'Jerusalem': 'Israel', 'Paris': 'France', 'London': 'UK', 'Helsinki': 'Finland'}
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
crazy_countries = {
    "Israel" : "Jerusalem",
    "France" : "Paris",
    "UK" : "London",
    "Texas" : "Paris",
    "Ohio" : "Jerusalem"
}

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
{ "Paris" : ["France", "Texas"]}

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
{'Paris': ['France', 'Texas']}
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
crazy_cities = {}
for land,city in crazy_countries.items():
    if city not in crazy_cities:
        crazy_cities[city] = [ land ]
    else:
        crazy_cities[city].append(land)
        

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print(crazy_cities)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
{'Jerusalem': ['Israel', 'Ohio'], 'Paris': ['France', 'Texas'], 'London': ['UK']}
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
_ = 2

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
"\\."

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'\\.'
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print('\\.')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
\.
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print('\\\\.')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
\\.
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print(r'\\.')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
\\.
```
</div>
</div>
</div>


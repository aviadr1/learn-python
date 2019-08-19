---
redirect_from:
  - "/05-collections/notebooks/july-fruits-sorting-dict-zip"
interact_link: content/05_collections/notebooks/july_fruits_sorting_dict_zip.ipynb
kernel_name: python3
has_widgets: false
title: 'July Fruits Sorting Dict Zip'
prev_page:
  url: /05_collections/notebooks/how_many_unique_words_in_dr_seuss_book.html
  title: 'How Many Unique Words In Dr Seuss Book'
next_page:
  url: /05_collections/notebooks/july_sets.html
  title: 'July Sets'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-python/blob/master/live%20class%20demonstrations/lesson%2005%20-%20july%20fruits%2C%20sorting%2C%20dict%2C%20zip.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
fruits = [
    'apple',
    'mango',
    'pear',
    'grapes'
]

prices = [
    14,
    7,
    8,
    25
]

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
max(fruits)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'pear'
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
min(fruits)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'apple'
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
max(prices)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
25
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
max('hello world')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'w'
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
max(range(10))

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
9
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
x = list(range(10))
x

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
max(x)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
9
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
sum(prices)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
54
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
x,y,z = "abc"

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
x,y,z = (1,2)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_traceback_line}
```

    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-15-6f419fd02ba5> in <module>
    ----> 1 x,y,z = (1,2)
    

    ValueError: not enough values to unpack (expected 3, got 2)


```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
"moshe cohen, 28, 1/1/1980, ussr, no"

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'moshe cohen, 28, 1/1/1980, ussr, no'
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
name, age, *others = "moshe cohen, 28, 1/1/1980, ussr, no".split(',')

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
name

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'moshe cohen'
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
age

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
' 28'
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
others

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
[' 1/1/1980', ' ussr', ' no']
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
name, *everythingelse, address = "moshe cohen, 28, 1/1/1980, ussr, kremlin".split(',')

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
name

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'moshe cohen'
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
address

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
' kremlin'
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
everythingelse

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
[' 28', ' 1/1/1980', ' ussr']
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
name, *everythingelse, address = "moshe cohen, 28, 1/1/1980, ussr, kremlin".split(',')

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
*blah, country, address = "moshe cohen, 28, 1/1/1980, ussr, kremlin".split(',')

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
blah

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
['moshe cohen', ' 28', ' 1/1/1980']
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
country

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
' ussr'
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
fruits

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
['apple', 'mango', 'pear', 'grapes']
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
fruits += ['watermelon']

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
fruits

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
['apple', 'mango', 'pear', 'grapes', 'watermelon']
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
fruits = ['tomato'] + fruits

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
fruits

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
['tomato', 'apple', 'mango', 'pear', 'grapes', 'watermelon']
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
fruits.insert(3, 'banana')

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
fruits

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
['tomato', 'apple', 'mango', 'banana', 'pear', 'grapes', 'watermelon']
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
fruits.pop(3)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'banana'
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
fruits

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
['tomato', 'apple', 'mango', 'pear', 'grapes', 'watermelon']
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
fruits.remove('pear')

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
fruits

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
['tomato', 'apple', 'mango', 'grapes', 'watermelon']
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
fruits.index('apple')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
1
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
fruits.pop(fruits.index('apple'))

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'apple'
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
x = [1,1,1,1,2,2,2,1,1,1]

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
x.remove(1)

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
[1, 1, 1, 2, 2, 2, 1, 1, 1]
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
while 1 in x:
    x.remove(1)

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
[2, 2, 2]
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
fruits = ['tomato', 'apple', 'mango', 'banana', 'pear', 'grapes', 'watermelon']

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
sorted(fruits)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
['apple', 'banana', 'grapes', 'mango', 'pear', 'tomato', 'watermelon']
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
sorted(fruits, key=len)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
['pear', 'apple', 'mango', 'tomato', 'banana', 'grapes', 'watermelon']
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
prices = [
    10,
    8,
    5,
    13,
    20,
    2,
    17
]

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
d = dict(zip(fruits, prices))
d

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
{'tomato': 10,
 'apple': 8,
 'mango': 5,
 'banana': 13,
 'pear': 20,
 'grapes': 2,
 'watermelon': 17}
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
d.get('apple')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
8
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
d.get('grapes')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
2
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
sorted(fruits, key=d.get)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
['grapes', 'mango', 'apple', 'tomato', 'banana', 'watermelon', 'pear']
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
sorted(fruits, key=d.get, reverse=True)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
['pear', 'watermelon', 'banana', 'tomato', 'apple', 'mango', 'grapes']
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
fruits.sort()

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
fruits

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
['apple', 'banana', 'grapes', 'mango', 'pear', 'tomato', 'watermelon']
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
oops = """
Yeah yeah yeah yeah yeah
Yeah yeah yeah yeah yeah yeah
I think I did it again
I made you believe we're more than just friends
Oh baby
It might seem like a crush
But it doesn't mean that I'm serious
'Cause to lose all my senses
That is just so typically me
Oh baby, baby
Oops, I did it again
I played with your heart, got lost in the game
Oh baby, baby
Oops, you think I'm in love
That I'm sent from above
I'm not that innocent
You see my problem is this
I'm dreaming away
Wishing that heroes, they truly exist
I cry, watching the days
Can't you see I'm a fool in so many ways
But to lose all my senses
That is just so typically me
Oh baby, oh
Oops, I did it again
I played with your heart, got lost in the game
Oh baby, baby
Oops, you think I'm in love
That I'm sent from above
I'm not that innocent
Yeah yeah yeah yeah yeah yeah
Yeah yeah yeah yeah yeah yeah
"All aboard"
"Britney, before you go, there's something I want you to have"
"Oh, it's beautiful, but wait a minute, isn't this?"
"Yeah, yes it is"
"But I thought the old lady dropped it into the ocean in the end"
"Well baby, I went down and got it for you"
"Aww, you shouldn't have"
Oops, I did it again to your heart
Got lost in this game, oh baby
Oops, you think that I'm sent from above
I'm not that innocent
Oops, I did it again
I played with your heart, got lost in the game
Oh baby, baby
Oops, you think I'm in love
That I'm sent from above
I'm not that innocent
Oops, I did it again
I played with your heart, got lost in the game
Oh baby, baby
Oops, you think I'm in love
That I'm sent from above
I'm not that innocent
"""

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
oops2 = oops.translate(str.maketrans('', '', """!,"'`."""))
#print(oops2)

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
len(set(oops2.split()))

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
107
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
myfruits = d

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
myfruits

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
{'tomato': 10,
 'apple': 8,
 'mango': 5,
 'banana': 13,
 'pear': 20,
 'grapes': 2,
 'watermelon': 17}
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
myfruits.keys()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
dict_keys(['tomato', 'apple', 'mango', 'banana', 'pear', 'grapes', 'watermelon'])
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
for key in myfruits.keys():
    print(key)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
tomato
apple
mango
banana
pear
grapes
watermelon
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
myfruits['apple']

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
8
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
for key in myfruits.keys():
    print(key)
    price = myfruits[key]
    print(price)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
tomato
10
apple
8
mango
5
banana
13
pear
20
grapes
2
watermelon
17
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
myfruits.values()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
dict_values([10, 8, 5, 13, 20, 2, 17])
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
myfruits.items()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
dict_items([('tomato', 10), ('apple', 8), ('mango', 5), ('banana', 13), ('pear', 20), ('grapes', 2), ('watermelon', 17)])
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
for keyvalue in myfruits.items():
    name = keyvalue[0]
    price = keyvalue[1]
    print(name, price)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
tomato 10
apple 8
mango 5
banana 13
pear 20
grapes 2
watermelon 17
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
for keyvalue in myfruits.items():
    name, price = keyvalue
    print(name, price)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
tomato 10
apple 8
mango 5
banana 13
pear 20
grapes 2
watermelon 17
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
for name, price in myfruits.items():
    print(name, price)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
tomato 10
apple 8
mango 5
banana 13
pear 20
grapes 2
watermelon 17
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
oops2

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'\nYeah yeah yeah yeah yeah\nYeah yeah yeah yeah yeah yeah\nI think I did it again\nI made you believe were more than just friends\nOh baby\nIt might seem like a crush\nBut it doesnt mean that Im serious\nCause to lose all my senses\nThat is just so typically me\nOh baby baby\nOops I did it again\nI played with your heart got lost in the game\nOh baby baby\nOops you think Im in love\nThat Im sent from above\nIm not that innocent\nYou see my problem is this\nIm dreaming away\nWishing that heroes they truly exist\nI cry watching the days\nCant you see Im a fool in so many ways\nBut to lose all my senses\nThat is just so typically me\nOh baby oh\nOops I did it again\nI played with your heart got lost in the game\nOh baby baby\nOops you think Im in love\nThat Im sent from above\nIm not that innocent\nYeah yeah yeah yeah yeah yeah\nYeah yeah yeah yeah yeah yeah\nAll aboard\nBritney before you go theres something I want you to have\nOh its beautiful but wait a minute isnt this?\nYeah yes it is\nBut I thought the old lady dropped it into the ocean in the end\nWell baby I went down and got it for you\nAww you shouldnt have\nOops I did it again to your heart\nGot lost in this game oh baby\nOops you think that Im sent from above\nIm not that innocent\nOops I did it again\nI played with your heart got lost in the game\nOh baby baby\nOops you think Im in love\nThat Im sent from above\nIm not that innocent\nOops I did it again\nI played with your heart got lost in the game\nOh baby baby\nOops you think Im in love\nThat Im sent from above\nIm not that innocent\n'
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
import collections

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
words = collections.Counter(oops2.split())

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
sorted(words.items(), key=lambda x: x[1], reverse=True)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
[('yeah', 19),
 ('Im', 17),
 ('I', 16),
 ('baby', 14),
 ('you', 11),
 ('in', 11),
 ('it', 10),
 ('Oops', 10),
 ('Oh', 8),
 ('that', 8),
 ('the', 8),
 ('think', 6),
 ('did', 6),
 ('again', 6),
 ('That', 6),
 ('Yeah', 5),
 ('your', 5),
 ('heart', 5),
 ('got', 5),
 ('lost', 5),
 ('game', 5),
 ('sent', 5),
 ('from', 5),
 ('above', 5),
 ('not', 5),
 ('innocent', 5),
 ('to', 4),
 ('is', 4),
 ('played', 4),
 ('with', 4),
 ('love', 4),
 ('just', 3),
 ('a', 3),
 ('But', 3),
 ('my', 3),
 ('so', 3),
 ('lose', 2),
 ('all', 2),
 ('senses', 2),
 ('typically', 2),
 ('me', 2),
 ('see', 2),
 ('this', 2),
 ('oh', 2),
 ('have', 2),
 ('made', 1),
 ('believe', 1),
 ('were', 1),
 ('more', 1),
 ('than', 1),
 ('friends', 1),
 ('It', 1),
 ('might', 1),
 ('seem', 1),
 ('like', 1),
 ('crush', 1),
 ('doesnt', 1),
 ('mean', 1),
 ('serious', 1),
 ('Cause', 1),
 ('You', 1),
 ('problem', 1),
 ('dreaming', 1),
 ('away', 1),
 ('Wishing', 1),
 ('heroes', 1),
 ('they', 1),
 ('truly', 1),
 ('exist', 1),
 ('cry', 1),
 ('watching', 1),
 ('days', 1),
 ('Cant', 1),
 ('fool', 1),
 ('many', 1),
 ('ways', 1),
 ('All', 1),
 ('aboard', 1),
 ('Britney', 1),
 ('before', 1),
 ('go', 1),
 ('theres', 1),
 ('something', 1),
 ('want', 1),
 ('its', 1),
 ('beautiful', 1),
 ('but', 1),
 ('wait', 1),
 ('minute', 1),
 ('isnt', 1),
 ('this?', 1),
 ('yes', 1),
 ('thought', 1),
 ('old', 1),
 ('lady', 1),
 ('dropped', 1),
 ('into', 1),
 ('ocean', 1),
 ('end', 1),
 ('Well', 1),
 ('went', 1),
 ('down', 1),
 ('and', 1),
 ('for', 1),
 ('Aww', 1),
 ('shouldnt', 1),
 ('Got', 1)]
```


</div>
</div>
</div>


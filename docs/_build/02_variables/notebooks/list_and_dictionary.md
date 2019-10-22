---
redirect_from:
  - "/02-variables/notebooks/list-and-dictionary"
interact_link: content/02_variables/notebooks/list_and_dictionary.ipynb
kernel_name: python3
has_widgets: false
title: 'List And Dictionary'
prev_page:
  url: /02_variables/notebooks/lists_and_indexing.html
  title: 'Lists And Indexing'
next_page:
  url: /02_variables/notebooks/mutability_vs_immutability.html
  title: 'Mutability Vs Immutability'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-python/blob/master/content/02_variables/notebooks/list_and_dictionary.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




1. compute 10+90
2. put the result 



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
fox = "the quick brown fox jumped over the lazy dog"

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
fox.upper().endswith("lazy dog")

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
"DOG" == "dog"

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
mylist = ["one", "two", "three"]
result = " ".join(mylist)
print(result)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
one two three
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
result

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'one two three'
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
type(mylist)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
list
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
type(result)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
str
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
len(mylist)

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
len(result)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
13
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
"sdklfjhasdlkfh"

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'sdklfjhasdlkfh'
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
["f.xd,ghdflskjgh", 10, 100, 0.5, "hewllo"]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
['f.xd,ghdflskjgh', 10, 100, 0.5, 'hewllo']
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
song = """Yeah yeah yeah yeah yeah
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
"""

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print(song)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
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

```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
words = song.split(' ')

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
len(words)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
74
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
words[0]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'Yeah'
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
words[7] = "boom"
words[14] = "boom"
words[21] = "boom"
words[28] = "boom"
words[35] = "boom"

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print(words)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
['Yeah', 'yeah', 'yeah', 'yeah', 'yeah\nYeah', 'yeah', 'yeah', 'boom', 'yeah', 'yeah\nI', 'think', 'I', 'did', 'it', 'boom', 'made', 'you', 'believe', "we're", 'more', 'than', 'boom', 'friends\nOh', 'baby\nIt', 'might', 'seem', 'like', 'a', 'boom', 'it', "doesn't", 'mean', 'that', "I'm", "serious\n'Cause", 'boom', 'lose', 'all', 'my', 'senses\nThat', 'is', 'just', 'so', 'typically', 'me\nOh', 'baby,', 'baby\nOops,', 'I', 'did', 'it', 'again\nI', 'played', 'with', 'your', 'heart,', 'got', 'lost', 'in', 'the', 'game\nOh', 'baby,', 'baby\nOops,', 'you', 'think', "I'm", 'in', 'love\nThat', "I'm", 'sent', 'from', "above\nI'm", 'not', 'that', 'innocent\n']
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
songboom = " ".join(words)
print(songboom)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Yeah yeah yeah yeah yeah
Yeah yeah yeah boom yeah yeah
I think I did it boom made you believe we're more than boom friends
Oh baby
It might seem like a boom it doesn't mean that I'm serious
'Cause boom lose all my senses
That is just so typically me
Oh baby, baby
Oops, I did it again
I played with your heart, got lost in the game
Oh baby, baby
Oops, you think I'm in love
That I'm sent from above
I'm not that innocent

```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print(song.replace('i', '1').replace('e', '3').replace('s', '5'))

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Y3ah y3ah y3ah y3ah y3ah
Y3ah y3ah y3ah y3ah y3ah y3ah
I th1nk I d1d 1t aga1n
I mad3 you b3l13v3 w3'r3 mor3 than ju5t fr13nd5
Oh baby
It m1ght 533m l1k3 a cru5h
But 1t do35n't m3an that I'm 53r1ou5
'Cau53 to lo53 all my 53n535
That 15 ju5t 5o typ1cally m3
Oh baby, baby
Oop5, I d1d 1t aga1n
I play3d w1th your h3art, got lo5t 1n th3 gam3
Oh baby, baby
Oop5, you th1nk I'm 1n lov3
That I'm 53nt from abov3
I'm not that 1nnoc3nt

```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
"the quick brown fox jumped over the lazy dog".replace("the", "da")

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'da quick brown fox jumped over da lazy dog'
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
{}

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
{}
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
[]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
[]
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
cities = {
    "israel" :         "jerusalem"      ,
    "uk" : "london",
    "russia" : "moscow"
}

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
cities

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
{'israel': 'jerusalem', 'uk': 'london', 'russia': 'moscow'}
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
cities['israel']

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'jerusalem'
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
cities["france"] = "paris"

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
{'israel': 'jerusalem', 'uk': 'london', 'russia': 'moscow', 'france': 'paris'}
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
cities['france']

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'paris'
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
leet = {
    'i' : '1',
    'e' : '3',
    's' : '5'
}

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
synonyms = {
    "good" : ['great', 'amzing', 'wonderful', "not bad"],
    "sad" : ['blue', 'depressed', 'down', 'gloom']
}

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
synonyms['sad']

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
['blue', 'depressed', 'down', 'gloom']
```


</div>
</div>
</div>



create a dictionary that maps the name of cheeses to prices of 100mg of that cheese.
```
 gouda costs 4.99 
 Edam costs 2.45
 Camambert costs 7.75
 Bree costs 7.27
```

without using "head math", compute the costs of gouda, edam and camambert together



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
cheese = {
    "gouda" : 4.99,
    "edam" : 2.45,
    "camambert" : 7.75,
    "bree" : 7.27
}

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
cheese["gouda"] + cheese['edam'] + cheese['camambert']

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
15.190000000000001
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
[cheese["gouda"] , cheese['edam'] , cheese['camambert']]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
[4.99, 2.45, 7.75]
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
cheese.keys()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
dict_keys(['gouda', 'edam', 'camambert', 'bree'])
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
cheese.values()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
dict_values([4.99, 2.45, 7.75, 7.27])
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
cheese.items()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
dict_items([('gouda', 4.99), ('edam', 2.45), ('camambert', 7.75), ('bree', 7.27)])
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
sorted(cheese.items(), key=lambda pair: pair[1])[0]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
('edam', 2.45)
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
cheese.pop('gouda')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
4.99
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
cheese

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
{'edam': 2.45, 'camambert': 7.75, 'bree': 7.27}
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
{
    
}

```
</div>

</div>


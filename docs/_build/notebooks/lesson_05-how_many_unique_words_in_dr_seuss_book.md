---
redirect_from:
  - "/notebooks/lesson-05-how-many-unique-words-in-dr-seuss-book"
interact_link: content/notebooks/lesson_05-how_many_unique_words_in_dr_seuss_book.ipynb
kernel_name: python3
has_widgets: false
title: 'Lesson 05-how Many Unique Words In Dr Seuss Book'
prev_page:
  url: /notebooks/lesson_05-extending_lists.html
  title: 'Lesson 05-extending Lists'
next_page:
  url: /notebooks/lesson_05-july_fruits_sorting_dict_zip.html
  title: 'Lesson 05-july Fruits Sorting Dict Zip'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-python/blob/master/live%20class%20demonstrations/lesson%2005%20-%20how%20many%20unique%20words%20in%20dr%20seuss%20book.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
set( [1,1,1,2,1,1,1] )

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
{1, 2}
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
{1, 2} == {2,1}

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
{2,1}

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
{1, 2}
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
{2,1} == {2,2,2,2,2,2,2,1}

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
greeneggs = """
I am Sam
I am Sam
Sam I am
That Sam-I-am
That Sam-I-am!
I do not like
That Sam-I-am
Do you like
Green eggs and ham
I do not like them
Sam-I-am
I do not like
Green eggs and ham
Would you like them
Here or there?
I would not like them
Here or there
I would not like them
Anywhere
I do not like
Green eggs and ham
I do not like them
Sam-I-am
Would you like them
In a house?
Would you like them
With a mouse?
I do not like them
In a house
I do not like them
With a mouse
I do not like them
Here or there
I do not like them
Anywhere
I do not like green eggs and ham
I do not like them, Sam-I-am
Would you eat them
In a box?
Would you eat them
With a fox?
Not in a box
Not with a fox
Not in a house
Not with a mouse
I would not eat them here or there
I would not eat them anywhere
I would not eat green eggs and ham
I do not like them, Sam-I-am
Would you? Could you?
In a car?
Eat them! Eat them!
Here they are
I woould not 
Could not
In a car
You may like them
You will see
You may like them
In a tree?
D not in a tree
I would not, could not in a tree
Not in a car! You let me be
I do not like them in a box
I do not like them with a fox
I do not like them in a house
I do mot like them with a mouse
I do not like them here or there
I do not like them anywhere
I do not like green eggs and ham
I do not like them, Sam-I-am
A train! A train!
A train! A train!
Could you, would you
On a train?
Not on a train! Not in a tree!
Not in a car! Sam! Let me be!
I would not, could not, in a box
I could not, would not, with a fox
I will not eat them with a mouse
I will not eat them in a house
I will not eat them here or there
I will not eat them anywhere
I do not like them, Sam-I-am
Say!
In the dark?
Here in the dark!
Would you, could you, in the dark?
I would not, could not
In the dark
Would you, could you
In the rain?
I would not, could not, in the rain
Not in the dark. Not on a train
Not in a car, Not in a tree
I do not like them, Sam, you see
Not in a house. Not in a box
Not with a mouse. Not with a fox
I will not eat them here or there
I do not like them anywhere!
You do not like
Green eggs and ham?
I do not
Like them
Sam-I-am
Could you, would you
With a goat?
I would not
Could not
With a goat!
Would you, could you
On a boat?
I could not, would not, on a boat
I will not, will not, with a goat
I will not eat them in the rain
I will not eat them on a train
Not in the dark! Not in a tree!
Not in a car! You let me be!
I do not like them in a box
I do not like them with a fox
I will not eat them in a house
I do not like them with a mouse
I do not like them here or there
I do not like them ANYWHERE!
I do not like
Green egss
And ham!
I do not like them
Sam-I-am
You do not like them
SO you say
Try them! Try them!
ANd you may
Try them and you may I say
Sam!
If you will let me be
I will try them
You will see
Say!
I like green eggs and ham!
I do!! I like them, Sam-I-am!
And I would eat them in a boat!
And I would eat them with a goat...
And I will eat them in the rain
And in the dark. And on a train
And in a car. And in a tree
They are so goodm so goodm you see!
So I will eat them in a box
And I will eat them with a fox
And I will eat them in a house
And I will eat them with a mouse
And I will eat them here and there
Say! I will eat them ANHYWHERE!
I do so like
Green eggs and ham!
Thank you!
Thank you
Sam-I-am!
"""

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
words = greeneggs.replace('?', ' ').replace(',', ' ').replace('.', ' ').replace('-', ' ').replace('!', ' ').lower().split()

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
809
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
wordset = set(words)

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
len(wordset)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
55
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
oopswords = oops.replace('?', ' ').replace(',', ' ').replace('.', ' ').replace('-', ' ').replace('!', ' ').replace('"', " ").lower().split()

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
len(oopswords)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
326
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
oopsset = set(oopswords)

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
len(oopsset)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
98
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
oopsset

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
{"'cause",
 'a',
 'aboard',
 'above',
 'again',
 'all',
 'and',
 'away',
 'aww',
 'baby',
 'beautiful',
 'before',
 'believe',
 'britney',
 'but',
 "can't",
 'crush',
 'cry',
 'days',
 'did',
 "doesn't",
 'down',
 'dreaming',
 'dropped',
 'end',
 'exist',
 'fool',
 'for',
 'friends',
 'from',
 'game',
 'go',
 'got',
 'have',
 'heart',
 'heroes',
 'i',
 "i'm",
 'in',
 'innocent',
 'into',
 'is',
 "isn't",
 'it',
 "it's",
 'just',
 'lady',
 'like',
 'lose',
 'lost',
 'love',
 'made',
 'many',
 'me',
 'mean',
 'might',
 'minute',
 'more',
 'my',
 'not',
 'ocean',
 'oh',
 'old',
 'oops',
 'played',
 'problem',
 'see',
 'seem',
 'senses',
 'sent',
 'serious',
 "shouldn't",
 'so',
 'something',
 'than',
 'that',
 'the',
 "there's",
 'they',
 'think',
 'this',
 'thought',
 'to',
 'truly',
 'typically',
 'wait',
 'want',
 'watching',
 'ways',
 "we're",
 'well',
 'went',
 'wishing',
 'with',
 'yeah',
 'yes',
 'you',
 'your'}
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
oopsset & wordset

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
{'a',
 'and',
 'i',
 'in',
 'like',
 'me',
 'not',
 'see',
 'so',
 'that',
 'the',
 'they',
 'with',
 'you'}
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
wordset - oopsset

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
{'am',
 'anhywhere',
 'anywhere',
 'are',
 'be',
 'boat',
 'box',
 'car',
 'could',
 'd',
 'dark',
 'do',
 'eat',
 'eggs',
 'egss',
 'fox',
 'goat',
 'goodm',
 'green',
 'ham',
 'here',
 'house',
 'if',
 'let',
 'may',
 'mot',
 'mouse',
 'on',
 'or',
 'rain',
 'sam',
 'say',
 'thank',
 'them',
 'there',
 'train',
 'tree',
 'try',
 'will',
 'woould',
 'would'}
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
oopsset - wordset

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
{"'cause",
 'aboard',
 'above',
 'again',
 'all',
 'away',
 'aww',
 'baby',
 'beautiful',
 'before',
 'believe',
 'britney',
 'but',
 "can't",
 'crush',
 'cry',
 'days',
 'did',
 "doesn't",
 'down',
 'dreaming',
 'dropped',
 'end',
 'exist',
 'fool',
 'for',
 'friends',
 'from',
 'game',
 'go',
 'got',
 'have',
 'heart',
 'heroes',
 "i'm",
 'innocent',
 'into',
 'is',
 "isn't",
 'it',
 "it's",
 'just',
 'lady',
 'lose',
 'lost',
 'love',
 'made',
 'many',
 'mean',
 'might',
 'minute',
 'more',
 'my',
 'ocean',
 'oh',
 'old',
 'oops',
 'played',
 'problem',
 'seem',
 'senses',
 'sent',
 'serious',
 "shouldn't",
 'something',
 'than',
 "there's",
 'think',
 'this',
 'thought',
 'to',
 'truly',
 'typically',
 'wait',
 'want',
 'watching',
 'ways',
 "we're",
 'well',
 'went',
 'wishing',
 'yeah',
 'yes',
 'your'}
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
2**64

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
18446744073709551616
```


</div>
</div>
</div>


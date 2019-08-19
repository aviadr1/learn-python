---
redirect_from:
  - "/14-standard-library/notebooks/namedtuple"
interact_link: content/14_standard_library/notebooks/namedtuple.ipynb
kernel_name: python3
has_widgets: false
title: 'Namedtuple'
prev_page:
  url: /14_standard_library/notebooks/namedtuple.html
  title: 'notebooks'
next_page:
  url: 
  title: ''
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-python/blob/master/live%20class%20demonstrations/lesson%2015%20-%20namedtuple.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




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
""".replace(',', ' ').replace('.', ' ').replace('`', ' ').split()

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
from collections import Counter

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
x = Counter(oops)

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
x.most_common(25)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
[('yeah', 19),
 ("I'm", 17),
 ('I', 16),
 ('baby', 14),
 ('in', 11),
 ('it', 10),
 ('you', 10),
 ('Oops', 10),
 ('that', 8),
 ('the', 8),
 ('Oh', 7),
 ('think', 6),
 ('did', 6),
 ('again', 6),
 ('That', 6),
 ('your', 5),
 ('heart', 5),
 ('got', 5),
 ('lost', 5),
 ('game', 5),
 ('sent', 5),
 ('from', 5),
 ('above', 5),
 ('not', 5),
 ('innocent', 5)]
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
len(x)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
112
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
hotel = """
On a dark desert highway, cool wind in my hair
Warm smell of colitas, rising up through the air
Up ahead in the distance, I saw a shimmering light
My head grew heavy and my sight grew dim
I had to stop for the night.
There she stood in the doorway;
I heard the mission bell
And I was thinking to myself
'This could be heaven or this could be Hell'
Then she lit up a candle and she showed me the way
There were voices down the corridor,
I thought I heard them say
Welcome to the Hotel California
Such a lovely place (such a lovely place)
Such a lovely face.
Plenty of room at the Hotel California
Any time of year (any time of year) you can find it here
Her mind is Tiffany-twisted, she got the Mercedes bends
She got a lot of pretty, pretty boys, that she calls friends
How they dance in the courtyard, sweet summer sweat
Some dance to remember, some dance to forget
So I called up the Captain,
'Please bring me my wine'
He said, 'we haven't had that spirit here since nineteen sixty-nine'
And still those voices are calling from far away,
Wake you up in the middle of the night
Just to hear them say"
Welcome to the Hotel California
Such a lovely place (such a lovely place)
Such a lovely face.
They livin' it up at the Hotel California
What a nice surprise (what a nice surprise), bring your alibis
Mirrors on the ceiling,
The pink champagne on ice
And she said, 'we are all just prisoners here, of our own device'
And in the master's chambers,
They gathered for the feast
They stab it with their steely knives,
But they just can't kill the beast
Last thing I remember, I was
Running for the door
I had to find the passage back to the place I was before
'Relax' said the night man,
'We are programmed to receive.
You can check out any time you like,
But you can never leave!'
""".replace(',', ' ').replace('.', ' ').replace('`', ' ').replace('!', ' ').split()

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
y = Counter(hotel)

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
set([word for word,n in x.most_common(25)]) - set([word for word,n in y.most_common(25)] )

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
{"I'm",
 'Oh',
 'Oops',
 'That',
 'above',
 'again',
 'baby',
 'did',
 'from',
 'game',
 'got',
 'heart',
 'innocent',
 'lost',
 'not',
 'sent',
 'that',
 'think',
 'yeah',
 'your'}
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
len(hotel)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
344
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
len(oops)

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
 y.most_common(25)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
[('the', 24),
 ('a', 12),
 ('I', 11),
 ('to', 10),
 ('of', 7),
 ('in', 6),
 ('she', 6),
 ('lovely', 6),
 ('up', 5),
 ('And', 4),
 ('Hotel', 4),
 ('California', 4),
 ('Such', 4),
 ('you', 4),
 ('my', 3),
 ('had', 3),
 ('for', 3),
 ('night', 3),
 ('was', 3),
 ('place', 3),
 ('time', 3),
 ('can', 3),
 ('it', 3),
 ('here', 3),
 ('dance', 3)]
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
x.most_common(25)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
[('yeah', 19),
 ("I'm", 17),
 ('I', 16),
 ('baby', 14),
 ('in', 11),
 ('it', 10),
 ('you', 10),
 ('Oops', 10),
 ('that', 8),
 ('the', 8),
 ('Oh', 7),
 ('think', 6),
 ('did', 6),
 ('again', 6),
 ('That', 6),
 ('your', 5),
 ('heart', 5),
 ('got', 5),
 ('lost', 5),
 ('game', 5),
 ('sent', 5),
 ('from', 5),
 ('above', 5),
 ('not', 5),
 ('innocent', 5)]
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
from collections import OrderedDict

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
from collections import namedtuple

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
help(namedtuple)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Help on function namedtuple in module collections:

namedtuple(typename, field_names, *, verbose=False, rename=False, module=None)
    Returns a new subclass of tuple with named fields.
    
    >>> Point = namedtuple('Point', ['x', 'y'])
    >>> Point.__doc__                   # docstring for the new class
    'Point(x, y)'
    >>> p = Point(11, y=22)             # instantiate with positional args or keywords
    >>> p[0] + p[1]                     # indexable like a plain tuple
    33
    >>> x, y = p                        # unpack like a regular tuple
    >>> x, y
    (11, 22)
    >>> p.x + p.y                       # fields also accessible by name
    33
    >>> d = p._asdict()                 # convert to a dictionary
    >>> d['x']
    11
    >>> Point(**d)                      # convert from a dictionary
    Point(x=11, y=22)
    >>> p._replace(x=100)               # _replace() is like str.replace() but targets named fields
    Point(x=100, y=22)

```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
Person = namedtuple('Person', ['name', 'age', 'country', 'id'])

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
beni = Person( 'beni', 25, 'israel', '123')

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
beni.name

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'beni'
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
beni.id

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'123'
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
beni[1]

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
beni.

```
</div>

</div>


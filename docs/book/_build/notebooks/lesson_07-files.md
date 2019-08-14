---
redirect_from:
  - "/notebooks/lesson-07-files"
interact_link: content/notebooks/lesson_07-files.ipynb
kernel_name: python3
has_widgets: false
title: 'Lesson 07-files'
prev_page:
  url: /notebooks/lesson_07-configparser.html
  title: 'Lesson 07-configparser'
next_page:
  url: /notebooks/lesson_07-file_example.html
  title: 'Lesson 07-file Example'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-python/blob/master/live%20class%20demonstrations/lesson%2007%20-%20files.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
greeneggs = """\
Green Eggs And Ham
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
"""
fout = open("green.txt", "w")
print(greeneggs, file=fout)
fout.close()

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
f = open("green.txt")
for line in f:
    print(line)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Green Eggs And Ham

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



```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
csv = """\
name, age, money
david, 30, 1000
moshe, 25, 500
lea, 35, 50000
tamar, 29, 600"""
fout = open("csv.txt", "w")
print(csv, file=fout)
fout.close()

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
f = open("csv.txt")
column1, column2, *others = f.readline().split()
for line in f:
    name, age, money = line.split()
    print(f"name={name}, age={age}, money={money}")

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
name=david,, age=30,, money=1000
name=moshe,, age=25,, money=500
name=lea,, age=35,, money=50000
name=tamar,, age=29,, money=600
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
['money']
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
with open("green.txt", "w") as fout:
    print(greeneggs, file=fout)
    
print("here fout has been closed already")

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
here fout has been closed already
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
dir(fout)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
['_CHUNK_SIZE',
 '__class__',
 '__del__',
 '__delattr__',
 '__dict__',
 '__dir__',
 '__doc__',
 '__enter__',
 '__eq__',
 '__exit__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__getstate__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__iter__',
 '__le__',
 '__lt__',
 '__ne__',
 '__new__',
 '__next__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 '_checkClosed',
 '_checkReadable',
 '_checkSeekable',
 '_checkWritable',
 '_finalizing',
 'buffer',
 'close',
 'closed',
 'detach',
 'encoding',
 'errors',
 'fileno',
 'flush',
 'isatty',
 'line_buffering',
 'mode',
 'name',
 'newlines',
 'read',
 'readable',
 'readline',
 'readlines',
 'seek',
 'seekable',
 'tell',
 'truncate',
 'writable',
 'write',
 'writelines']
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
import sys
x = 0
if x == 0:
    print("error", file=sys.stderr)

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
f = open("csv.txt")


```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
#column1, column2, *others = f.readline().split()
for line in f:
    name, age, money = line.split()
    print(f"name={name}, age={age}, money={money}")

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
name=e,, age=age,, money=money
name=david,, age=30,, money=1000
name=moshe,, age=25,, money=500
name=lea,, age=35,, money=50000
name=tamar,, age=29,, money=600
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
f.seek(3)

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
data = {
    1: [],
    2: [ {1: ["one"]}],
    3: "blah",
    4: [[[],[],[123]]]
     
}

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
fout = open("data.json.txt", "w")
import json
json.dump(data, fout, indent=1)
fout.close()

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
fin = open("data.json.txt")
dataout = json.load(fin)


```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
dataout

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
{'1': [], '2': [{'1': ['one']}], '3': 'blah', '4': [[[], [], [123456]]]}
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
{"1": [], "2": [{"1": ["one"]}], "3": "blah", "4": [[[], [], [123456]]]}

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
{'1': [], '2': [{'1': ['one']}], '3': 'blah', '4': [[[], [], [123456]]]}
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
dataout == {"1": [], "2": [{"1": ["one"]}], "3": "blah", "4": [[[], [], [123456]]]}

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
help(json.dump)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Help on function dump in module json:

dump(obj, fp, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)
    Serialize ``obj`` as a JSON formatted stream to ``fp`` (a
    ``.write()``-supporting file-like object).
    
    If ``skipkeys`` is true then ``dict`` keys that are not basic types
    (``str``, ``int``, ``float``, ``bool``, ``None``) will be skipped
    instead of raising a ``TypeError``.
    
    If ``ensure_ascii`` is false, then the strings written to ``fp`` can
    contain non-ASCII characters if they appear in strings contained in
    ``obj``. Otherwise, all such characters are escaped in JSON strings.
    
    If ``check_circular`` is false, then the circular reference check
    for container types will be skipped and a circular reference will
    result in an ``OverflowError`` (or worse).
    
    If ``allow_nan`` is false, then it will be a ``ValueError`` to
    serialize out of range ``float`` values (``nan``, ``inf``, ``-inf``)
    in strict compliance of the JSON specification, instead of using the
    JavaScript equivalents (``NaN``, ``Infinity``, ``-Infinity``).
    
    If ``indent`` is a non-negative integer, then JSON array elements and
    object members will be pretty-printed with that indent level. An indent
    level of 0 will only insert newlines. ``None`` is the most compact
    representation.
    
    If specified, ``separators`` should be an ``(item_separator, key_separator)``
    tuple.  The default is ``(', ', ': ')`` if *indent* is ``None`` and
    ``(',', ': ')`` otherwise.  To get the most compact JSON representation,
    you should specify ``(',', ':')`` to eliminate whitespace.
    
    ``default(obj)`` is a function that should return a serializable version
    of obj or raise TypeError. The default simply raises TypeError.
    
    If *sort_keys* is true (default: ``False``), then the output of
    dictionaries will be sorted by key.
    
    To use a custom ``JSONEncoder`` subclass (e.g. one that overrides the
    ``.default()`` method to serialize additional types), specify it with
    the ``cls`` kwarg; otherwise ``JSONEncoder`` is used.

```
</div>
</div>
</div>


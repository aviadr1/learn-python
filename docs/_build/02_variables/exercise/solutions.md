---
redirect_from:
  - "/02-variables/exercise/solutions"
interact_link: content/02_variables/exercise/solutions.ipynb
kernel_name: python3
has_widgets: false
title: 'Solutions'
prev_page:
  url: /02_variables/exercise/questions.html
  title: 'Questions'
next_page:
  url: /02_variables/notebooks/dictionary.html
  title: 'notebooks'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-python/blob/master/content/02_variables/exercise/solutions.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




# help for str.split() function
print the help for the function str.split



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
help(str.split)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Help on method_descriptor:

split(...)
    S.split(sep=None, maxsplit=-1) -> list of strings
    
    Return a list of the words in S, using sep as the
    delimiter string.  If maxsplit is given, at most maxsplit
    splits are done. If sep is not specified or is None, any
    whitespace string is a separator and empty strings are
    removed from the result.

```
</div>
</div>
</div>



# split a string

1. create the following string, and put it in a variable called `sent`
```
"the quick brown fox jumped over the lazy dog"
```

2.  then **split** it into a list 
    so that each word is an an element in the list. <br> 
    and put the result into another variable called `words`
    
   
3. print the variable `words`

expected ouput:
```
['the', 'quick', 'brown', 'fox', 'jumped', 'over', 'the', 'lazy', 'dog']
```



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
sent = "the quick brown fox jumped over the lazy dog"
words = sent.split()
print(words)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
['the', 'quick', 'brown', 'fox', 'jumped', 'over', 'the', 'lazy', 'dog']
```
</div>
</div>
</div>



# str.join()

1. use the function `help` to read the documentation for the str.join function
1. read this code
```
mylist = ["one", "two", "three"]
result = " ".join(mylist)
print(result)
```
   1. can you guess what this code does ? 
   1. what is the function join?
   1. use help or documentation online if you can't guess
   1. copy this code to the cell below and run it to see if you were right




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
help(str.join)

# one two three
# join will add a space ' ' between each two words in mylist
mylist = ["one", "two", "three"]
result = " ".join(mylist)
print(result)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Help on method_descriptor:

join(...)
    S.join(iterable) -> str
    
    Return a string which is the concatenation of the strings in the
    iterable.  The separator between elements is S.

one two three
```
</div>
</div>
</div>



# using str.upper() and str.join()

1. split the sentence `"the quick brown fox jumped over the lazy dog"` into words using the function .split() 
   and put the result in a variable called `words` .
   

2. replace the the words "dog" and "fox" in the `words` list with *uppercase* "DOG" and "FOX" <br>

   HINTS:
   * use the .upper() function
   * use indexing like `words[3]` to acccess a particular word in the `words` list
   
   
3. use the function join to convert the list back into a string


4. print the result
   
expected output:
```
"the quick brown FOX jumped over the lazy DOG"
```



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
words = "the quick brown fox jumped over the lazy dog".split()
# print(words)
words[3] = words[3].upper()
words[-1] = words[-1].upper()
# print(words)
result = " ".join(words)
print(result)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
the quick brown FOX jumped over the lazy DOG
```
</div>
</div>
</div>



# Dictionary

1. create a dictionary that maps the name of cheeses to prices of 100mg of that cheese.

        gouda costs 4.99 
        Edam costs 2.45
        Camambert costs 7.75
        Bree costs 7.27
    
1. without using "head math", compute the costs of gouda, edam and camambert together 





<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
costs = {
    "Gouda" : 4.99 ,
    "Edam" : 2.45,
    "Camambert" : 7.75,
    "Bree" : 7.27,
    "Cheddar":  2.89,
}

print(costs["Gouda"] + costs["Edam"] + costs["Camambert"])

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
15.190000000000001
```
</div>
</div>
</div>


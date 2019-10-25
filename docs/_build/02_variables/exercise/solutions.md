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




# basic values and types
1. calculate `2+8` and put the result in tha variable `x`. 
   - print the value of `x`
     > hint: use the function `print()`
   - what is the type of `x`?
     > hint: use the function `type()`
2. calculate `5 / 2` and put the result in the variable `y`. print `y` and the type of `y`
3. put `"hello world"` into a variable named _`greeting`_. 
   - print the variable and the type of the variable
   - what is the `len` of _`greeting`_?
     > hint: use the function `len()`
4. put the values `1`, `2` and `3` into _`list1`_ and the values `"a"`, `"b"` and `"c"` into _`list2`_.
   - calcluate _`list1`_ + _`list2`_ and put the result into _`list3`_
    - print _`list3`_ 
    - print the `type` of _`list3`_
    - print the `len` of _`list3`_
    



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# 1
x = 2 + 8
print(type(x), x)

# 2
y = 5/2
print(type(y), y)

# 3
greeting = "hello world"
print(type(greeting), greeting)
print(len(greeting))

# 4
list1 = [1,2,3]
list2 = ["a", "b", "c"]
list3 = list1 + list2
print(type(list3), list3)
print(len(list3))

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
<class 'int'> 10
<class 'float'> 2.5
<class 'str'> hello world
11
<class 'list'> [1, 2, 3, 'a', 'b', 'c']
6
```
</div>
</div>
</div>



# getting help
suppose we want to understand how to use a function. we can use the `help()` function for that!

1. let's try to use the function _`str.upper()`_, by copying this code below and running it:
```python
print( "hello".upper() )
```
2. lets see how to get help for a function. type the following code into a cell below. this will explain what the function _`str.upper`_ does
```python
help("hello".upper)
```





<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# 1
print( "hello".upper() )

# 2
help("hello".upper)


```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
HELLO
Help on built-in function upper:

upper() method of builtins.str instance
    Return a copy of the string converted to uppercase.

```
</div>
</div>
</div>



# some simple string functions
1. lets get help for __all__ the cool functions the type _`str`_ has. lets call `help(str)`. run the following code:
```python
help(str)
```

2. read the documentation you've just printed, for the following functions: 
`lower, upper, title, islower, isupper` and try to figure out what they do. you can try to use them, read the documentation again, google for them. anything that helps you understand.

3. convert this string to uppercase
`"the quick brown fox jumped over the lazy dog"`
> hint: use one of the functions you've learned in question #2

4. is the string `"I JusT mEt YoU, anD tHIs is CraaZy, sO CAll mE mayBe"` in lower case? can you convert it to lower case?
> hints :
> 1. there is a function that checks if a string is lower case
> 2. there is a function that converts a string to lower case



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# 1
help(str)

# 3
sentence = "the quick brown fox jumped over the lazy dog"
print(sentence.upper())

# 4
crazy = "I JusT mEt YoU, anD tHIs is CraaZy, sO CAll mE mayBe"
print()
print("is lower? " , crazy)
print(crazy.islower())
print()
print("is lower? ", crazy.lower())
print(crazy.lower().islower())

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Help on class str in module builtins:

class str(object)
 |  str(object='') -> str
 |  str(bytes_or_buffer[, encoding[, errors]]) -> str
 |  
 |  Create a new string object from the given object. If encoding or
 |  errors is specified, then the object must expose a data buffer
 |  that will be decoded using the given encoding and error handler.
 |  Otherwise, returns the result of object.__str__() (if defined)
 |  or repr(object).
 |  encoding defaults to sys.getdefaultencoding().
 |  errors defaults to 'strict'.
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __format__(self, format_spec, /)
 |      Return a formatted version of the string as described by format_spec.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(self, key, /)
 |      Return self[key].
 |  
 |  __getnewargs__(...)
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __hash__(self, /)
 |      Return hash(self).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mod__(self, value, /)
 |      Return self%value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __rmod__(self, value, /)
 |      Return value%self.
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  __sizeof__(self, /)
 |      Return the size of the string in memory, in bytes.
 |  
 |  __str__(self, /)
 |      Return str(self).
 |  
 |  capitalize(self, /)
 |      Return a capitalized version of the string.
 |      
 |      More specifically, make the first character have upper case and the rest lower
 |      case.
 |  
 |  casefold(self, /)
 |      Return a version of the string suitable for caseless comparisons.
 |  
 |  center(self, width, fillchar=' ', /)
 |      Return a centered string of length width.
 |      
 |      Padding is done using the specified fill character (default is a space).
 |  
 |  count(...)
 |      S.count(sub[, start[, end]]) -> int
 |      
 |      Return the number of non-overlapping occurrences of substring sub in
 |      string S[start:end].  Optional arguments start and end are
 |      interpreted as in slice notation.
 |  
 |  encode(self, /, encoding='utf-8', errors='strict')
 |      Encode the string using the codec registered for encoding.
 |      
 |      encoding
 |        The encoding in which to encode the string.
 |      errors
 |        The error handling scheme to use for encoding errors.
 |        The default is 'strict' meaning that encoding errors raise a
 |        UnicodeEncodeError.  Other possible values are 'ignore', 'replace' and
 |        'xmlcharrefreplace' as well as any other name registered with
 |        codecs.register_error that can handle UnicodeEncodeErrors.
 |  
 |  endswith(...)
 |      S.endswith(suffix[, start[, end]]) -> bool
 |      
 |      Return True if S ends with the specified suffix, False otherwise.
 |      With optional start, test S beginning at that position.
 |      With optional end, stop comparing S at that position.
 |      suffix can also be a tuple of strings to try.
 |  
 |  expandtabs(self, /, tabsize=8)
 |      Return a copy where all tab characters are expanded using spaces.
 |      
 |      If tabsize is not given, a tab size of 8 characters is assumed.
 |  
 |  find(...)
 |      S.find(sub[, start[, end]]) -> int
 |      
 |      Return the lowest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Return -1 on failure.
 |  
 |  format(...)
 |      S.format(*args, **kwargs) -> str
 |      
 |      Return a formatted version of S, using substitutions from args and kwargs.
 |      The substitutions are identified by braces ('{' and '}').
 |  
 |  format_map(...)
 |      S.format_map(mapping) -> str
 |      
 |      Return a formatted version of S, using substitutions from mapping.
 |      The substitutions are identified by braces ('{' and '}').
 |  
 |  index(...)
 |      S.index(sub[, start[, end]]) -> int
 |      
 |      Return the lowest index in S where substring sub is found, 
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Raises ValueError when the substring is not found.
 |  
 |  isalnum(self, /)
 |      Return True if the string is an alpha-numeric string, False otherwise.
 |      
 |      A string is alpha-numeric if all characters in the string are alpha-numeric and
 |      there is at least one character in the string.
 |  
 |  isalpha(self, /)
 |      Return True if the string is an alphabetic string, False otherwise.
 |      
 |      A string is alphabetic if all characters in the string are alphabetic and there
 |      is at least one character in the string.
 |  
 |  isascii(self, /)
 |      Return True if all characters in the string are ASCII, False otherwise.
 |      
 |      ASCII characters have code points in the range U+0000-U+007F.
 |      Empty string is ASCII too.
 |  
 |  isdecimal(self, /)
 |      Return True if the string is a decimal string, False otherwise.
 |      
 |      A string is a decimal string if all characters in the string are decimal and
 |      there is at least one character in the string.
 |  
 |  isdigit(self, /)
 |      Return True if the string is a digit string, False otherwise.
 |      
 |      A string is a digit string if all characters in the string are digits and there
 |      is at least one character in the string.
 |  
 |  isidentifier(self, /)
 |      Return True if the string is a valid Python identifier, False otherwise.
 |      
 |      Use keyword.iskeyword() to test for reserved identifiers such as "def" and
 |      "class".
 |  
 |  islower(self, /)
 |      Return True if the string is a lowercase string, False otherwise.
 |      
 |      A string is lowercase if all cased characters in the string are lowercase and
 |      there is at least one cased character in the string.
 |  
 |  isnumeric(self, /)
 |      Return True if the string is a numeric string, False otherwise.
 |      
 |      A string is numeric if all characters in the string are numeric and there is at
 |      least one character in the string.
 |  
 |  isprintable(self, /)
 |      Return True if the string is printable, False otherwise.
 |      
 |      A string is printable if all of its characters are considered printable in
 |      repr() or if it is empty.
 |  
 |  isspace(self, /)
 |      Return True if the string is a whitespace string, False otherwise.
 |      
 |      A string is whitespace if all characters in the string are whitespace and there
 |      is at least one character in the string.
 |  
 |  istitle(self, /)
 |      Return True if the string is a title-cased string, False otherwise.
 |      
 |      In a title-cased string, upper- and title-case characters may only
 |      follow uncased characters and lowercase characters only cased ones.
 |  
 |  isupper(self, /)
 |      Return True if the string is an uppercase string, False otherwise.
 |      
 |      A string is uppercase if all cased characters in the string are uppercase and
 |      there is at least one cased character in the string.
 |  
 |  join(self, iterable, /)
 |      Concatenate any number of strings.
 |      
 |      The string whose method is called is inserted in between each given string.
 |      The result is returned as a new string.
 |      
 |      Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'
 |  
 |  ljust(self, width, fillchar=' ', /)
 |      Return a left-justified string of length width.
 |      
 |      Padding is done using the specified fill character (default is a space).
 |  
 |  lower(self, /)
 |      Return a copy of the string converted to lowercase.
 |  
 |  lstrip(self, chars=None, /)
 |      Return a copy of the string with leading whitespace removed.
 |      
 |      If chars is given and not None, remove characters in chars instead.
 |  
 |  partition(self, sep, /)
 |      Partition the string into three parts using the given separator.
 |      
 |      This will search for the separator in the string.  If the separator is found,
 |      returns a 3-tuple containing the part before the separator, the separator
 |      itself, and the part after it.
 |      
 |      If the separator is not found, returns a 3-tuple containing the original string
 |      and two empty strings.
 |  
 |  replace(self, old, new, count=-1, /)
 |      Return a copy with all occurrences of substring old replaced by new.
 |      
 |        count
 |          Maximum number of occurrences to replace.
 |          -1 (the default value) means replace all occurrences.
 |      
 |      If the optional argument count is given, only the first count occurrences are
 |      replaced.
 |  
 |  rfind(...)
 |      S.rfind(sub[, start[, end]]) -> int
 |      
 |      Return the highest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Return -1 on failure.
 |  
 |  rindex(...)
 |      S.rindex(sub[, start[, end]]) -> int
 |      
 |      Return the highest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Raises ValueError when the substring is not found.
 |  
 |  rjust(self, width, fillchar=' ', /)
 |      Return a right-justified string of length width.
 |      
 |      Padding is done using the specified fill character (default is a space).
 |  
 |  rpartition(self, sep, /)
 |      Partition the string into three parts using the given separator.
 |      
 |      This will search for the separator in the string, starting at the end. If
 |      the separator is found, returns a 3-tuple containing the part before the
 |      separator, the separator itself, and the part after it.
 |      
 |      If the separator is not found, returns a 3-tuple containing two empty strings
 |      and the original string.
 |  
 |  rsplit(self, /, sep=None, maxsplit=-1)
 |      Return a list of the words in the string, using sep as the delimiter string.
 |      
 |        sep
 |          The delimiter according which to split the string.
 |          None (the default value) means split according to any whitespace,
 |          and discard empty strings from the result.
 |        maxsplit
 |          Maximum number of splits to do.
 |          -1 (the default value) means no limit.
 |      
 |      Splits are done starting at the end of the string and working to the front.
 |  
 |  rstrip(self, chars=None, /)
 |      Return a copy of the string with trailing whitespace removed.
 |      
 |      If chars is given and not None, remove characters in chars instead.
 |  
 |  split(self, /, sep=None, maxsplit=-1)
 |      Return a list of the words in the string, using sep as the delimiter string.
 |      
 |      sep
 |        The delimiter according which to split the string.
 |        None (the default value) means split according to any whitespace,
 |        and discard empty strings from the result.
 |      maxsplit
 |        Maximum number of splits to do.
 |        -1 (the default value) means no limit.
 |  
 |  splitlines(self, /, keepends=False)
 |      Return a list of the lines in the string, breaking at line boundaries.
 |      
 |      Line breaks are not included in the resulting list unless keepends is given and
 |      true.
 |  
 |  startswith(...)
 |      S.startswith(prefix[, start[, end]]) -> bool
 |      
 |      Return True if S starts with the specified prefix, False otherwise.
 |      With optional start, test S beginning at that position.
 |      With optional end, stop comparing S at that position.
 |      prefix can also be a tuple of strings to try.
 |  
 |  strip(self, chars=None, /)
 |      Return a copy of the string with leading and trailing whitespace remove.
 |      
 |      If chars is given and not None, remove characters in chars instead.
 |  
 |  swapcase(self, /)
 |      Convert uppercase characters to lowercase and lowercase characters to uppercase.
 |  
 |  title(self, /)
 |      Return a version of the string where each word is titlecased.
 |      
 |      More specifically, words start with uppercased characters and all remaining
 |      cased characters have lower case.
 |  
 |  translate(self, table, /)
 |      Replace each character in the string using the given translation table.
 |      
 |        table
 |          Translation table, which must be a mapping of Unicode ordinals to
 |          Unicode ordinals, strings, or None.
 |      
 |      The table must implement lookup/indexing via __getitem__, for instance a
 |      dictionary or list.  If this operation raises LookupError, the character is
 |      left untouched.  Characters mapped to None are deleted.
 |  
 |  upper(self, /)
 |      Return a copy of the string converted to uppercase.
 |  
 |  zfill(self, width, /)
 |      Pad a numeric string with zeros on the left, to fill a field of the given width.
 |      
 |      The string is never truncated.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  maketrans(x, y=None, z=None, /)
 |      Return a translation table usable for str.translate().
 |      
 |      If there is only one argument, it must be a dictionary mapping Unicode
 |      ordinals (integers) or characters to Unicode ordinals, strings or None.
 |      Character keys will be then converted to ordinals.
 |      If there are two arguments, they must be strings of equal length, and
 |      in the resulting dictionary, each character in x will be mapped to the
 |      character at the same position in y. If there is a third argument, it
 |      must be a string, whose characters will be mapped to None in the result.

THE QUICK BROWN FOX JUMPED OVER THE LAZY DOG

is lower?  I JusT mEt YoU, anD tHIs is CraaZy, sO CAll mE mayBe
False

is lower?  i just met you, and this is craazy, so call me maybe
True
```
</div>
</div>
</div>



# input from the user
run the following code to get input from the _user_ (you are the user!)
```python
name = input("what is your name: ")
print("hi", name)
```

your programs now have the power to ask questions!





<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
name = input("what is your name: ")
print("hi", name)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
what is your name: aviad
hi aviad
```
</div>
</div>
</div>



# BMI: Body mass index
In health the BMI (body mass index) is defined as $$BMI=\frac{weight}{height^2}$$ 

where the weight is in kilograms, and the height is in meters.

for example for weight 80kg and height 2.0m the BMI is
$80 / (2^2) = 80 /4 = 20 $

1. put 97 into a variable called `weight`
2. put 1.84 into a variabled called `height`
3. write code to compute and print the bmi






<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
weight = 97
height = 1.84
bmi = weight / height**2
print(bmi)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
28.650756143667294
```
</div>
</div>
</div>



# BMI with input from user
1. use the `input()` function to ask the user for his weight, put in variable `weight`
2. what is the type of the variable `weight`?
3. use the following code to convert the value to a `float`
```python
w = float(weight)
```
   what is the type of `w` now?
4. ask the user for his height and convert to float
5. compute and print the bmi



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
weight = input("what is your weight? ")
print(type(weight), weight)
w = float(weight)
print(type(w), w)
height = input("what is your height? ")
h = float(height)
bmi  = w/h**2
print(bmi)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
what is your weight? 80
<class 'str'> 80
<class 'float'> 80.0
what is your height? 1.8
24.691358024691358
```
</div>
</div>
</div>



# help for str.split() function
print the `help` for the function _`str.split`_
> hint: use the `help()` function



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

split(self, /, sep=None, maxsplit=-1)
    Return a list of the words in the string, using sep as the delimiter string.
    
    sep
      The delimiter according which to split the string.
      None (the default value) means split according to any whitespace,
      and discard empty strings from the result.
    maxsplit
      Maximum number of splits to do.
      -1 (the default value) means no limit.

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

join(self, iterable, /)
    Concatenate any number of strings.
    
    The string whose method is called is inserted in between each given string.
    The result is returned as a new string.
    
    Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'

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



# 4 boom
in this exercise, we're going to take some song lyrics, and replace every 4th word of each line with the word "boom". and then print out the lyrics.
> NOTE: this exercise is simple but takes a lot of lines of code. 
> we _will_ learn loops __IN THE NEXT LESSON__. loops will help us write shorter solutions, but for now __YOU DONT NEED LOOPS__

use the following code, which puts an _important_ 😜 string in a variable named _`song`_ 
```python
song = """
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say good bye
Never gonna tell a lie and hurt you
"""
```
[![This is important](https://globalpremierbenefits.com/wp-content/uploads/2018/10/Click-Here-small-_0-300x107.jpg)](https://www.youtube.com/watch?v=dQw4w9WgXcQ "Everything Is AWESOME")


1. split this string into a list of lines. put it in variable called `lines`
   > hint: string have a function called `.splitlines()`
   
2. split the line 0 into words. put it in variable called words0
   - now also split line 1. put it into `words1`
   - repeat for line 2 ..., line 5, put each into word1, ... word5

   > hint: this should take you 6 simples lines.
   
3. replace the 4th word of line 1, line 2, ... line 6 with the word `"boom"``
   > hint: you __don't__ need loops. this again takes 6 lines
   
4. now join `words0`. put the result into variable boom0
   - continue to join `words1`, `words2` ... `words5` into `boom1`, `boom2` ... `boom5`
   
5. create a list that contains `boom0`, `boom1`, ... `boom5`, call it `boom`

6. join the lines in `boom` back into a string. put it into a variable called `result`
   > hint: use this code
   ```python
   result = "\n".join(boom)
   ```

7. print the result

[![This is important](https://cdn.instructables.com/FJI/WGSW/FPIUQQ3K/FJIWGSWFPIUQQ3K.LARGE.jpg?auto=webp&frame=1&width=320)](https://www.youtube.com/watch?v=dQw4w9WgXcQ "Everything Is AWESOME")


> expected output:
```
Never gonna give you boom
Never gonna let you boom
Never gonna run around boom desert you
Never gonna make you boom
Never gonna say good boom
Never gonna tell a boom and hurt you
```



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
### useful: data
song = """Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say good bye
Never gonna tell a lie and hurt you
"""

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
lines = song.splitlines()

words0 = lines[0].split()
words1 = lines[1].split()
words2 = lines[2].split()
words3 = lines[3].split()
words4 = lines[4].split()
words5 = lines[5].split()

words0[4] = "boom"
words1[4] = "boom"
words2[4] = "boom"
words3[4] = "boom"
words4[4] = "boom"
words5[4] = "boom"

boom0 = " ".join(words0)
boom1 = " ".join(words1)
boom2 = " ".join(words2)
boom3 = " ".join(words3)
boom4 = " ".join(words4)
boom5 = " ".join(words5)

boom = [boom0, boom1, boom2, boom3, boom4, boom5]
result = "\n".join(boom)
print(result)


```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Never gonna give you boom
Never gonna let you boom
Never gonna run around boom desert you
Never gonna make you boom
Never gonna say good boom
Never gonna tell a boom and hurt you
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
    
1. without using "head math", write simple code to compute the costs of gouda, edam and camambert together 
> hint: the solution is one simple but long line of code, which uses the `+` operator 3 times

1. add a new cheese to the dictionary: 
  `Cottage` cheese, which costs `3.2`
> hint: the solution takes just one very simple line of code

1. the government has added a new tax on milk products, now every cheese costs has increased by 27% ! can you update the costs in the dictionary?
> hint: the solution takes 5 (almost identical) lines of code

1. what does the following code do?
```python
pi = 3.14159265
print(pi)
pi_rounded = round(pi, 2)
print(pi_rounded)
```
can you use the `round()` function to round the prices of cheese, so that it has costs in dollars and cents (Shekels and agorot)?






<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# 1
print()
print(1)
print('-' * 10)
costs = {
    "Gouda" : 4.99 ,
    "Edam" : 2.45,
    "Camambert" : 7.75,
    "Bree" : 7.27
}
print(costs)

# 2
print()
print(2)
print('-' * 10)
print(costs["Gouda"] + costs["Edam"] + costs["Camambert"])

# 3
print()
print(3)
print('-' * 10)
costs["Cottage"] = 3.2
print(costs)

# 4
print()
print(4)
print('-' * 10)
costs['Gouda'] = costs['Gouda'] * 1.27
costs['Edam'] = costs['Edam'] * 1.27
costs['Camambert'] = costs['Camambert'] * 1.27
costs['Bree'] = costs['Bree'] * 1.27
costs['Cottage'] = costs['Cottage'] * 1.27
print(costs)

# 5
print()
print(5)
print('-' * 10)
pi = 3.14159265
print(pi)
pi_rounded = round(pi, 2)
print(pi_rounded)

costs['Gouda'] = round(costs['Gouda'], 2)
costs['Edam'] = round(costs['Edam'], 2)
costs['Camambert'] = round(costs['Camambert'], 2)
costs['Bree'] = round(costs['Bree'], 2)
costs['Cottage'] = round(costs['Cottage'], 2)
print(costs)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```

1
----------
{'Gouda': 4.99, 'Edam': 2.45, 'Camambert': 7.75, 'Bree': 7.27}

2
----------
15.190000000000001

3
----------
{'Gouda': 4.99, 'Edam': 2.45, 'Camambert': 7.75, 'Bree': 7.27, 'Cottage': 3.2}

4
----------
{'Gouda': 6.3373, 'Edam': 3.1115000000000004, 'Camambert': 9.8425, 'Bree': 9.232899999999999, 'Cottage': 4.064}

5
----------
3.14159265
3.14
{'Gouda': 6.34, 'Edam': 3.11, 'Camambert': 9.84, 'Bree': 9.23, 'Cottage': 4.06}
```
</div>
</div>
</div>


---
redirect_from:
  - "/08-functions/notebooks/veriadic-funcs-args"
interact_link: content/08_functions/notebooks/veriadic_funcs_args.ipynb
kernel_name: python3
has_widgets: false
title: 'Veriadic Funcs Args'
prev_page:
  url: /08_functions/notebooks/variadic_functions_unpacking.html
  title: 'Variadic Functions Unpacking'
next_page:
  url: /09_advanced_collections/exercise/questions.html
  title: '09 advanced collections'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-python/blob/master/live%20class%20demonstrations/lesson%2008%20-%20veriadic%20funcs%20args.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def varfunc(*args):
    print(f"type={type(args)}, len={len(args)}")
    print(args)
    

                  

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
varfunc()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
type=<class 'tuple'>, len=0
()
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
varfunc(1,2,3)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
type=<class 'tuple'>, len=3
(1, 2, 3)
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
varfunc("h", "e", "l", "l", "o")

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
type=<class 'tuple'>, len=5
('h', 'e', 'l', 'l', 'o')
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def varfunc2(a,b,c, *args):
    print(a,b,c)
    print(f"type={type(args)}, len={len(args)}")
    print(args)

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
varfunc2()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_traceback_line}
```

    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-6-1062b2caca7b> in <module>
    ----> 1 varfunc2()
    

    TypeError: varfunc2() missing 3 required positional arguments: 'a', 'b', and 'c'


```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
varfunc2(1,2,3)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
1 2 3
type=<class 'tuple'>, len=0
()
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
varfunc2(1,2,3, 4, 5, 6)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
1 2 3
type=<class 'tuple'>, len=3
(4, 5, 6)
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
varfunc(end="\n")

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_traceback_line}
```

    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-9-e70da5c7e22a> in <module>
    ----> 1 varfunc(end="\n")
    

    TypeError: varfunc() got an unexpected keyword argument 'end'


```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print(1,2,3, sep =" @ ", end=" !!! \n")

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
1 @ 2 @ 3 !!! 
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def myprint(*args, sep=' ', end='\n'):
    print(*args, sep=sep, end=end)

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
myprint("hello", "world", "nice", "to", "meet", "you")

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
hello world nice to meet you
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print('hello')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
hello
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
myprint(blah="blah")

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_traceback_line}
```

    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-22-3095fd74f9d2> in <module>
    ----> 1 myprint(blah="blah")
    

    TypeError: myprint() got an unexpected keyword argument 'blah'


```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
myprint(just_invented_this="blah")

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_traceback_line}
```

    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-24-d660da8a1e87> in <module>
    ----> 1 myprint(just_invented_this="blah")
    

    TypeError: myprint() got an unexpected keyword argument 'just_invented_this'


```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
dict(a=1, b=2, blah=10, testthis=100)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
{'a': 1, 'b': 2, 'blah': 10, 'testthis': 100}
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def mydict(**kwargs):
    print(f"type={type(kwargs)}, len={len(kwargs)}")
    print(kwargs)
    #return kwargs
    return dict(**kwargs)

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
mydict(a=1, b=2, blah=10, testthis=100)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
type=<class 'dict'>, len=4
{'a': 1, 'b': 2, 'blah': 10, 'testthis': 100}
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
mydict(
    param1 = "I",
    p2 = "can",
    p3 = "send",
    p4 = "anything",
    whynot = "!"
)
    

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
type=<class 'dict'>, len=5
{'param1': 'I', 'p2': 'can', 'p3': 'send', 'p4': 'anything', 'whynot': '!'}
```
</div>
</div>
<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
{'param1': 'I', 'p2': 'can', 'p3': 'send', 'p4': 'anything', 'whynot': '!'}
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
x = mydict(
    param1 = "I",
    p2 = "can",
    p3 = "send",
    p4 = "anything",
    whynot = "!"
) 

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
type=<class 'dict'>, len=5
{'param1': 'I', 'p2': 'can', 'p3': 'send', 'p4': 'anything', 'whynot': '!'}
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print(x)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
{'param1': 'I', 'p2': 'can', 'p3': 'send', 'p4': 'anything', 'whynot': '!'}
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def full_variadic(*args, **kwargs):
    print(args)
    print(kwargs)
    

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
full_variadic(1,2,3, name='avi', lname="blah")

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
(1, 2, 3)
{'name': 'avi', 'lname': 'blah'}
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def make_wrapper(func):
    
    def the_wrapper(*args, **kwargs):
        print("I'm wrapping the func", func.__name__)
        print(args)
        print(kwargs)
        x = func(*args, **kwargs)
        print("returning", x)
        return x
    
    return the_wrapper


```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
myprint = make_wrapper(print)

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
myprint(1,2,3, end=" @@@\n")

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
I'm wrapping the func print
(1, 2, 3)
{'end': ' @@@\n'}
1 2 3 @@@
returning None
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
import math

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
mysin = make_wrapper(math.sin)

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
mysin(0)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
I'm wrapping the func sin
(0,)
{}
returning 0.0
```
</div>
</div>
<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
0.0
```


</div>
</div>
</div>


---
redirect_from:
  - "/07-files/notebooks/file-open-write"
interact_link: content/07_files/notebooks/file_open_write.ipynb
kernel_name: python3
has_widgets: false
title: 'File Open Write'
prev_page:
  url: /07_files/notebooks/file_example.html
  title: 'File Example'
next_page:
  url: /07_files/notebooks/json.html
  title: 'Json'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-python/blob/master/content/07_files/notebooks/file_open_write.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
f= open("myfile.txt", "w")
print("hello", file=f)

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
f.close()

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
f=open("myfile.txt")
lines = f.readlines()
print(lines)
f.close()

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
f=open("myfile.txt")
for line in f:
    print(line, end="")
f.close()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
I am Daniel

I am Sam
Sam I am

That Sam-I-am
That Sam-I-am!
I do not like
That Sam-I-am

Do you like
Green eggs and ham

I do not like them,
Sam-I-am.
I do not like
Green eggs and ham.

Would you like them
Here or there?

I would not like them
Here or there.
I would not like them
Anywhere.
I do not like
Green eggs and ham.
I do not like them,
Sam-I-am

Would you like them
In a house?
Would you like them
With a mouse?

I do not like them
In a house.
I do not like them
With a mouse.
I do not like them
Here or there.
I do not like them
Anywhere.
I do not like green eggs and ham.
I do not like them, Sam-I-am.

Would you eat them
In a box?
Would you eat them
With a fox?

Not in a box.
Not with a fox.
Not in a house.
Not with a mouse.
I would not eat them here or there.
I would not eat them anywhere.
I would not eat green eggs and ham.
I do not like them, Sam-I-am.

Would you? Could you?
In a car?
Eat them! Eat them!
Here they are.

I woould not,
Could not,
In a car

You may like them.
You will see.
You may like them
In a tree?

I would not, could not in a tree.
Not in a car! You let me be.
I do not like them in a box.
I do not like them with a fox
I do not like them in a house
I do mot like them with a mouse
I do not like them here or there.
I do not like them anywhere.
I do not like green eggs and ham.
I do not like them, Sam-I-am.

A train! A train!
A train! A train!
Could you, would you
On a train?

Not on a train! Not in a tree!
Not in a car! Sam! Let me be!
I would not, could not, in a box.
I could not, would not, with a fox.
I will not eat them with a mouse
I will not eat them in a house.
I will not eat them here or there.
I will not eat them anywhere.
I do not like them, Sam-I-am.

Say!
In the dark?
Here in the dark!
Would you, could you, in the dark?

I would not, could not,
In the dark.

Would you, could you,
In the rain?

I would not, could not, in the rain.
Not in the dark. Not on a train,
Not in a car, Not in a tree.
I do not like them, Sam, you see.
Not in a house. Not in a box.
Not with a mouse. Not with a fox.
I will not eat them here or there.
I do not like them anywhere!

You do not like
Green eggs and ham?

I do not
Like them,
Sam-I-am.

Could you, would you,
With a goat?

I would not,
Could not.
With a goat!

Would you, could you,
On a boat?```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
f=open("myfile.txt")
for linenumber, line in enumerate(f):
    print(linenumber, ":", line, end="")
    

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
0 : I am Daniel
1 : 
2 : I am Sam
3 : Sam I am
4 : 
5 : That Sam-I-am
6 : That Sam-I-am!
7 : I do not like
8 : That Sam-I-am
9 : 
10 : Do you like
11 : Green eggs and ham
12 : 
13 : I do not like them,
14 : Sam-I-am.
15 : I do not like
16 : Green eggs and ham.
17 : 
18 : Would you like them
19 : Here or there?
20 : 
21 : I would not like them
22 : Here or there.
23 : I would not like them
24 : Anywhere.
25 : I do not like
26 : Green eggs and ham.
27 : I do not like them,
28 : Sam-I-am
29 : 
30 : Would you like them
31 : In a house?
32 : Would you like them
33 : With a mouse?
34 : 
35 : I do not like them
36 : In a house.
37 : I do not like them
38 : With a mouse.
39 : I do not like them
40 : Here or there.
41 : I do not like them
42 : Anywhere.
43 : I do not like green eggs and ham.
44 : I do not like them, Sam-I-am.
45 : 
46 : Would you eat them
47 : In a box?
48 : Would you eat them
49 : With a fox?
50 : 
51 : Not in a box.
52 : Not with a fox.
53 : Not in a house.
54 : Not with a mouse.
55 : I would not eat them here or there.
56 : I would not eat them anywhere.
57 : I would not eat green eggs and ham.
58 : I do not like them, Sam-I-am.
59 : 
60 : Would you? Could you?
61 : In a car?
62 : Eat them! Eat them!
63 : Here they are.
64 : 
65 : I woould not,
66 : Could not,
67 : In a car
68 : 
69 : You may like them.
70 : You will see.
71 : You may like them
72 : In a tree?
73 : 
74 : I would not, could not in a tree.
75 : Not in a car! You let me be.
76 : I do not like them in a box.
77 : I do not like them with a fox
78 : I do not like them in a house
79 : I do mot like them with a mouse
80 : I do not like them here or there.
81 : I do not like them anywhere.
82 : I do not like green eggs and ham.
83 : I do not like them, Sam-I-am.
84 : 
85 : A train! A train!
86 : A train! A train!
87 : Could you, would you
88 : On a train?
89 : 
90 : Not on a train! Not in a tree!
91 : Not in a car! Sam! Let me be!
92 : I would not, could not, in a box.
93 : I could not, would not, with a fox.
94 : I will not eat them with a mouse
95 : I will not eat them in a house.
96 : I will not eat them here or there.
97 : I will not eat them anywhere.
98 : I do not like them, Sam-I-am.
99 : 
100 : Say!
101 : In the dark?
102 : Here in the dark!
103 : Would you, could you, in the dark?
104 : 
105 : I would not, could not,
106 : In the dark.
107 : 
108 : Would you, could you,
109 : In the rain?
110 : 
111 : I would not, could not, in the rain.
112 : Not in the dark. Not on a train,
113 : Not in a car, Not in a tree.
114 : I do not like them, Sam, you see.
115 : Not in a house. Not in a box.
116 : Not with a mouse. Not with a fox.
117 : I will not eat them here or there.
118 : I do not like them anywhere!
119 : 
120 : You do not like
121 : Green eggs and ham?
122 : 
123 : I do not
124 : Like them,
125 : Sam-I-am.
126 : 
127 : Could you, would you,
128 : With a goat?
129 : 
130 : I would not,
131 : Could not.
132 : With a goat!
133 : 
134 : Would you, could you,
135 : On a boat?```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
with open("output.txt", "w") as f:
    print("hello", file=f)
    #f.write("hello\n")



```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
import sys
print('hello')
print('world', file=sys.stdout)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
hello
world
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print('sorry, stuff failed', file=sys.stderr)

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
sys.stdin


```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
<_io.TextIOWrapper name='<stdin>' mode='r' encoding='cp1252'>
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
f = open("input.txt")
print(1, f.readlines())
print(2, f.readlines())
f.seek(0)
print(3, f.readlines())



```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
1 ['hello.py will read from this file\n']
2 []
3 ['hello.py will read from this file\n']
```
</div>
</div>
</div>


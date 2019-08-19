---
redirect_from:
  - "/04-strings/notebooks/print-parameters"
interact_link: content/04_strings/notebooks/print_parameters.ipynb
kernel_name: python3
has_widgets: false
title: 'Print Parameters'
prev_page:
  url: /04_strings/notebooks/formatting_bitahon.html
  title: 'Formatting Bitahon'
next_page:
  url: /04_strings/notebooks/split_join.html
  title: 'Split Join'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-python/blob/master/live%20class%20demonstrations/lesson%2004%20-%20print%20parameters.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print(1,2,3,4,5)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
1 2 3 4 5
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print(1,2,3,4,5, sep="\t")
print(1,2,3,4,5, sep="\t@@@\t")

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
1	2	3	4	5
1	@@@	2	@@@	3	@@@	4	@@@	5
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
#print(1,2,3,4,5, end="\n")
print(1,2,3,4,5, end="\t@@@\n")

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
1 2 3 4 5	@@@
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
for i in range(1,10+1):
    for j in range(1, 10+1):
        print(i*j, end='\t')
    print()


```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
1	2	3	4	5	6	7	8	9	10	
2	4	6	8	10	12	14	16	18	20	
3	6	9	12	15	18	21	24	27	30	
4	8	12	16	20	24	28	32	36	40	
5	10	15	20	25	30	35	40	45	50	
6	12	18	24	30	36	42	48	54	60	
7	14	21	28	35	42	49	56	63	70	
8	16	24	32	40	48	56	64	72	80	
9	18	27	36	45	54	63	72	81	90	
10	20	30	40	50	60	70	80	90	100	
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
import sys
print(1,2,3)
print(1,2,3, file=sys.stdout)
print(1,2,3, file=sys.stderr)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
1 2 3
1 2 3
```
</div>
</div>
</div>


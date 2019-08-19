---
redirect_from:
  - "/03-flow-control/notebooks/lesson-03-1-100-multiplication-matrix-luah-kefel-"
interact_link: content/03_flow_control/notebooks/lesson_03-1-100_multiplication_matrix_Luah_Kefel_.ipynb
kernel_name: python3
has_widgets: false
title: 'Lesson 03-1-100 Multiplication Matrix Luah Kefel '
prev_page:
  url: /03_flow_control/notebooks/lesson_03-1-100_multiplication_matrix_Luah_Kefel_.html
  title: 'notebooks'
next_page:
  url: /03_flow_control/notebooks/lesson_03-break_continue.html
  title: 'Lesson 03-break Continue'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-python/blob/master/live%20class%20demonstrations/lesson%2003%20-%201-100%20multiplication%20matrix%20%28Luah%20Kefel%29.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
for col in range(1,11):
    for row in range(1,11):
        print(col,"*",row,"=",col*row)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
1 * 1 = 1
1 * 2 = 2
1 * 3 = 3
1 * 4 = 4
1 * 5 = 5
1 * 6 = 6
1 * 7 = 7
1 * 8 = 8
1 * 9 = 9
1 * 10 = 10
2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
2 * 4 = 8
2 * 5 = 10
2 * 6 = 12
2 * 7 = 14
2 * 8 = 16
2 * 9 = 18
2 * 10 = 20
3 * 1 = 3
3 * 2 = 6
3 * 3 = 9
3 * 4 = 12
3 * 5 = 15
3 * 6 = 18
3 * 7 = 21
3 * 8 = 24
3 * 9 = 27
3 * 10 = 30
4 * 1 = 4
4 * 2 = 8
4 * 3 = 12
4 * 4 = 16
4 * 5 = 20
4 * 6 = 24
4 * 7 = 28
4 * 8 = 32
4 * 9 = 36
4 * 10 = 40
5 * 1 = 5
5 * 2 = 10
5 * 3 = 15
5 * 4 = 20
5 * 5 = 25
5 * 6 = 30
5 * 7 = 35
5 * 8 = 40
5 * 9 = 45
5 * 10 = 50
6 * 1 = 6
6 * 2 = 12
6 * 3 = 18
6 * 4 = 24
6 * 5 = 30
6 * 6 = 36
6 * 7 = 42
6 * 8 = 48
6 * 9 = 54
6 * 10 = 60
7 * 1 = 7
7 * 2 = 14
7 * 3 = 21
7 * 4 = 28
7 * 5 = 35
7 * 6 = 42
7 * 7 = 49
7 * 8 = 56
7 * 9 = 63
7 * 10 = 70
8 * 1 = 8
8 * 2 = 16
8 * 3 = 24
8 * 4 = 32
8 * 5 = 40
8 * 6 = 48
8 * 7 = 56
8 * 8 = 64
8 * 9 = 72
8 * 10 = 80
9 * 1 = 9
9 * 2 = 18
9 * 3 = 27
9 * 4 = 36
9 * 5 = 45
9 * 6 = 54
9 * 7 = 63
9 * 8 = 72
9 * 9 = 81
9 * 10 = 90
10 * 1 = 10
10 * 2 = 20
10 * 3 = 30
10 * 4 = 40
10 * 5 = 50
10 * 6 = 60
10 * 7 = 70
10 * 8 = 80
10 * 9 = 90
10 * 10 = 100
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
for i in range(1,11):
    for j  in range(1,11):
        print(i*j, "\t", end="")
    print()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
1 	2 	3 	4 	5 	6 	7 	8 	9 	10 	
2 	4 	6 	8 	10 	12 	14 	16 	18 	20 	
3 	6 	9 	12 	15 	18 	21 	24 	27 	30 	
4 	8 	12 	16 	20 	24 	28 	32 	36 	40 	
5 	10 	15 	20 	25 	30 	35 	40 	45 	50 	
6 	12 	18 	24 	30 	36 	42 	48 	54 	60 	
7 	14 	21 	28 	35 	42 	49 	56 	63 	70 	
8 	16 	24 	32 	40 	48 	56 	64 	72 	80 	
9 	18 	27 	36 	45 	54 	63 	72 	81 	90 	
10 	20 	30 	40 	50 	60 	70 	80 	90 	100 	
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
i=1
j=1
while i<=10:
    j=1
    while j<=10:
        print(i*j, "\t", end="")
        j=j+1
    i=i+1
    print()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
1 	2 	3 	4 	5 	6 	7 	8 	9 	10 	
2 	4 	6 	8 	10 	12 	14 	16 	18 	20 	
3 	6 	9 	12 	15 	18 	21 	24 	27 	30 	
4 	8 	12 	16 	20 	24 	28 	32 	36 	40 	
5 	10 	15 	20 	25 	30 	35 	40 	45 	50 	
6 	12 	18 	24 	30 	36 	42 	48 	54 	60 	
7 	14 	21 	28 	35 	42 	49 	56 	63 	70 	
8 	16 	24 	32 	40 	48 	56 	64 	72 	80 	
9 	18 	27 	36 	45 	54 	63 	72 	81 	90 	
10 	20 	30 	40 	50 	60 	70 	80 	90 	100 	
```
</div>
</div>
</div>


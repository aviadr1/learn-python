---
redirect_from:
  - "/03-flow-control/notebooks/for-loop-examples"
interact_link: content/03_flow_control/notebooks/for_loop_examples.ipynb
kernel_name: python3
has_widgets: false
title: 'For Loop Examples'
prev_page:
  url: /03_flow_control/notebooks/for_loop.html
  title: 'For Loop'
next_page:
  url: /03_flow_control/notebooks/for_while_with_password_example.html
  title: 'For While With Password Example'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-python/blob/master/content/03_flow_control/notebooks/for_loop_examples.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
costs = {
    "Gouda" : 4.99 ,
    "Edam" : 2.45,
    "Camambert" : 7.75,
    "Bree" : 7.27
}

costs['Gouda'] = costs['Gouda'] * 1.27
costs['Edam'] = costs['Edam'] * 1.27
costs['Camambert'] = costs['Camambert'] * 1.27
costs['Bree'] = costs['Bree'] * 1.27

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
prices = [4.99 , 2.45, 7.75, 7.27, 10, 20, 30, 40, 50, 60]

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
total = 0
total = total + prices[0]
total = total + prices[1]
total = total + prices[2]
total = total + prices[3]
print(total)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
22.46
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
total = 0
for price in prices:
    #print('this price:', price)
    total = total + price
    #print('total now:', total)

print()  
print("result: ", total)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```

result:  232.46
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print("a")
print("b")
print("c")


```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
a
b
c
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print("a", end=" ")
print("b", end=" ")
print("c", end=" ")

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
a b c ```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
quote = "ill be back"
for character in quote:
    print(character)

#iillll  bbee  bbaacckk

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
i
l
l
 
b
e
 
b
a
c
k
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
quote

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'ill be back'
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
for word in quote.split():
    print(word, end=' ')
    print(word, end=' ')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
ill ill be be back back ```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
for char in quote:
    print('!', end='')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
!!!!!!!!!!!```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
for x in range(10):
    print(x, end=' ')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
0 1 2 3 4 5 6 7 8 9 ```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
for x in range(10, 20):
    print(x, end=' ')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
10 11 12 13 14 15 16 17 18 19 ```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
nums = []
nums.append(0)
nums.append(1)
nums.append(2)
nums.append(3)
nums.append(4)
nums.append(5)
nums.append(6)
nums.append(7)
nums.append(8)

nums

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
[0, 1, 2, 3, 4, 5, 6, 7, 8]
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
nums = []
for x in range(10):
    nums.append(x)

print(nums)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
for x in range(10):
    print('*', end="")

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
**********```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
for x in range(10):
    for y in range(10):
        print('*', end="")
    print()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
**********
**********
**********
**********
**********
**********
**********
**********
**********
**********
```
</div>
</div>
</div>


---
redirect_from:
  - "/04-strings/exercise/solutions"
interact_link: content/04_strings/exercise/solutions.ipynb
kernel_name: python3
has_widgets: false
title: 'Solutions'
prev_page:
  url: /04_strings/exercise/questions.html
  title: 'Questions'
next_page:
  url: /04_strings/notebooks/formatting_bitahon.html
  title: 'notebooks'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-python/blob/master/content/04_strings/exercise/solutions.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




# multiplying a string

> _what does the following code do?_
> ```
> "hello " * 3
> ``` 

can you use this idea to print a triangle of `"*"` using __just a single for loop__?



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
for i in range(1, 10):
    print("*" * i)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
*
**
***
****
*****
******
*******
********
*********
```
</div>
</div>
</div>



# controlling precision with str.format()
can you print the value 10/3, with only 2 digits of precision?
   - hint: use the .format() function



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
"{:.2f}".format(10/3)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'3.33'
```


</div>
</div>
</div>



# CSV
here is some data in CSV (Comma Seperated Values) format:
```
   name, age, country
   avi cohen, 30, israel
   ben hur, 25, united kingdom
   can davidovich, 40, georgia
   david ben shalem, 60, united states of america
   efrat ben dagan levi, 25, united arab emirates
```

   1. print only the names of the people in this data, and nothing else
      - note: don't print commas `','`
      - hint: use `splitlines()` and `split()`
      
      
   2. print only the ages
   
   
   3. print only country names
   
   
   4. print only the last 3 lines (hint: use splicing)
   
   
   5. print the data without the header (hint: use splicing)
   
   
   6. print every second line, without the header (hint: use splicing)
   
   
   7. print a smaller csv that has just ages and countries, 
      without the header and without names



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
data = """\
name, age, country
avi cohen, 30, israel
ben hur, 25, united kingdom
can davidovich, 40, georgia
david ben shalem, 60, united states of america
efrat ben dagan levi, 25, united arab emirates
"""

# a
for line in data.splitlines()[1:] :
    columns = line.split(',')
    name = columns[0].strip()
    print(name)

print()

# b
for line in data.splitlines()[1:] :
    columns = line.split(',')
    age = columns[1].strip()
    print(age)

print()
    
# c
for line in data.splitlines()[1:] :
    columns = line.split(',')
    country = columns[2].strip()
    print(country)

print()

# d
print('\n'.join(data.splitlines()[1: ]))

print()

# e
print('\n'.join(data.splitlines()[-3: ]))

print()

# f
print('\n'.join(data.splitlines()[1::2]))

print()

#g
for line in data.splitlines()[1:]:
    age_country = line.split(',')[1:]
    print(', '.join(age_country))

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
avi cohen
ben hur
can davidovich
david ben shalem
efrat ben dagan levi

30
25
40
60
25

israel
united kingdom
georgia
united states of america
united arab emirates

avi cohen, 30, israel
ben hur, 25, united kingdom
can davidovich, 40, georgia
david ben shalem, 60, united states of america
efrat ben dagan levi, 25, united arab emirates

can davidovich, 40, georgia
david ben shalem, 60, united states of america
efrat ben dagan levi, 25, united arab emirates

avi cohen, 30, israel
can davidovich, 40, georgia
efrat ben dagan levi, 25, united arab emirates

 30,  israel
 25,  united kingdom
 40,  georgia
 60,  united states of america
 25,  united arab emirates
```
</div>
</div>
</div>



# printing receipts

lets print a simple receipt using the .format() function
   the receipt will have 4 lines, looking like this:
```   
    cost           :  362.50 NIS
    vat            :   17.00 %
    vat            :   61.62 NIS
    total          :  424.12 NIS
```  

to determine the cost and the vat, lets use random numbers.
use the following code:

```
import random
cost_nis = round(random.normalvariate(200, 50), 2)
vat_percent = random.randint(160, 180) / 10
# print(cost_nis, vat_percent)
```
     
compute the vat in NIS and the total and print the receipt
     
- NOTE: make sure that the numbers in the receipt are nicely aligned to make it readble!
- HINT: use the `str.format()` function, read the [specification](https://docs.python.org/3/library/string.html#format-specification-mini-language) or go through some [examples](https://docs.python.org/3/library/string.html#format-examples) to get the hang of this mini-langauge     



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
import random
cost_nis = round(random.normalvariate(200, 50), 2)
vat_percent = random.randint(160, 180) / 10
# print(cost_nis, vat_percent)

receipt = """\
cost         : {:6.2f} NIS
vat          : {:6.2f} %
vat          : {:6.2f} NIS
total        : {:6.2f} NIS
""".format(cost_nis, vat_percent, cost_nis * vat_percent / 100, cost_nis + cost_nis*vat_percent/100)

print(receipt)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
cost         : 194.86 NIS
vat          :  18.00 %
vat          :  35.07 NIS
total        : 229.93 NIS

```
</div>
</div>
</div>



# `**` a full receipt

given a menu with prices that can look like this:
```
     prices = {
         "steak" : 150,
         "omelet" : 25,
         "coca cola" : 12,
         "orange juice" : 16,
         "pizza" : 49,
         "hamburger" : 59,
         "pita" : 1.5,
         "tomato salad" : 13.5
     }
```

and an a list containing an order from a table, such as:

```
order = ["steak", "steak", "pita", "pizza", "coca cola"]
```

use a for loop to print a full receipt  
```
steak          :  150.00 NIS
steak          :  150.00 NIS
pita           :    1.50 NIS
pizza          :   49.00 NIS
coca cola      :   12.00 NIS
----------------------------
cost           :  362.50 NIS
vat            :   17.00 %
vat            :   61.62 NIS
total          :  424.12 NIS
```




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
### useful: data
prices = {
         "steak" : 150,
         "omelet" : 25,
         "coca cola" : 12,
         "orange juice" : 16,
         "pizza" : 49,
         "hamburger" : 59,
         "pita" : 1.5,
         "tomato salad" : 13.5
     }

order = ["steak", "steak", "pita", "pizza", "coca cola"]

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
cost = 0
part1 = ""
for item in order:
    price = prices[item]
    cost += price
    
    line = "{:15}:  {:6.2f} NIS\n".format(item, price)
    part1 += line

part1 += '-' * 28 + '\n'
vat = 17
part2 = """\
cost           :  {:6.2f} NIS
vat            :  {:6.2f} %
vat            :  {:6.2f} NIS
total          :  {:6.2f} NIS
""".format(cost, vat, cost * vat / 100, cost + cost*vat/100)

print(part1 + part2)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
steak          :  150.00 NIS
steak          :  150.00 NIS
pita           :    1.50 NIS
pizza          :   49.00 NIS
coca cola      :   12.00 NIS
----------------------------
cost           :  362.50 NIS
vat            :   17.00 %
vat            :   61.62 NIS
total          :  424.12 NIS

```
</div>
</div>
</div>


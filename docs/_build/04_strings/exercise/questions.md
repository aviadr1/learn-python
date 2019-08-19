---
redirect_from:
  - "/04-strings/exercise/questions"
interact_link: content/04_strings/exercise/questions.ipynb
kernel_name: python3
has_widgets: false
title: 'Questions'
prev_page:
  url: /04_strings/exercise/questions.html
  title: 'exercise'
next_page:
  url: /04_strings/exercise/solutions.html
  title: 'Solutions'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-python/blob/master/exercises/ex%2004%20-%20questions.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




# multiplying a string

> _what does the following code do?_
> ```
> "hello " * 3
> ``` 

can you use this idea to print a triangle of `"*"` using __just a single for loop__?



# controlling precision with str.format()
can you print the value 10/3, with only 2 digits of precision?
   - hint: use the .format() function



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


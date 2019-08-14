---
redirect_from:
  - "/exercises/ex-05-questions"
interact_link: content/exercises/ex_05-questions.ipynb
kernel_name: python3
has_widgets: false
title: 'Ex 05-questions'
prev_page:
  url: /exercises/ex_04-solutions.html
  title: 'Ex 04-solutions'
next_page:
  url: /exercises/ex_05-solutions.html
  title: 'Ex 05-solutions'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-python/blob/master/exercises/ex%2005%20-%20questions.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




# 1. list of random numbers
using the following code, create a list of __25 random numbers__
```
   import random
   random.randint(0, 100) # generates a random number between 0 and 100
```   
   example result: (write code to randomly create this list)
```
   [90, 10, 14, 15,    20, 20, 87, 23,
    8,  2,  44, 29,    10, 13, 33, 99,
    9,  3,  23, 25]
```



# 2. create a sub-list
create a list of all the numbers between 0-100 that are dividible by 7:

   0, 7, 14, 21, ... 
   
how many different ways can you think of to do this?
   
 1. using a for loop
 2. using range
 3. using range and slicing



# 3.  removing from a list `*`
remove from the list you created in question #1, all the numbers that are divisible by 7

how many ways can you think of doing this?

1. using `.remove()`
2. using `.pop()`

test your solution using this code:
```
for x in mylist:
    assert i % 7 != 0
```




# 4. reversing words in a sentence
print the words in the following sentence in reverse order
```
    the quick brown fox jumped over the lazy dog   
    --> dog lazy the over jumped fox brown quick the
```    
do it in as many ways as you can
1. using slicing
2. using pop
3. using loop and range




# 5. remove first and last
remove the first and last numbers from the list #1 and put them in variable x,y
   how can you do this with the least number of lines?
   
1. using indexing and -1
2. using unpacking
3. using pop



# 6. intersection between lists
create any two lists list1, list2
example:
```
list1 = "the fox condemns the trap, not himself".split()
list2 = "the quick brown fox jumped over them lazy dog".split()
```

1. now, using the keyword 'in' and a loop check if list1 has *any* item that also belongs in list2
2. now also create a list called list_1_2 that has the entire list of items that exist in both list1 and list2 




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
### useful: test data
list1 = "the fox condemns the trap, not himself".split()
list2 = "the quick brown fox jumped over the lazy dog".split()

```
</div>

</div>



# 7. intersection between lists using sets

solve question #6 using `set`

hint: you no longer need loops



# 8. random numbers without duplicates
using the type `set`, 
- create a list of exactly 20 random numbers(between 0-100), 
- that have no duplicates 



# 9. remove duplicates
- create a list of 15 random numbers betwen 1-10
- using the type `set()`  
  remove all the duplicate numbers from the list 
   
1. do it without caring about the order of items
2. `**` can you also do it, while preserving the original order of the list?



# 10. uniques and dups `**`
- get a list of 20 random numbers, each in range 0-10
- from this list, which numbers were  ...
  1. unique? i.e. they appeared only once in the list?
  2. dups? i.e. they appeared more than once in the list?
   
    
hint: you may need a for loop and having one or two sets



# 11. results of automated testing

imagine you're running automated tests for a new build of your project. 
and this build "build1" fails some test. 
then the engineers go on to try to fix the bugs and create "build2" which also fails some tests

example:
```
  build1_fails = [1, 3, 6, 12, 13, 19, 20, 23, 24, 25, 33, 34, 45, 66, 67, 87, 100, 145, 149]
  build2_fails = [2, 9, 10, 11, 12, 13, 14, 15, 16, 19, 20, 87, 88, 89, 145, 146 ]
```

1. which tests were fixed by build2? that is, they failed in build1 and stopped failing in build2?
2. which tests got broken by build2? that is, they worked on build1 and started failing in build2?
3. which broken tests did not get solved by build2? that is, they failed on both build1 and build2?
4. `**` which tests succeeded in both builds (hint: imagine there are 150 tests overall, named 1, 2, ..., 149, 150) 



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
### useful: example data
build1_fails = [1, 3, 6, 12, 13, 19, 20, 23, 24, 25, 33, 34, 45, 66, 67, 87, 100, 145, 149]
build2_fails = [2, 9, 10, 11, 12, 13, 14, 15, 16, 19, 20, 87, 88, 89, 145, 146 ]

```
</div>

</div>



# 12. 144 dictionary
- look at your phone's phonebook, and select 4 people you have phone numbers for
- create an "144" dictionary for these people 
that maps names of people to their phone numbers



# 13. reverse 411 dictionary

1. take the dictionary from the previous question and create a _reverse_ "411" dictionary
    that maps phone numbers back to people's names
    
    
2. `**` sharing phone numbers:
   - what happens if two people share the same phone number?
   - can you still reverse the dictionary and preserve all the information?


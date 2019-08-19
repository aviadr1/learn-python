---
redirect_from:
  - "/05-collections/exercise/solutions"
interact_link: content/05_collections/exercise/solutions.ipynb
kernel_name: python3
has_widgets: false
title: 'Solutions'
prev_page:
  url: /05_collections/exercise/questions.html
  title: 'Questions'
next_page:
  url: /05_collections/notebooks/dictionaries_checkpoint.html
  title: 'notebooks'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-python/blob/master/content/05_collections/exercise/solutions.ipynb" target="_blank">
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



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
import random
rand = []
for i in range(25):
    rand.append(random.randint(0, 100))
    
print(rand)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
[17, 16, 30, 99, 35, 36, 18, 9, 24, 93, 92, 65, 62, 32, 89, 32, 26, 74, 47, 53, 38, 20, 8, 1, 1]
```
</div>
</div>
</div>



# 2. create a sub-list
create a list of all the numbers between 0-100 that are dividible by 7:

   0, 7, 14, 21, ... 
   
how many different ways can you think of to do this?
   
 1. using a for loop
 2. using range
 3. using range and slicing



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# 1
a = []
for i in range(100):
    if i%7==0:
        a.append(i)
print(a)

#2
b = list(range(0, 100,7))
print(b)

#3
c = list(range(100))[::7]
print(c)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
[0, 7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98]
[0, 7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98]
[0, 7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98]
```
</div>
</div>
</div>



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




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
number7s = list(range(0, 100,7))

# remove
list1 = sorted(rand[:]) # copy and sort list from #1
print("random list: ", list1)
print('all divisible by 7: ', number7s)
print()

number7s = list(range(0, 100, 7)) # multiples of 7
for x in number7s:
    while x in list1:
        list1.remove(x) #remove() removes only the first occurance
print(sorted(list1))

for x in list1:
    assert x % 7 != 0

# pop solution #1
list2 = rand[:]
i=0
while i<len(list2):
    if list2[i] in number7s:
        list2.pop(i)
    else:
        i+=1
print(sorted(list2))
        
# pop solution #2
list3 = rand[:]
# iterate on the list in reverse to avoid changing indexes
for i in range(len(list3) - 1, -1, -1): 
    if list3[i] in number7s:
        list3.pop(i)
print(sorted(list3))


```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
random list:  [1, 1, 8, 9, 16, 17, 18, 20, 24, 26, 30, 32, 32, 35, 36, 38, 47, 53, 62, 65, 74, 89, 92, 93, 99]
all divisible by 7:  [0, 7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98]

[1, 1, 8, 9, 16, 17, 18, 20, 24, 26, 30, 32, 32, 36, 38, 47, 53, 62, 65, 74, 89, 92, 93, 99]
[1, 1, 8, 9, 16, 17, 18, 20, 24, 26, 30, 32, 32, 36, 38, 47, 53, 62, 65, 74, 89, 92, 93, 99]
[1, 1, 8, 9, 16, 17, 18, 20, 24, 26, 30, 32, 32, 36, 38, 47, 53, 62, 65, 74, 89, 92, 93, 99]
```
</div>
</div>
</div>



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




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
x="the quick brown fox jumped over the lazy dog"

# slicing
print(" ".join(x.split()[::-1]))

# pop
words = x.split()
while words:
    print(words.pop(), end=" ")
print()

# loop and range
words = x.split()
for i in range (-1, -len(words) -1, -1):
    print(words[i], end=" ")
print()

# loop and slicing
for word in x.split()[::-1]:
    print(word, end=" ")
print()

# reversed
print(" ".join(list(reversed(x.split()))))

# in place reverse
words = x.split()
words.reverse() # in-place
print(" ".join(words))

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
dog lazy the over jumped fox brown quick the
dog lazy the over jumped fox brown quick the 
dog lazy the over jumped fox brown quick the 
dog lazy the over jumped fox brown quick the 
dog lazy the over jumped fox brown quick the
dog lazy the over jumped fox brown quick the
```
</div>
</div>
</div>



# 5. remove first and last
remove the first and last numbers from the list #1 and put them in variable x,y
   how can you do this with the least number of lines?
   
1. using indexing and -1
2. using unpacking
3. using pop



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print(rand)

# using indexing and -1
list1 = rand[:] # list from #1
x, y = list1[0], list1[-1]
print(x, list1[1:-1], y)

#using unpacking
list1 = rand[:] # list from #1
x, *everythingelse, y = list1
print(x, everythingelse, y)

# using pop
list1 = rand[:] # list from #1
x,y =list1.pop(0), list1.pop(-1)
print(x,list1, y)


```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
[17, 16, 30, 99, 35, 36, 18, 9, 24, 93, 92, 65, 62, 32, 89, 32, 26, 74, 47, 53, 38, 20, 8, 1, 1]
17 [16, 30, 99, 35, 36, 18, 9, 24, 93, 92, 65, 62, 32, 89, 32, 26, 74, 47, 53, 38, 20, 8, 1] 1
17 [16, 30, 99, 35, 36, 18, 9, 24, 93, 92, 65, 62, 32, 89, 32, 26, 74, 47, 53, 38, 20, 8, 1] 1
17 [16, 30, 99, 35, 36, 18, 9, 24, 93, 92, 65, 62, 32, 89, 32, 26, 74, 47, 53, 38, 20, 8, 1] 1
```
</div>
</div>
</div>



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



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# 1)
for word in list1:
    if word in list2:
        print('1:', word)
        break
        
# 2)
words = []
for word in list1:
    if word in list2:
        words.append(word)

print('2:', words)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
1: the
2: ['the', 'fox', 'the']
```
</div>
</div>
</div>



# 7. intersection between lists using sets

solve question #6 using `set`

hint: you no longer need loops



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print( set(list1) & set(list2)) # & calls set.intersection

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
{'fox', 'the'}
```
</div>
</div>
</div>



# 8. random numbers without duplicates
using the type `set`, 
- create a list of exactly 20 random numbers(between 0-100), 
- that have no duplicates 



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
result=set()
while len(result) < 20:
    result.add(random.randint(0, 100))
print(sorted(result))

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
[14, 17, 18, 26, 29, 37, 43, 45, 46, 48, 54, 56, 59, 63, 70, 75, 89, 90, 92, 93]
```
</div>
</div>
</div>



# 9. remove duplicates
- create a list of 15 random numbers betwen 1-10
- using the type `set()`  
  remove all the duplicate numbers from the list 
   
1. do it without caring about the order of items
2. `**` can you also do it, while preserving the original order of the list?



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
rand = []
for i in range(15):
    rand.append(random.randint(0, 10))

list1 = rand[:]
print(list1)

# in normal sorted order 
print(set(list1))

# in the same order as the original list
print(sorted(set(list1), key=list1.index))

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
[3, 7, 0, 9, 1, 0, 6, 6, 0, 6, 2, 6, 2, 0, 1]
{0, 1, 2, 3, 6, 7, 9}
[3, 7, 0, 9, 1, 6, 2]
```
</div>
</div>
</div>



# 10. uniques and dups `**`
- get a list of 20 random numbers, each in range 0-10
- from this list, which numbers were  ...
  1. unique? i.e. they appeared only once in the list?
  2. dups? i.e. they appeared more than once in the list?
   
    
hint: you may need a for loop and having one or two sets



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# create random list
rand = []
for i in range(20):
    rand.append(random.randint(0, 10))

# calculate uniques
seen = set()
uniq = set()
for x in rand:
    if x not in seen:
        uniq.add(x)
        seen.add(x)
    else:
        uniq.discard(x)

# print results
dups = seen - uniq
print(sorted(rand))
print("seen: ", seen)
print("uniques: ", uniq)
print("dups: ", dups)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
[0, 0, 1, 2, 2, 3, 3, 3, 4, 4, 4, 6, 7, 7, 8, 9, 9, 9, 9, 10]
seen:  {0, 1, 2, 3, 4, 6, 7, 8, 9, 10}
uniques:  {1, 6, 8, 10}
dups:  {0, 2, 3, 4, 7, 9}
```
</div>
</div>
</div>



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



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print("1: ", set(build1_fails) - set(build2_fails))
print("2: ", set(build2_fails) - set(build1_fails))
print("3: ", set(build1_fails) & set(build2_fails))

print()
print("4: ", set(range(150)) - (set(build2_fails) | set(build1_fails) ))

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
1:  {1, 33, 3, 34, 66, 6, 67, 100, 45, 149, 23, 24, 25}
2:  {2, 9, 10, 11, 14, 15, 16, 146, 88, 89}
3:  {12, 13, 145, 19, 20, 87}

4:  {0, 4, 5, 7, 8, 17, 18, 21, 22, 26, 27, 28, 29, 30, 31, 32, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 147, 148}
```
</div>
</div>
</div>



# 12. 144 dictionary
- look at your phone's phonebook, and select 4 people you have phone numbers for
- create an "144" dictionary for these people 
that maps names of people to their phone numbers



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
d144 = {
    "avi" : "053-111",
    "ben" : "053-222",
    "hen" : "053-222",
    "gaddy" : "053-333",
    "daddy" : "053-333",
    "zvi" : "053-444",
    "zvika" : "053-444"
}

```
</div>

</div>



# 13. reverse 411 dictionary

1. take the dictionary from the previous question and create a _reverse_ "411" dictionary
    that maps phone numbers back to people's names
    
    
2. `**` sharing phone numbers:
   - what happens if two people share the same phone number?
   - can you still reverse the dictionary and preserve all the information?



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
#1
d441 = {}
for name, phone in d144.items():
    d441[phone] = name
print(d441)

#2
d441 = {}
for name, phone in d144.items():
    if phone not in d441:
        d441[phone] = [name]
    else:
        names = d441[phone]
        names.append(name)

print(d441)       

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
{'053-111': 'avi', '053-222': 'hen', '053-333': 'daddy', '053-444': 'zvika'}
{'053-111': ['avi'], '053-222': ['ben', 'hen'], '053-333': ['gaddy', 'daddy'], '053-444': ['zvi', 'zvika']}
```
</div>
</div>
</div>


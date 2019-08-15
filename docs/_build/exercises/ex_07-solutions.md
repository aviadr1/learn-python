---
redirect_from:
  - "/exercises/ex-07-solutions"
interact_link: content/exercises/ex_07-solutions.ipynb
kernel_name: python3
has_widgets: false
title: 'Ex 07-solutions'
prev_page:
  url: /exercises/ex_07-questions.html
  title: 'Ex 07-questions'
next_page:
  url: /exercises/ex_08-questions.html
  title: 'Ex 08-questions'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-python/blob/master/exercises/ex%2007%20-%20solutions.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




# current working directory
use the following code to see what your current working directory is
```
import os
current_working_directory = os.path.realpath('.')
print(current_working_directory)
```

whenever you open files without specifying a full path, the operating system will assume you are using this directory




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
import os
current_working_directory = os.path.realpath('.')
print(current_working_directory)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
C:\Users\jbt\Downloads
```
</div>
</div>
</div>



# look at a folder in windows file explorer
> **on windows OS only**

use the following code to open the windows file explorer in your current working directory. <br>
this will be useful when you're looking for files you are creating

```
# windows only
import subprocess
current_working_directory = os.path.realpath('.')
if os.name == 'nt':
    subprocess.Popen('explorer.exe ' + current_working_directory)
```

notice how it opened a new window for you




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# windows only
import subprocess
current_working_directory = os.path.realpath('.')
if os.name == 'nt':
    subprocess.Popen('explorer.exe ' + current_working_directory)

```
</div>

</div>



# write file

1. use the following code to open the file ex07.txt for writing
    ```
    f = open('ex07.txt', 'w')
    ```

2. here's some text to write into the file

    ```
    dead_parrot = """
    I wish to complain about this parrot what I purchased not half an hour ago from this very boutique.

    Oh yes, the, uh, the Norwegian Blue...What's,uh...What's wrong with it?

    I'll tell you what's wrong with it, my lad. 'E's dead, that's what's wrong with it!

    No, no, 'e's uh,...he's resting.
    """
    ```

3. don't forget to close the file
   <br><br>

4. can you find this file on your hard drive?




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
f = open('ex07.txt', 'w')

dead_parrot = """
I wish to complain about this parrot what I purchased not half an hour ago from this very boutique.

Oh yes, the, uh, the Norwegian Blue...What's,uh...What's wrong with it?

I'll tell you what's wrong with it, my lad. 'E's dead, that's what's wrong with it!

No, no, 'e's uh,...he's resting.
"""

print(dead_parrot, file=f)

f.close()

import subprocess, os
if os.name == 'nt': 
    subprocess.Popen('notepad.exe ex07.txt')

```
</div>

</div>



# reading a file

use `open()` and a for loop to read the contents of the `"ex07.txt"` file, line by line



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
f = open('ex07.txt')
for line in f:
    print(line, end="")

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```

I wish to complain about this parrot what I purchased not half an hour ago from this very boutique.

Oh yes, the, uh, the Norwegian Blue...What's,uh...What's wrong with it?

I'll tell you what's wrong with it, my lad. 'E's dead, that's what's wrong with it!

No, no, 'e's uh,...he's resting.

```
</div>
</div>
</div>



# convenience functions - read_file

Lets write a convenience function called `readfile` that accepts one parameter called `filename` 
```
def readfile(filename):
```
the function should:
1. opens the file to a variable called f
1. reads and returns all the content of the file (use `f.read()`)
1. closes the file

Also lets write convenience function called `printfile` that accepts one parameter called `filename` like so:
```
def printfile(filename):
    print(readfile(filename))
```
Lets use `printfile` function on `'ex07.txt'` to read its contents





<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def readfile(filename):
    with open(filename) as f:
        return f.read()

def printfile(filename):
    print(readfile(filename))

printfile('ex07.txt')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```

I wish to complain about this parrot what I purchased not half an hour ago from this very boutique.

Oh yes, the, uh, the Norwegian Blue...What's,uh...What's wrong with it?

I'll tell you what's wrong with it, my lad. 'E's dead, that's what's wrong with it!

No, no, 'e's uh,...he's resting.


```
</div>
</div>
</div>



# transforming a file
we want to write an ALL CAPS version of ex07.txt where all the text is in uppercase

1. open the 'ex07.txt' input file for reading <br><br>

1. open a new 'ex07.allcaps.txt' output file for writing <br><br>

1. use a for loop on the read file to read the text line by line
   1. convert each line to uppercase
   1. write the line to the output file 
   <br><br>
   
1. don't forget to close the files <br><br>

1. make sure the new file is there




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
f = open('ex07.txt')
fout = open('ex07.allcaps.txt', 'w')
for line in f:
    print(line.upper(), end="", file=fout)
    
fout.close()
f.close()

printfile('ex07.allcaps.txt')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```

I WISH TO COMPLAIN ABOUT THIS PARROT WHAT I PURCHASED NOT HALF AN HOUR AGO FROM THIS VERY BOUTIQUE.

OH YES, THE, UH, THE NORWEGIAN BLUE...WHAT'S,UH...WHAT'S WRONG WITH IT?

I'LL TELL YOU WHAT'S WRONG WITH IT, MY LAD. 'E'S DEAD, THAT'S WHAT'S WRONG WITH IT!

NO, NO, 'E'S UH,...HE'S RESTING.


```
</div>
</div>
</div>



# renaming and deleting files

1. use the following code to delete the file `"ex07.txt"`
```
import os
os.remove('ex07.txt')
```

1. use the `os.rename()` function (use help to figure out how to use it) to rename the file `'ex07.allcaps.txt'` to `"ex07.txt"`

> **now we've "rewritten" the ex07.txt file to be in all caps** <br>
> but what _really_ happened is that we wrote a new file, and then replaced the old file with the new file
> in most cases of working on files, this is the right way to approach problems and how many scripts, editors or programs work > in the real world



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
os.remove('ex07.txt')
os.rename('ex07.allcaps.txt', 'ex07.txt')


```
</div>

</div>



# writing a CSV file

> The so-called CSV (Comma Separated Values) format is the most common import and export format for spreadsheets and databases. CSV format was used for many years prior to attempts to describe the format in a standardized way in RFC 4180. 

here's a some information about bank customers, their name, current money in the bank, and the salary check that they have received 

```
transactions = [
#    name             , money in bank now  , salary
    ['eric idle'      , 10000              , 5000  ],
    ['terry gilliam'  ,  2500              , 12500 ],
    ['graham chapman' , -5000              , 20000 ]
    ]
```

can you use a loop to write this, along with a header, to a CSV file named `"transactions.csv"`?

expected output in transactions.csv:

    name, money in bank now, salary
    eric idle, 10000, 5000
    terry gilliam, 2500, 12500
    graham chapman, 
    
    



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
transactions = [
#    name             , money in bank now  , salary  
    ['eric idle'      , 10000              , 5000  ],
    ['terry gilliam'  ,  2500              , 12500 ],
    ['graham chapman' , -5000              , 20000 ]
    ]

f = open('transactions.csv', 'w')
print('name', 'money in bank now', 'salary', sep=', ', file=f)
for trans in transactions:
    name, money, salary = trans
    print(name, money, salary, sep=', ', file=f)
    
f.close()
    
printfile('transactions.csv')    

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
name, money in bank now, salary
eric idle, 10000, 5000
terry gilliam, 2500, 12500
graham chapman, -5000, 20000

```
</div>
</div>
</div>



# transforming a CSV file

Lets compute how much money each bank customer will have after their salary kicks in
and write the results into a new file called `"totals.csv"`
this file needs only 2 columns - we drop the salary column

expected output for `totals.csv`:

    name, money in bank now 
    eric idle, 15000
    terry gilliam, 15000
    graham chapman, 15000
    




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
f = open('transactions.csv', 'r')
fout = open('totals.csv', 'w')
print('name', 'money in bank now', sep=', ', file=fout)
f.readline()
for trans in transactions:
    name, money, salary = trans
    money = int(money) + int(salary)
    print(name, money, sep=', ', file=fout)
    
f.close()
fout.close()

printfile('totals.csv')  

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
name, money in bank now
eric idle, 15000
terry gilliam, 15000
graham chapman, 15000

```
</div>
</div>
</div>



# Creating  and deleting directories

1. import the module `shutil` and use the `shutil.rmtree('mydir1') ` function to remove a directory called mydir1 if it exists
   > CAREFUL: `rmtree` will delete whole folders and subdirectories without prompt and without recovery. like a `rm -rf` 
1. use the `os.mkdir()` function to create a directory called `mydir1` in the current working directory
2. use the `os.makedirs()` function to create a sub-directory called `mydir1/mydir2/mydir3'
3. create a file called `surprise.txt` in `mydir1/mydir2/mydir3` and put the line `'nobody expects the spanish inquisition'` into that file
4. convince yourself that `os.remove()` can delete files and empty directories, but cannot delete folders with 'stuff' in them



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
import os
import shutil
shutil.rmtree('mydir1')
os.mkdir('mydir1')
os.makedirs('mydir1/mydir2/mydir3')
with open('mydir1/mydir2/mydir3/surprise.txt', 'w') as f:
    print('nobody expects the spanish inquisition', file=f)

```
</div>

</div>



# writing a JSON file

1. Create some complex object made of lists, tuples, dictionaries, strings, put it in variable named `data`
   example:
   ```
   data = [{
        "userId":"rirani",
        "jobTitleName":"Developer",
        "firstName":"Romin",
        "lastName":"Irani",
        "preferredFullName":"Romin Irani",
        "employeeCode":"E1",
        "region":"CA",
        "phoneNumber":"408-1234567",
        "emailAddress":"romin.k.irani@gmail.com"
    },
    {
        "userId":"nirani",
        "jobTitleName":"Developer",
        "firstName":"Neil",
        "lastName":"Irani",
        "preferredFullName":"Neil Irani",
        "employeeCode":"E2",
        "region":"CA",
        "phoneNumber":"408-1111111",
        "emailAddress":"neilrirani@gmail.com"
    }]
    ```
2. use the `open()` function to open a file called `data.json.txt` into variable named `fout`
3. import the `json` module and use the `json.dump(data, f)` function to write your object to the file
4. close the file 
5. open the file with a text editor program and compare with your original 
6. use `open()` function to open the file for reading with variable `fin`
7. use the `data2 = json.load(fin)` function to read the file into a variable named `data2`
8. use `==` to compare `data` and `data2`. do they have the same content? 



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
data = [{
        "userId":"rirani",
        "jobTitleName":"Developer",
        "firstName":"Romin",
        "lastName":"Irani",
        "preferredFullName":"Romin Irani",
        "employeeCode":"E1",
        "region":"CA",
        "phoneNumber":"408-1234567",
        "emailAddress":"romin.k.irani@gmail.com"
    },
    {
        "userId":"nirani",
        "jobTitleName":"Developer",
        "firstName":"Neil",
        "lastName":"Irani",
        "preferredFullName":"Neil Irani",
        "employeeCode":"E2",
        "region":"CA",
        "phoneNumber":"408-1111111",
        "emailAddress":"neilrirani@gmail.com"
    }]

import json
with open('data.json.txt', 'w') as fout:
    json.dump(data, fout)

with open('data.json.txt', 'r') as fin:
    data2 = json.load(fin)
    
assert data == data2

```
</div>

</div>


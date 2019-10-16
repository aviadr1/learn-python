---
redirect_from:
  - "/07-files/path-and-shutil"
interact_link: content/07_files/path_and_shutil.ipynb
kernel_name: python3
has_widgets: false
title: '07 files'
prev_page:
  url: /06_regular_expressions/notebooks/lesson_06-sub_python2-to-python3.html
  title: 'Lesson 06-sub Python2-to-python3'
next_page:
  url: /07_files/path_and_shutil.html
  title: 'Path And Shutil'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-python/blob/master/content/07_files/path_and_shutil.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```from pathlib import Path

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```Path

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
pathlib.Path
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```cwd = Path.cwd()
cwd

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
PosixPath('/content')
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```type(cwd)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
pathlib.PosixPath
```


</div>
</div>
</div>



# what's in the directory?

use the function `iterdir()` to see all the contents of a directory 



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```import shutil
for subfolder in ['my_folder', 'blah']:
    try: 
        shutil.rmtree(str(cwd / subfolder))
    except:
        pass

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```for item in cwd.iterdir():
    print(item)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
/content/.config
/content/sample_data
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```list(cwd.iterdir())

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
[PosixPath('/content/.config'), PosixPath('/content/sample_data')]
```


</div>
</div>
</div>



# create a subdirectory



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```my_folder = cwd / 'my_folder'

if not my_folder.exists():
    my_folder.mkdir()
    
print(my_folder)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
/content/my_folder
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```my_folder.exists()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
True
```


</div>
</div>
</div>



# create a file in a directory



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```my_file = my_folder / 'my_file.txt'
my_file.touch()
print(my_file)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
/content/my_folder/my_file.txt
```
</div>
</div>
</div>



# one-shot write/read content to file



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```my_file.write_text('hello!')
my_file.read_text()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'hello!'
```


</div>
</div>
</div>



# parent folder



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```print(my_file.parent, type(my_file.parent))
print(my_file)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
/content/my_folder <class 'pathlib.PosixPath'>
/content/my_folder/my_file.txt
```
</div>
</div>
</div>



# filename without the path of the parent folder



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```my_file.name

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'my_file.txt'
```


</div>
</div>
</div>



# just the extension / suffix



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```my_file.suffix

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'.txt'
```


</div>
</div>
</div>



# filename without extension



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```my_file.stem

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'my_file'
```


</div>
</div>
</div>



# new file name



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```my_file1 = my_file.with_name(my_file.stem + '-1' + my_file.suffix)
print(my_file1)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
/content/my_folder/my_file-1.txt
```
</div>
</div>
</div>



# does file exist?




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```print(my_file, '\t exists?', my_file.exists())
print(my_file1, '\t exists?', my_file1.exists())

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
/content/my_folder/my_file.txt 	 exists? True
/content/my_folder/my_file-1.txt 	 exists? False
```
</div>
</div>
</div>



# copy file



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```import shutil

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```my_file.read_text()
shutil.copyfile(src=my_file, dst=my_file1)

print(my_file1, '\t exists?', my_file1.exists())
my_file1.read_text()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
/content/my_folder/my_file-1.txt 	 exists? True
```
</div>
</div>
<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'hello!'
```


</div>
</div>
</div>



# globbing
globbing means searching for files with wildcards ? or *



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```# lets create a csv file
my_csv = my_folder / 'my_data.csv'
my_csv.write_text('1, 2, 3, 4')
print(my_csv)
print(my_csv.read_text())

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
/content/my_folder/my_data.csv
1, 2, 3, 4
```
</div>
</div>
</div>



...
now we can search for the files with wildcards!




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```for item in my_folder.glob('*.txt'):
    print(item)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
/content/my_folder/my_file.txt
/content/my_folder/my_file-1.txt
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```for item in my_folder.glob('*.csv'):
    print(item)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
/content/my_folder/my_data.csv
```
</div>
</div>
</div>



# copy folder



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```my_other_folder = cwd / 'my_other_folder'
if my_other_folder.exists():
    shutil.rmtree(my_other_folder)
    
shutil.copytree(src=my_folder, dst=my_other_folder)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
PosixPath('/content/my_other_folder')
```


</div>
</div>
</div>



# recursively walk a folder



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```import os

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```for dirpath, dirnames, filenames in os.walk(cwd):
    print(dirpath)
    print('files: -->', filenames)
    print('subdirectories: -->', dirnames)
    print()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_traceback_line}
```

    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-4-f57b0f406b6e> in <module>()
    ----> 1 for dirpath, dirnames, filenames in os.walk(cwd):
          2     print(dirpath)
          3     print('files: -->', filenames)
          4     print('subdirectories: -->', dirnames)
          5     print()


    NameError: name 'cwd' is not defined


```
</div>
</div>
</div>



# rename directory



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```blah_folder = my_other_folder.with_name('blah')

# rename cannot rename a directory, because it is not empty
### my_other_folder.rename(blah_folder)

# use shutil.move instead
shutil.move(src=str(my_other_folder), dst=str(blah_folder))

for item in blah_folder.parent.iterdir():
    print(item)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_traceback_line}
```

    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-1-ab0196c931a7> in <module>()
    ----> 1 blah_folder = my_other_folder.with_name('blah')
          2 
          3 # rename cannot rename a directory, because it is not empty
          4 ### my_other_folder.rename(blah_folder)
          5 


    NameError: name 'my_other_folder' is not defined


```
</div>
</div>
</div>



# relative directory



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```# '.' is current directory
print(Path('.').resolve())

# appending /. just still means the same directory
print( (my_folder / '.').resolve() )

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
/content
/content/my_folder
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```# '..' means parent directory
print(Path('..').resolve())

# appending /.. means the parent directory of the given directory
print( (my_folder / '..').resolve() )

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
/
/content
/content/my_folder/..
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```# you can use .. to walk up in a directory
print( (my_folder / '..' / 'my_folder' / '..' / '.' / 'my_folder' / '..' / 'my_folder').resolve() )

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
/content/my_folder
```
</div>
</div>
</div>


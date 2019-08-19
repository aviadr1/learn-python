---
redirect_from:
  - "/13-multiprocessing/notebooks/os-system-subprocess"
interact_link: content/13_multiprocessing/notebooks/os_system_subprocess.ipynb
kernel_name: python3
has_widgets: false
title: 'Os System Subprocess'
prev_page:
  url: /13_multiprocessing/notebooks/os_system_subprocess.html
  title: 'notebooks'
next_page:
  url: /13_multiprocessing/notebooks/os_system_subprocess_popen.html
  title: 'Os System Subprocess Popen'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-python/blob/master/live%20class%20demonstrations/lesson%2013%20-%20os.system%20subprocess.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
import os

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
os.system("notepad.exe")

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
0
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
os.system("explorer.exe c:\\windows")

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
1
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
os.system(r'C:\Users\jbt\Downloads\QAPYTH3_2.3\IK_QAPYTH3\DG_13_Multitasking.pptx')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
0
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
import subprocess

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
help(subprocess.Popen)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Help on class Popen in module subprocess:

class Popen(builtins.object)
 |  Execute a child program in a new process.
 |  
 |  For a complete description of the arguments see the Python documentation.
 |  
 |  Arguments:
 |    args: A string, or a sequence of program arguments.
 |  
 |    bufsize: supplied as the buffering argument to the open() function when
 |        creating the stdin/stdout/stderr pipe file objects
 |  
 |    executable: A replacement program to execute.
 |  
 |    stdin, stdout and stderr: These specify the executed programs' standard
 |        input, standard output and standard error file handles, respectively.
 |  
 |    preexec_fn: (POSIX only) An object to be called in the child process
 |        just before the child is executed.
 |  
 |    close_fds: Controls closing or inheriting of file descriptors.
 |  
 |    shell: If true, the command will be executed through the shell.
 |  
 |    cwd: Sets the current directory before the child is executed.
 |  
 |    env: Defines the environment variables for the new process.
 |  
 |    universal_newlines: If true, use universal line endings for file
 |        objects stdin, stdout and stderr.
 |  
 |    startupinfo and creationflags (Windows only)
 |  
 |    restore_signals (POSIX only)
 |  
 |    start_new_session (POSIX only)
 |  
 |    pass_fds (POSIX only)
 |  
 |    encoding and errors: Text mode encoding and error handling to use for
 |        file objects stdin, stdout and stderr.
 |  
 |  Attributes:
 |      stdin, stdout, stderr, pid, returncode
 |  
 |  Methods defined here:
 |  
 |  __del__(self, _maxsize=9223372036854775807, _warn=<built-in function warn>)
 |  
 |  __enter__(self)
 |  
 |  __exit__(self, type, value, traceback)
 |  
 |  __init__(self, args, bufsize=-1, executable=None, stdin=None, stdout=None, stderr=None, preexec_fn=None, close_fds=<object object at 0x00000204D8CBB140>, shell=False, cwd=None, env=None, universal_newlines=False, startupinfo=None, creationflags=0, restore_signals=True, start_new_session=False, pass_fds=(), *, encoding=None, errors=None)
 |      Create new Popen instance.
 |  
 |  communicate(self, input=None, timeout=None)
 |      Interact with process: Send data to stdin.  Read data from
 |      stdout and stderr, until end-of-file is reached.  Wait for
 |      process to terminate.
 |      
 |      The optional "input" argument should be data to be sent to the
 |      child process (if self.universal_newlines is True, this should
 |      be a string; if it is False, "input" should be bytes), or
 |      None, if no data should be sent to the child.
 |      
 |      communicate() returns a tuple (stdout, stderr).  These will be
 |      bytes or, if self.universal_newlines was True, a string.
 |  
 |  kill = terminate(self)
 |  
 |  poll(self)
 |      Check if child process has terminated. Set and return returncode
 |      attribute.
 |  
 |  send_signal(self, sig)
 |      Send a signal to the process.
 |  
 |  terminate(self)
 |      Terminates the process.
 |  
 |  wait(self, timeout=None, endtime=None)
 |      Wait for child process to terminate.  Returns returncode
 |      attribute.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)

```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
p = subprocess.Popen('notepad.exe')

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
p

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
<subprocess.Popen at 0x204de562cf8>
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
p.wait()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
0
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
p = []
for i in range(10):
    p.append(subprocess.Popen('notepad.exe'))

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
for proc in p:
    proc.kill()

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
p

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
[<subprocess.Popen at 0x204de0bb2e8>,
 <subprocess.Popen at 0x204ddbe29e8>,
 <subprocess.Popen at 0x204dde5db00>,
 <subprocess.Popen at 0x204dde5db38>,
 <subprocess.Popen at 0x204dde5d080>,
 <subprocess.Popen at 0x204dde5d048>,
 <subprocess.Popen at 0x204dde5db70>,
 <subprocess.Popen at 0x204de013c88>,
 <subprocess.Popen at 0x204de013b70>,
 <subprocess.Popen at 0x204de0139e8>]
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
p[0].wait(10)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_traceback_line}
```

    ---------------------------------------------------------------------------

    TimeoutExpired                            Traceback (most recent call last)

    <ipython-input-19-31fbf64c54f2> in <module>
    ----> 1 p[0].wait(10)
    

    c:\python36\lib\subprocess.py in wait(self, timeout, endtime)
       1055                                                     timeout_millis)
       1056                 if result == _winapi.WAIT_TIMEOUT:
    -> 1057                     raise TimeoutExpired(self.args, timeout)
       1058                 self.returncode = _winapi.GetExitCodeProcess(self._handle)
       1059             return self.returncode


    TimeoutExpired: Command 'notepad.exe' timed out after 10 seconds


```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
p[0].wait(10)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
0
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
p = subprocess.Popen('cmd /c dir', stdout=subprocess.PIPE)

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
p.stdout.readlines()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
[b' Volume in drive C has no label.\r\n',
 b' Volume Serial Number is BAC2-CB8A\r\n',
 b'\r\n',
 b' Directory of C:\\Users\\jbt\r\n',
 b'\r\n',
 b'05/30/2019  02:20 PM    <DIR>          .\r\n',
 b'05/30/2019  02:20 PM    <DIR>          ..\r\n',
 b'06/24/2018  11:27 AM    <DIR>          .android\r\n',
 b'11/08/2016  01:13 PM    <DIR>          .AndroidStudio2.2\r\n',
 b'03/12/2017  12:42 PM    <DIR>          .AndroidStudio2.3\r\n',
 b'11/26/2017  01:37 PM    <DIR>          .AndroidStudio3.0\r\n',
 b'05/01/2018  12:03 PM    <DIR>          .AndroidStudio3.1\r\n',
 b'03/12/2017  05:11 PM    <DIR>          .config\r\n',
 b'06/24/2018  12:41 PM    <DIR>          .dotnet\r\n',
 b'11/19/2018  10:32 AM    <DIR>          .eclipse\r\n',
 b'11/08/2016  01:25 PM                16 .emulator_console_auth_token\r\n',
 b'11/26/2017  01:44 PM    <DIR>          .gradle\r\n',
 b'12/13/2015  09:56 AM    <DIR>          .idlerc\r\n',
 b'05/30/2019  02:10 PM    <DIR>          .ipynb_checkpoints\r\n',
 b'05/12/2019  10:07 AM    <DIR>          .ipython\r\n',
 b'05/20/2019  09:46 AM    <DIR>          .jupyter\r\n',
 b'11/20/2018  11:49 AM    <DIR>          .nbprofiler\r\n',
 b'03/12/2017  05:06 PM                75 .node_repl_history\r\n',
 b'06/24/2018  01:46 PM    <DIR>          .nuget\r\n',
 b'11/30/2015  01:30 PM    <DIR>          .oracle_jre_usage\r\n',
 b'03/07/2019  11:06 AM    <DIR>          .p2\r\n',
 b'05/03/2018  11:42 AM               344 .packettracer\r\n',
 b'06/24/2018  12:17 PM    <DIR>          .PyCharmCE2018.1\r\n',
 b'06/24/2018  01:46 PM    <DIR>          .templateengine\r\n',
 b'11/19/2018  10:32 AM    <DIR>          .tooling\r\n',
 b'11/26/2017  01:44 PM    <DIR>          .VirtualBox\r\n',
 b'07/03/2016  10:32 AM    <DIR>          .vscode\r\n',
 b'12/24/2018  12:20 AM    <DIR>          3D Objects\r\n',
 b'05/30/2019  11:11 AM    <DIR>          blah\r\n',
 b'05/12/2019  02:56 PM                78 blah.txt\r\n',
 b'05/03/2018  11:30 AM    <DIR>          Cisco Packet Tracer 6.2sv\r\n',
 b'05/03/2018  11:40 AM    <DIR>          Cisco Packet Tracer 7.0\r\n',
 b'12/24/2018  12:20 AM    <DIR>          Contacts\r\n',
 b'05/20/2019  04:14 PM                83 csv.txt\r\n',
 b'05/20/2019  04:53 PM               142 data.json.txt\r\n',
 b'05/23/2019  08:56 PM    <DIR>          Desktop\r\n',
 b'05/20/2019  04:39 PM             4,473 dir.txt\r\n',
 b'05/26/2019  08:37 PM    <DIR>          Documents\r\n',
 b'05/23/2019  07:15 PM    <DIR>          Downloads\r\n',
 b'11/29/2018  04:31 PM    <DIR>          eclipse-workspace\r\n',
 b'05/20/2019  04:38 PM                22 error.txt\r\n',
 b'05/20/2019  02:30 PM            20,018 ex 05.ipynb\r\n',
 b'05/23/2019  02:52 PM            19,486 ex 08.ipynb\r\n',
 b'05/23/2019  04:22 PM             7,665 ex 09.ipynb\r\n',
 b'12/24/2018  12:20 AM    <DIR>          Favorites\r\n',
 b'05/12/2019  10:27 AM             1,386 file example.ipynb\r\n',
 b'05/12/2019  02:12 PM               462 green eggs and ham.txt\r\n',
 b'05/20/2019  04:16 PM               384 green.txt\r\n',
 b'05/12/2016  07:08 PM    <DIR>          Intel\r\n',
 b'05/12/2019  10:23 AM            22,688 lesson 01 - exploring python 12.5.19.ipynb\r\n',
 b'05/20/2019  04:54 PM            12,285 lesson 07 - files.ipynb\r\n',
 b'05/23/2019  12:05 PM            12,203 lesson 08 - nested functions.ipynb\r\n',
 b'05/23/2019  04:58 PM            12,328 lesson 08 - veriadic funcs.ipynb\r\n',
 b'05/23/2019  04:59 PM             4,401 lesson 08 -lambda.ipynb\r\n',
 b'05/23/2019  04:47 PM             4,165 lesson 09 - lazy lists generators.ipynb\r\n',
 b'05/23/2019  04:07 PM             2,668 lesson 09 - list comprehension order.ipynb\r\n',
 b'05/23/2019  04:39 PM             2,104 lesson 09 - template for list comprehension.ipynb\r\n',
 b'12/24/2018  12:21 AM    <DIR>          Links\r\n',
 b'12/24/2018  12:20 AM    <DIR>          Music\r\n',
 b'05/30/2019  11:23 AM               540 myfirstmodule.py\r\n',
 b'05/30/2019  10:50 AM                74 myfirstmodule.txt\r\n',
 b'11/22/2018  02:03 PM                 0 New Text Document.txt\r\n',
 b'03/15/2017  02:42 PM    <DIR>          node_modules\r\n',
 b'05/20/2019  04:38 PM                23 normal.txt\r\n',
 b'05/23/2019  01:35 PM    <DIR>          OneDrive\r\n',
 b'12/24/2018  12:20 AM    <DIR>          Pictures\r\n',
 b'05/30/2019  09:58 AM    <DIR>          PycharmProjects\r\n',
 b'12/24/2018  12:21 AM    <DIR>          Saved Games\r\n',
 b'12/24/2018  12:20 AM    <DIR>          Searches\r\n',
 b'06/24/2018  01:41 PM    <DIR>          source\r\n',
 b'05/20/2019  04:37 PM               109 streams.py\r\n',
 b'05/23/2019  09:43 AM                 7 test.json\r\n',
 b'05/12/2019  11:13 AM                36 test.py\r\n',
 b'05/12/2019  02:26 PM             1,974 test.xml\r\n',
 b'05/23/2019  11:41 AM                51 testfunc.py\r\n',
 b'05/12/2019  12:16 PM            17,835 Untitled.ipynb\r\n',
 b'05/12/2019  01:32 PM             7,730 Untitled1.ipynb\r\n',
 b'05/20/2019  11:50 AM             6,324 Untitled10.ipynb\r\n',
 b'05/20/2019  12:06 PM             1,873 Untitled11.ipynb\r\n',
 b'05/20/2019  01:51 PM            20,857 Untitled12.ipynb\r\n',
 b'05/20/2019  02:40 PM             8,299 Untitled13.ipynb\r\n',
 b'05/20/2019  02:47 PM             2,999 Untitled14.ipynb\r\n',
 b'05/20/2019  02:57 PM             2,553 Untitled15.ipynb\r\n',
 b'05/20/2019  03:59 PM             1,371 Untitled16.ipynb\r\n',
 b'05/20/2019  04:19 PM             1,875 Untitled17.ipynb\r\n',
 b'05/23/2019  09:56 AM            19,385 Untitled18.ipynb\r\n',
 b'05/23/2019  04:53 PM            19,017 Untitled19.ipynb\r\n',
 b'05/12/2019  02:10 PM             6,781 Untitled2.ipynb\r\n',
 b'05/30/2019  09:49 AM             4,486 Untitled20.ipynb\r\n',
 b'05/23/2019  01:44 PM             2,780 Untitled21.ipynb\r\n',
 b'05/23/2019  02:02 PM               669 Untitled22.ipynb\r\n',
 b'05/30/2019  10:00 AM             2,763 Untitled23.ipynb\r\n',
 b'05/30/2019  10:16 AM             2,729 Untitled24.ipynb\r\n',
 b'05/30/2019  10:35 AM             5,035 Untitled25.ipynb\r\n',
 b'05/30/2019  10:49 AM            37,403 Untitled26.ipynb\r\n',
 b'05/30/2019  11:24 AM            20,264 Untitled27.ipynb\r\n',
 b'05/30/2019  11:58 AM            10,260 Untitled28.ipynb\r\n',
 b'05/30/2019  12:04 PM             3,068 Untitled29.ipynb\r\n',
 b'05/12/2019  02:16 PM             1,961 Untitled3.ipynb\r\n',
 b'05/30/2019  12:25 PM            10,265 Untitled30.ipynb\r\n',
 b'05/30/2019  02:03 PM            21,511 Untitled31.ipynb\r\n',
 b'05/30/2019  02:20 PM            11,261 Untitled32.ipynb\r\n',
 b'05/12/2019  02:37 PM            15,257 Untitled4.ipynb\r\n',
 b'05/12/2019  03:00 PM             9,291 Untitled5.ipynb\r\n',
 b'05/12/2019  04:01 PM            14,554 Untitled6.ipynb\r\n',
 b'05/12/2019  04:54 PM             6,235 Untitled7.ipynb\r\n',
 b'05/20/2019  09:54 AM             5,756 Untitled8.ipynb\r\n',
 b'05/20/2019  10:14 AM            11,148 Untitled9.ipynb\r\n',
 b'12/24/2018  12:20 AM    <DIR>          Videos\r\n',
 b'03/01/2016  08:13 AM    <DIR>          workspace\r\n',
 b'05/30/2019  11:23 AM    <DIR>          __pycache__\r\n',
 b'              64 File(s)        443,885 bytes\r\n',
 b'              47 Dir(s)  162,530,553,856 bytes free\r\n']
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
import multiprocessing


```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
help(multiprocessing)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Help on package multiprocessing:

NAME
    multiprocessing

DESCRIPTION
    # Package analogous to 'threading.py' but using processes
    #
    # multiprocessing/__init__.py
    #
    # This package is intended to duplicate the functionality (and much of
    # the API) of threading.py but uses processes instead of threads.  A
    # subpackage 'multiprocessing.dummy' has the same API but is a simple
    # wrapper for 'threading'.
    #
    # Copyright (c) 2006-2008, R Oudkerk
    # Licensed to PSF under a Contributor Agreement.
    #

PACKAGE CONTENTS
    connection
    context
    dummy (package)
    forkserver
    heap
    managers
    pool
    popen_fork
    popen_forkserver
    popen_spawn_posix
    popen_spawn_win32
    process
    queues
    reduction
    resource_sharer
    semaphore_tracker
    sharedctypes
    spawn
    synchronize
    util

SUBMODULES
    reducer

CLASSES
    builtins.Exception(builtins.BaseException)
        multiprocessing.context.ProcessError
            multiprocessing.context.AuthenticationError
            multiprocessing.context.BufferTooShort
            multiprocessing.context.TimeoutError
    multiprocessing.process.BaseProcess(builtins.object)
        multiprocessing.context.Process
    
    class AuthenticationError(ProcessError)
     |  Common base class for all non-exit exceptions.
     |  
     |  Method resolution order:
     |      AuthenticationError
     |      ProcessError
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |  
     |  Data descriptors inherited from ProcessError:
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.Exception:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from builtins.BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class BufferTooShort(ProcessError)
     |  Common base class for all non-exit exceptions.
     |  
     |  Method resolution order:
     |      BufferTooShort
     |      ProcessError
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |  
     |  Data descriptors inherited from ProcessError:
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.Exception:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from builtins.BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class Process(multiprocessing.process.BaseProcess)
     |  Process objects represent activity that is run in a separate process
     |  
     |  The class is analogous to `threading.Thread`
     |  
     |  Method resolution order:
     |      Process
     |      multiprocessing.process.BaseProcess
     |      builtins.object
     |  
     |  Methods inherited from multiprocessing.process.BaseProcess:
     |  
     |  __init__(self, group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __repr__(self)
     |      Return repr(self).
     |  
     |  is_alive(self)
     |      Return whether process is alive
     |  
     |  join(self, timeout=None)
     |      Wait until child process terminates
     |  
     |  run(self)
     |      Method to be run in sub-process; can be overridden in sub-class
     |  
     |  start(self)
     |      Start child process
     |  
     |  terminate(self)
     |      Terminate process; sends SIGTERM signal or uses TerminateProcess()
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from multiprocessing.process.BaseProcess:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  authkey
     |  
     |  daemon
     |      Return whether process is a daemon
     |  
     |  exitcode
     |      Return exit code of process or `None` if it has yet to stop
     |  
     |  ident
     |      Return identifier (PID) of process or `None` if it has yet to start
     |  
     |  name
     |  
     |  pid
     |      Return identifier (PID) of process or `None` if it has yet to start
     |  
     |  sentinel
     |      Return a file descriptor (Unix) or handle (Windows) suitable for
     |      waiting for process termination.
    
    class ProcessError(builtins.Exception)
     |  Common base class for all non-exit exceptions.
     |  
     |  Method resolution order:
     |      ProcessError
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |  
     |  Data descriptors defined here:
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.Exception:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from builtins.BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class TimeoutError(ProcessError)
     |  Common base class for all non-exit exceptions.
     |  
     |  Method resolution order:
     |      TimeoutError
     |      ProcessError
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |  
     |  Data descriptors inherited from ProcessError:
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.Exception:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from builtins.BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args

FUNCTIONS
    Array(typecode_or_type, size_or_initializer, *, lock=True) method of multiprocessing.context.DefaultContext instance
        Returns a synchronized shared array
    
    Barrier(parties, action=None, timeout=None) method of multiprocessing.context.DefaultContext instance
        Returns a barrier object
    
    BoundedSemaphore(value=1) method of multiprocessing.context.DefaultContext instance
        Returns a bounded semaphore object
    
    Condition(lock=None) method of multiprocessing.context.DefaultContext instance
        Returns a condition object
    
    Event() method of multiprocessing.context.DefaultContext instance
        Returns an event object
    
    JoinableQueue(maxsize=0) method of multiprocessing.context.DefaultContext instance
        Returns a queue object
    
    Lock() method of multiprocessing.context.DefaultContext instance
        Returns a non-recursive lock object
    
    Manager() method of multiprocessing.context.DefaultContext instance
        Returns a manager associated with a running server process
        
        The managers methods such as `Lock()`, `Condition()` and `Queue()`
        can be used to create shared objects.
    
    Pipe(duplex=True) method of multiprocessing.context.DefaultContext instance
        Returns two connection object connected by a pipe
    
    Pool(processes=None, initializer=None, initargs=(), maxtasksperchild=None) method of multiprocessing.context.DefaultContext instance
        Returns a process pool object
    
    Queue(maxsize=0) method of multiprocessing.context.DefaultContext instance
        Returns a queue object
    
    RLock() method of multiprocessing.context.DefaultContext instance
        Returns a recursive lock object
    
    RawArray(typecode_or_type, size_or_initializer) method of multiprocessing.context.DefaultContext instance
        Returns a shared array
    
    RawValue(typecode_or_type, *args) method of multiprocessing.context.DefaultContext instance
        Returns a shared object
    
    Semaphore(value=1) method of multiprocessing.context.DefaultContext instance
        Returns a semaphore object
    
    SimpleQueue() method of multiprocessing.context.DefaultContext instance
        Returns a queue object
    
    Value(typecode_or_type, *args, lock=True) method of multiprocessing.context.DefaultContext instance
        Returns a synchronized shared object
    
    active_children()
        Return list of process objects corresponding to live child processes
    
    allow_connection_pickling() method of multiprocessing.context.DefaultContext instance
        Install support for sending connections and sockets
        between processes
    
    cpu_count() method of multiprocessing.context.DefaultContext instance
        Returns the number of CPUs in the system
    
    current_process()
        Return process object representing the current process
    
    freeze_support() method of multiprocessing.context.DefaultContext instance
        Check whether this is a fake forked process in a frozen executable.
        If so then run code specified by commandline and exit.
    
    get_all_start_methods() method of multiprocessing.context.DefaultContext instance
    
    get_context(method=None) method of multiprocessing.context.DefaultContext instance
    
    get_logger() method of multiprocessing.context.DefaultContext instance
        Return package logger -- if it does not already exist then
        it is created.
    
    get_start_method(allow_none=False) method of multiprocessing.context.DefaultContext instance
    
    log_to_stderr(level=None) method of multiprocessing.context.DefaultContext instance
        Turn on logging and add a handler which prints to stderr
    
    set_executable(executable) method of multiprocessing.context.DefaultContext instance
        Sets the path to a python.exe or pythonw.exe binary used to run
        child processes instead of sys.executable when using the 'spawn'
        start method.  Useful for people embedding Python.
    
    set_forkserver_preload(module_names) method of multiprocessing.context.DefaultContext instance
        Set list of module names to try to load in forkserver process.
        This is really just a hint.
    
    set_start_method(method, force=False) method of multiprocessing.context.DefaultContext instance

DATA
    __all__ = ['Array', 'AuthenticationError', 'Barrier', 'BoundedSemaphor...

FILE
    c:\python36\lib\multiprocessing\__init__.py


```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
multiprocessing.Queue

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
<bound method BaseContext.Queue of <multiprocessing.context.DefaultContext object at 0x00000204DB93EF98>>
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
q = multiprocessing.Queue()

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
q.

```
</div>

</div>


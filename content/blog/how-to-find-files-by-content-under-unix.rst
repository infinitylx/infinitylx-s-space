How To Find Files by Content Under Unix
=======================================

:date: 2011-12-18 13:10
:tags: howto, rtfm, linux
:category: blog
:author: Wladislaw Merezhko
:lang: en

Q. I had written lots of code in C for my school work and saved it as
source code under /home/user/c/\*.c and \*.h. How do I find files by
content such as string or words (function name such as main() under UNIX
shell prompt?

A. You need to use following tools:

[a] grep command : print lines matching a pattern.

[b] find command: search for files in a directory hierarchy.

grep command to find files by content
.....................................

Type the command as follows:

::

    grep 'string' *.txt
    grep 'main(' *.c
    grep '#include<example.h>' *.c
    grep 'getChar*' *.c
    grep -i 'ultra' *.conf
    grep -iR 'ultra' *.conf

Where:
    
-i:
    Ignore case distinctions in both the PATTERN (match valid, VALID, ValID string) and the input files (math file.c FILE.c FILE.C filename);
    
-R:
    Read all files under each directory, recursively.

Highlighting searched patterns
..............................

You can highlight patterns easily while searching large number of files:

::

    $ grep --color=auto -iR 'getChar();' *.c

Displaying file names and line number for searched patterns

You may also need to display filenames and numbers:
::

    $ grep --color=auto -iRnH 'getChar();' *.c

Where,
    -n : Prefix each line of output with the 1-based line number within
its input file.
    -H Print the file name for each match. This is the default when
there is more than one file to search.

::

    $grep --color=auto -nH 'DIR' *

You can also use find command:

::

    $ find . -name "*.c" -print | xargs grep "main("


`Permalink`_

.. _Permalink: http://blog.infinitylx.org.ua/how-to-find-files-by-content-under-unix
.. _Leave a comment  »: http://blog.infinitylx.org.ua/how-to-find-files-by-content-under-unix#comment

# Notes



Need a "new" script -- creates a new object and opens in editor
Need a "query" script or query view -- this gets the reference needed for specific object
Need like some sort of tag querying and tag management


Every object needs an associated json meta file, or there needs to be a singular
index file?



So also I might be getting too bogged down with specific in-file stuff, but
really I should start with just entire files and being able to connect them to
eachother.



If I ever want to reference something in a specific file, maybe it automatically
breaks it into new object? Need to figure out how to reference specific part of
a file


Need a good tag query and creation system

Maybe meta data shouldn't ever be in the file itself at all?


How to deal with different object types? (some might be code, some might be
markdown, some might be latex, etc.)

Want to have different object types within same "hyper document" too, like a
notebook


WHEN CREATING NEW NOTE, need to have extra window with help about common
syntax/etc.

it is posible to have multiple syntax highlights at once:
https://www.vim.org/scripts/script.php?script_id=4168


## Usecases

### Making collection of related resources that I'm finding all at once

Similar to referencing a pdf or website, but automatically grab from a given
list

### Referencing a pdf or website

Specify some targt and it automatically moves into store or scrapes. Then make
it easy to add a description of it and do tagging

### Code snippet

Quickly record a useful code snippet:
should have the snippet as well as accompanying information and maybe resources
or informaiton source

Tags to indicate the language and potential use cases?

accompanying information should be a "description of", need some way to indicate
that named connection. Description especially is probably going to be common

How would a title in the connecting hyperdocument relate?


ex:

raw:

---------------------------------------------
# TQDM is a very useful python library

Extremely simple progress bar for any iterable

```python
from tqdm import tqdm
for thing in tqdm(some_iterable_thing):
	# ...
```

For iterating rows in a dataframe:
```python
for index, row in tqdm(df.iterrows(), total=df.shape[0]):
	# ...
```
---------------------------------------------

note that in some cases I may want multiple samples shown side by side
Should also be a shortcut to copy a snippet to clipboard?

---------------------------------------------
# TQDM is a very useful python library

:::utility
```python
from tqdm import tqdm
for thing in tqdm(some_iterable_thing):
	# ...
```
Extremely simple progress bar for any iterable



:::ds,keywords:pandas|dataframe|
```python
For iterating rows in a dataframe:
for index, row in tqdm(df.iterrows(), total=df.shape[0]):
	# ...
```
For iterating rows in a dataframe

---------------------------------------------

A title or section header is an additional piece of text that applies to all sub
things

NOTE: this approach doesn't handle dividing up sections nicely though. Unless we
also divide by section automatically


Maybe just rely on code blocks to indicate break out things? (or as one method
of doing so)

3 empty lines can indicate the end of a description. Alternatively, if the last
line is the ::: meta line(s), then that can indicate the end as well

```file
testing/test
```
This is a description



:::use:tools,project:thing,remind(3 days)
```link
www.google.com
```
This is a link description



note that rendering code snippets into markdown would be easy, just expand and
add the three backticks with language name




So the useful things pertaining specifically to code snippets:
* Very easy to add new snippets and brief descriptions and tags
* Reference them in documentation or collection documents (may want a live
  markdown viewer in terminal or something as writing)
* Create snippets for vim from them (maybe)
* Export to a github of useful snippets
* Ability to quickly find snippets when needed for reference



## Syntax

Going to have to have a special syntax to handle kofi specific things. Use yaml
at top?

When you first create something it goes in the cache


the three equals indicate the end of the object:

=====
[[[uuid]]] -- link to specific object
{{{uuid}}} -- embed specific object
{{{query=somequery}}} -- embed results of a query
=====

can use :: at beginning of lines for something

-----
[meta information]
-----

surrounding by 
{
}
means to create a new object (and replace with embedding)

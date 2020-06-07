# Notes


Everything based off of a single "root", anything here is a
top-level/highest-level thing


## Potential libraries
* urwid
* ueberzug

* gutentags for vim

* neovim-remote



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





A big thing will be hyper documents and having them able to act as "worktrees".
E.g. I can have a work tree for a particular project. And all of my projects.
Etc. (You can have the tree (or network) that you care about in a pane of the
window)
Similarly, a common use case might be to be writing something while having a
reference hyperdocument open at the same time

An important thing will be to be able to embed with specific "views" (e.g.
kanban) NOTE: will need syntax for that


Some common "things"/relationships:
* description
* scratch notes
* summary


It may be nice to, after creating scratch notes, to have a peli-pal-like
interface to be able to move around and organize them. (even in creating
something like this, that would be handy)


Be like leo, where you can insert buttons that attach to python scripts and
things!


Would be useful to have an auto-render/preview functionality


the viewer interface is going to be a big deal


----
are tags just based on what "trees" a thing is in? (need to not call it that,
since they're not necessarily trees) hypertree? Does this make sense?
So really, every object is the intersection of all its hypertrees, but it also
needs an ordering within each hypertree? NO. NO ORDERING.


...but so, does every random python snippet get added to a "python" hypertree?
That's not useful or organized. Also too restrictive to require a hyperdocument?

I might want to see "snippets" > "python", but also "python" > "snippets"
(fixing this might involve that querying idea again) Auto adding to some
hypertrees might be useful to avoid having to manually select every single tree
I want it in.

Also, what if I duplicate a hyperdocument view, and just change how it's viewed?
Do I really make another "tag" for that?

What if something is a resource, but only matters for a particular project? Do I
really want to pollute "resources" with stuff in my "some project" > "resources"?
- I think this can be solved by allowing you to do either. You can add to
  "someproject">"resources" and/or "resources"


So I don't think "querying" is necessary, just when a new thing is created and
needs to be added to another tree, it auto inserts an embedding or reference in
that other tree. (based on some rules that could be defined somewhere in that
tree? e.g. in some sections it might just a list of links, in others it might be
a list of links with a description)

Noooo, but wait, what if I want to add it both to "snippets" and "snippets" >
"python"? 

I think there just need to be rules, so whenever something gets made, it might
auto be added to some trees, you might explicitly add it to others (which might
further trigger additional rules) etc. And this is fine. Maybe in terms of
display we just prioritize root names and leaf names of hypertrees it's in?

----


There can also be arbitrary properties/fields, but should have an interface to
help determine if existing properties/fields on other objects might be
applicable



Have a separate interface that once you create a thing/snippets, you go back
through and with shortcuts can quickly add the correct tags/add it to the
correct trees


So everything needs to have some sort of a display type

Properties of an object:
* ID
* Date created
* Date updated
* Default display mode
* Keywords <---- eehhhh, this is dangerous, shouldn't this be tags then?
* Name/title
* Type (markdown,link,pdf,etc?)
* Edits (count)
* Description
* Connections-from (this is essentially where the tags/hypertrees come in)
* Connections-to
	^ to capture side-connections, this may just need to be typed connections
	"parents","children", etc. in a single connections property

NOTE: the above --- thing still does not account for sideways connections. If I
summarize one or multiple objects, need a way to handle that. It's a typed/named
connection
$$$$$$$$ CURRENT CONSIDERATION $$$$$$$$$$$
(though this is sort of like a bunch of text followed by a bunch of links to
what it was summarizing...but this isn't doesn't correctly capture the
relationship, because the sumarizee shouldn't be in the "tree" or a child of the
summary, it's an updated/cleaned/restated sideways connection
other than summarizations, what are other sideways connections/non-parent or
child connections? Explicitly drawing similarities? Attaching a script or button
or other? Really even a description could be a sideways connection (if we did
this, we would _not_ want propagation [e.g. if we have a display that pulls in
descriptions, we don't want that description object to be explicitly connected
to. So maybe some objects can "propagate" and others can't?])
Could also have random thoughts about something that I want to attach that
aren't formal summaries

Ability to add "cleaned nodes" which are nodes for publication/display?


WHAT ABOUT IMAGES?



"display mode" is really like choosing a "renderer"
So it can be rendered as straight markdown, or as a kanban (where each list is a
section of the board and each item is a card)



I really think I may want to focus on using vim _only as the immediate editor_.
Almost everything else takes place in the visual editor part. So have a joplin
like setup, where there's two panes, and doing stuff in the one just sends
commands to the neovim window to edit that particular object. 

the problem is that there should still be a way to export for external editing
and then an import that pulls it back. Something that inserts special syntax
that can then be read back in. Maybe doesn't need all the meta data, it just
needs the object ID, or something similar. So export isn't a "render" per say,
but something similar. 

So, to be clear, you can make it so you can edit more than one object at a time,
but it's better for just straight editing the text, rather than manipulating all
the meta stuff as well.



I do think a hypergraph is accurate to describe all of this


have ability to split left vim pane into multiple so can edit multiple objects
at once



ability to "fork" currently 'active' hypergraph/workspace

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





## 2020.6.5 

All reference management should be done with a .bib

https://pypi.org/project/pybib/

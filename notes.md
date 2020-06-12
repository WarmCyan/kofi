will need to use $data_dir

in vim, ctrl+shift+l will insert description as well

NOTE: all new notes will automatically be linked to "inbox" until manually
organized out? (until backlinked to something else?) (we should have special
syntax for a backlink) pandoc supports {} for attributes after links, so we
could put in a class for "backlink" or something similar (maybe styled to be
a lot smaller/out of the way). Inbox could also be
the "entry point" note, which contains both unlinked things as well as recent
workspaces, etc.



syntax to create new is
<!--< [insert the title you want]() -->
<!--/-->

<!-- <insert the title you want|2020123.md> -->
<!-- description (only if the link that was expanded had the description next to
it) --> Honestly actually no, if you're expanding a note, it's almost certainly
on a line by itself and could use the description anyway
<!-- </insert the title you want|2020123.md> --> any changes to title made here
should be ignored

NOTE: it's a thing to run `:echo expand('<cfile>')` and that expansion will give
you the filename under the cursor


de-expansion could be done by calling a script with all of the content and the
line number of the cursor? (then python could figure it out) [if no line no
given, just de-expand all]


need a thing to handle on-save of a file in vim?:
* apply changes to any expanded files
* create any new expanded files
* render (if this is implemented yet)
* refresh link titles
* update date-updated

is expansion/collapsing handled by vim or external script? Since expansion has
to handle nesting, probably easier if it's handled by a python script. (also
easy to replace current line in vim)



if graph should be rendered image, image could be stored in place gitignored


TODO: Still have nothing for searches, still have nothing for reference
management, also need inbox and workspace management

where should all these vim settings stuff go? I don't want to apply to all
markdown files. Separate locally sourced (in zettelkasten folder) vimrc?



```
Hint: If you would like to do something else than setting an option, you could
define an autocommand that checks the file for a specific string.  For
example:
	au BufReadPost * if getline(1) =~ "VAR" | call SetVar() | endif
And define a function SetVar() that does something with the line containing
"VAR".
```


Sooo check every file for opening <!-- KOFI -->

inbox class parses current inbox to find all links in each section


python packages:
* pyflute



IMPORTANT:
We need a way to be able to mark/keep track of a collection, maybe easier than
ws by itself. Like have an active note and a shortcut to auto add to that
note?

Also, it would sure be nice if links between things in the same page would link
to eachother instead of other pages

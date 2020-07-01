
# Kofi Tools Documentation
## `kofi-active-dir`

Prints out the directory of the currently active zettelkasten.

**Output:** single line containing directory  

**Examples:**
```bash
pushd $(kofi-active-dir) > /dev/null
# ...
popd > /dev/null
```

```
$ kofi-active-dir
/home/dwl/tmp/testzettel
```
## `kofi-background-process-write`

Any longer-running background tasks that should run on file write go here (to avoid editor delay.)

* Updates recent notes
* Updates inbox
* Runs any output script
* Renders given file
* Reloads qutebrowser

**Arguments:**
1. filename of the file that was just changed

**Examples:**
```bash
nohup kofi-background-process-write $filename &
```
## `kofi-check-backlink`

Searches given file to see if a (specifically) backlink exists to the other given file.

**Arguments:**
1. The file to check if there's a backlink _to_.
2. The file to check if there's a backlink _from_.

**Output:** `backlink exists` if there is a backlink from arg2 to arg1, `no backlink` if not.

**Examples:**
```
$ kofi-check-backlink $current_file $destination_file
no backlink
```
## `kofi-clean-public`


## `kofi-create-backlink`

Creates a backlink from arg2 to arg1 if one does not already exist.

**Arguments:**
1. The file to make a backlink _to_.
2. The file to make a backlink _from_.

**Output:** `backlink created` if successfully created a backlink from arg2 to arg1, `backlink exists` if already a backlink.

**Examples:**
```
$ kofi-create-backlink $current_file $destination_file
backlink created
```
## `kofi-create-expanded`

Takes any new note expansion syntax, creates the new notes, and replaces syntax in original file.

**Arguments:**
1. The filename to check for new expansions.

**Examples:**
```
$ kofi-create-expanded $current_file
```
## `kofi-create-map`

Collects the set of notes and links from a given root node and outputs the graphviz dot representation of the collection.

**Arguments:**
1. The filename of the note to use as the "root" node of the graph.

**Output:**
Prints out the graphviz dot syntax notation.

**Examples:**
```
$ kofi-create-map $current_file
strict digraph G
{
"filename.md"[ label="title" URL="filename.html" ];
...
}
```
## `kofi-create-note`


## `kofi-create-recent`


## `kofi-datetimestamp`


## `kofi-fold-expansion`


## `kofi-get-expansion`


## `kofi-get-link`


## `kofi-get-property`

Checks and returns the requested boolean metadata from a file.

**Arguments:**
1. the boolean property to check
2. filename of the file

**Output:**
Either `true` if `$2: True` is in the file, or `false`"

**Examples:**
```bash
$ kofi-get-property "hidden" $current_file 
true
```

```python
import sys
import util
filename = sys.argv[1]
if util.run_shell("kofi-get-property", "public", filename) == "true":
# do things
```
## `kofi-get-title`


## `kofi-init`


## `kofi-log`


## `kofi-log-pipe`


## `kofi-ls`


## `kofi-new-note`


## `kofi-open`


## `kofi-output-map`


## `kofi-process-write`


## `kofi-propagate-expanded`


## `kofi-refresh-expansions`


## `kofi-refresh-includes`


## `kofi-refresh-links`


## `kofi-render`


## `kofi-render-map`


## `kofi-render-public`


## `kofi-render-sync-down`


## `kofi-render-sync-up`


## `kofi-run-script`


## `kofi-search-edit`


## `kofi-serve`


## `kofi-set`


## `kofi-set-date`


## `kofi-set-meta`


## `kofi-set-public`


## `kofi-set-recent`


## `kofi-start`


## `kofi-sync`


## `kofi-update-inbox`


## `kofi-wrap-expansions`

Finds all expansion syntaxes and wraps them in a specially classed div for styling. This creates a cached copy rather than altering original file. The class used will be ".expansion"

**Arguments:**
1. The filename of the note to fix
2. The filename to save the fixed copy to

**Examples:**
```
$ kofi-wrap-expansions $somenote cache/$somenote
```
## `kofi-write-note-content`



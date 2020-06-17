
# Kofi Tools Documentation
## `active-dir`

Prints out the directory of the currently active zettelkasten

Output: single line containing directory  

Examples:
```bash
pushd $(kofi active-dir) > /dev/null
# ...
popd > /dev/null
```

```
$ kofi active-dir
/home/dwl/tmp/testzettel
```
## `background-process-write`

Any longer-running background tasks that should run on file write go here (to avoid editor delay.)

* Updates recent notes
* Updates inbox
* Runs any output script
* Renders given file
* Reloads qutebrowser

Arguments:
1. filename of the file that was just changed

Examples:
```bash
nohup background-process-write $filename &
```
## `check-backlink`


## `create-backlink`


## `create-expanded`


## `create-map`


## `create-note`


## `create-recent`


## `datetimestamp`


## `fold-expansion`


## `get-expansion`


## `get-hidden`


## `get-link`


## `get-title`


## `kofi-init`


## `kofi-ls`


## `kofi-set`


## `kofi-sync`


## `log`


## `log-pipe`


## `new-note`


## `open`


## `output-map`


## `process-write`


## `propagate-expanded`


## `refresh-expansions`


## `refresh-includes`


## `refresh-links`


## `render`


## `render-map`


## `run-script`


## `search-edit`


## `serve`


## `set-date`


## `set-meta`


## `set-recent`


## `update-inbox`


## `write-note-content`



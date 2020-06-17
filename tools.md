
# Kofi Tools Documentation
## `kn`


## `kofi`


## `kofi-active-dir`

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
## `kofi-background-process-write`

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
## `kofi-check-backlink`


## `kofi-create-backlink`


## `kofi-create-expanded`


## `kofi-create-map`


## `kofi-create-note`


## `kofi-create-recent`


## `kofi-datetimestamp`


## `kofi-fold-expansion`


## `kofi-get-expansion`


## `kofi-get-hidden`


## `kofi-get-link`


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


## `kofi-run-script`


## `kofi-search-edit`


## `kofi-serve`


## `kofi-set`


## `kofi-set-date`


## `kofi-set-meta`


## `kofi-set-recent`


## `kofi-start`


## `kofi-sync`


## `kofi-update-inbox`


## `kofi-write-note-content`


## `kse`



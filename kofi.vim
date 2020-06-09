if exists("loaded_kofi")
	finish
endif
let g:loaded_kofi=1

function! KofiGetLink(lines)
	let filename = a:lines[0][0:match(a:lines[0], ':')-1]
	echo filename
	let fulllink = system("get-link " . filename)
	return fulllink
endfunction

inoremap <expr> <C-l> fzf#vim#complete(fzf#wrap({
			\ 'prefix': expand("<cword>"),
			\ 'source': 'rg ^ --line-number --glob "*.md"',
			\ 'options': '',
			\ 'reducer': { lines -> KofiGetLink(lines) }}))


nnoremap <leader>n i<!-- <lt><Bar>> --><cr><cr><!-- <lt>/> --><esc>kk0f<Bar>i

" NOTE: below get-expansion could also get filename under cursor with expand("<cfile>")
" though this isn't as good since you can't run from beginning of line
nmap <c-e> V:'<,'>!get-expansion<cr>
nmap <c-d> :silent exec "!fold-expansion " . expand('%:t') . " " . line('.')<cr>:edit<cr>

autocmd BufWritePost *.md :silent exec "!process-write " . expand('%:t') | :edit

function KofiMakeBacklink()
	let dest_file = expand("<cfile>")
	let cur_file = expand("%:t")
	let result = system("create-backlink " . cur_file  . " " . dest_file)[:-2]
	if result == "backlink created"
		echo "backlink created"
		execute ":vsplit " . dest_file
		execute "normal! gg/" . cur_file . "\<cr>"
		nohlsearch
	else
		echo "backlink exists"
	endif
endfunction

nmap <c-m> :call KofiMakeBacklink()<cr>
nmap <c-q> :echo system("check-backlink " . expand("%:t") . " " . expand("<cfile>"))[:-2]<cr>


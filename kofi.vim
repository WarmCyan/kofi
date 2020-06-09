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

nmap <c-e> V:'<,'>!get-expansion<cr>

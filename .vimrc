call plug#begin('~/.vim/plugged')

" Status line
Plug 'vim-airline/vim-airline'
"Plug 'itchyny/lightline.vim'

" Themes
Plug 'ghifarit53/tokyonight-vim'
"Plug 'catppuccin/vim', { 'as': 'catppuccin' }

call plug#end()

" Themes
" ------
set termguicolors
set noshowmode

" Tokyo Night theme
let g:tokyonight_style = 'night'
let g:tokyonight_enable_italic = 0

colorscheme tokyonight
let g:airline_theme = "tokyonight"

"colorscheme catppuccin_mocha

" Lightline
"set laststatus=2
"set noshowmode
" let g:lightline = {'colorscheme': 'catppuccin_mocha'}


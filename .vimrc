call plug#begin('~/.vim/plugged')

" Status line
Plug 'vim-airline/vim-airline'

" Themes
Plug 'ghifarit53/tokyonight-vim'

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


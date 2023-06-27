# Use powerline
USE_POWERLINE="true"
# Source manjaro-zsh-configuration
if [[ -e /usr/share/zsh/manjaro-zsh-config ]]; then
  source /usr/share/zsh/manjaro-zsh-config
fi
# Use manjaro zsh prompt
if [[ -e /usr/share/zsh/manjaro-zsh-prompt ]]; then
  source /usr/share/zsh/manjaro-zsh-prompt
fi

HISTSIZE=10000
SAVEHIST=10000

# Virtualenvwrapper
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/Development
source /usr/bin/virtualenvwrapper.sh

# Zoxide
eval "$(zoxide init zsh)"

# fzf
export FZF_CTRL_T_OPTS="--preview \"bat --style=numbers --color=always --line-range :500 {}\""
source /usr/share/fzf/key-bindings.zsh
source /usr/share/fzf/completion.zsh

##########
# Aliases #
###########

alias ls="exa -lah --git --icons"
alias cd="z"
alias ..='cd ..'
alias ...='cd ../..'
alias ....='cd ../../..'
alias mkdir='mkdir -pv'
alias youtube-dl='yt-dlp'

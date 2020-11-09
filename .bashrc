export BASH_SILENCE_DEPRECATION_WARNING=1
# Don't put duplicate lines or lines starting with space in the hystory
HISTCONTROL=ignoreboth
HISTSIZE=1000
HISTFILESIZE=2000

# Append to the hystory file, don't overwrite it
shopt -s histappend

# Update the values of LINES and COLUMNS
shopt -s checkwinsize

PS1="\342\224\214($(if [[ ${EUID} == 0 ]]; then echo '\[\033[01;31m\]👑⚡\h⚡👑'; else echo '\[\033[01;36m\]\u 🍩 \h'; fi)\[\033[1;37m\])\342\224\200(\w)\342\224\200(\[\033[1;33m\]\$(ls -1 | wc -l | sed 's: ::g') files\[\033[1;37m\])\342\224\200(\[\033[1;35m\]\$(ls -1a | grep -e '^\..*' | wc -l | sed 's: ::g') dot files\[\033[1;37m\])\342\224\200($(if [[ $? -ne 0 ]]; then echo '\[\033[1;31m\]'; else echo '\[\033[1;32m\]'; fi)$?\[\033[1;37m\])\n\342\224\224\342\206\222🍩"

alias ls="ls -FG"
alias ll="ls -laFG"
alias grep="grep --color=auto"
alias ..="cd .."
alias ttyc="tty-clock -c -C 4"
alias bpy="bpytop"

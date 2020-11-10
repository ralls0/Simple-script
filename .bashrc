# ____       _ _
#|  _ \ __ _| | |___  ___
#| |_) / _` | | / __|/ _ \
#|  _ < (_| | | \__ \ (_) |
#|_| \_\__,_|_|_|___/\___/
#

### EXPORT
export TERM="xterm-256color"              # getting proper colors
export HISTCONTROL=ignoredups:erasedups   # no duplicate entries
export BASH_SILENCE_DEPRECATION_WARNING=1 # 

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

### PROMPT
PS1="\342\224\214($(if [[ ${EUID} == 0 ]]; then echo '\[\033[01;31m\]👑⚡\h⚡👑'; else echo '\[\033[01;36m\]\u 🍩 \h'; fi)\[\033[1;37m\])\342\224\200(\w)\342\224\200(\[\033[1;33m\]\$(ls -1 | wc -l | sed 's: ::g') files\[\033[1;37m\])\342\224\200(\[\033[1;35m\]\$(ls -1a | grep -e '^\..*' | wc -l | sed 's: ::g') dot files\[\033[1;37m\])\342\224\200($(if [[ $? -ne 0 ]]; then echo '\[\033[1;31m\]'; else echo '\[\033[1;32m\]'; fi)$?\[\033[1;37m\])\n\342\224\224\342\206\222🍩"

### PATH
if [ -d "$HOME/.bin" ] ;
  then PATH="$HOME/.bin:$PATH"
fi

if [ -d "$HOME/.local/bin" ] ;
  then PATH="$HOME/.local/bin:$PATH"
fi

### SHOPT
shopt -s autocd         # change to named directory
shopt -s cdspell        # autocorrects cd misspellings
shopt -s cmdhist        # save multi-line commands in history as single line
shopt -s dotglob
shopt -s histappend     # do not overwrite history
shopt -s expand_aliases # expand aliases
shopt -s checkwinsize   # checks term size when bash regains control

#ignore upper and lowercase when TAB completion
bind "set completion-ignore-case on"

### ARCHIVE EXTRACTION
# usage: ex <file>
ex ()
{
  if [ -f $1 ] ; then
    case $1 in
      *.tar.bz2)   tar xjf $1   ;;
      *.tar.gz)    tar xzf $1   ;;
      *.bz2)       bunzip2 $1   ;;
      *.rar)       unrar x $1   ;;
      *.gz)        gunzip $1    ;;
      *.tar)       tar xf $1    ;;
      *.tbz2)      tar xjf $1   ;;
      *.tgz)       tar xzf $1   ;;
      *.zip)       unzip $1     ;;
      *.Z)         uncompress $1;;
      *.7z)        7z x $1      ;;
      *.deb)       ar x $1      ;;
      *.tar.xz)    tar xf $1    ;;
      *.tar.zst)   unzstd $1    ;;      
      *)           echo "'$1' cannot be extracted via ex()" ;;
    esac
  else
    echo "'$1' is not a valid file"
  fi
}

### ALIAS
# Colorize grep output
alias grep='grep --color=auto'
alias egrep='egrep --color=auto'
alias fgrep='fgrep --color=auto'

# confirm before overwriting something
alias cp="cp -i"
alias mv='mv -i'
alias rm='rm -i'

# adding flags
alias df='df -h'                          # human-readable sizes
alias free='free -m'                      # show sizes in MB

# the terminal rickroll
alias rr='curl -s -L https://raw.githubusercontent.com/keroserene/rickrollrc/master/roll.sh | bash'

alias ls="ls -FG"
alias ll="ls -laFG"
alias ..="cd .."
alias ttyc="tty-clock -s -x -c -C 4"
alias bpy="bpytop"

# clear
# [ $[$RANDOM % 10] = 0 ] && timeout 4 cmatrix || clear 

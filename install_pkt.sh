#!/bin/bash

if [ $# -lt 2 ];
then
	echo -e "[!] Numero insufficiente di parametri!\n[?]\t$0 [gestore pacchetti] [install] [update] [upgrade] [show]\n"
	exit 1
fi

install_cmd="$1 $2"
update_cmd="$1 $3"
upgrade_cmd="$1 $4"
show_cmd="$1 $5"

# Update
echo -e "[*] Eseguo l'update\n"
sudo $update_cmd

# Upgrade
echo "[?] Desideri eseguire l'upgrade [y/N] "
read response

if [ $response = 'y' -o $response = 'Y' -o $response = 's' -o $response = 'S' ];
then
	echo -e "[*] Eseguo l'upgrade\n"
	sudo $upgrade_cmd
fi

# Base Software
sudo $install_cmd curl
sudo $install_cmd git
sudo $install_cmd vim
v=$($show_cmd python3 | head -2 | tail -1 | cut -d ' ' -f 2 | cut -d '-' -f 1)
sudo $install_cmd python=$v*
sudo $install_cmd python3-pip

# Extra Software
sudo $install_cmd htop 
sudo $install_cmd tty-clock 
sudo $install_cmd bpytop
sudo $install_cmd asciiquarium
sudo $install_cmd sl
sudo $install_cmd broot 	# broot --sizes
sudo $install_cmd cmatrix
sudo $install_cmd lolcat
sudo $install_cmd figlet 
# sudo $install_cmd ponysay


exit 0

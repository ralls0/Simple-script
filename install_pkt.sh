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

# Create ~/.tmp/
mkdir ~/.tmp

# Create ~/.prove/
mkdir ~/.prove

# Create ~/.fonts/
mkdir ~/.fonts

# Create ~/.git-clone/
mkdir ~/.git-clone

# Add repository
sudo add-apt-repository ppa:ytvwld/asciiquarium

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
sudo $install_cmd cmake
sudo $install_cmd git gitk git-gui git-flow
sudo $install_cmd vim
sudo $install_cmd rar unrar zip unzip
v=$($show_cmd python3 | head -2 | tail -1 | cut -d ' ' -f 2 | cut -d '-' -f 1)
sudo $install_cmd python=$v*
sudo $install_cmd python3-pip
sudo $install_cmd python3-dev
sudo $install_cmd rofi
sudo $install_cmd polybar
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# Update 
echo -e "[*] Eseguo l'update\n"
sudo $update_cmd

# Extra Software
sudo $install_cmd htop 
sudo $install_cmd tty-clock 
# sudo $install_cmd bpytop
python3 -m pip install psutil
git clone https://github.com/aristocratos/bpytop.git ~/.git-clone/
(cd ~/.git-clone/bpytop; sudo make install)
sudo $install_cmd libcurses-perl
sudo $install_cmd asciiquarium
sudo $install_cmd sl
# sudo $install_cmd broot 	# broot --sizes
git clone https://github.com/Canop/broot.git ~/.git-clone/
(cd ~/.git-clone/broot; cargo install --path .)
sudo $install_cmd ranger
sudo $install_cmd cmatrix
sudo $install_cmd lolcat
sudo $install_cmd figlet 
# sudo $install_cmd ponysay

# Fonts
sudo $install_cmd fonts-font-awesome
sudo $install_cmd fonts-roboto

# Visual Studio Code
curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
sudo install -o root -g root -m 644 packages.microsoft.gpg /usr/share/keyrings/
sudo sh -c 'echo "deb [arch=amd64 signed-by=/usr/share/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/vscode stable main" > /etc/apt/sources.list.d/vscode.list'

# Spotify
curl -sS https://download.spotify.com/debian/pubkey.gpg | sudo apt-key add - 
echo "deb http://repository.spotify.com stable non-free" | sudo tee /etc/apt/sources.list.d/spotify.list

exit 0

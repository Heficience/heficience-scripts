user_path=$(echo $HOME)
install_path=$user_path/.autocompletion

sudo rm -f /usr/bin/autocompletion # remove the link in /usr/bin
rm -rf $install_path/ # remove the autocompletion folder

echo "Autocompletion uninstalled successfully"
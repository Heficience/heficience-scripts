
#!/bin/bash

mkdir -p "$HOME/.icons/"
mkdir -p "$HOME/Applications/"
mkdir -p "$HOME/.local/share/applications/"

wget "https://github.com/Heficience/Heficience-menu/raw/4.20/Images/Heficience_Icone.svg" -O "$HOME/.icons/heficience-menu.svg"
wget "https://github.com/Heficience/Heficience-menu/releases/download/4.20/Linux-Heficience-Menu-4.20-x86_64.AppImage" 
mv "./Linux-Heficience-Menu-4.20-x86_64.AppImage" "$HOME/Applications/Heficience-Menu-x86_64.AppImage"

chmod +x "$HOME/Applications/Heficience-Menu-x86_64.AppImage"

cat << FIN > "$HOME/.local/share/applications/heficience-munu.desktop"
[Desktop Entry]
Comment[fr_FR]=
Comment=
Exec=$HOME/Applications/Heficience-Menu-x86_64.AppImage
GenericName[fr_FR]=Utilisation facile d'un PC
GenericName=Easy use of a PC
Icon=$HOME/.icons/heficience-menu.svg
MimeType=
Name[fr_FR]=Heficience-Menu
Name=Heficience-Menu
Path=$HOME
Categories=Utility;
StartupNotify=true
Terminal=false
TerminalOptions=
Type=Application
X-DBUS-ServiceName=
X-DBUS-StartupType=
X-KDE-SubstituteUID=false
X-KDE-Username=
FIN

echo "Heficience-Menu installed correctly"

#!/bin/bash

ICON="$HOME/.icons/heficience-menu.svg"
APPPIMAGE="$HOME/Applications/Heficience-Menu-x86_64.AppImage"
APPDESKTOP="$HOME/.local/share/applications/heficience-munu.desktop"

test -f "$ICON" && rm "$ICON"

test -f "$APPPIMAGE" && rm "$APPPIMAGE"

test -f "$APPDESKTOP" && rm "$APPDESKTOP"

if [ -z "$(ls -A $HOME/Applications)" ]; then
   rmdir "$HOME/Applications"
fi

echo "Heficience-Menu uninstalled correctly"

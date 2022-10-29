#!/bin/bash
us=$(logname)
cd /home/$us
(
    echo "#リポジトリの複製"
    echo "リポジトリの複製"
    #git clone https://github.com/PEANUT-Sh/store.git
) | zenity --progress --title="あ" --text="あ"
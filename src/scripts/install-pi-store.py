import tkinter as tk
import tkinter.messagebox as msg
import subprocess as lcmd

question = msg.askyesno('確認-pi-store', 'Pi-storeをインストールしますか?')
#反応の分岐
if (question == True):
    lcmd.run(['wget', '-qO-', 'https://raw.githubusercontent.com/PEANUT-Sh/store/main/src/scripts/install-pi-store.sh', '|', 'bash'])

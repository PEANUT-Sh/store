import tkinter as tk
import tkinter.messagebox as msg
import subprocess as lcmd

question = msg.askyesno('確認-pi-store', 'Pi-storeをインストールしますか?')
#反応の分岐
if (response == True):
    lcmd.run([''])

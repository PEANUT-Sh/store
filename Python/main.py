import tkinter as tk
base = tk.Tk()
base.title("Pi-store home")
base.configure(bg="white")

game = tk.Button(base, text='ゲーム', background='white', cursor='hand2')
programming = tk.Button(base, text='プログラミング', background='white', cursor='hand2')
game.pack()
programming.pack()


base.mainloop()
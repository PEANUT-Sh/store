import tkinter as tk
base = tk.Tk()
base.title("Pi-store home")
base.configure(bg="white")

icon = tk.PhotoImage(file="Python/images/ICON.png")

canvas = tk.Canvas(bg="white", width=699, height=410)
canvas.place(x=0, y=0)
canvas.create_image(0, 0, image=icon, anchor=tk.NW)

game = tk.Button(base, text='ゲーム', background='white', cursor='hand2')
programming = tk.Button(base, text='プログラミング', background='white', cursor='hand2')
accessory = tk.Button(base, text='アクセサリ', background='white', cursor='hand2')
game.grid()
programming.grid()
accessory.grid()


base.mainloop()
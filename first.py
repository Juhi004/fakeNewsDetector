import tkinter as tk
import tkinter.scrolledtext as tkst


def change():
    global count
    global result
    if count == 0:
        count = 1
        result.config(text=verdict2,
                      fg='red')
        result.update()
    elif count == 1:
        count = 0
        result.config(text=verdict1,
                      fg='green')
        result.update()


root = tk.Tk()
root.title('Fake News Detector')
explanation = """Enter the article to be tested below"""

w = tk.Label(root,
             padx=120,
             pady=10,
             text=explanation,
             font='Times 12',
             fg='blue').pack()
verdict1 = """The article is Genuine"""
verdict2 = """The article is Fake"""
count = 0
scroll = tkst.ScrolledText(root, width=45, height=15, padx=5, pady=10).pack()
button = tk.Button(root, text='Check', width=25, command=change).pack()
result = tk.Label(root,
                 text=verdict1,
                 font='Times 16 bold',
                 fg='green')
result.pack()


root.mainloop()
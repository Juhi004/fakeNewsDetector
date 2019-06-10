import tkinter as tk
from tkinter import ttk
import tkinter.scrolledtext as tkst
from prediction import detecting_fake_news

LARGE_FONT = ("Verdana", 12)
SMALL_FONT = ("Verdana", 10)


class ShowGui(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        # tk.Tk.iconbitmap(self, default="something.ico")    ....This command is used to change the icon

        tk.Tk.wm_title(self, "Fake News Detection")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, TrainingPage, TestingPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Welcome!", font=LARGE_FONT)
        label.pack(pady=50, padx=50)
        button1 = ttk.Button(self, text="Train the Algorithm",
                             command=lambda: controller.show_frame(TrainingPage))
        button1.pack()
        space = tk.Label(self, width=10)
        space.pack()
        button2 = ttk.Button(self, text="Test the Algorithm",
                             command=lambda: controller.show_frame(TestingPage))
        button2.pack()


class TrainingPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Training Algorithm", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        label2 = tk.Label(self, text="Enter the path of the file for training", font=SMALL_FONT)
        label2.pack(pady=10, padx=10)
        entry = tk.Entry(self, width=50)
        entry.pack()
        space = tk.Label(self, width=10)
        space.pack()
        button = ttk.Button(self, text="Train")
        button.pack()
        space = tk.Label(self, width=10)
        space.pack()
        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()


class TestingPage(tk.Frame):

    @staticmethod
    def put_text(var, result1, result2):
        print(var)
        pg = detecting_fake_news(var)
        print(pg.verdict)
        print(pg.prob)
        result1.config(text=pg.verdict)
        result2.config(text="Truth Probability Score: " + str(pg.prob))

    @staticmethod
    def clear_it(result1, result2):
        result1.config(text="")
        result2.config(text="")

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, padx=150, text="Testing Algorithm", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        result1 = tk.Label(font=LARGE_FONT,
                           fg='green')
        result2 = tk.Label(pady=5,
                           font=SMALL_FONT)

        scroll = tkst.ScrolledText(self, width=45, height=15, padx=5, pady=10)
        button = ttk.Button(self,
                            text='Check', width=25,
                            command=lambda: self.put_text(scroll.get('1.0', 'end-1c'), result1, result2))

        scroll.pack()
        button.pack()
        space = tk.Label(self, width=10)
        space.pack()
        clear = ttk.Button(self,
                           text="Clear",
                           command=lambda: self.clear_it(result1, result2))
        clear.pack()

        result1.pack()
        result2.pack()
        space = tk.Label(self, width=10)
        space.pack()
        button1 = ttk.Button(self,
                             text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()


app = ShowGui()
app.mainloop()

'''
remove verdict after pressing 'Go back to home'
and that also in respective colour according to the result
'''



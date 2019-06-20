# GUI of the model
import tkinter as tk
from tkinter import ttk
import tkinter.scrolledtext as tkst
from conversion import convert_speaker, convert_statement, convert_topic
from NBtwo import predict, confusion_mtarix, create_model
from data_processing import encode_data
import preprocessing

LARGE_FONT = ("Verdana", 12)
SMALL_FONT = ("Verdana", 10)


class ShowGui(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        # tk.Tk.iconbitmap(self, default="something.ico")    ....Command for changing the icon

        tk.Tk.wm_title(self, "Fake News Detector")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, TrainingPage, PerformancePage, TestingPage):
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
        button2 = ttk.Button(self, text="Performance of Algorithm",
                             command=lambda: controller.show_frame(PerformancePage))
        button2.pack()
        space = tk.Label(self, width=10)
        space.pack()
        button3 = ttk.Button(self, text="Test the Algorithm",
                             command=lambda: controller.show_frame(TestingPage))
        button3.pack()


class TrainingPage(tk.Frame):

    def onHeartBeat(self):
        self.config(cursor="wait")
        self.update()
        print("Sending heartbeats")

    def onTrain(self, var1, var2):
        if not self.isBusy:
            self.isBusy = True
            encode_data(self, var1, var2)
            self.isBusy = False
            self.config(cursor="")

    def onBackToHome(self):
        if not self.isBusy:
            self.controller.show_frame(StartPage)

    def __init__(self, parent, controller):
        self.isBusy = False
        self.controller = controller
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Training Algorithm", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        label2 = tk.Label(self, text="Enter the path of train dataset", font=SMALL_FONT)
        label2.pack(pady=10, padx=10)
        entry1 = tk.Entry(self, width=50)
        entry1.pack()
        space = tk.Label(self, width=10)
        space.pack()
        label3 = tk.Label(self, text="Enter the path of test dataset", font=SMALL_FONT)
        label3.pack(pady=10, padx=10)
        entry2 = tk.Entry(self, width=50)
        entry2.pack()
        space = tk.Label(self, width=10)
        space.pack()
        button = ttk.Button(self, text="Train",
                            command=lambda: self.onTrain(entry1.get(), entry2.get()))
        button.pack()
        space = tk.Label(self, width=10)
        space.pack()
        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: self.onBackToHome())
        button1.pack()


class PerformancePage(tk.Frame):

    def show_performance(self):
        confusion_matrix = confusion_mtarix()
        print(confusion_matrix)
        self.matrix.config(text="Confusion Matrix:")
        self.matrix.update()
        self.values1.config(text=str(confusion_matrix[0][0]) + "  " + str(confusion_matrix[0][1]))
        self.values1.update()
        self.values2.config(text=str(confusion_matrix[1][0]) + "  " + str(confusion_matrix[1][1]))
        self.values2.update()
        total = confusion_matrix[0][0] + confusion_matrix[0][1] + confusion_matrix[1][0] + confusion_matrix[1][1]
        precision = confusion_matrix[1][1] / (confusion_matrix[0][1] + confusion_matrix[1][1])
        accuracy = (confusion_matrix[1][1] + confusion_matrix[0][0]) / total
        sensitivity = confusion_matrix[1][1] / (confusion_matrix[1][0] + confusion_matrix[1][1])
        prevalance = (confusion_matrix[1][0] + confusion_matrix[1][1]) / total
        specificity = confusion_matrix[0][0] / (confusion_matrix[0][0] + confusion_matrix[0][1])
        mis_rate = (confusion_matrix[0][1] + confusion_matrix[1][0]) / total
        self.l1.config(text="Precision- " + str(precision))
        self.l1.update()
        self.l2.config(text="Accuracy- " + str(accuracy))
        self.l2.update()
        self.l3.config(text="Sensitivity- " + str(sensitivity))
        self.l3.update()
        self.l4.config(text="Prevalance- " + str(prevalance))
        self.l4.update()
        self.l5.config(text="Specificity- " + str(specificity))
        self.l5.update()
        self.l6.config(text="Miscalculation Rate- " + str(mis_rate))
        self.l6.update()

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Performance of Algorithm", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        space = tk.Label(self, width=10)
        space.pack()
        button = ttk.Button(self, text="Show Performance",
                            command=lambda: self.show_performance())
        button.pack()
        space = tk.Label(self, width=10)
        space.pack()
        self.matrix = tk.Label(self)
        self.matrix.pack(pady=10, padx=10)
        self.values1 = tk.Label(self)
        self.values1.pack()
        self.values2 = tk.Label(self)
        self.values2.pack(pady=10, padx=10)
        self.l1 = tk.Label(self)
        self.l1.pack()
        self.l2 = tk.Label(self)
        self.l2.pack()
        self.l3 = tk.Label(self)
        self.l3.pack()
        self.l4 = tk.Label(self)
        self.l4.pack()
        self.l5 = tk.Label(self)
        self.l5.pack()
        self.l6 = tk.Label(self)
        self.l6.pack()
        space = tk.Label(self, width=10)
        space.pack()
        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()


class TestingPage(tk.Frame):

    @staticmethod
    def put_text(var1, var2, var3, result1):
        print(var1)
        print(var2)
        print(var3)
        st = convert_statement(var1)
        top = convert_topic(var2)
        spek = convert_speaker(var3)
        ans = predict(st, top, spek)
        if ans == [0]:
            res = "False"
            result1.config(text=res,fg='red', font=LARGE_FONT)
            result1.update()
        else:
            res = "True"
            result1.config(text=res, fg='green', font=LARGE_FONT)
            result1.update()
        print(ans)

    def clear_it(self):
        self.result1.config(text="")
        self.entry1.delete(0, 'end')
        self.entry2.delete(0, 'end')
        self.scroll.delete(1.0, 'end')

    def onBackToHome(self, controller):
        self.clear_it()
        controller.show_frame(StartPage)

    def __init__(self, parent, controller):
        create_model()
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, padx=150, text="Testing Algorithm", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        label1 = tk.Label(self, text="Statement")
        label2 = tk.Label(self, text="Topic")
        label3 = tk.Label(self, text="Speaker")

        self.entry1 = tk.Entry(self, width=45)
        self.entry2 = tk.Entry(self, width=45)

        self.result1 = tk.Label(font=LARGE_FONT, width=20)

        self.scroll = tkst.ScrolledText(self, width=45, height=15, padx=5, pady=10)
        button = ttk.Button(self,
                            text='Check', width=25,
                            command=lambda: self.put_text(self.scroll.get('1.0', 'end-1c'),self.entry1.get(),self.entry2.get(),self.result1))

        label1.pack()
        self.scroll.pack()
        label2.pack()
        self.entry1.pack()
        label3.pack()
        self.entry2.pack()
        space = tk.Label(self, width=10)
        space.pack()
        button.pack()
        space = tk.Label(self, width=10)
        space.pack()
        clear = ttk.Button(self,
                           text="Clear",
                           command=lambda: self.clear_it())
        clear.pack()

        self.result1.pack()
        space = tk.Label(self, width=10)
        space.pack()
        button1 = ttk.Button(self,
                             text="Back to Home",
                             command=lambda: self.onBackToHome(controller))
        button1.pack(side='right')
        space = tk.Label(self, width=10)
        space.pack()


app = ShowGui()
app.mainloop()

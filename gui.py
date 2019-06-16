# GUI of the model
import tkinter as tk
from tkinter import ttk
import tkinter.scrolledtext as tkst
# from prediction import detecting_fake_news
from conversion import convert_speaker, convert_statement, convert_topic
from NBtwo import predict, confusion_mtarix
from data_processing import encode_data

LARGE_FONT = ("Verdana", 12)
SMALL_FONT = ("Verdana", 10)

print("starting of gui code")


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

    def onTrain(self):
        if not self.isBusy :
            self.isBusy = True
            encode_data(self)
            self.isBusy = False
            self.config(cursor="")

    def onBackToHome(self):
        if not self.isBusy :
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
                            command=lambda: self.onTrain())
        button.pack()
        space = tk.Label(self, width=10)
        space.pack()
        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: self.onBackToHome())
        button1.pack()
        train_path = entry1.get()
        print("oo " + str(train_path))
        test_path = entry1.get()
        print("oo "+ str(test_path))
        # send these paths to data_processing and start encoding process


class PerformancePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Performance of Algorithm", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        confusion_matrix = confusion_mtarix()
        # row1 = confusion_matrix[0][1]
        print(confusion_matrix)
        matrix = tk.Label(self, text="Confusion Matrix:")
        matrix.pack(pady=10, padx=10)
        values1 = tk.Label(self, text=str(confusion_matrix[0][0])+"  "+str(confusion_matrix[0][1]))
        values1.pack()
        values2 = tk.Label(self, text=str(confusion_matrix[1][0]) + "  " + str(confusion_matrix[1][1]))
        values2.pack(pady=10, padx=10)
        total = confusion_matrix[0][0]+confusion_matrix[0][1]+confusion_matrix[1][0]+confusion_matrix[1][1]
        precision = confusion_matrix[1][1]/(confusion_matrix[0][1]+confusion_matrix[1][1])
        accuracy = (confusion_matrix[1][1]+confusion_matrix[0][0])/total
        sensitivity = confusion_matrix[1][1]/(confusion_matrix[1][0]+confusion_matrix[1][1])
        prevalance = (confusion_matrix[1][0]+confusion_matrix[1][1])/total
        specificity = confusion_matrix[0][0]/(confusion_matrix[0][0]+confusion_matrix[0][1])
        mis_rate = (confusion_matrix[0][1]+confusion_matrix[1][0])/total
        l1 = tk.Label(self, text="Precision- "+str(precision)).pack()
        l1 = tk.Label(self, text="Accuracy- "+str(accuracy)).pack()
        l1 = tk.Label(self, text="Sensitivity- "+str(sensitivity)).pack()
        l1 = tk.Label(self, text="Prevalance- "+str(prevalance)).pack()
        l1 = tk.Label(self, text="Specificity- "+str(specificity)).pack()
        l1 = tk.Label(self, text="Miscalculation Rate- "+str(mis_rate)).pack()
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


    @staticmethod
    def clear_it(result1):
        result1.config(text="")

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, padx=150, text="Testing Algorithm", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        label1 = tk.Label(self, text="Statement")
        label2 = tk.Label(self, text="Topic")
        label3 = tk.Label(self, text="Speaker")

        entry1 = tk.Entry(self, width=45)
        entry2 = tk.Entry(self, width=45)

        result1 = tk.Label(font=LARGE_FONT, width=20)

        scroll = tkst.ScrolledText(self, width=45, height=15, padx=5, pady=10)
        button = ttk.Button(self,
                            text='Check', width=25,
                            command=lambda: self.put_text(scroll.get('1.0', 'end-1c'),entry1.get(),entry2.get(),result1))

        label1.pack()
        scroll.pack()
        label2.pack()
        entry1.pack()
        label3.pack()
        entry2.pack()
        space = tk.Label(self, width=10)
        space.pack()
        button.pack()
        space = tk.Label(self, width=10)
        space.pack()
        clear = ttk.Button(self,
                           text="Clear",
                           command=lambda: self.clear_it(result1))
        clear.pack()

        result1.pack()
        space = tk.Label(self, width=10)
        space.pack()
        button1 = ttk.Button(self,
                             text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack(side='right')
        space = tk.Label(self, width=10)
        space.pack()


app = ShowGui()
app.mainloop()

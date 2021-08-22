from tkinter import *
from tkinter import ttk
from tkinter import filedialog


class Window(Tk):
    def __init__(self):
        super(Window, self).__init__()

        self.title("Dialog Widget")
        self.minsize(500, 400)
        self.wm_iconbitmap("myicon.ico")

        self.label_frame = ttk.LabelFrame(self, text="Open A File")
        self.label_frame.grid(column=0, row=1, padx=20, pady=20)

        self.create_button()

    def create_button(self):
        button = ttk.Button(self.label_frame,
                            text="Browse A File", command=self.fileDialog)
        button.grid(column=1, row=1)

    def fileDialog(self):
        file_name = filedialog.askopenfilename(initialdir="/",
                                               title="Select A File", filetype=(("jpeg", "*.jpg"),
                                                                                ("All Files", "*.*")))
        label = ttk.Label(self.label_frame, text="")
        label.grid(column=1, row=2)
        label.configure(text=file_name)


window = Window()
window.mainloop()
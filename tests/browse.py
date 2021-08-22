# from tkinter import *
# from tkinter import filedialog
#
# base = Tk()
# # Create a canvas
# base.geometry('150x150')
#
#
# # Function for opening the file
# def file_opener():
#     inputFile = filedialog.askopenfile(initialdir="/")
#     print(inputFile)
#     print(inputFile.name)
#     label = Label(base, text=inputFile.name).pack()
#     t
#     for i in inputFile:
#         print(i)
#
#
# # Button label
# x = Button(base, text='Select a .txt/.csv file', command=lambda: file_opener()).pack()
#
# mainloop()

from tkinter import *
from tkinter import filedialog

fileNames = []

def openFile():
    tf = filedialog.askopenfilenames(
        initialdir="C:/Users/MainFrame/Desktop/",
        title="Open Text file",
        filetypes=(("Text Files", "*.xml"),)
    )
    pathh.insert(END, tf)
    for f in tf:
        tf = open(f)  # or tf = open(tf, 'r')
        fileNames.append(tf.name)
        # data = tf.read()
        data = tf.name
        txtarea.insert(END, data)
        tf.close()

    print(fileNames)


ws = Tk()
ws.title("PythonGuides")
ws.geometry("400x450")
ws['bg'] = '#fb0'

txtarea = Text(ws, width=40, height=20)
txtarea.pack(pady=20)

pathh = Entry(ws)
# pathh.pack(side=LEFT, expand=True, fill=X, padx=20)


Button(
    ws,
    text="Open File",
    command=openFile
).pack(side=RIGHT, expand=True, fill=X, padx=20)

ws.mainloop()

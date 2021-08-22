from tkinter import *
from tkinter import filedialog

ws = Tk()
ws.title("Revenue Analyzer")
ws.geometry("1024x768")
ws['bg'] = '#fb0'

txtarea = Text(ws, width=40, height=20)
txtarea.pack(pady=20)
# pathh = Entry(ws)

def openFile():
    tf = filedialog.askopenfilename(
        initialdir="C:/Users/MainFrame/Desktop/",
        title="Open Text file",
        filetypes=(("Text Files", "*.txt"),)
    )
    # pathh.insert(END, tf)
    tf = open(tf)  # or tf = open(tf, 'r')
    data = tf.name
    # data = tf.read()
    txtarea.insert(END, data)
    tf.close()


Button(
    ws,
    text="Open File",
    command=openFile
).pack(side=RIGHT, expand=False, fill=X, padx=20)

ws.mainloop()

# def openFile():
#     tf = filedialog.askopenfilename(
#         initialdir="C:/Users/MainFrame/Desktop/",
#         title="Open Text file",
#         filetypes=(("Text Files", "*.txt"),)
#     )
#     pathh.insert(END, tf)
#     tf = open(tf)  # or tf = open(tf, 'r')
#     data = tf.read()
#     txtarea.insert(END, data)
#     tf.close()
#
#
# ws = Tk()
# ws.title("PythonGuides")
# ws.geometry("400x450")
# ws['bg'] = '#fb0'

# txtarea = Text(ws, width=40, height=20)
# txtarea.pack(pady=20)
#
# pathh = Entry(ws)
#
# Button(
#     ws,
#     text="Open File",
#     command=openFile
# ).pack(side=RIGHT, expand=True, fill=X, padx=20)

# ws.mainloop()

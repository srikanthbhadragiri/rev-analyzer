# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import tkinter
import pandas as pd
import xml.etree.ElementTree as ET
from pandastable import Table

# tree = ET.parse('xml/movies.xml')
# root = tree.getroot()
#
#
# def iter_movie(movie):
#     for mov in root.iter('movie'):
#         mov_dict = mov.attrib.copy()
#         print(type(mov_dict), mov_dict)
#         mov_dict.update(mov.attrib)
#         for feature in mov:
#             mov_dict[feature.tag] = feature.text
#         print(mov_dict)
#         yield mov_dict
#
#
# mov_df = pd.DataFrame(list(iter_movie(root.iter('movie'))))
# print(mov_df)

# Export to excel
mov_df.to_excel(r'export_dataframe.xlsx', index=False, header=True)
window = tkinter.Tk()
# to rename the title of the window
window.title("My Project")
# # pack is used to show the object in the window
label = tkinter.Label(window, text="Welcome to DataCamp's Tutorial on Tkinter!").pack()
#
# # You will first create a division with the help of Frame class and align them on TOP and BOTTOM with pack() method.
top_frame = tkinter.Frame(window).pack()
bottom_frame = tkinter.Frame(window).pack(side="bottom")

pt = Table(bottom_frame)
pt.show()

# # Once the frames are created then you are all set to add widgets in both the frames.
# btn1 = tkinter.Button(top_frame, text="Button1",
#                       fg="red").pack()  # 'fg or foreground' is for coloring the contents (buttons)
# btn2 = tkinter.Button(top_frame, text="Button2", fg="green").pack()
# btn3 = tkinter.Button(bottom_frame, text="Button3", fg="purple").pack(
#     side="left")  # 'side' is used to left or right align the widgets
# btn4 = tkinter.Button(bottom_frame, text="Button4", fg="orange").pack(side="left")
# btn5 = tkinter.Button(bottom_frame, text="Button5", fg="red").pack(side="right")
window.mainloop()

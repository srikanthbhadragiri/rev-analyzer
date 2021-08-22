from tkinter import *
from pandastable import Table, TableModel
import pandas as pd
import xml.etree.ElementTree as ET

tree = ET.parse('../xml/MF1397_A001_2021-03-31_IS015009.xml')
root = tree.getroot()


def iter_movie(Claim):
    for mov in root.iter('Claim'):
        mov_dict = mov.attrib.copy()
        # print(type(mov_dict), mov_dict)
        mov_dict.update(mov.attrib)
        for feature in mov:
            mov_dict[feature.tag] = feature.text
        print(mov_dict)
        yield mov_dict


mov_df = pd.DataFrame(list(iter_movie(root.iter('Claim'))))
print(mov_df)


class TestApp(Frame):
    """Basic test frame for the table"""

    def __init__(self, parent=None):
        self.parent = parent
        Frame.__init__(self)
        self.main = self.master
        self.main.geometry('600x400+200+100')
        self.main.title('Table app')
        f = Frame(self.main)
        f.pack(fill=BOTH, expand=1)
        df = mov_df  # TableModel.getSampleData()
        self.table = pt = Table(f, dataframe=df,
                                showtoolbar=False, showstatusbar=False, editable=False)
        pt.show()
        return


app = TestApp()
# launch the app
app.mainloop()

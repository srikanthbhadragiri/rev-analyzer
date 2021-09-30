from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkcalendar import Calendar
import cls.ClsDBConn as db
import cls.ClsProcessFiles as pf


class RevAnalyzer:
    _xmlFileNames = []

    def __init__(self, root):
        root.title('Revenue Analyzer')
        root.resizable(False, False)
        root.configure(background='#e1d8b9')
        root.geometry("1024x768")

        self.tabControl = ttk.Notebook(root)
        self.adminTab = ttk.Frame(self.tabControl)
        self.reportTab = ttk.Frame(self.tabControl)

        self.tabControl.add(self.adminTab, text='Admin')
        self.tabControl.add(self.reportTab, text='Reports')
        self.tabControl.pack(expand=1, fill="both")

        self.adm_frame1 = ttk.Frame(self.adminTab)
        self.adm_frame1.pack()

        ttk.Label(self.adm_frame1, text="Welcome to Revenue Analyzer Admin module").grid(column=0, row=0, padx=10,
                                                                                         pady=10, columnspan=3)
        ttk.Button(self.adm_frame1, text="Create Database", command=self.createDBTables).grid(column=0, row=1,
                                                                                         padx=10, pady=10)
        ttk.Button(self.adm_frame1, text="Select Files", command=self.selectFiles).grid(column=1, row=1, padx=10, pady=10)
        ttk.Button(self.adm_frame1, text="Process Files", command=self.processFiles).grid(column=2, row=1, padx=10, pady=10)

        self.text_comments = Text(self.adm_frame1, width=70, height=30)
        self.text_comments.grid(row=3, column=0, columnspan=2, padx=5)


    def createDBTables(self):
        conn = db.DBConnection()
        if conn.verifyConnection():
            conn.createTables()

    def selectFiles(self):
        self._xmlFileNames.clear()
        tf = filedialog.askopenfilenames(
            initialdir="C:/Users/MainFrame/Desktop/",
            title="Open Text file",
            filetypes=(("Text Files", "*.xml"),)
        )
        for f in tf:
            tf = open(f)
            self._xmlFileNames.append(tf.name)
            data = tf.name[tf.name.rindex("/") + 1:]  # tf.name
            self.text_comments.insert(END, data)
            self.text_comments.insert(END, '\n')
            tf.close()

    def processFiles(self):
        pf.ProcessFiles.process(self, self._xmlFileNames)

    def getProcessedClaimIds(self, data):
        print("getProcessedClaimIds ---- ")
        clm_list = []
        for clm in data:
            # print(clm['claim']['ClaimID'])
            clm_list.append(clm['claim']['ClaimID'])
            clm_list.append(clm['claim']['ClaimID'])
        return clm_list

    def getClaimType(self, data):
        for clm in data:
            # print(clm['claim']['ClaimType'])
            return clm['claim']['ClaimType']


def main():
    root = Tk()
    analyzer = RevAnalyzer(root)
    root.mainloop()


if __name__ == "__main__":
    main()
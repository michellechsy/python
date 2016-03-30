import os
from Tkconstants import W, N, S, E, RIGHT, Y, END, SEL, INSERT
from Tkinter import Tk, Text, Menu, Scrollbar
from tkFileDialog import asksaveasfilename, askopenfile
from tkMessageBox import showinfo, askyesno


class Notepad:

    __root = Tk()

    #Default window width and height
    __thisWidth = 300
    __thisHeight = 300
    __thisTextArea = Text(__root)
    __thisMenuBar = Menu(__root)
    __thisFileMenu = Menu(__thisMenuBar, tearoff=0)
    __thisEditMenu = Menu(__thisMenuBar, tearoff=0)
    __thisHelpMenu = Menu(__thisMenuBar, tearoff=0)
    __thisScrollBar = Scrollbar(__thisTextArea)
    __file = None

    def __init__(self, **kwargs):
        # set window size
        try:
            self.__thisWidth = kwargs['width']
            self.__thisHeight = kwargs['height']
        except KeyError:
            pass

        self.__root.title("Untitled - Notepad")
        self.createWidget()
        self.configMenuWithEvents()

        self.__thisScrollBar.pack(side=RIGHT, fill=Y)
        self.__thisScrollBar.config(command=self.__thisTextArea.yview)
        self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set)
        self.__thisTextArea.edit_modified(False)


    def createWidget(self):

        # center the window
        screenWidth = self.__root.winfo_width()
        screenHeight = self.__root.winfo_height()

        left = (screenWidth / 2) - (self.__thisWidth / 2)
        top = (screenHeight / 2) - (self.__thisHeight / 2)

        self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth, self.__thisHeight, left, top))

        # make the textArea auto resizable
        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_columnconfigure(0, weight=1)

        self.__thisTextArea.grid(sticky=N + E + S + W)


    def configMenuWithEvents(self):
        # add controls (widget)

        self.__thisFileMenu.add_command(label="New", command=self.__newFile)
        self.__thisFileMenu.add_command(label="Open", command=self.__openFile)
        self.__thisFileMenu.add_command(label="Save", command=self.__saveFile)
        self.__thisFileMenu.add_command(label="Close", command=self.__closeFile)
        # self.__thisFileMenu.add_command(label="CloseAll", command=self.__closeAllFile)

        self.__thisFileMenu.add_separator()
        self.__thisFileMenu.add_command(label="Exit", command=self.__quitApplication)
        self.__thisMenuBar.add_cascade(label="File", menu=self.__thisFileMenu)

        self.__thisEditMenu.add_command(label="Cut", command=self.__cut)
        self.__thisEditMenu.add_command(label="Copy", command=self.__copy)
        self.__thisEditMenu.add_command(label="Paste", command=self.__paste)
        self.__thisEditMenu.add_command(label="Select All", command=self.__selectAll)
        self.__thisEditMenu.add_command(label="Clear All", command=self.__clearText)
        self.__thisMenuBar.add_cascade(label="Edit", menu=self.__thisEditMenu)

        self.__thisHelpMenu.add_command(label="About Notepad", command=self.__showAbout)
        self.__thisMenuBar.add_cascade(label="Help", menu=self.__thisHelpMenu)

        self.__thisTextArea.bind("<Control-Key-a>", self.__selectAll)
        self.__thisTextArea.bind("<Control-Key-A>", self.__selectAll)

        self.__root.config(menu=self.__thisMenuBar)


    def __quitApplication(self):
        self.__root.destroy()

    def __showAbout(self):
        showinfo("Notepad", "Created by: Michelle")

    def __openFile(self):
        # strange result: return a NoneType
        # self.__file == askopenfilename(parent=self.__root,
        #                                defaultextension='.txt',
        #                                filetypes=[
        #                                    ("All Files", "*.*"),
        #                                    ("Text Documents", "*.txt")
        #                                ])
        file = askopenfile(parent=self.__root, mode='rb', title='Select a file')
        self.__file = file.name

        if self.__file == "":
            self.__file = None

        else:
            print("opened file: " + self.__file)
            basename = os.path.basename(self.__file)
            self.__root.title(basename + " - Notepad")
            self.__thisTextArea.delete(1.0, END)

            # file = open(self.__file, "r")
            self.__thisTextArea.insert(1.0, file.read())
            self.__thisTextArea.focus()
            file.close()

    def __newFile(self):
        self.__root.title("Untitled - Notepad")
        self.__file = None
        self.__thisTextArea.delete(1.0, END)

    def __saveFile(self):
        if self.__file == None:
            self.__file = asksaveasfilename(initialfile='Untitled.txt',
                                            defaultextension=".txt",
                                            filetypes=[
                                                ("All Files", "*.*"),
                                                ("Text Documents", "*.txt")
                                            ])
            if self.__file == "":
                self.__file = None
            else:
                file = open(self.__file, "w")
                file.write(self.__thisTextArea.get(1.0, END))
                self.__thisTextArea.edit_modified(False)
                file.close()

                self.__root.title(os.path.basename(self.__file) + " - Notepad")
                return "saved"
        else:
            file = open(self.__file, "w")
            file.write(self.__thisTextArea.get(1.0, END))
            self.__thisTextArea.edit_modified(False)
            file.close()
            return "saved"


    def __cut(self):
        self.__thisTextArea.event_generate("<<Cut>>")

    def __copy(self):
        self.__thisTextArea.event_generate("<<Copy>>")

    def __paste(self):
        self.__thisTextArea.event_generate("<<Paste>>")

    def __selectAll(self, event=None):
        self.__thisTextArea.tag_add(SEL, "1.0", END)
        self.__thisTextArea.mark_set(INSERT, END)
        self.__thisTextArea.see(INSERT)
        return "break"

    def __clearText(self):
        self.__thisTextArea.delete(1.0, END)

    def __closeFile(self):
        if self.save_if_modified() != None:
            self.__newFile()


    def save_if_modified(self, event=None):
        if self.__thisTextArea.edit_modified():
            if askyesno(title="Save File", message="Do you want to save all the changes?"):
                saved = self.__saveFile()
                if saved == "saved":
                    return True
                else:
                    return None
                # self.__thisTextArea.edit_modified(False)
            else:
                return False

        else:  # not modified
            return True

    def run(self):
        # run main app
        self.__root.mainloop()

notepad = Notepad(width=600, height=400)
notepad.run()

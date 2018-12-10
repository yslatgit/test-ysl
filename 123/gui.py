from tkinter import *
from tkinter.scrolledtext import ScrolledText
def load():
    with open(filename.get()) as file:
        contents.delete('1.0', END)
        contents.insert(INSERT, file.read())
def save():
    with open(filename.get(), 'w') as file:
        file.write(contents.get('1.0', END))
top = Tk()
top.title("Simple Editor")
contents = ScrolledText()
contents.pack(side=LEFT)
contents.pack(side=BOTTOM,fill=BOTH)
filename = Entry()
filename.pack(side=LEFT, expand=True, fill=X)
Button(text='Open', command=load).pack(side=LEFT)
Button(text='Save', command=save).pack(side=RIGHT)
mainloop()
from tkinter import Tk, Label, Listbox, Text, Button, END
from tkinter import ttk
from main import todo

        
def _init_(self, root):
        self.root = root
        self.root.title("To-do-list")
        self.root.geometry("650410x300")
        self.root =Tk()
        self.label = Label(self.root, text="To-Do-List-App",
                        font="ariel, 25 bold", width=10, bd=5,
                        bg="purple", fg="black")
        self.label.pack(side="top", fill="both")

        self.label2 = Label(self.root, text="Add Task",
                         font="ariel,18 bold", width=10, bd=5,
                         bg="purple", fg="black")
        self.label2.place(x=40,y=54)

        self.label3 = Label(self.root, text="Tasks",
                         font="ariel,18 bold", width=10, bd=5,
                         bg="purple", fg="black")
        self.label3.place(x=320, y=54)

        self.main_text = Listbox(self.root, height=9, bd=5, width=23,
                             font="ariel,20 italic bold")
        self.main_text.place(x=200, y=100)

        self.text = Text(self.root, bd=5, height=2, width=30,
                     font="ariel,10 bold")
        self.text.place(x=20,y=120)

        self.button = Button(self.root, text="Add", font="sarif,20 bold italic",
                          width=10, bd=5, bg="purple", fg="black",
                          command=self.add)
        self.button.place(x=30, y=180)

        self.button2 = Button(self.root, text="delete", font="sarif,20 bold italic",
                          width=10, bd=5, bg="purple", fg="black",
                          command=self.delete)
        self.button2.place(x=30, y=200)

def add(self):
    content = self.text.get(1.0, END)
    self.main_text.insert(END, content)
    with open("data.txt", "a") as file:
        file.write(content)
    self.text.delete(1.0, END)

def delete(self):
    selection = self.main_text.curselection()
    if selection:
        delete_index = selection[0]
        look = self.main_text.get(delete_index)
        with open("data.txt", "r+") as f:
            new_f= f.readlines()
            f.seek(0)
            for line in new_f:
                if look not in line:
                    f.write(line)
            f.truncate()
        self.main_text.delete(delete_index)
        with open("data.txt", "r") as file:
            read = file.readlines()
            ready = [line.split() for line in read]
        self.main_text.delete(0, END)
        for r in ready:
            self.main_text.insert(END, r)
        file.close()
        
        
        
def main():
     root = Tk()
     ui = todo(root)
     root.mainloop()
                
        

if _name_ == "_main_":
        main()
from tkinter import *

window = Tk()
window.title("Tkinter Python")
window.minsize(width=500, height=500)
window.config(padx=20, pady=20)


#label
my_label = Label(text="Label")
my_label.config(bg="black")
my_label.config(fg="white")
my_label.config(padx=10, pady=10)
my_label.pack()


#button
def button_clicked():
    print("button clicked")
    print(my_text.get("1.0", END))  #1.0 -> 1 ->
    #-> -> line, 0 -> character

#Search: how to get text widget in tkinter

my_button = Button(text="button", command=button_clicked)
my_button.config(bg="red")
my_button.config(padx=10, pady=10)
my_button.pack()


#entry(singleline)
my_entry = Entry(width=20)
my_entry.focus()
my_entry.pack()


#text(multiline)
my_text = Text(width=40, height=20)
#my_text.focus()
my_text.pack()


#scale-a view for the user to select

def scale_selected(value):
    print(value)

my_scale = Scale(from_=0, to=100, command=scale_selected)
my_scale.pack()


#spinbox

def spinbox_selected():
    print(my_spinbox.get())

my_spinbox = Spinbox(from_=0, to=50, command=spinbox_selected)
my_spinbox.pack()


#checkbutton

def checkbutton_selected():
    print(check_state.get())

check_state = IntVar()
my_checkbutton = Checkbutton(text="check", variable=check_state, command=checkbutton_selected)
my_checkbutton.config(bg="light green")
my_checkbutton.pack()


#radio button

def radiobutton_selected():
    print(radio_state.get())

radio_state = IntVar()
my_radiobutton = Radiobutton(text="option 1", value=10, variable=radio_state, command=radiobutton_selected)
my_radiobutton2 = Radiobutton(text="option 2", value=20, variable=radio_state, command=radiobutton_selected)
my_radiobutton.pack()
my_radiobutton2.pack()


#listbox

def listbox_selected(event):
    print(my_listbox.get(my_listbox.curselection()))

my_listbox = Listbox()
name_list = ["Geralt", "Yeneffer", "Cirella", "Jaskier"]
for i in range(len(name_list)):
    my_listbox.insert(i, name_list[i])
my_listbox.bind("<<ListboxSelect>>", listbox_selected)
my_listbox.pack()

#Search: python tkinter listbox print selected items


window.mainloop()
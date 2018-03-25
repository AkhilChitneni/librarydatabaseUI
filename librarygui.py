from tkinter import *
import backend

window = Tk()
window.wm_title("Libray database")
window.configure(background="#a1dbcd")

def get_selected_row(event):
    global selected_tuple
    index=list1.curselection()[0]
    selected_tuple = list1.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0,END)
    e2.insert(END,selected_tuple[2])
    e3.delete(0,END)
    e3.insert(END,selected_tuple[3])
    e4.delete(0,END)
    e4.insert(END,selected_tuple[4])

def view_command():
    list1.delete(0,END)
    #list1.insert(END,"ID NAME SID BNAME BID")
    #list1.insert(END,"_____________________________________")
    for row in backend.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in backend.search(name_text.get(),id_text.get(),book_name.get(),book_id.get()):
         list1.insert(END,row)

def add_command():
    if (name_text.get()=="" or id_text.get()=="" or book_name.get()=="" or book_id.get()==""):
        variable.set("empty blanks are not allowed")
        l6.configure(fg='red')
    else:
        backend.insert(name_text.get(),id_text.get(),book_name.get(),book_id.get())
        variable.set("New Entry added succesfully")
        l6.configure(fg="green")
        list1.delete(0,END)
        list1.insert(END,(name_text.get(),id_text.get(),book_name.get(),book_id.get()))


def update_command():
    if (name_text.get()=="" or id_text.get()=="" or book_name.get()=="" or book_id.get()==""):
        variable.set("empty blanks are not allowed")
        l6.configure(fg='red')
    else:
        backend.update(selected_tuple[0],name_text.get(),id_text.get(),book_name.get(),book_id.get())
        view_command()
        variable.set("upadated succesfully")
        l6.configure(fg="green")

def delete_command():
    backend.delete(selected_tuple[0])
    view_command()
    variable.set("deleted succesfully")
    l6.configure(fg="green")

def close_command():
    window.destroy()

l1 = Label(window,text="Name of the Student",bg="#a1dbcd")
l1.grid(row=0,column=0,padx=(5,5),pady=(8,8))

l2 = Label(window,text="ID",bg="#a1dbcd")
l2.grid(row=0,column=2,padx=(5,5),pady=(8,8))

l3 = Label(window,text="Title of the book",bg="#a1dbcd")
l3.grid(row=1,column=0,padx=(5,5),pady=(8,8))

l4 = Label(window,text="Book No",bg="#a1dbcd")
l4.grid(row=1,column=2,padx=(5,5),pady=(8,8))

l5 = Label(window,text="Display",bg="#a1dbcd")
l5.grid(row=2,column=0,padx=(5,5),pady=(8,3),columnspan=2)

variable=StringVar()
l6 = Label(window,textvariable=variable,bg="#a1dbcd")
l6.grid(row=3,column=0,padx=(5,5),pady=(3,3),columnspan=2)

name_text=StringVar()
e1 = Entry(window,textvariable = name_text)
e1.grid(row=0,column=1,padx=(5,5),pady=(8,8))

id_text=StringVar()
e2 = Entry(window,textvariable = id_text)
e2.grid(row=0,column=3,padx=(5,5),pady=(8,8))

book_name = StringVar()
e3 = Entry(window,textvariable=book_name)
e3.grid(row=1,column=1,padx=(5,5),pady=(8,8))

book_id = StringVar()
e4 = Entry(window,textvariable=book_id)
e4.grid(row=1,column=3,padx=(5,5),pady=(8,8))

list1 = Listbox(window,height=20,width=50)
list1.grid(row=4,column=0,rowspan=10,columnspan=2,padx=(10,5),pady=(8,8))

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.bind('<<ListboxSelect>>',get_selected_row)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

b1 = Button(window,text="View all",width=10,command=view_command,fg="#a1dbcd",bg="#383a39")
b1.grid(row=4,column=3,padx=(5,5),pady=(8,8))

b2 = Button(window,text="Search Entry",width=10,command=search_command,fg="#a1dbcd",bg="#383a39")
b2.grid(row=5,column=3,padx=(5,5),pady=(8,8))

b3 = Button(window,text="Add Entry",width=10,command=add_command,fg="#a1dbcd",bg="#383a39")
b3.grid(row=6,column=3,padx=(5,5),pady=(8,8))

b4 = Button(window,text="Update",width=10,command=update_command,fg="#a1dbcd",bg="#383a39")
b4.grid(row=7,column=3,padx=(5,5),pady=(8,8))

b5 = Button(window,text="Delete",width=10,command=delete_command,fg="#a1dbcd",bg="#383a39")
b5.grid(row=8,column=3,padx=(5,5),pady=(8,8))

b6 = Button(window,text="Close",width=10,command=close_command,fg="#a1dbcd",bg="#383a39")
b6.grid(row=9,column=3,padx=(5,5),pady=(8,8))


window.mainloop()

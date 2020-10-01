from tkinter import *
#function for creating file
def saveinfo():
    with open(f"{fnameval.get()}.txt", 'a') as f:
        f.write("--------------Coding Challenge---------------------\n"
                f"First Name: {fnameval.get()}\n"
                f"Last Name: {lnameval.get()}\n"
                f"Email: {emailval.get()}\n"
                f"Phone number: {phoneval.get()}\n"
                f"Age : {ageval.get()}\n"
                "------------***Thanks for participating***-------------------")
root = Tk()
#Defining Windows size
root.geometry("333x220")
root.minsize(333, 220)
root.maxsize(333, 220)
#Titles
root.title("Coding Challenge")
#Frame and  Lables
f1 =Frame(root,borderwidth=13, bg="lightblue", relief=SUNKEN)
f1.pack(fill="x",anchor="w")
fname = Label(f1, text="First Name", font="Comicsans 16 bold", fg= "Black", bg='lightblue')
lname = Label(f1, text= "Last Name", font="Comicsans 16 bold", fg= "Black", bg='lightblue')
email = Label(f1, text= "Email", font="Comicsans 16 bold", fg= "Black", bg='lightblue')
phone= Label(f1, text= "Phone Number", font="Comicsans 16 bold", fg= "Black", bg='lightblue')
age = Label(f1, text= "Age", font="Comicsans 16 bold", fg= "Black", bg='lightblue')
#griding and Giviging location to the texts
fname.grid(row=0)
lname.grid(row=1)
email.grid(row=2)
phone.grid(row=3)
age.grid(row=4)
#Defining Variables
fnameval = StringVar()
lnameval = StringVar()
emailval = StringVar()
phoneval = IntVar()
ageval = IntVar()
#Creating Entry 
fnameEntry = Entry(f1, textvariable=fnameval)
lnameEntry = Entry(f1, textvariable=lnameval) 
emailEntry = Entry(f1, textvariable=emailval) 
phoneEntry = Entry(f1, textvariable=phoneval) 
ageEntry = Entry(f1, textvariable=ageval)
#placing entry
fnameEntry.grid(row=0, column=2)
lnameEntry.grid(row=1, column=2)
emailEntry.grid(row=2, column=2)
phoneEntry.grid(row=3, column=2)
ageEntry.grid(row=4, column=2)
#Button of submit
Button(f1, text="Submit", command=saveinfo).grid()
root.mainloop()
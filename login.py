from tkinter import *
from tkinter import messagebox
from student import Student

def getDept(name):
    root = Tk() 
    ob = Student(root,name)
    #print(name)
def Branch():
    uname = e1.get()
    password = e2.get()

 
    if(uname == "" and password == "") :
        messagebox.showinfo("", "Blank Not allowed")

    elif(uname == "Admin" and password == "123"):
        messagebox.showinfo("","Login Success")
        f2 = Frame()
        f2.place(x=0, y=0, width=1200, height= 600)
        Label(f2, text="Student Registration System", bg="crimson", fg="white", font=("times new roman",30,"bold")).place(x=550, y=10)
        Label(f2, text="Select Branch", bg="crimson", fg="white", font=("times new roman",20,"bold")).place(x=730, y=100)

        b2 = Button(f2, text="IT",command= lambda: getDept("it"), height = 3, width = 30, bg="crimson", fg="white", font=("times new roman",13,"bold")).place(x=660, y=180)
 
        b3 = Button(f2, text="CSE",command= lambda: getDept("cse"), height = 3, width = 30, bg="crimson", fg="white", font=("times new roman",13,"bold")).place(x=660, y=260)
 
        b4 = Button(f2, text="CIVIL",command= lambda: getDept("civil"), height = 3, width = 30, bg="crimson", fg="white", font=("times new roman",13,"bold")).place(x=660, y=340)

        b5 = Button(f2, text="EXTC",command= lambda: getDept("extc"), height = 3, width = 30, bg="crimson", fg="white", font=("times new roman",13,"bold")).place(x=660, y=420)

        b6 = Button(f2, text="MECH",command= lambda: getDept("mech"), height = 3, width = 30, bg="crimson", fg="white", font=("times new roman",13,"bold")).place(x=660, y=500)

    else :
        messagebox.showinfo("","Incorrent Username and Password")

 
root = Tk()
root.title("Student Registration System")
root.geometry("1350x700+0+0")
global e1
global e2

Label(root, text="Student Registration System", bg="crimson", fg="white", font=("times new roman",30,"bold")).place(x=550, y=10)
Label(root, text="UserName", bg="crimson", fg="white", font=("times new roman",20,"bold")).place(x=600, y=100)
Label(root, text="Password", bg="crimson", fg="white", font=("times new roman",20,"bold")).place(x=600, y=170)
 
e1 = Entry(root, font=("times new roman",16,"bold"), bd=5, relief=GROOVE)
e1.place(x=750, y=100)
 
e2 = Entry(root, font=("times new roman",16,"bold"), bd=5, relief=GROOVE)
e2.place(x=750, y=170)
e2.config(show="*")
 
 
Button(root, text="Login", command=Branch ,height = 3, width = 25, fg="black", font=("times new roman",13,"bold") ).place(x=670, y=250)

root.mainloop()

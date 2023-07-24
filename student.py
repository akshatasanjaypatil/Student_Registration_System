from tkinter import *
from tkinter import ttk
import tkinter as tk
import sqlite3
from db_helper import *
from db_helper import delete as deleteFrmDb


class Student:

	def __init__(self, root, name):
		self.root = root
		self.root.title("Student Registration System")
		self.root.geometry("1350x700+0+0")
		self.deptName = name
		title = Label(self.root, text="Student Registration System", font=(
			"Times New Roman", 40, "bold"), bg="yellow", fg="red")
		title.pack(side=TOP, fill=X)

		db = sqlite3.connect("students.db")
		create_table(db, self.deptName, roll_number='integer', name='text', email='text', gender='text', contact='text',
					 dob='text', address='text')
# =======================================================Manage Farme==========================================================
		rollno = tk.StringVar(root)
		name1 = tk.StringVar(root)
		email = tk.StringVar(root)
		gender = tk.StringVar(root)
		contact = tk.StringVar(root)
		dob = tk.StringVar(root)
		searchBy = tk.StringVar(root)
		whatToSearch = tk.StringVar(root)
		# address=tk.StringVar(root)
		# print("ABC",self.deptName)
		Manage_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
		Manage_Frame.place(x=20, y=100, width=500, height=600)

		m_title = Label(Manage_Frame, text="Manage Students", bg="crimson",
						fg="white", font=("times new roman", 30, "bold"))
		m_title.grid(row=0, columnspan=2, pady=20)

		lbl_roll = Label(Manage_Frame, text="Roll No.", bg="crimson",
						 fg="white", font=("times new roman", 20, "bold"))
		lbl_roll.grid(row=1, column=0, pady=10, padx=20, sticky="w")

		txt_Roll = Entry(Manage_Frame, font=(
			"times new roman", 15, "bold"), bd=5, textvariable=rollno, relief=GROOVE)
		txt_Roll.grid(row=1, column=1, pady=10, padx=20, sticky="w")

		lbl_name = Label(Manage_Frame, text="Name", bg="crimson",
						 fg="white", font=("times new roman", 20, "bold"))
		lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky="w")

		txt_name = Entry(Manage_Frame, font=(
			"times new roman", 15, "bold"), bd=5, textvariable=name1, relief=GROOVE)
		txt_name.grid(row=2, column=1, pady=10, padx=20, sticky="w")

		lbl_Email = Label(Manage_Frame, text="Email", bg="crimson",
						  fg="white", font=("times new roman", 20, "bold"))
		lbl_Email.grid(row=3, column=0, pady=10, padx=20, sticky="w")

		txt_Email = Entry(Manage_Frame, font=(
			"times new roman", 15, "bold"), bd=5, textvariable=email, relief=GROOVE)
		txt_Email.grid(row=3, column=1, pady=10, padx=20, sticky="w")

		lbl_Gender = Label(Manage_Frame, text="Gender", bg="crimson",
						   fg="white", font=("times new roman", 20, "bold"))
		lbl_Gender.grid(row=4, column=0, pady=10, padx=20, sticky="w")

		combo_gender = ttk.Combobox(Manage_Frame, font=(
			"times new roman", 13, "bold"), textvariable=gender, state='readonly')
		combo_gender['values'] = ("Male", "Female", "Others")
		combo_gender.grid(row=4, column=1, padx=20, pady=10)

		lbl_Contact = Label(Manage_Frame, text="Contact", bg="crimson",
							fg="white", font=("times new roman", 20, "bold"))
		lbl_Contact.grid(row=5, column=0, pady=10, padx=20, sticky="w")

		txt_Contact = Entry(Manage_Frame, font=(
			"times new roman", 15, "bold"), bd=5, textvariable=contact, relief=GROOVE)
		txt_Contact.grid(row=5, column=1, pady=10, padx=20, sticky="w")

		lbl_DOB = Label(Manage_Frame, text="D.O.B", bg="crimson",
						fg="white", font=("times new roman", 20, "bold"))
		lbl_DOB.grid(row=6, column=0, pady=10, padx=20, sticky="w")

		txt_DOB = Entry(Manage_Frame, font=(
			"times new roman", 15, "bold"), bd=5, textvariable=dob, relief=GROOVE)
		txt_DOB.grid(row=6, column=1, pady=10, padx=20, sticky="w")

		lbl_Address = Label(Manage_Frame, text="Address", bg="crimson",
							fg="white", font=("times new roman", 20, "bold"))
		lbl_Address.grid(row=7, column=0, pady=10, padx=20, sticky="w")

		txt_Address = Text(Manage_Frame, width=30, height=4,
						   font=("times new roman", 10))
		txt_Address.grid(row=7, column=1, pady=10, padx=20, sticky="w")

		def addInDb():
			Rollno = rollno.get()
			Name1 = name1.get()
			Email = email.get()
			Gender = gender.get()
			Contact = contact.get()
			Dob = dob.get()
			Address = txt_Address.get("1.0", "end")
			insert(db, self.deptName, Rollno, Name1,
				   Email, Gender, Contact, Dob, Address)
			db.commit()
			print(Rollno, Name1, Email, Gender, Contact, Dob, Address)
			rollno.set("")
			name1.set("")
			email.set("")
			gender.set("")
			contact.set("")
			dob.set("")
			txt_Address.delete("1.0", "end")

		saveBtnAdd = Button(Manage_Frame, text="Add in DB",
							command=addInDb, width=10)
		saveBtnAdd.grid(
			row=7, column=2, padx=10, pady=10)



		def showDetails():
			lbl_name.grid()
			txt_name.grid()
			lbl_Email.grid()
			txt_Email.grid()
			lbl_Gender.grid()
			combo_gender.grid()
			lbl_Contact.grid()
			txt_Contact.grid()
			lbl_DOB.grid()
			txt_DOB.grid()
			lbl_Address.grid()
			txt_Address.grid()
			updateDataBtn.grid()
			Rollno = rollno.get()
			Student_table.delete(*Student_table.get_children())
			cur = db.cursor()
			# print("SELECT * FROM "+self.deptName +
			# 			" where "+SearchBy+"= "+WhatToSearch+";")
			cur.execute("SELECT * FROM "+self.deptName +
						" where roll_number=  "+Rollno+"")
			
			results = []
			while True:
				result = cur.fetchone()
				if not result:
					break
				results.append(result)
			print(results)

			# rollno.set(results[0])
			name1.set(results[0][1])
			email.set(results[0][2])
			gender.set(results[0][3])
			contact.set(results[0][4])
			dob.set(results[0][5])
			txt_Address.insert("1.0", results[0][6])

		def updateDB():
			cur = db.cursor()
			cur.execute( "update "+self.deptName + " set name= '"+name1.get()+"',email= '"+email.get() + "',gender= '"+gender.get()+
					"',contact= '"+contact.get()+ "',dob= '"+dob.get()+"',address= '"+txt_Address.get("1.0", "end")+"' where roll_number= "+rollno.get()+";")
			db.commit()
			name1.set("")
			email.set("")
			gender.set("")
			contact.set("")
			dob.set("")
			rollno.set("")
			txt_Address.delete("1.0", "end")

		updateDataBtn = Button(Manage_Frame, text="Update DB", width=10,command=updateDB)
		updateDataBtn.grid(
			row=7, column=2, padx=10, pady=10)

		

		viewDetails = Button(Manage_Frame, text="View Details",
							 width=10, command=showDetails)
		viewDetails.grid(
			row=1, column=2, padx=10, pady=10)

		def deleteFromDb():
			Rollno = rollno.get()
			# insert(db, "student" ,Rollno,self.deptName)
			deleteFrmDb(db, self.deptName, "roll_number", Rollno)
			# cur = db.cursor()
			# print(type(self.deptName))
			# print("delete FROM student where roll_number= "+Rollno + " and dept_name= "+ self.deptName + ";")
			# cur.execute("delete FROM student where roll_number= "+Rollno + " and dept_name= "+ self.deptName + ";")
			db.commit()
			print(Rollno)
			rollno.set("")
		deleteDetails = Button(
			Manage_Frame, text="Delete Details", width=10, command=deleteFromDb)
		deleteDetails.grid(
			row=1, column=2, padx=10, pady=10)
# ====================================================Button Frame==============================================

		def add():
			lbl_roll.grid()
			txt_Roll.grid()
			lbl_name.grid()
			txt_name.grid()
			lbl_Email.grid()
			txt_Email.grid()
			lbl_Gender.grid()
			combo_gender.grid()
			lbl_Contact.grid()
			txt_Contact.grid()
			lbl_DOB.grid()
			txt_DOB.grid()
			lbl_Address.grid()
			txt_Address.grid()
			saveBtnAdd.grid()
			viewDetails.grid_remove()
			updateDataBtn.grid_remove()
			deleteDetails.grid_remove()

		def update():
			lbl_roll.grid()
			txt_Roll.grid()

			lbl_name.grid_remove()
			txt_name.grid_remove()
			lbl_Email.grid_remove()
			txt_Email.grid_remove()
			lbl_Gender.grid_remove()
			combo_gender.grid_remove()
			lbl_Contact.grid_remove()
			txt_Contact.grid_remove()
			lbl_DOB.grid_remove()
			txt_DOB.grid_remove()
			lbl_Address.grid_remove()
			txt_Address.grid_remove()
			saveBtnAdd.grid_remove()
			saveBtnAdd.grid_remove()
			updateDataBtn.grid_remove()
			deleteDetails.grid_remove()

			viewDetails.grid()

		def delete():
			lbl_roll.grid()
			txt_Roll.grid()

			lbl_name.grid_remove()
			txt_name.grid_remove()
			lbl_Email.grid_remove()
			txt_Email.grid_remove()
			lbl_Gender.grid_remove()
			combo_gender.grid_remove()
			lbl_Contact.grid_remove()
			txt_Contact.grid_remove()
			lbl_DOB.grid_remove()
			txt_DOB.grid_remove()
			lbl_Address.grid_remove()
			txt_Address.grid_remove()
			saveBtnAdd.grid_remove()
			saveBtnAdd.grid_remove()
			viewDetails.grid_remove()
			updateDataBtn.grid_remove()
			deleteDetails.grid()

		btn_Frame = Frame(Manage_Frame, bd=4, relief=RIDGE, bg="crimson")
		btn_Frame.place(x=15, y=520, width=430)

		# def test():
		#         Manage_Frame.place_forget()
		#         m_title.grid_remove()
		#         txt_Roll.grid_remove()

		# def test1():
		#         txt_Roll.grid()
		Addbtn = Button(btn_Frame, text="Add", width=10, command=add).grid(
			row=0, column=0, padx=10, pady=10)
		update = Button(btn_Frame, text="Update", width=10, command=update).grid(
			row=0, column=1, padx=10, pady=10)
		deletebtn = Button(btn_Frame, text="Delete", width=10, command=delete).grid(
			row=0, column=2, padx=10, pady=10)

  # hide all fields when page loads

		def load():
			lbl_roll.grid_remove()
			txt_Roll.grid_remove()
			lbl_name.grid_remove()
			txt_name.grid_remove()
			lbl_Email.grid_remove()
			txt_Email.grid_remove()
			lbl_Gender.grid_remove()
			combo_gender.grid_remove()
			lbl_Contact.grid_remove()
			txt_Contact.grid_remove()
			lbl_DOB.grid_remove()
			txt_DOB.grid_remove()
			lbl_Address.grid_remove()
			txt_Address.grid_remove()
			saveBtnAdd.grid_remove()
			viewDetails.grid_remove()
			updateDataBtn.grid_remove()
			deleteDetails.grid_remove()

		load()


# ======================================================== Details Farme==============================================

		def getData():
			Student_table.delete(*Student_table.get_children())
			results = select_all(db, self.deptName)
			# print("ABCd",results)
			for i in results:
				i = tuple(list(i).pop())
			for item in results:
				Student_table.insert(parent='', index='end',
									 text=f'{3 + 1}', values=(item))

		def search():
			SearchBy = searchBy.get()
			WhatToSearch = whatToSearch.get()
			Student_table.delete(*Student_table.get_children())
			cur = db.cursor()
			# print("SELECT * FROM "+self.deptName +
			# 			" where "+SearchBy+"= "+WhatToSearch+";")
			cur.execute("SELECT * FROM "+self.deptName +
						" where "+SearchBy+"= '"+WhatToSearch+"';")
			searchBy.set("")
			whatToSearch.set("")
			results = []
			while True:
				result = cur.fetchone()
				if not result:
					break
				results.append(result) 
						
			for i in results:
				i = tuple(list(i).pop())
			for item in results:
				Student_table.insert(parent='', index='end',
									 text=f'{3 + 1}', values=(item))

		Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
		Detail_Frame.place(x=550, y=100, width=900, height=600)

		lbl_search = Label(Detail_Frame, text="Search By", bg="crimson",
						   fg="white", font=("times new roman", 20, "bold"))
		lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

		combo_search = ttk.Combobox(Detail_Frame, width=10, font=(
			"times new roman", 13, "bold"), state='readonly', textvariable=searchBy)
		combo_search['values'] = ("roll_number", "name", "contact")
		combo_search.grid(row=0, column=1, padx=20, pady=10)

		txt_search = Entry(Detail_Frame, width=20, font=(
			"times new roman", 14, "bold"), bd=5, relief=GROOVE, textvariable=whatToSearch)
		txt_search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

		searchbtn = Button(Detail_Frame, text="Search", width=15, pady=5, command=search).grid(
			row=0, column=3, padx=10, pady=10)
		showallbtn = Button(Detail_Frame, text="Refresh", width=15, pady=5, command=getData).grid(
			row=0, column=4, padx=10, pady=10)

# ========================================Table Frame================================================================
		Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="crimson")
		Table_Frame.place(x=10, y=70, width=850, height=500)

		scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
		scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
		Student_table = ttk.Treeview(Table_Frame, columns=("roll", "name", "email", "gender",
														   "contact", "dob", "Address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
		scroll_x.pack(side=BOTTOM, fill=X)
		scroll_y.pack(side=RIGHT, fill=Y)
		scroll_x.config(command=Student_table.xview)
		scroll_y.config(command=Student_table.yview)
		Student_table.heading("roll", text="Roll No.")
		Student_table.heading("name", text="Name")
		Student_table.heading("email", text="Email")
		Student_table.heading("gender", text="Gender")
		Student_table.heading("contact", text="Contact")
		Student_table.heading("dob", text="D.O.B")
		Student_table.heading("Address", text="Address")
		Student_table['show'] = 'headings'
		Student_table.column("roll", width=100)
		Student_table.column("name", width=100)
		Student_table.column("email", width=100)
		Student_table.column("gender", width=100)
		Student_table.column("contact", width=100)
		Student_table.column("dob", width=100)
		Student_table.column("Address", width=150)
		Student_table.pack(fill=BOTH, expand=1)
		#Student_table.insert("", 1, "", text="Amit", values=(1,"Amit","Amit@email.com","Male","1234567891","01/02/03","Mumbai"))
		#Student_table.insert("", 2, "", text="viresh", values=(2,"Amit","Amit@email.com","Male","1234567891","01/02/03","Mumbai"))

		getData()
#     def load(self):
#             self.lbl_roll.grid_remove()


# root = Tk()
# ob = Student(root)
# # ob.load()
# root.mainloop()

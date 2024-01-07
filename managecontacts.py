from tkinter import*
from tkinter.ttk import*
from sqlite3 import*
from tkinter import messagebox
from datetime import datetime, date

class ManageContactsFrame(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent)

        s=Style()
        s.configure('TFrame',background='white')
        s.configure('TLabel',background='white',font=('Arial',15))
        s.configure('TButton',font=('Arial',15))
        s.configure('Treeview.Heading',font=('Arial',15))
        s.configure('Treeview',font=('Arial',12),rowheight=25)

        self.pack(fill=BOTH,expand=TRUE)

        self.con=connect("contacts.db")
        self.cur=self.con.cursor()

        self.create_view_all_contacts_frame()

    def fill_contacts_treeview(self):
        for contact in self.contacts_treeview.get_children():
            self.contacts_treeview.delete(contact)
        contacts=self.cur.fetchall()
        for contact in contacts:
            self.contacts_treeview.insert("",END,values=contact)
        
    def create_view_all_contacts_frame(self):
        self.view_all_contacts_frame= Frame(self)
        self.view_all_contacts_frame.place(relx=.5, rely=.5, anchor= CENTER)


        add_new_contact_button=Button(self.view_all_contacts_frame,text="Add New Contact",command=self.add_new_contact_button_click)
        add_new_contact_button.grid(row=0,column=1,sticky=E,pady=25)

        name_label=Label(self.view_all_contacts_frame,text="Search Name:")
        name_label.grid(row=1,column=0)

        self.name_entry=Entry(self.view_all_contacts_frame,font=('Arial',15),width=82)
        self.name_entry.grid(row=1,column=1,pady=10)
        self.name_entry.bind('<KeyRelease>',self.name_entry_key_release)

        

        self.contacts_treeview=Treeview(self.view_all_contacts_frame,columns=('Visitor_id','Visit_Date','Name','Contact_no','Place','In_time','out_time','Purpose_of_visit','Whom_to_visit'),show='headings')
        self.contacts_treeview.heading('Visitor_id',text="Visitor id",anchor=W)
        self.contacts_treeview.heading('Visit_Date',text="Visit Date",anchor=W)
        self.contacts_treeview.heading('Name',text="Name",anchor=W)
        self.contacts_treeview.heading('Contact_no',text="Contact no",anchor=W)
        self.contacts_treeview.heading('Place',text="Place",anchor=W)
        self.contacts_treeview.heading('In_time',text="In Time",anchor=W)
        self.contacts_treeview.heading('out_time',text="Out Time",anchor=W)
        self.contacts_treeview.heading('Purpose_of_visit',text="Purpose Of Visit",anchor=W)
        self.contacts_treeview.heading('Whom_to_visit',text="Whom to Visit",anchor=W)
        self.contacts_treeview.column('Visitor_id',width=100)
        self.contacts_treeview.column('Visit_Date',width=100)
        self.contacts_treeview.column('Name',width=120)
        self.contacts_treeview.column('Contact_no',width=120)
        self.contacts_treeview.column('Place',width=120)
        self.contacts_treeview.column('In_time',width=90)
        self.contacts_treeview.column('out_time',width=100)
        self.contacts_treeview.column('Purpose_of_visit',width=160)
        self.contacts_treeview.column('Whom_to_visit',width=140)
        self.contacts_treeview.grid(row=2,column=0,columnspan=2,pady=10)
        self.contacts_treeview.bind('<<TreeviewSelect>>',self.contacts_treeview_row_selection)

        self.cur.execute("select * from Contact")
        self.fill_contacts_treeview()


    def add_new_contact_button_click(self):
        self.view_all_contacts_frame.destroy()
        
        self.add_new_contact_frame=Frame(self)
        self.add_new_contact_frame.place(relx=.5,rely=.5,anchor=CENTER)

        Visit_Date_label=Label(self.add_new_contact_frame,text="Visit Date:")
        Visit_Date_label.grid(row=1,column=0,sticky=E)

        today = date.today()
        print(today)
        self.Visit_Date_entry=Entry(self.add_new_contact_frame,width=30,font=('Arial',15))
        self.Visit_Date_entry.grid(row=1,column=1)
        self.Visit_Date_entry.insert(0, str(today))
        self.Visit_Date_entry.bind('<Return>', self.visit_date_entry_return_key)
        
        Name_label=Label(self.add_new_contact_frame,text="Name:")
        Name_label.grid(row=2,column=0,sticky=E)

        self.Name_entry=Entry(self.add_new_contact_frame,width=30,font=('Arial',15))
        self.Name_entry.grid(row=2,column=1,pady=5)
        self.Name_entry.bind('<Return>', self.Name_entry_return_key)

        Contact_no_label=Label(self.add_new_contact_frame,text="Contact no:")
        Contact_no_label.grid(row=3,column=0,sticky=E)
        

        self.Contact_no_entry=Entry(self.add_new_contact_frame,width=30,font=('Arial',15))
        self.Contact_no_entry.grid(row=3,column=1,pady=5)
        self.Contact_no_entry.bind('<KeyPress>', self.contact_no_entry_key_press)
        self.Contact_no_entry.bind('<Return>', self.Contact_no_entry_return_key)

        Place_label=Label(self.add_new_contact_frame,text="Place:")
        Place_label.grid(row=4,column=0,sticky=E)

        self.Place_entry=Entry(self.add_new_contact_frame,width=30,font=('Arial',15))
        self.Place_entry.grid(row=4,column=1,pady=5)
        self.Place_entry.bind('<Return>', self.Place_entry_return_key)
        

        In_time_label=Label(self.add_new_contact_frame,text="In Time:")
        In_time_label.grid(row=5,column=0,sticky=E)

        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        self.In_time_entry=Entry(self.add_new_contact_frame,width=30,font=('Arial',15))
        self.In_time_entry.grid(row=5,column=1,pady=5)
        self.In_time_entry.insert(0, str(current_time))
        self.In_time_entry.bind('<Return>', self.In_time_entry_return_key)

        out_time_label=Label(self.add_new_contact_frame,text="Out Time:")
        out_time_label.grid(row=6,column=0,sticky=E)

        self.out_time_entry=Entry(self.add_new_contact_frame,width=30,font=('Arial',15))
        self.out_time_entry.grid(row=6,column=1,pady=5)
        self.out_time_entry.bind('<Return>', self.out_time_entry_return_key)

        Purpose_of_visit_label=Label(self.add_new_contact_frame,text="Purpose Of Visit:")
        Purpose_of_visit_label.grid(row=7,column=0,sticky=E)

        self.Purpose_of_visit_entry=Entry(self.add_new_contact_frame,width=30,font=('Arial',15))
        self.Purpose_of_visit_entry.grid(row=7,column=1,pady=5)
        self.Purpose_of_visit_entry.bind('<Return>', self.Purpose_of_visit_entry_return_key)

        Whom_to_visit_label=Label(self.add_new_contact_frame,text="Whom to Visit:")
        Whom_to_visit_label.grid(row=8,column=0,sticky=E)

        self.Whom_to_visit_entry=Entry(self.add_new_contact_frame,width=30,font=('Arial',15))
        self.Whom_to_visit_entry.grid(row=8,column=1,pady=5)
        self.Whom_to_visit_entry.bind('<Return>', self.Whom_to_visit_entry_return_key)

        add_button=Button(self.add_new_contact_frame,text="Add",width=30,command=self.add_button_click)
        add_button.grid(row=9,column=1,pady=5)


    def visit_date_entry_return_key(self,event):
        self.Name_entry.focus()

    def Name_entry_return_key(self,event):
        self.Contact_no_entry.focus()

    def Contact_no_entry_return_key(self,event):
        self.Place_entry.focus()

    def Place_entry_return_key(self,event):
        self.In_time_entry.focus()

    def In_time_entry_return_key(self,event):
        self.out_time_entry.focus()

    def out_time_entry_return_key(self,event):
        self.Purpose_of_visit_entry.focus()
        
    def Purpose_of_visit_entry_return_key(self,event):
        self.Whom_to_visit_entry.focus()

    def Whom_to_visit_entry_return_key(self,event):
        add_button.focus()

    def add_button_click(self):
        self.cur.execute("select * from Contact where Contactno = ?",(self.Contact_no_entry.get(),))
        contact=self.cur.fetchone()
        if contact is None:
            if not self.Name_entry.get().replace(" ", "").isalpha():
                messagebox.showerror('Error Message', 'Not a name')
                self.Name_entry.focus()
                self.Name_entry.insert(0,"")
            elif not self.Name_entry.get().isupper():
                messagebox.showerror('Error Message', 'Enter name in Capital letter')
                self.Name_entry.focus()
                self.Name_entry.insert(0,"")
            elif not self.Contact_no_entry.get().replace(" ", "").isdigit():
                messagebox.showerror('Error Message', 'Not a proper contact no')
                self.Contact_no_entry.insert(0,"")
                self.Contact_no_entry.focus()
            elif len(self.Contact_no_entry.get()) != 10:
                messagebox.showerror('Error Message', 'Enter contact no of 10 digits')
                self.Contact_no_entry.insert(0,"")
                self.Contact_no_entry.focus()
            elif not self.Contact_no_entry.get():
                messagebox.showerror('Error Message', 'Enter Contact no properly')
                self.Contact_no_entry.insert(0,"")
                self.Contact_no_entry.focus()
            elif not self.Place_entry.get().replace(" ", "").isalpha():
                messagebox.showerror('Error Message', 'please enter place properly ')
                self.Place_entry.insert(0,"")
                self.Place_entry.focus()
            elif not self.Place_entry.get():
                messagebox.showerror('Error Message', 'Enter Place properly')
                self.Place_entry.insert(0,"")
                self.Place_entry.focus()
            elif not self.Purpose_of_visit_entry.get().replace(" ", "").isalpha():
                messagebox.showerror('Error Message', 'Please enter purpose of visit properly')
                self.Purpose_of_visit_entry.insert(0,"")
                self.Purpose_of_visit_entry.focus()
            elif not self.Purpose_of_visit_entry.get():
                messagebox.showerror('Error Message', 'Enter Purpose of visit properly')
                self.Purpose_of_visit_entry.insert(0,"")
                self.Purpose_of_visit_entry.focus()
            elif not self.Whom_to_visit_entry.get().replace(" ", "").isalpha():
                messagebox.showerror('Error Message', 'Please enter whom to visit properly')
                self.Whom_to_visit_entry.insert(0,"")
                self.Whom_to_visit_entry.focus()
            else:
                self.cur.execute("insert into Contact(VisitDate,Name,Contactno,Place,Intime,outtime,Purposeofvisit,Whomtovisit)values(?,?,?,?,?,?,?,?)",
                                 (self.Visit_Date_entry.get(),self.Name_entry.get(),self.Contact_no_entry.get(),self.Place_entry.get(),
                                  self.In_time_entry.get(),self.out_time_entry.get(),self.Purpose_of_visit_entry.get(),self.Whom_to_visit_entry.get()))
                self.con.commit()
                messagebox.showinfo("Success Message","Contact details are added successfully")
                self.add_new_contact_frame.destroy()
                self.create_view_all_contacts_frame()
        else:
            messagebox.showerror("Error Message","Contacts details are already added")

    def contact_no_entry_key_press(self,event):
        if len(self.Contact_no_entry.get()) == 10:
            self.Contact_no_entry.config(state= "disabled")

    def name_entry_key_release(self,event):
        self.cur.execute("select * from Contact where Name like ?",('%'+self.name_entry.get()+'%',))
        self.fill_contacts_treeview()

    def contacts_treeview_row_selection(self,event):
        contact=self.contacts_treeview.item(self.contacts_treeview.selection())['values']
        self.view_all_contacts_frame.destroy()
        
        self.update_delete_contact_frame=Frame(self)
        self.update_delete_contact_frame.place(relx=.5,rely=.5,anchor=CENTER)

        Visitor_id_label=Label(self.update_delete_contact_frame,text="Visitor id:")
        Visitor_id_label.grid(row=1,column=0,sticky=E)

        self.Visitor_id_entry=Entry(self.update_delete_contact_frame,width=30,font=('Arial',15))
        self.Visitor_id_entry.grid(row=1,column=1,pady=5)
        self.Visitor_id_entry.insert(END,contact[0])

        Visit_Date_label=Label(self.update_delete_contact_frame,text="Visit Date:")
        Visit_Date_label.grid(row=2,column=0,sticky=E)

        self.Visit_Date_entry=Entry(self.update_delete_contact_frame,width=30,font=('Arial',15))
        self.Visit_Date_entry.grid(row=2,column=1,pady=5)
        self.Visit_Date_entry.insert(END,contact[1])

        Name_label=Label(self.update_delete_contact_frame,text="Name:")
        Name_label.grid(row=3,column=0,sticky=E)

        self.Name_entry=Entry(self.update_delete_contact_frame,width=30,font=('Arial',15))
        self.Name_entry.grid(row=3,column=1,pady=5)
        self.Name_entry.insert(END,contact[2])

        Contact_no_label=Label(self.update_delete_contact_frame,text="Contact no:")
        Contact_no_label.grid(row=4,column=0,sticky=E)

        self.Contact_no_entry=Entry(self.update_delete_contact_frame,width=30,font=('Arial',15))
        self.Contact_no_entry.grid(row=4,column=1,pady=5)
        self.old_Contact_no=contact[3]
        self.Contact_no_entry.insert(END,contact[3])

        Place_label=Label(self.update_delete_contact_frame,text="Place:")
        Place_label.grid(row=5,column=0,sticky=E)

        self.Place_entry=Entry(self.update_delete_contact_frame,width=30,font=('Arial',15))
        self.Place_entry.grid(row=5,column=1,pady=5)
        self.Place_entry.insert(END,contact[4])

        In_time_label=Label(self.update_delete_contact_frame,text="In Time:")
        In_time_label.grid(row=6,column=0,sticky=E)

        self.In_time_entry=Entry(self.update_delete_contact_frame,width=30,font=('Arial',15))
        self.In_time_entry.grid(row=6,column=1,pady=5)
        self.In_time_entry.insert(END,contact[5])

        out_time_label=Label(self.update_delete_contact_frame,text="Out Time:")
        out_time_label.grid(row=7,column=0,sticky=E)

        self.out_time_entry=Entry(self.update_delete_contact_frame,width=30,font=('Arial',15))
        self.out_time_entry.grid(row=7,column=1,pady=5)
        self.out_time_entry.insert(END,contact[6])

        Purpose_of_visit_label=Label(self.update_delete_contact_frame,text="Purpose Of Visit:")
        Purpose_of_visit_label.grid(row=8,column=0,sticky=E)

        self.Purpose_of_visit_entry=Entry(self.update_delete_contact_frame,width=30,font=('Arial',15))
        self.Purpose_of_visit_entry.grid(row=8,column=1,pady=5)
        self.Purpose_of_visit_entry.insert(END,contact[7])

        Whom_to_visit_label=Label(self.update_delete_contact_frame,text="Whom to Visit:")
        Whom_to_visit_label.grid(row=9,column=0,sticky=E)

        self.Whom_to_visit_entry=Entry(self.update_delete_contact_frame,width=30,font=('Arial',15))
        self.Whom_to_visit_entry.grid(row=9,column=1,pady=5)
        self.Whom_to_visit_entry.insert(END,contact[8])

        Update_button=Button(self.update_delete_contact_frame,text="Update",width=30,command=self.update_button_click)
        Update_button.grid(row=10,column=1,pady=5)

        Delete_button=Button(self.update_delete_contact_frame,text="Delete",width=30,command=self.delete_button_click)
        Delete_button.grid(row=11,column=1,pady=5)

    def update_button_click(self):
        self.cur.execute("update Contact set VisitDate=?,Name=?,Contactno=?,Place=?,Intime=?,outtime=?,Purposeofvisit=?,Whomtovisit=? where Contactno=?",
                        (self.Visit_Date_entry.get(),self.Name_entry.get(),self.Contact_no_entry.get(),self.Place_entry.get(),
                              self.In_time_entry.get(),self.out_time_entry.get(),self.Purpose_of_visit_entry.get(),self.Whom_to_visit_entry.get(),self.old_Contact_no))
        self.con.commit()
        messagebox.showinfo("Sucess Message"," Contacts details are updated succesfully")
        self.update_delete_contact_frame.destroy()
        self.create_view_all_contacts_frame()

    def delete_button_click(self):
        if messagebox.askquestion("Confirmation Message","Are you sure to Delete?")=='yes':
           self.cur.execute("delete from Contact where Contactno=?",(self.old_Contact_no,))
           self.con.commit()
           messagebox.showinfo("Sucess Message"," Contacts details are updated succesfully")
           self.update_delete_contact_frame.destroy()
           self.create_view_all_contacts_frame()

           

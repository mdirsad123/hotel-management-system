from cProfile import label
from tkinter import*
from turtle import hideturtle
from PIL import Image,ImageTk 
from tkinter import  ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox





class Roombooking:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+240+240")
        
        #=============Vaiables=================
        
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()
        
        
        #================title=================
        lbl_title=Label(self.root,text="ROOMBOOKING DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)
        
        
        #================logo=================
        img2=Image.open(r"image\logo.png")
        img2=img2.resize((100,40),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)
        
        
        
        #================lable frame=================
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="RoomBooking Details",font=("times new roman",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)
        
        #================lable and entrys=================
        
        #Customer contact
        lbl_cust_contact=Label(labelframeleft,text="Customer Contact:",font=("arial",10,"bold"),padx=2,pady=6)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)
        
        enty_contact=ttk.Entry(labelframeleft,textvariable=self.var_contact,font=("arial",13,"bold"),width=20)
        enty_contact.grid(row=0,column=1,sticky=W)
        
        #featch data button
        btnFeatchData=Button(labelframeleft,command=self.fetch_contact,text="Featch",font=("arial",8,"bold"),bg="black",fg="gold",width=8)
        btnFeatchData.place(x=347,y=5)
        
        #Check_in date
        check_in_date=Label(labelframeleft,text="Check in Date:",font=("arial",10,"bold"),padx=2,pady=6)
        check_in_date.grid(row=1,column=0,sticky=W)
        txtcheck_in_date=ttk.Entry(labelframeleft,textvariable=self.var_checkin,font=("arial",13,"bold"),width=29)
        txtcheck_in_date.grid(row=1,column=1)
        
        #Check_out date
        lbl_check_out=Label(labelframeleft,text="Check Out Date:",font=("arial",10,"bold"),padx=2,pady=6)
        lbl_check_out.grid(row=2,column=0,sticky=W)
        txt_check_out=ttk.Entry(labelframeleft,textvariable=self.var_checkout,font=("arial",13,"bold"),width=29)
        txt_check_out.grid(row=2,column=1)
        
        #Room Type
        label_RoomType=Label(labelframeleft,text="Room Type:",font=("arial",10,"bold"),padx=2,pady=6)
        label_RoomType.grid(row=3,column=0,sticky=W)
        
        conn=mysql.connector.connect(host="localhost",username="root",password="sahil",database="hotel_managment_system")
        my_cursor=conn.cursor()    
        my_cursor.execute("select RoomType from details")   
        ide=my_cursor.fetchall()
        
        combo_RoomType=ttk.Combobox(labelframeleft,textvariable=self.var_roomtype,font=("arial",10,"bold"),width=29,state="readonly")
        combo_RoomType ["value"]=ide
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3,column=1)
        
        
        #Available Room
        lblRoomAvailable=Label(labelframeleft,text="Available Room :",font=("arial",10,"bold"),padx=2,pady=6)
        lblRoomAvailable.grid(row=4,column=0,sticky=W)
        # txtRoomAvailable=ttk.Entry(labelframeleft,textvariable=self.var_roomavailable,font=("arial",13,"bold"),width=29)
        # txtRoomAvailable.grid(row=4,column=1)
        
        conn=mysql.connector.connect(host="localhost",username="root",password="Gulshan@1234",database="hotel_managment_system")
        my_cursor=conn.cursor()    
        my_cursor.execute("select RoomNo from details")   
        rows=my_cursor.fetchall()
        
        combo_RoomType=ttk.Combobox(labelframeleft,textvariable=self.var_roomavailable,font=("arial",10,"bold"),width=29,state="readonly")
        combo_RoomType ["value"]=rows
        combo_RoomType.current(0)
        combo_RoomType.grid(row=4,column=1)
        
        #Meal
        lblMeal=Label(labelframeleft,text="Meal:",font=("arial",10,"bold"),padx=2,pady=6)
        lblMeal.grid(row=5,column=0,sticky=W)
        txtMeal=ttk.Entry(labelframeleft,textvariable=self.var_meal,font=("arial",13,"bold"),width=29)
        txtMeal.grid(row=5,column=1)
        
        #No. of Day
        lblNoOfDays=Label(labelframeleft,text="No. Of Days:",font=("arial",10,"bold"),padx=2,pady=6)
        lblNoOfDays.grid(row=6,column=0,sticky=W)
        txtNoOfDays=ttk.Entry(labelframeleft,textvariable=self.var_noofdays,font=("arial",13,"bold"),width=29)
        txtNoOfDays.grid(row=6,column=1)
        
        #Paid Tax
        lblPaidTax=Label(labelframeleft,text="Paid Tex:",font=("arial",10,"bold"),padx=2,pady=6)
        lblPaidTax.grid(row=7,column=0,sticky=W)
        txtlPaidTax=ttk.Entry(labelframeleft,textvariable=self.var_paidtax,font=("arial",13,"bold"),width=29)
        txtlPaidTax.grid(row=7,column=1) 
        
        #sub total
        lblSubTotal=Label(labelframeleft,text="Sub Total:",font=("arial",10,"bold"),padx=2,pady=6)
        lblSubTotal.grid(row=8,column=0,sticky=W)
        txtSubTotal=ttk.Entry(labelframeleft,textvariable=self.var_actualtotal,font=("arial",13,"bold"),width=29)
        txtSubTotal.grid(row=8,column=1)
        
        #Total Cost
        lblTotalCost=Label(labelframeleft,text="Total Cost:",font=("arial",10,"bold"),padx=2,pady=6)
        lblTotalCost.grid(row=9,column=0,sticky=W)
        txtTotalCost=ttk.Entry(labelframeleft,textvariable=self.var_total,font=("arial",13,"bold"),width=29)
        txtTotalCost.grid(row=9,column=1)
        
        #================Bill_btn========================
        btnBill=Button(labelframeleft,text="Bill",command=self.total,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnBill.grid(row=10,column=0,padx=1,sticky=W)
        
        #================btn========================
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)
        
        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnAdd.grid(row=0,column=0,padx=1)
        
        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnUpdate.grid(row=0,column=1,padx=1)
        
        btnDelete=Button(btn_frame,text="Delete",command=self.mDelete,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnDelete.grid(row=0,column=2,padx=1)
        
        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnReset.grid(row=0,column=3,padx=1)
        
        #================Right Side Image=================
        img3=Image.open(r"image\bed.jpg")
        img3=img3.resize((500,440),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        lblimg=Label(self.root,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg.place(x=760,y=55,width=500,height=440)
        
        
        #================Table frame serach system=================
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and search system",font=("times new roman",12,"bold"),padx=2)
        Table_Frame.place(x=435,y=280,width=860,height=260)
        
        
        lblSearchBy=Label(Table_Frame,text="Search By:",font=("arial",10,"bold"),bg="red",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)
        

        self.serch_var=StringVar()
        combo_Search=ttk.Combobox(Table_Frame,textvariable=self.serch_var,font=("arial",10,"bold"),width=24,state="readonly")
        combo_Search ["value"]=("Contact","Room")
        combo_Search.current(0)
        combo_Search.grid(row=0,column=1,padx=2)
        
        self.txt_search=StringVar()
        txtSearch=ttk.Entry(Table_Frame,textvariable=self.txt_search,font=("arial",13,"bold"),width=29)
        txtSearch.grid(row=0,column=2,padx=2)
        
        
        btnSearch=Button(Table_Frame,text="Search",command=self.search,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnSearch.grid(row=0,column=3,padx=1)
        
        btnShowAll=Button(Table_Frame,text="Show All",command=self.fetch_data,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnShowAll.grid(row=0,column=4,padx=1)
        
        #================Show Table Data========================
        details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=840,height=180)
        
        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)
        
        self.room_Table=ttk.Treeview(details_table,columns=("contact","checkinDate","checkoutDate","RoomType","roomavailable","meal","noOfDays"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.room_Table.xview)
        scroll_y.config(command=self.room_Table.yview)
        
        self.room_Table.heading("contact",text="Contact")
        self.room_Table.heading("checkinDate",text="Check-In")
        self.room_Table.heading("checkoutDate",text="Check-out")
        self.room_Table.heading("RoomType",text="Room Type")
        self.room_Table.heading("roomavailable",text="Room No.")
        self.room_Table.heading("meal",text="Meal")
        self.room_Table.heading("noOfDays",text="noOfDate")
       
        
        self.room_Table["show"]="headings"
        
        self.room_Table.column("contact",width=100)
        self.room_Table.column("checkinDate",width=100)
        self.room_Table.column("checkoutDate",width=100)
        self.room_Table.column("RoomType",width=100)
        self.room_Table.column("roomavailable",width=100)
        self.room_Table.column("meal",width=100)
        self.room_Table.column("noOfDays",width=100)
    
        self.room_Table.pack(fill=BOTH,expand=1)
        
        self.room_Table.bind("<ButtonRelease-1>",self.get_cuersor)
        self.fetch_data()
        
    #=================Add_Data===============================   
        
    def add_data(self):
        if self.var_contact.get()=="" or self.var_checkin .get()=="":
            messagebox.showerror("Error","All field are requaired",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Gulshan@1234",database="hotel_managment_system")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_contact.get(),
                                                                                        self.var_checkin.get(),
                                                                                        self.var_checkout.get(),
                                                                                        self.var_roomtype.get(),
                                                                                        self.var_roomavailable.get(),
                                                                                        self.var_meal.get(),
                                                                                        self.var_noofdays.get()

                                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Room Booked ",parent=self.root)
            except Exception as es:
                messagebox.showwarning("warning", f"some think want wrong :{str(es)}",parent=self.root)    
                
    #==============fetch data=======================
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Gulshan@1234",database="hotel_managment_system")
        my_cursor=conn.cursor()    
        my_cursor.execute("select * from room")   
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_Table.delete(*self.room_Table.get_children())
            for i in rows:
                self.room_Table.insert("", END,values=i)     
                conn.commit()
            conn.close()
            
    #get_cuersor        
    def get_cuersor(self,envent):
        Cursor_row=self.room_Table.focus()
        content=self.room_Table.item(Cursor_row)
        row=content["values"]
        
        self.var_contact.set(row[0])
        self.var_checkin.set(row[1])
        self.var_checkout.set(row[2])
        self.var_roomtype.set(row[3])
        self.var_roomavailable.set(row[4])
        self.var_meal.set(row[5])
        self.var_noofdays.set(row[6])
        
        
    #update_function    
    def update(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter mobile number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Gulshan@1234",database="hotel_managment_system")
            my_cursor=conn.cursor()    
            my_cursor.execute("update room set check_in=%s,check_out=%s,roomtype=%s,roomavailable=%s,meal=%s,noOfdays=%s where Contact=%s",(
            
                                                                                        self.var_checkin.get(),
                                                                                        self.var_checkout.get(),
                                                                                        self.var_roomtype.get(),
                                                                                        self.var_roomavailable.get(),
                                                                                        self.var_meal.get(),
                                                                                        self.var_noofdays.get(),
                                                                                        self.var_contact.get()
                                                                                         
                                                                                        )) 
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("update","Room details has been updated sucessfully",parent=self.root)
    
    
    #============Delete============
    def mDelete(self):
        mDelete=messagebox.askyesno("Hospital management system","Do You Want To Delelte this Customers",parent=self.root)  
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="Gulshan@1234",database="hotel_managment_system")
            my_cursor=conn.cursor() 
            query="delete from room where Contact=%s"
            Value=(self.var_contact.get(),)  
            my_cursor.execute(query,Value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()    
        
    #============Reset============
    def reset(self):
        self.var_contact.set("")
        self.var_checkin.set("")
        self.var_checkout.set("")
        self.var_roomtype.set("")
        self.var_roomavailable.set("")
        self.var_meal.set("")
        self.var_noofdays.set("")
        self.var_paidtax.set("")
        self.var_actualtotal.set("")
        self.var_total.set("")
        
        
    #============All_Data_Fetch=====================    
    def fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please Enter Contact No.",parent=self.root)
            
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Gulshan@1234",database="hotel_managment_system")
            my_cursor=conn.cursor()
            query=("select Name from customers where Mobile=%s")
            value = (self.var_contact.get(),)
            my_cursor.execute(query,value)
            row = my_cursor.fetchone()
            
            if row==None:
                messagebox.showerror("Error","This No. is not found",parent=self.root)
                
            else:
                conn.commit()
                conn.close()
                
                ShowDataFrame=Frame(self.root,bd=4,padx=2,relief=RIDGE)
                ShowDataFrame.place(x=450,y=55,width=300,height=180)
                
                lblName=Label(ShowDataFrame,text="Name : ",font=("arial",12,"bold"))
                lblName.place(x=0,y=0)
                
                lbl=Label(ShowDataFrame,text=row ,font=("arial",12,"bold"))
                lbl.place(x=90,y=0)
                
                
                #==============Gender===================
                conn=mysql.connector.connect(host="localhost",username="root",password="Gulshan@1234",database="hotel_managment_system")
                my_cursor=conn.cursor()
                query=("select Gender from customers where Mobile=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query,value)
                row = my_cursor.fetchone()
                
                lblGender=Label(ShowDataFrame,text="Gender : ",font=("arial",12,"bold"))
                lblGender.place(x=0,y=30)
                
                lbl2=Label(ShowDataFrame,text=row ,font=("arial",12,"bold"))
                lbl2.place(x=90,y=30)
                
                #================email====================
                
                conn=mysql.connector.connect(host="localhost",username="root",password="Gulshan@1234",database="hotel_managment_system")
                my_cursor=conn.cursor()
                query=("select Email from customers where Mobile=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query,value)
                row = my_cursor.fetchone()
                
                lblEmail=Label(ShowDataFrame,text="Email : ",font=("arial",12,"bold"))
                lblEmail.place(x=0,y=60)
                
                lbl3=Label(ShowDataFrame,text=row ,font=("arial",12,"bold"))
                lbl3.place(x=90,y=60)
                
                #================Nationality====================
                
                conn=mysql.connector.connect(host="localhost",username="root",password="Gulshan@1234",database="hotel_managment_system")
                my_cursor=conn.cursor()
                query=("select Nationality from customers where Mobile=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query,value)
                row = my_cursor.fetchone()
                
                lblNationality=Label(ShowDataFrame,text="Nationality : ",font=("arial",12,"bold"))
                lblNationality.place(x=0,y=90)
                
                lbl4=Label(ShowDataFrame,text=row ,font=("arial",12,"bold"))
                lbl4.place(x=90,y=90)
                
                
                #================Address====================
                
                conn=mysql.connector.connect(host="localhost",username="root",password="Gulshan@1234",database="hotel_managment_system")
                my_cursor=conn.cursor()
                query=("select Address from customers where Mobile=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query,value)
                row = my_cursor.fetchone()
                
                lblAddress=Label(ShowDataFrame,text="Address : ",font=("arial",12,"bold"))
                lblAddress.place(x=0,y=120)
                
                lbl5=Label(ShowDataFrame,text=row ,font=("arial",12,"bold"))
                lbl5.place(x=90,y=120)
    
    #Search System 
    #============Search============  
    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Gulshan@1234",database="hotel_managment_system")
        my_cursor=conn.cursor()
        
        my_cursor.execute("select * from room where "+str(self.serch_var.get())+"LIKE'%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len (rows)!=0:
            self.room_Table.delete(*self.room_Table.get_children())
            for i in rows:
                self.room_Table.insert("",END,values=i)
            conn.commit()
        conn.close()
    
        
    def total(self):
        inDate=self.var_checkin.get()
        outDate=self.var_checkout.get()
        inDate=datetime.strptime(inDate,"%d/%m/%Y")
        outDate=datetime.strptime(outDate,"%d/%m/%Y")
        self.var_noofdays.set(abs(outDate-inDate).days)
        
        if (self.var_meal.get()=="BreakFast" and self.var_roomtype.get()=="Luxary"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.09))
            ST="rs."+str("%.2f"%((q5)))
            TT="rs."+str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
            
        elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Single"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.09))
            ST="rs."+str("%.2f"%((q5)))
            TT="rs."+str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
            
            
        elif (self.var_meal.get()=="BreakFast" and self.var_roomtype.get()=="Duplex"):
            q1=float(500)
            q2=float(1000)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.09))
            ST="rs."+str("%.2f"%((q5)))
            TT="rs."+str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
        
            
            
    


















if __name__=="__main__":
    root=Tk()
    obj=Roombooking(root)
    root.mainloop()
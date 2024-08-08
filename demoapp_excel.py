from tkinter import *
import random, pandas as pd
import os,tempfile, smtplib
from tkinter import messagebox
from datetime import datetime

class Bill_App:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x750")
        self.root.maxsize(width = 1330,height = 700)
        self.root.minsize(width = 1330,height = 700)
        self.root.title("Billing Software")
        
        self.cus_name = StringVar()
        self.city = StringVar()
        self.c_phone = StringVar()
        #For Generating Random Bill Numbers
        self.x = random.randint(1000,9999)
        self.c_bill_no = StringVar()
        #Seting Value to variable
        self.c_bill_no.set(str(self.x))

        self.bath_soap = IntVar()
        self.face_cream = IntVar()
        self.face_wash = IntVar()
        self.hair_spray = IntVar()
        self.body_lotion = IntVar()
        self.rice = IntVar()
        self.daal = IntVar()
        self.food_oil = IntVar()
        self.wheat = IntVar()
        self.sugar = IntVar()
        self.maza = IntVar()
        self.coke = IntVar()
        self.frooti = IntVar()
        self.nimko = IntVar()
        self.biscuits = IntVar()
        self.total_cosmetics = StringVar()
        self.total_grocery = StringVar()
        self.total_other = StringVar()
        self.tax_cos = StringVar()
        self.tax_groc = StringVar()
        self.tax_other = StringVar()


        #===================================
        bg_color = "#074463"
        fg_color = "white"
        lbl_color = 'white'
        #Title of App
        title = Label(self.root,text = "Billing Software",bd = 12,relief = GROOVE,fg = fg_color,bg = bg_color,font=("times new roman",30,"bold"),pady = 3).pack(fill = X)

        #==========Customers Frame==========#
        F1 = LabelFrame(text = "Customer Details",font = ("time new roman",12,"bold"),fg = "gold",bg = bg_color,relief = GROOVE,bd = 10)
        F1.place(x = 0,y = 80,relwidth = 1)

        #===============Customer Name===========#
        cname_lbl = Label(F1, text="Customer Name", bg=bg_color, fg=fg_color, font=("times new roman", 12, "bold")).grid(
    row=0, column=0, padx=10, pady=5)

        cname_en = Entry(F1, bd=8, relief=GROOVE, textvariable=self.cus_name)
        cname_en.grid(row=0, column=1, ipady=4, ipadx=30, pady=5)

        city_lbl = Label(F1, text="City", bg=bg_color, fg=fg_color, font=("times new roman", 12, "bold")).grid(
            row=0, column=2, padx=10, pady=5)

        city_en = Entry(F1, bd=8, relief=GROOVE, textvariable=self.city)
        city_en.grid(row=0, column=3, ipady=4, ipadx=30, pady=5)

        cphon_lbl = Label(F1, text="Phone No", bg=bg_color, fg=fg_color, font=("times new roman", 12, "bold")).grid(
            row=0, column=4, padx=20)

        cphon_en = Entry(F1, bd=8, relief=GROOVE, textvariable=self.c_phone)
        cphon_en.grid(row=0, column=5, ipady=4, ipadx=30, pady=5)

        #====================Customer Bill No==================#
        cbill_lbl = Label(F1,text = "Bill No.",bg = bg_color,fg = fg_color,font = ("times new roman",12,"bold"))
        cbill_lbl.grid(row = 0,column = 6,padx = 20)
        self.cbill_en = Entry(F1,bd = 8,relief = GROOVE,textvariable = self.c_bill_no)
        self.cbill_en.grid(row = 0,column = 7,ipadx = 0,ipady = 1,pady = 1)
        
        #====================Bill Search Button===============#
        bill_btn = Button(F1,text = "SEARCH",bd = 7,relief = GROOVE,font = ("times new roman",12,"bold"),bg = bg_color,fg = fg_color,command=self.search_bill)
        bill_btn.grid(row = 0,column = 8,ipady = 5,padx = 50,ipadx = 19,pady = 5)

        #==================Cosmetics Frame=====================#
        F2 = LabelFrame(self.root,text = 'Cosmetics',bd = 10,relief = GROOVE,bg = bg_color,fg = "gold",font = ("times new roman",13,"bold"))
        F2.place(x = 5,y = 180,width = 325,height = 380)

        #===========Frame Content
        bath_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Bath Soap")
        bath_lbl.grid(row = 0,column = 0,padx = 10,pady = 20)
        bath_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.bath_soap)
        bath_en.grid(row = 0,column = 1,ipady = 5,ipadx = 5)

        #=======Face Cream
        face_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Face Cream")
        face_lbl.grid(row = 1,column = 0,padx = 10,pady = 20)
        face_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.face_cream)
        face_en.grid(row = 1,column = 1,ipady = 5,ipadx = 5)

        #========Face Wash
        wash_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Face Wash")
        wash_lbl.grid(row = 2,column = 0,padx = 10,pady = 20)
        wash_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.face_wash)
        wash_en.grid(row = 2,column = 1,ipady = 5,ipadx = 5)

        #========Hair Spray
        hair_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Hair Spray")
        hair_lbl.grid(row = 3,column = 0,padx = 10,pady = 20)
        hair_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.hair_spray)
        hair_en.grid(row = 3,column = 1,ipady = 5,ipadx = 5)

        #============Body Lotion
        lot_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Body Lotion")
        lot_lbl.grid(row = 4,column = 0,padx = 10,pady = 20)
        lot_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.body_lotion)
        lot_en.grid(row = 4,column = 1,ipady = 5,ipadx = 5)

        #==================Grocery Frame=====================#
        F2 = LabelFrame(self.root,text = 'Grocery',bd = 10,relief = GROOVE,bg = bg_color,fg = "gold",font = ("times new roman",13,"bold"))
        F2.place(x = 330,y = 180,width = 325,height = 380)

        #===========Frame Content
        rice_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Rice")
        rice_lbl.grid(row = 0,column = 0,padx = 10,pady = 20)
        rice_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.rice)
        rice_en.grid(row = 0,column = 1,ipady = 5,ipadx = 5)

        #=======
        oil_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Food Oil")
        oil_lbl.grid(row = 1,column = 0,padx = 10,pady = 20)
        oil_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.food_oil)
        oil_en.grid(row = 1,column = 1,ipady = 5,ipadx = 5)

        #=======
        daal_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Daal")
        daal_lbl.grid(row = 2,column = 0,padx = 10,pady = 20)
        daal_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.daal)
        daal_en.grid(row = 2,column = 1,ipady = 5,ipadx = 5)

        #========
        wheat_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Wheat")
        wheat_lbl.grid(row = 3,column = 0,padx = 10,pady = 20)
        wheat_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.wheat)
        wheat_en.grid(row = 3,column = 1,ipady = 5,ipadx = 5)

        #============
        sugar_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Sugar")
        sugar_lbl.grid(row = 4,column = 0,padx = 10,pady = 20)
        sugar_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.sugar)
        sugar_en.grid(row = 4,column = 1,ipady = 5,ipadx = 5)

        #==================Other Stuff=====================#

        F2 = LabelFrame(self.root,text = 'Others',bd = 10,relief = GROOVE,bg = bg_color,fg = "gold",font = ("times new roman",13,"bold"))
        F2.place(x = 655,y = 180,width = 325,height = 380)

        #===========Frame Content
        maza_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Maza")
        maza_lbl.grid(row = 0,column = 0,padx = 10,pady = 20)
        maza_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.maza)
        maza_en.grid(row = 0,column = 1,ipady = 5,ipadx = 5)

        #=======
        cock_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Coke")
        cock_lbl.grid(row = 1,column = 0,padx = 10,pady = 20)
        cock_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.coke)
        cock_en.grid(row = 1,column = 1,ipady = 5,ipadx = 5)

        #=======
        frooti_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Frooti")
        frooti_lbl.grid(row = 2,column = 0,padx = 10,pady = 20)
        frooti_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.frooti)
        frooti_en.grid(row = 2,column = 1,ipady = 5,ipadx = 5)

        #========
        cold_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Nimkos")
        cold_lbl.grid(row = 3,column = 0,padx = 10,pady = 20)
        cold_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.nimko)
        cold_en.grid(row = 3,column = 1,ipady = 5,ipadx = 5)

        #============
        bis_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Biscuits")
        bis_lbl.grid(row = 4,column = 0,padx = 10,pady = 20)
        bis_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.biscuits)
        bis_en.grid(row = 4,column = 1,ipady = 5,ipadx = 5)

        #===================Bill Aera================#
        F3 = Label(self.root,bd = 10,relief = GROOVE)
        F3.place(x = 960,y = 180,width = 365,height = 380)
        #===========
        bill_title = Label(F3,text = "Bill Area",font = ("Lucida",13,"bold"),bd= 7,relief = GROOVE)
        bill_title.pack(fill = X)

        #============
        scroll_y = Scrollbar(F3,orient = VERTICAL)
        self.txt = Text(F3,yscrollcommand = scroll_y.set)
        scroll_y.pack(side = RIGHT,fill = Y)
        scroll_y.config(command = self.txt.yview)
        self.txt.pack(fill = BOTH,expand = 1)

        #===========Buttons Frame=============#
        F4 = LabelFrame(self.root,text = 'Bill Menu',bd = 10,relief = GROOVE,bg = bg_color,fg = "gold",font = ("times new roman",13,"bold"))
        F4.place(x = 0,y = 560,relwidth = 1,height = 145)

        #===================
        cosm_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Total Cosmetics")
        cosm_lbl.grid(row = 0,column = 0,padx = 10,pady = 0)
        cosm_en = Entry(F4,bd = 8,relief = GROOVE,textvariable = self.total_cosmetics)
        cosm_en.grid(row = 0,column = 1,ipady = 2,ipadx = 5)

        #===================
        gro_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Total Grocery")
        gro_lbl.grid(row = 1,column = 0,padx = 10,pady = 5)
        gro_en = Entry(F4,bd = 8,relief = GROOVE,textvariable = self.total_grocery)
        gro_en.grid(row = 1,column = 1,ipady = 2,ipadx = 5)

        #================
        oth_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Others Total")
        oth_lbl.grid(row = 2,column = 0,padx = 10,pady = 5)
        oth_en = Entry(F4,bd = 8,relief = GROOVE,textvariable = self.total_other)
        oth_en.grid(row = 2,column = 1,ipady = 2,ipadx = 5)

        #================
        cosmt_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Cosmetics Tax")
        cosmt_lbl.grid(row = 0,column = 2,padx = 30,pady = 0)
        cosmt_en = Entry(F4,bd = 8,relief = GROOVE,textvariable = self.tax_cos)
        cosmt_en.grid(row = 0,column = 3,ipady = 2,ipadx = 5)

        #=================
        grot_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Grocery Tax")
        grot_lbl.grid(row = 1,column = 2,padx = 30,pady = 5)
        grot_en = Entry(F4,bd = 8,relief = GROOVE,textvariable = self.tax_groc)
        grot_en.grid(row = 1,column = 3,ipady = 2,ipadx = 5)

        #==================
        otht_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Others Tax")
        otht_lbl.grid(row = 2,column = 2,padx = 10,pady = 5)
        otht_en = Entry(F4,bd = 8,relief = GROOVE,textvariable = self.tax_other)
        otht_en.grid(row = 2,column = 3,ipady = 2,ipadx = 5)

        #====================
        total_btn = Button(F4,text = "Total",bg = bg_color,fg = fg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command = self.total)
        total_btn.grid(row = 1,column = 4,ipadx = 20,padx = 30)

        #====================
        print_btn = Button(F4,text = "Print",bg = bg_color,fg = fg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command = self.print_bill)
        print_btn.grid(row = 1,column = 5,ipadx = 10)

        #========================
        genbill_btn = Button(F4,text = "Generate Bill",bg = bg_color,fg = fg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command = self.bill_area)
        genbill_btn.grid(row = 1,column = 6,ipadx = 10,padx = 30)

        #====================
        clear_btn = Button(F4,text = "Clear",bg = bg_color,fg = fg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command = self.clear)
        clear_btn.grid(row = 1,column = 7,ipadx = 10)

        #======================
        email_btn = Button(F4,text = "Email",bg = bg_color,fg = fg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command = self.email)
        email_btn.grid(row = 1,column = 8,ipadx = 10,padx = 30)

#Function to get total prices
    def total(self):
        #=================Total Cosmetics Prices
        self.total_cosmetics_prices = (
            (self.bath_soap.get() * 40)+
            (self.face_cream.get() * 140)+
            (self.face_wash.get() * 240)+
            (self.hair_spray.get() * 340)+
            (self.body_lotion.get() * 260)
        )
        self.total_cosmetics.set("Rs. "+str(self.total_cosmetics_prices))
        self.tax_cos.set("Rs. "+str(round(self.total_cosmetics_prices*0.05)))
        #====================Total Grocery Prices
        self.total_grocery_prices = (
            (self.wheat.get()*100)+
            (self.food_oil.get() * 180)+
            (self.daal.get() * 80)+
            (self.rice.get() *80)+
            (self.sugar.get() * 170)

        )
        self.total_grocery.set("Rs. "+str(self.total_grocery_prices))
        self.tax_groc.set("Rs. "+str(round(self.total_grocery_prices*0.05)))
        #======================Total Other Prices
        self.total_other_prices = (
            (self.maza.get() * 20)+
            (self.frooti.get() * 50)+
            (self.coke.get() * 60)+
            (self.nimko.get() * 20)+
            (self.biscuits.get() * 20)
        )
        self.total_other.set("Rs. "+str(self.total_other_prices))
        self.tax_other.set("Rs. "+str(round(self.total_other_prices*0.05)))


#Function For Text Area
    def welcome_soft(self):
        self.txt.delete('1.0',END)
        self.txt.insert(END,"       Welcome To DAIICT's Retail \n")
        self.txt.insert(END,f"\nBill No. : {str(self.c_bill_no.get())}")
        self.txt.insert(END,f"\nCustomer Name : {str(self.cus_name.get())}")
        self.txt.insert(END,f"\nPhone No. : {str(self.c_phone.get())}")
        self.txt.insert(END,"\n========================================")
        self.txt.insert(END,"\nProduct          Qty         Price")
        self.txt.insert(END,"\n========================================")

#Function to clear the bill area
    def clear(self):
        self.txt.delete('1.0',END)

    def search_bill(self):
        for i in os.listdir('bills/'):
            if i.split('.')[0]==self.cbill_en.get():
                f=open(f'bills/{i}','r')
                self.txt.delete(1.0,END)
                for data in f:
                    self.txt.insert(END,data)
                f.close()
                break
        else:
            messagebox.showerror('Error','Invalid Bill Number')

    def print_bill(self):
        if self.txt.get(1.0,END)=='\n':
            messagebox.showerror('Error','Bill is empty')
        else:
            file = tempfile.mktemp('.txt')
            open(file,'w').write(self.txt.get(1.0,END))
            os.startfile(file,'print')
        


    def save_bill(self):
        if not os.path.exists('bills'):
            os.mkdir('bills')
        result = messagebox.askyesno('Confirm','Do you want to save the bill?')
        if result:
            bill_content=self.txt.get(1.0,END)
            file=open(f'bills/{self.x}.txt','w')
            file.write(bill_content)
            file.close()
            messagebox.showinfo('Success',f'Bill number {self.x} is saved successfully')
            self.x=random.randint(500,1000)
            # self.c_bill_no.set(str(self.x))
#Add Product name , qty and price to bill area
    def bill_area(self):
        # Sample data
        data = [
            [self.c_bill_no,'08-09-23', self.cus_name.get(), self.city.get(), str(self.c_phone.get()), 'Face Wash', 'Cosmetics', self.bath_soap.get() +
            self.face_cream.get()+
            self.face_wash.get()+
            self.hair_spray.get()+
            self.body_lotion.get()+
            self.wheat.get()+
            self.food_oil.get()+
            self.daal.get()+
            self.rice.get()+
            self.sugar.get()+
            self.maza.get()+
            self.frooti.get()+
            self.coke.get()+
            self.nimko.get()+
            self.biscuits.get(), 35, self.total_cosmetics_prices]
        ]

        # Define column names
        # columns = ['ID', 'Date', 'Customer Name', 'City', 'Phone Number', 'Product', 'Category', 'Quantity', 'Unit Price', 'Total Price']

        excel_filename = "C:/Users/Kushal/Desktop/daiict/python/project/retail_dataset1.csv"

# Create a DataFrame from the data
        df = pd.DataFrame(data)

        # try:
        #     # Try to read the existing data from the Excel file
        #     existing_df = pd.read_csv(excel_filename)

        #     # If successful, append the new data to the existing DataFrame
        #     # df = pd.concat([existing_df, df])
        # except FileNotFoundError:
        #     # If the file doesn't exist, we'll just use the new data
        #     pass
        # df.to_csv(excel_filename, index=False)
        # print(f'Data saved to {excel_filename}')

        self.welcome_soft()
        if self.bath_soap.get() != 0:
            self.txt.insert(END,f"\nBath Soap         {self.bath_soap.get()}           {self.bath_soap.get() * 40}")
        if self.face_cream.get() != 0:
            self.txt.insert(END,f"\nFace Cream        {self.face_cream.get()}           {self.face_cream.get() * 140}")
        if self.face_wash.get() != 0:
            self.txt.insert(END,f"\nFace Wash         {self.face_wash.get()}           {self.face_wash.get() * 240}")
        if self.hair_spray.get() != 0:
            self.txt.insert(END,f"\nHair Spray        {self.hair_spray.get()}           {self.hair_spray.get() * 340}")
        if self.body_lotion.get() != 0 :
            self.txt.insert(END,f"\nBody Lotion       {self.body_lotion.get()}           {self.body_lotion.get() * 260}")
        if self.wheat.get() != 0:
            self.txt.insert(END,f"\nWheat             {self.wheat.get()}           {self.wheat.get() * 100}")
        if self.food_oil.get() != 0:
            self.txt.insert(END,f"\nFood Oil          {self.food_oil.get()}           {self.food_oil.get() * 180}")
        if self.daal.get() != 0:
            self.txt.insert(END,f"\nDaal              {self.daal.get()}           {self.daal.get() * 80}")
        if self.rice.get() != 0:
            self.txt.insert(END,f"\nRice              {self.rice.get()}           {self.rice.get() * 80}")
        if self.sugar.get() != 0:
            self.txt.insert(END,f"\nSugar             {self.sugar.get()}           {self.sugar.get() * 170}")
        if self.maza.get() != 0:
            self.txt.insert(END,f"\nMaza              {self.maza.get()}           {self.maza.get() * 20}")
        if self.frooti.get() != 0:
            self.txt.insert(END,f"\nFrooti            {self.frooti.get()}           {self.frooti.get() * 50}")
        if self.coke.get() != 0:
            self.txt.insert(END,f"\nCoke              {self.coke.get()}           {self.coke.get() * 60}")
        if self.nimko.get() != 0:
            self.txt.insert(END,f"\nNimko             {self.nimko.get()}           {self.nimko.get() * 20}")
        if self.biscuits.get() != 0:
            self.txt.insert(END,f"\nBiscuits          {self.biscuits.get()}           {self.biscuits.get() * 20}")
        self.txt.insert(END,"\n=========================================")
        self.txt.insert(END,f"\n                      Total(with Tax) : {self.total_cosmetics_prices+self.total_grocery_prices+self.total_other_prices+self.total_cosmetics_prices * 0.05+self.total_grocery_prices * 0.05+self.total_other_prices * 0.05}")
        self.save_bill()


    def email(self):
        def send_gmail():
            try:
                ob =smtplib.SMTP("smtp.gmail.com",587)
                ob.starttls()

                ob.set_debuglevel(1)
                
                useEmail= "202318006@daiict.ac.in"

                subject = "Subject of your email"
                headers = f"Subject: {subject}\nFrom: {useEmail}\nTo: {emailAdressrentryEntry.get()}\n"
                ob.login(useEmail,'ddbv rmgx zaiq hmmj')
                messague = self.txt.get(1.0,END)
                email_content = headers + "\n" + messague
                ob.sendmail(useEmail, emailAdressrentryEntry.get(),email_content)
            
                ob.quit()
                messagebox.showinfo('Sucess','Bill is succesfully send!')
            except:
                messagebox.showerror('Error','Bill is Empty')

            
        #  if textarea.get(1.0,END) == '\n':
        #     messagebox.showerror('Error','Bill is Empty')
        #  else:
        root1 = Toplevel()
        root1.config(bg='#074463')
        root1.title('Send Email')
        root1.resizable(0,0)

        senderFrame = LabelFrame(root1,text='SENDER',font=("Segoe UI",15,'bold'),bg='#074463',fg='white',bd=5, relief= GROOVE)
        senderFrame.grid(row = 0, column=0,padx=40, pady=20)

        senderLabel = Label(senderFrame, text="Sender's Email:",font=("Segoe UI",12,'bold'),bg= 'chartreuse3')
        senderLabel.grid(row=0,column=0, padx= 10, pady= 8)

        senderentry = Entry(senderFrame,bd=2, width= 23,font=("Segoe UI",14), relief= GROOVE)
        senderentry.insert(0, "202318006@daiict.ac.in")
        senderentry.grid(row=0, column=1, padx= 10, pady= 8)

        passwordLabel = Label(senderFrame, text="Password",font=("Segoe UI",12,'bold'),bg= 'chartreuse3')
        passwordLabel.grid(row=1,column=0, padx= 10, pady= 8)

        passwordentry = Entry(senderFrame,bd=2, width= 23,font=("Segoe UI",14), relief= GROOVE,show='*')
        passwordentry.grid(row=1, column=1, padx= 10, pady= 8)

        recipientFrame = LabelFrame(root1,text='RECIPIENT',font=("Segoe UI",15,'bold'),bg='#074463',bd=5, relief= GROOVE,fg='white')
        recipientFrame.grid(row = 1, column=0,padx=40, pady=20)

        emailAdressLabel = Label(recipientFrame, text="Email Address:",font=("Segoe UI",12,'bold'),bg= 'chartreuse3')
        emailAdressLabel.grid(row=0,column=0, padx= 10, pady= 8)

        emailAdressrentryEntry = Entry(recipientFrame,bd=2, width= 23,font=("Segoe UI",14), relief= GROOVE)
        emailAdressrentryEntry.grid(row=0, column=1, padx= 10, pady= 8)

        # messagueLabel =  Label(recipientFrame, text="Message:",font=("Segoe UI",12,'bold'),bg= '#0744633')
        # messagueLabel.grid(row=1, column=0, padx= 10, pady= 8)

        # messageArea = Text(recipientFrame,font=("Segoe UI",12,'bold'), bd =2 , relief=SUNKEN,width=42,height=11)
        # messageArea.grid(row=2, column=0, columnspan=2)
        # messageArea.insert(END,'/t/t***** Welcome *****')
        # messageArea.insert(END,f'\n Bill Number: {self.c_bill_no}')
        # messageArea.insert(END,f'\n Custome Name: {self.cus_name.get()}')
        # messageArea.insert(END,f'\n Phone Number: {self.c_phone.get()}')   
        # messageArea.insert(END,'\n' +'='*34)
        # messageArea.insert(END,'\n Products /t/t QTY /t  Price')
        # messageArea.insert(END,'\n'+ '='*34 +'\n')
        # messageArea.delete(1.0,END)
        # messageArea.insert(END,self.txt.get(1.0,END).replace('=','').replace('-','').replace('/t/t/t','/t/t'))
        messagueLabel =  Label(recipientFrame, text="Message:",font=("Segoe UI",12,'bold'),bg= 'chartreuse3')
        messagueLabel.grid(row=1, column=0, padx= 10, pady= 8)

        messageArea = Text(recipientFrame,font=("Segoe UI",12,'bold'), bd =2 , relief=SUNKEN,width=42,height=11)
        messageArea.grid(row=2, column=0, columnspan=2)
        messageArea.insert(END,'/t/t***** Welcome *****')
        messageArea.insert(END,f'\n Bill Number: {self.c_bill_no}')
        messageArea.insert(END,f'\n Custome Name: {self.cus_name.get()}')
        messageArea.insert(END,f'\n Phone Number: {self.c_phone.get()}')    
        messageArea.insert(END,'\n' +'='*34)
        messageArea.insert(END,'\n Products /t/t QTY /t  Price')
        messageArea.insert(END,'\n'+ '='*34 +'\n')        
        messageArea.insert(END,self.txt.get(1.0,END).replace('=','.').replace('-','.').replace('/t/t/t','/t/t'))
        

        # TaxsList = {'comestictTaxLEntry':['Comestic Tax',self.tax_cos],'groceryTaxLEntry':['Grocery Tax',self.tax_groc],
        #         'Other TaxEntry':['Other Tax',self.tax_other]}
        # for tax_entry, (display_NameTax,Taxs) in TaxsList.items():
        #     entrytax = globals().get(tax_entry)
        #     if entrytax is not None and Taxs != 0:
        #         messageArea.insert(END,f"{display_NameTax}: Rs {Taxs} \n")
        # messageArea.insert(END,f"\n Total Bill with Tax: Rs {Taxs}")
        
        sendButton = Button(recipientFrame, text= 'SEND', font=('Segoe UI',15,'bold'),bd=5,relief=GROOVE,command= send_gmail)
        sendButton.grid(row=3,column=0, columnspan= 2, padx=5)
        root1.mainloop()

        
        

root = Tk()
object = Bill_App(root)
root.mainloop()



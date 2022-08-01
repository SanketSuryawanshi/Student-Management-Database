# /////////////////////////  STUDENT DATABASE MANAGEMENT SYSTEM /////////////////////// #


# /////////////////////////////// Importing Modules /////////////////////////////////////// #
import time
from tkinter import *
from tkinter import Toplevel
from tkinter import messagebox as msg
from tkinter.ttk import Treeview
from tkinter import ttk
import random

# ///////////////////////////////////////////////  Function  ////////////////////////////////////////// #


# ///////////////////////////////////////////////  SQL dataBase Connect   ////////////////////////////////////////// #

def CONNECTDATABASE():
    pass


# //////////////////////////////////////// ADD DELETE UPDATE TOP LEVEL COMMAND  => DGBOX()  GUI Only  ////////////////////////////////////#

def ADD():

    # ///////////////////////////////////////////////  ADD STUDENT DATABASE CODE  ////////////////////////////////////////// #
    def SUBMITADDDB():
        print("ADD")

    # //////////////////////// Basic GUI //////////////////////////#
    addRoot = Toplevel(master=DataEnteryFrame)
    addRoot.grab_set()
    addRoot.focus_set()
    addRoot.geometry("470x470+220+200")
    addRoot.wm_iconbitmap("student.ico")
    addRoot.title("Add Student To DataBase")
    addRoot.configure()
    addRoot.resizable(False,False)
    addRoot.configure(bg="blue")

    # //////////////////////// Labesl ////////////////////////// #

    idLabel = Label(addRoot,text="Enter ID :",bg="gold",font="roman 20 bold",relief=GROOVE,bd=5,width=12)
    idLabel.place(x=10,y=10)

    NameLabel = Label(addRoot,text="Enter Name :",bg="gold",font="roman 20 bold",relief=GROOVE,bd=5,width=12)
    NameLabel.place(x=10,y=70)

    iMobileLabel = Label(addRoot,text="Enter Mobile :",bg="gold",font="roman 20 bold",relief=GROOVE,bd=5,width=12)
    iMobileLabel.place(x=10,y=130)

    EmailLabel = Label(addRoot,text="Enter Email :",bg="gold",font="roman 20 bold",relief=GROOVE,bd=5,width=12)
    EmailLabel.place(x=10,y=190)

    AdressLabel = Label(addRoot,text="Enter Adress :",bg="gold",font="roman 20 bold",relief=GROOVE,bd=5,width=12)
    AdressLabel.place(x=10,y=250)

    GenderLabel = Label(addRoot,text="Enter Gender :",bg="gold",font="roman 20 bold",relief=GROOVE,bd=5,width=12)
    GenderLabel.place(x=10,y=310)

    DOBLabel = Label(addRoot,text="Enter DOB :",bg="gold",font="roman 20 bold",relief=GROOVE,bd=5,width=12)
    DOBLabel.place(x=10,y=370)

    # /////////////////////////////////////// Buttons ////////////////////////////////////// #
    idVar = IntVar()
    idVar.set("")
    NameVar = StringVar()
    MobileVar = StringVar()
    EmailVar = StringVar()
    AddressVar = StringVar()
    GenderVar = StringVar()
    DOBVar = StringVar()


    idEntry = Entry(addRoot, font="roman 16  bold",bd=5,textvariable=idVar)
    idEntry.place(x=230,y=10)

    NameEntry = Entry(addRoot, font="roman 16  bold",bd=5,textvariable=NameVar)
    NameEntry.place(x=230,y=70)

    MobileEntry = Entry(addRoot, font="roman 16  bold",bd=5,textvariable=MobileVar)
    MobileEntry.place(x=230,y=130)

    EmailEntry = Entry(addRoot, font="roman 16  bold",bd=5,textvariable=EmailVar)
    EmailEntry.place(x=230,y=190)

    AddressEntry = Entry(addRoot, font="roman 16  bold",bd=5,textvariable=AddressVar)
    AddressEntry.place(x=230,y=250)

    GenderEntry = Entry(addRoot, font="roman 16  bold",bd=5,textvariable=GenderVar)
    GenderEntry.place(x=230,y=310)

    DOBEntry = Entry(addRoot, font="roman 16  bold",bd=5,textvariable=DOBVar)
    DOBEntry.place(x=230,y=370)

    SubmitADDDB = Button(addRoot,text="Add Student",font="roman 15 bold",
              relief=RIDGE, bd=5, bg="red", width=23,fg="blue",activebackground="blue",activeforeground="white",command=SUBMITADDDB)
    SubmitADDDB.place(x=150,y=420)
 
    addRoot.mainloop()

def SEARCH():
    print("Student SEARCH")
    # ///////////////////////////////////////////////  SERACH STUDENT DATABASE CODE  ////////////////////////////////////////// #
    def SUBMITSEARCHDB():
        print("Search")

    # //////////////////////// Basic GUI //////////////////////////#
    SearchRoot = Toplevel(master=DataEnteryFrame)
    SearchRoot.grab_set()
    SearchRoot.focus_set()
    SearchRoot.geometry("470x540+220+200")
    SearchRoot.wm_iconbitmap("student.ico")
    SearchRoot.title("Search Student To DataBase")
    SearchRoot.configure()
    SearchRoot.resizable(False,False)
    SearchRoot.configure(bg="firebrick")

    # //////////////////////// Labesl ////////////////////////// #

    idLabel = Label(SearchRoot,text="Enter ID :",bg="gold",font="roman 20 bold",relief=GROOVE,bd=5,width=12)
    idLabel.place(x=10,y=10)

    NameLabel = Label(SearchRoot,text="Enter Name :",bg="gold",font="roman 20 bold",relief=GROOVE,bd=5,width=12)
    NameLabel.place(x=10,y=70)

    iMobileLabel = Label(SearchRoot,text="Enter Mobile :",bg="gold",font="roman 20 bold",relief=GROOVE,bd=5,width=12)
    iMobileLabel.place(x=10,y=130)

    EmailLabel = Label(SearchRoot,text="Enter Email :",bg="gold",font="roman 20 bold",relief=GROOVE,bd=5,width=12)
    EmailLabel.place(x=10,y=190)

    AdressLabel = Label(SearchRoot,text="Enter Adress :",bg="gold",font="roman 20 bold",relief=GROOVE,bd=5,width=12)
    AdressLabel.place(x=10,y=250)

    GenderLabel = Label(SearchRoot,text="Enter Gender :",bg="gold",font="roman 20 bold",relief=GROOVE,bd=5,width=12)
    GenderLabel.place(x=10,y=310)

    DateLabel = Label(SearchRoot,text="Enter Date :",bg="gold",font="roman 20 bold",relief=GROOVE,bd=5,width=12)
    DateLabel.place(x=10,y=370)

    DOBLabel = Label(SearchRoot,text="Enter DOB :",bg="gold",font="roman 20 bold",relief=GROOVE,bd=5,width=12)
    DOBLabel.place(x=10,y=440)

    # /////////////////////////////////////// Buttons ////////////////////////////////////// #
    idVar = IntVar()
    idVar.set("")
    NameVar = StringVar()
    MobileVar = StringVar()
    EmailVar = StringVar()
    AddressVar = StringVar()
    GenderVar = StringVar()
    DOBVar = StringVar()
    DateVar = StringVar()


    idEntry = Entry(SearchRoot, font="roman 16  bold",bd=5,textvariable=idVar)
    idEntry.place(x=230,y=10)

    NameEntry = Entry(SearchRoot, font="roman 16  bold",bd=5,textvariable=NameVar)
    NameEntry.place(x=230,y=70)

    MobileEntry = Entry(SearchRoot, font="roman 16  bold",bd=5,textvariable=MobileVar)
    MobileEntry.place(x=230,y=130)

    EmailEntry = Entry(SearchRoot, font="roman 16  bold",bd=5,textvariable=EmailVar)
    EmailEntry.place(x=230,y=190)

    AddressEntry = Entry(SearchRoot, font="roman 16  bold",bd=5,textvariable=AddressVar)
    AddressEntry.place(x=230,y=250)

    GenderEntry = Entry(SearchRoot, font="roman 16  bold",bd=5,textvariable=GenderVar)
    GenderEntry.place(x=230,y=310)

    DOBEntry = Entry(SearchRoot, font="roman 16  bold",bd=5,textvariable=DOBVar)
    DOBEntry.place(x=230,y=440)

    DateEntery = Entry(SearchRoot, font="roman 16  bold",bd=5,textvariable=DateVar)
    DateEntery.place(x=230,y=370)

    SubmitSearchDB = Button(SearchRoot,text="Seach Student",font="roman 15 bold",
              relief=RIDGE, bd=5, bg="red", width=23,fg="blue",activebackground="blue",activeforeground="white",command=SUBMITSEARCHDB)
    SubmitSearchDB.place(x=150,y=490)
 
    SearchRoot.mainloop()

def DELETE():
    print("Student DELETE")

def UPDATE():
    print("Student UPDATE")
     # ///////////////////////////////////////////////  UPDATE STUDENT DATABASE CODE  ////////////////////////////////////////// #
    def SUBMITUPDATEDB():
        print("UPDTAE")

    # //////////////////////// Basic GUI //////////////////////////#
    UpdateRoot = Toplevel(master=DataEnteryFrame)
    UpdateRoot.grab_set()
    UpdateRoot.focus_set()
    UpdateRoot.geometry("470x590+220+150")
    UpdateRoot.wm_iconbitmap("student.ico")
    UpdateRoot.title("UPpdate Student To DataBase")
    UpdateRoot.configure()
    UpdateRoot.resizable(False,False)
    UpdateRoot.configure(bg="firebrick1")

    # //////////////////////// Labesl ////////////////////////// #

    idLabel = Label(UpdateRoot,text="Enter ID :",bg="gold",font="roman 20 bold",relief=GROOVE,bd=5,width=12)
    idLabel.place(x=10,y=10)

    NameLabel = Label(UpdateRoot,text="Enter Name :",bg="gold",font="roman 20 bold",relief=GROOVE,bd=5,width=12)
    NameLabel.place(x=10,y=70)

    iMobileLabel = Label(UpdateRoot,text="Enter Mobile :",bg="gold",font="roman 20 bold",relief=GROOVE,bd=5,width=12)
    iMobileLabel.place(x=10,y=130)

    EmailLabel = Label(UpdateRoot,text="Enter Email :",bg="gold",font="roman 20 bold",relief=GROOVE,bd=5,width=12)
    EmailLabel.place(x=10,y=190)

    AdressLabel = Label(UpdateRoot,text="Enter Adress :",bg="gold",font="roman 20 bold",relief=GROOVE,bd=5,width=12)
    AdressLabel.place(x=10,y=250)

    GenderLabel = Label(UpdateRoot,text="Enter Gender :",bg="gold",font="roman 20 bold",relief=GROOVE,bd=5,width=12)
    GenderLabel.place(x=10,y=310)

    DateLabel = Label(UpdateRoot,text="Enter Date :",bg="gold",font="roman 20 bold",relief=GROOVE,bd=5,width=12)
    DateLabel.place(x=10,y=370)

    DOBLabel = Label(UpdateRoot,text="Enter DOB :",bg="gold",font="roman 20 bold",relief=GROOVE,bd=5,width=12)
    DOBLabel.place(x=10,y=440)

    UpdateTime = Label(UpdateRoot,text="Enter Time :",bg="gold",font="roman 20 bold",relief=GROOVE,bd=5,width=12)
    UpdateTime.place(x=10,y=490)

    # /////////////////////////////////////// Buttons ////////////////////////////////////// #
    idVar = IntVar()
    idVar.set("")
    NameVar = StringVar()
    MobileVar = StringVar()
    EmailVar = StringVar()
    AddressVar = StringVar()
    GenderVar = StringVar()
    DOBVar = StringVar()
    DateVar = StringVar()
    TimeVar = StringVar()


    idEntry = Entry(UpdateRoot, font="roman 16  bold",bd=5,textvariable=idVar)
    idEntry.place(x=230,y=10)

    NameEntry = Entry(UpdateRoot, font="roman 16  bold",bd=5,textvariable=NameVar)
    NameEntry.place(x=230,y=70)

    MobileEntry = Entry(UpdateRoot, font="roman 16  bold",bd=5,textvariable=MobileVar)
    MobileEntry.place(x=230,y=130)

    EmailEntry = Entry(UpdateRoot, font="roman 16  bold",bd=5,textvariable=EmailVar)
    EmailEntry.place(x=230,y=190)

    AddressEntry = Entry(UpdateRoot, font="roman 16  bold",bd=5,textvariable=AddressVar)
    AddressEntry.place(x=230,y=250)

    GenderEntry = Entry(UpdateRoot, font="roman 16  bold",bd=5,textvariable=GenderVar)
    GenderEntry.place(x=230,y=310)

    DateEntery = Entry(UpdateRoot, font="roman 16  bold",bd=5,textvariable=DateVar)
    DateEntery.place(x=230,y=370)

    DOBEntry = Entry(UpdateRoot, font="roman 16  bold",bd=5,textvariable=DOBVar)
    DOBEntry.place(x=230,y=440)

    TimeEntery = Entry(UpdateRoot, font="roman 16  bold",bd=5,textvariable=TimeVar)
    TimeEntery.place(x=230,y=490)

    SubmitUpadteDB = Button(UpdateRoot,text="Search Student",font="roman 15 bold",
              relief=RIDGE, bd=5, bg="lawn green", width=23,fg="blue",activebackground="blue",activeforeground="white",command=SUBMITUPDATEDB)
    SubmitUpadteDB.place(x=150,y=540)
 
    UpdateRoot.mainloop()


def SHOWALL():
    print("Student SHOWALL")

def EXPORTDATA():
    print("Student EXPORT")

def EXIT():
    res = msg.askyesno(title="Notification",message="Do You Want To Exit ?")
    if(res==True):
        print("Student EXIT")
        root.destroy()


# ///////////////////////////////////////////////  GUI dataBase Connect   ////////////////////////////////////////// #

def ConnectDB():

    # //////////////////////////// Basic GUI //////////////////////////////#
    DBroot = Toplevel()
    DBroot.grab_set()
    DBroot.focus_set()
    DBroot.geometry("470x250+800+230")
    DBroot.wm_iconbitmap("student.ico")
    DBroot.title("Connect To DataBase")
    DBroot.configure()
    DBroot.resizable(False,False)
    DBroot.configure(bg="blue")

    # ////////////////////////////// Labels ///////////////////////////////////// #

    Host = Label(DBroot, text="Enter Host :", font="times 20  bold",
                    relief=GROOVE, bd=3, bg="gold2", width=13)
    Host.place(x=10,y=10)

    User = Label(DBroot, text="Enter User :", font="times 20  bold",
                    relief=GROOVE, bd=3, bg="gold2", width=13)
    User.place(x=10,y=70)
    
    Password = Label(DBroot, text="Enter Password :", font="times 20  bold",
                    relief=GROOVE, bd=3, bg="gold2", width=13)
    Password.place(x=10,y=130)

    # ////////////////////////////// Entry Box ///////////////////////////////////// #

    hostVar = StringVar()
    UserVar = StringVar()
    PasswordVar = StringVar()

    HostEntry = Entry(DBroot, font="roman 16  bold",bd=5,textvariable=hostVar)
    HostEntry.place(x=250,y=10)

    UserEntry = Entry(DBroot, font="roman 16  bold",bd=5,textvariable=UserVar)
    UserEntry.place(x=250,y=70)

    PasswordEntry = Entry(DBroot, font="roman 16  bold",bd=5,textvariable=PasswordVar)
    PasswordEntry.place(x=250,y=130)

    # /////////////////////////////////// Button ////////////////////////////// #
    SubmitDB = Button(DBroot,text="Connect DataBase",font="roman 15 bold",
              relief=RIDGE, bd=5, bg="red", width=23,fg="blue",activebackground="blue",activeforeground="white",command=CONNECTDATABASE)
    SubmitDB.place(x=150,y=190)

    DBroot.mainloop()    

# /////////////////////////////////////////////// Slider  Function  ////////////////////////////////////////// #

colors = ['red','green','blue','pink','gold2','cyan']

def IntroLabel():
    global count, text
    if(count>=len(ss)):
        count=0
        text=""
        sliderLabel.configure(text=text)
    else:
        text = text+ ss[count]
        count = count + 1
        color = random.choice(colors)
        sliderLabel.configure(text=text,fg=color)
    sliderLabel.after(200,IntroLabel)


# ////////////////////////////////////////////////// Time Function ///////////////////////////////////////// #

def TimeFunction():
    time_string = time.strftime("%H:%M:%S")
    date_string = time.strftime("%d/%m/%Y")
    Clock.configure(text=f"Date : {date_string} \n Time : {time_string} ")
    Clock.after(1000,TimeFunction)    


# ///////////////////////////////  Making GUI /////////////////////////////////////// #

# ////////////////////////////////// Making Basic GUI ///////////////////////////////// #

root = Tk()
root.title("STUDENT MANAGEMENT SYSTEM - SANKET")
root.configure(bg="gold2")
root.geometry("1174x700+200+50")
root.resizable(False, False)
root.wm_iconbitmap("student.ico")

# /////////////////////////////////// Frames ////////////////////////////////////////////// #


# /////////////////////////////////// Left Frames ////////////////////////////////////////////// #
DataEnteryFrame = Frame(root, bg="gold2", relief=GROOVE,
                        bd=5, width=500, height=600)
DataEnteryFrame.place(x=10, y=90)

# /////////////////////////////////// Right Frames ////////////////////////////////////////////// #
ShowDataFrame = Frame(root, bg="white", relief=GROOVE,
                      bd=5, width=600, height=600)
ShowDataFrame.place(x=550, y=90)
# ShowDataFrame.columnconfigure(2,weight=1)
# ShowDataFrame.rowconfigure(1,weight=1)

# ////////////////////////////////// Making GUI Timestamp ///////////////////////////////// #
Clock = Label(root, text="", font="times 14 bold",
              relief=RIDGE, bd=5, bg="lawn green", width=20)
Clock.place(x=10, y=10)
TimeFunction()

# ////////////////////////////////// Making GUI Title SlideBar ///////////////////////////////// #
count = 0
ss = "Welcome To Student Management System"
text=""
sliderLabel = Label(root, text="", font="chiller 30 italic bold",
                    relief=RIDGE, bd=5, bg="cyan", width=35)
sliderLabel.place(x=260, y=10)
IntroLabel()

# ////////////////////////////////// Making GUI  Connect To DataBase ///////////////////////////////// #
DataBaseConnect = Button(root,text="Connect DataBase",font="chiller 20  italic bold",
              relief=RIDGE, bd=5, bg="lawn green", width=23,fg="orange",activebackground="blue",activeforeground="white",command=ConnectDB)
DataBaseConnect.place(x=890,y=10)


# /////////////////////////////////////////////// Frame DataEntery Left Frame Buttons  /////////////////////////////////////////////// #

AddStudent = Button(DataEnteryFrame,text=" 1. Add Student",font="roman 20 bold",
              relief=RIDGE, bd=5, bg="lightblue", width=23,fg="orange",activebackground="blue",activeforeground="white",command=ADD)
AddStudent.place(x=50,y=30)

SearchStudent = Button(DataEnteryFrame,text="2. Search Student",font="roman 20 bold",
              relief=RIDGE, bd=5, bg="lightblue", width=23,fg="orange",activebackground="blue",activeforeground="white",command=SEARCH)
SearchStudent.place(x=50,y=100)

DeleteStudent = Button(DataEnteryFrame,text="3. Delete Student",font="roman 20 bold",
              relief=RIDGE, bd=5, bg="lightblue", width=23,fg="orange",activebackground="blue",activeforeground="white",command=DELETE)
DeleteStudent.place(x=50,y=170)

UpdateStudent = Button(DataEnteryFrame,text="4. Update Student",font="roman 20 bold",
              relief=RIDGE, bd=5, bg="lightblue", width=23,fg="orange",activebackground="blue",activeforeground="white",command=UPDATE)
UpdateStudent.place(x=50,y=240)

ShowAll = Button(DataEnteryFrame,text="5. Show All",font="roman 20 bold",
              relief=RIDGE, bd=5, bg="lightblue", width=23,fg="orange",activebackground="blue",activeforeground="white",command=SHOWALL)
ShowAll.place(x=50,y=310)

ExportData = Button(DataEnteryFrame,text="6. Export Data",font="roman 20 bold",
              relief=RIDGE, bd=5, bg="lightblue", width=23,fg="orange",activebackground="blue",activeforeground="white",command=EXPORTDATA)
ExportData.place(x=50,y=380)

Exit = Button(DataEnteryFrame,text="7. Exit",font="roman 20 bold",
              relief=RIDGE, bd=5, bg="lightblue", width=23,fg="orange",activebackground="blue",activeforeground="white",command=EXIT)
Exit.place(x=50,y=450)

DeveloperLabel = Label(DataEnteryFrame, text="Developer - SANKET", font="roman 18  bold",
                    relief=RIDGE, bd=5, bg="cyan", width=25)
DeveloperLabel.place(x=150, y=540)



# /////////////////////////////////////////////// Frame ShowDataFrame Right Frame  /////////////////////////////////////////////// #
style = ttk.Style()
style.configure('Treeview.Heading',font="chiller 20 bold",foreground="blue")

# /////////////////////////////////////////// tree View ///////////////////////////////////////////#
StudentTable = Treeview(ShowDataFrame,columns=('ID','Name','Mobile No','Email','Address','Gender','DOB','Added Date','Added Time'),height=27)

# ///////////////////////////////////////////// Scroll Bar /////////////////////////////////////// #
scroll_x = Scrollbar(ShowDataFrame,orient=HORIZONTAL,command=StudentTable.xview)
scroll_Y = Scrollbar(ShowDataFrame,orient=VERTICAL,command=StudentTable.yview)

scroll_x.pack(side=BOTTOM,fill=X)
scroll_Y.pack(side=RIGHT,fill=Y)

StudentTable.configure(yscrollcommand=scroll_Y.set,xscrollcommand=scroll_x.set)

# ///////////////////////////////////// Header /////////////////////////// #
StudentTable.heading('ID',text="ID")
StudentTable.heading('Name',text="Name")
StudentTable.heading('Mobile No',text="Mobile No")
StudentTable.heading('Address',text="Address")
StudentTable.heading('Gender',text="Gender")
StudentTable.heading('DOB',text="DOB")
StudentTable.heading('Added Date',text="Added Date")
StudentTable.heading('Added Time',text="Added Time")
StudentTable['show'] = 'headings'
# StudentTable.column('ID',width=100)

# StudentTable.pack(side=RIGHT)
StudentTable.place(x=0,y=0)
StudentTable.pack(fill=BOTH,expand=1)

# ////////////////////////////////// Making GUI STOP ///////////////////////////////// #
root.mainloop()

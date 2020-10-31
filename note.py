from tkinter import *
from tkinter import messagebox as m_box
from tkinter import ttk
t=Tk()
t.maxsize(width=1800,height=1800)

n=ttk.Notebook()
n.place(x=0,y=0,width=1800,height=1800)

f1=Frame(bg="cyan")
n.add(f1,text="home")
u=Label(f1,text="WELCOME TO OUR SITE",font=("times new roman",20,"bold"),bg="white",fg="red")
u.place(x=500,y=0)
u=Label(f1,text="Hey Dear Viewers We welcome you to our site we Have 10000 jobs For you",font=("times new roman",20,"bold"),bg="white",fg="green")
u.place(x=250,y=100)
u=Label(f1,text="We Have Jobs which you Like, We Provide you Golden Opertunity",font=("times new roman",20,"bold"),bg="white",fg="green")
u.place(x=250,y=150)
u=Label(f1,text="Hurry Up what are You Waiting For .Start Your Career With Us",font=("times new roman",20,"bold"),bg="white",fg="green")
u.place(x=250,y=200)

u=Label(f1,text="Get Your Dream Jobs Here At One Place.Get Your Job Very Easily. ",font=("times new roman",15,"bold"),bg="white",fg="green")
u.place(x=20,y=300)
u=Label(f1,text="Pay After Your Recuritment Only Else Get Your Money Back.",font=("times new roman",15,"bold"),bg="white",fg="green")
u.place(x=20,y=350)


u=Label(f1,text="Payment Here ",font=("times new roman",20,"bold"),bg="white",fg="green")
u.place(x=200,y=400)
u1=Label(f1,text="Card No",font=("",15))
u1.place(x=200,y=450)
e1=Entry(f1,font=("",12))
e1.place(x=300,y=450,width=200)
u2=Label(f1,text="CVV No",font=("",15))
u2.place(x=200,y=500)
e2=Entry(f1,font=("",12))
e2.place(x=300,y=500,width=120)
def submit():
    m_box.showinfo('sumit','Payment Done Sucessfully')
b1=Button(f1,text="Submit",command=submit)
b1.place(x=300,y=550,width=80,height=40)








f2=Frame(bg="blue")
n.add(f2,text="Search Jobs")
u=Label(f2,text="Right Jobs For You",font=("Algerian",50,"bold"))
u.place(x=20,y=0)
u=Label(f2,text="Airlines job vacancy,",font=("times new roman",20,"bold"),bg="white")
u.place(x=30,y=150)
u=Label(f2,text="REMEMBER WE DO NOT CHARGE YOU FOR YOUR JOB.",font=("times new roman",15,"bold"),bg="white",fg="green")
u.place(x=20,y=300)
u=Label(f2,text="JUST YOU HAVE TO REGISTERED YOURSELF WITH US.",font=("times new roman",15,"bold"),bg="white",fg="green")
u.place(x=20,y=350)
u=Label(f2,text="IF YOU ARE INTEREST AIRLINES THEN THIS IS THE RIGHT PLACE FOR YOU.",font=("times new roman",15,"bold"),bg="white",fg="green")
u.place(x=20,y=400)
u=Label(f2,text="MALE AND FEMALE BOTH CAN APPLY.NOW",font=("times new roman",15,"bold"),bg="white",fg="green")
u.place(x=20,y=450)
u=Label(f2,text=" ARE URGENTLY VACANCY FOR AIRLINES GROUND STAFF DEPARTMENT.",font=("times new roman",15,"bold"),bg="white",fg="green")
u.place(x=20,y=500)
u=Label(f2,text="SO FRESHERS & EXPERIENCE CANDIDATE BOTH CAN APPLY. ",font=("times new roman",15,"bold"),bg="white",fg="green")
u.place(x=20,y=550)
u=Label(f2,text="QUALIFICATION-MINIMUM 10TH PASS OR ABOVE.AGE:-18-32 FOR MALE,18-30",font=("times new roman",15,"bold"),bg="white",fg="green")
u.place(x=20,y=600)
u=Label(f2,text="FEMALEPOST:01.GROUND HANDLING CSASKILL-GOOD COMMUNICATION AND PERSONALITY.",font=("times new roman",15,"bold"),bg="white",fg="green")
u.place(x=20,y=650)
u=Label(f2,text="Minimum Experience : 0 years",font=("times new roman",15,"bold"),bg="white",fg="green")
u.place(x=20,y=700)
u=Label(f2,text="Maximum Experience : 1 years",font=("times new roman",15,"bold"),bg="white",fg="green")
u.place(x=20,y=750)
u=Label(f2,text="Search Jobs Near By You",font=("times new roman",15,"bold"),bg="white")
u.place(x=1100,y=50)
clicked=StringVar()
u=Label(f2,text="SELECT",font=("",15))
u.place(x=1100,y=100)
drop=OptionMenu(f2,clicked,"Jammu&Kashmir","Delhi","Bihar","Andhra Pradesh","Arunachal Pradesh","Assam","Jharkhand","Kerala","Maharashtra","Madhya Pradesh","Gujrat","Rajasthan","Orissa","Goa","West Bengal")
drop.place(x=1200,y=100)
def Click():
    m_box.showinfo('Click','submitted')

b1=Button(f2,text="Click",command=Click)
b1.place(x=1100,y=150,width=80,height=40)

f3=Frame(bg="pink")
n.add(f3,text="Contact us")
u=Label(f3,text="We care You",font=("",50))
u.place(x=600,y=0)

u=Label(f3,text="Contact Information")
u.place(x=100,y=150)
u=Label(f3,text="Mobile No-9021435678")
u.place(x=100,y=200)
u=Label(f3,text="Email Id-techjob@gmail.com")
u.place(x=100,y=250)
u=Label(f3,text="post Comment",font=("",15))
u.place(x=700,y=250)
text=Text(f3)
text.place(x=700,y=300)
def submit():
    m_box.showinfo('submit','Your post is submitted')
b1=Button(f3,text="Submit",command=submit)
b1.place(x=800,y=700,width=80,height=40)


f4=Frame(bg="yellow")
n.add(f4,text="Apply jobs")
u=Label(f4,text="Regisration form",font=("",25))
u.place(x=150,y=30)
u1=Label(f4,text="First Name")
u1.place(x=100,y=80)
e1=Entry(f4,font=("",12))
e1.place(x=200,y=80,width=120)
u2=Label(f4,text="Last Name")
u2.place(x=100,y=130)
e2=Entry(f4,font=("",12))
e2.place(x=200,y=130,width=120)
u3=Label(f4,text="Mobile No")
u3.place(x=100,y=180)
e3=Entry(f4,font=("",12))
e3.place(x=200,y=180,width=150)
u4=Label(f4,text="Email Id")
u4.place(x=100,y=230)
e4=Entry(f4,font=("",12))
e4.place(x=200,y=230,width=180)
i=IntVar()
r1=Radiobutton(f4,text="Male",value=1,variable=i)
r1.place(x=200,y=280)
r2=Radiobutton(f4,text="Female",value=2,variable=i)
r2.place(x=300,y=280)
u4=Label(f4,text="Address")
u4.place(x=100,y=330)
text=Text(f4)
text.place(x=200,y=330,height=200,width=500)

def submit():
    m_box.showinfo('Regis','Do you want to submit')
 
b1=Button(f4,text="Submit",command=submit)
b1.place(x=200,y=600,width=80,height=40)
    
    

t.mainloop()

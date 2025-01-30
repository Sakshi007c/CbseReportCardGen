

from tkinter import *
import mysql.connector
from tkinter import messagebox


def marksheet10():
    mydb = mysql.connector.connect(
        host="localhost", user="root", passwd="sarvangi@123", database="marksheet")
    mycursor = mydb.cursor()
    en = str(e11.get())
    mycursor.execute("select * from marks where ROLL='"+en+"'")
    for i in mycursor:
        ab = i[1]
        b = i[2]
        c = i[3]
        d = i[4]
        e = i[5]
        f = i[6]
        g = i[7]
        if ab+g >= 90:
            zz = 'A'
        elif ab+g >= 80:
            zz = 'B'
        elif ab+g >= 70:
            zz = 'C'
        else:
            zz = 'D'
        if b+g >= 90:
            za = 'A'
        elif b+g >= 80:
            za = 'B'
        elif b+g >= 70:
            za = 'C'
        else:
            za = 'D'
        if c+g >= 90:
            zb = 'A'
        elif c+g >= 80:
            zb = 'B'
        elif c+g >= 70:
            zb = 'C'
        else:
            zb = 'D'
        if d+g >= 90:
            zc = 'A'
        elif d+g >= 80:
            zc = 'B'
        elif d+g >= 70:
            zc = 'C'
        else:
            zc = 'D'
        if e+g >= 90:
            zd = 'A'
        elif e+g >= 80:
            zd = 'B'
        elif e+g >= 70:
            zd = 'C'
        else:
            zd = 'D'
        if f+g >= 90:
            ze = 'A'
        elif f+g >= 80:
            ze = 'B'
        elif f+g >= 70:
            ze = 'C'
        else:
            ze = 'D'
    mycursor2 = mydb.cursor()
    mycursor2.execute("select * from class10 where ROLL='"+en+"'")
    for i in mycursor:
        t1 = i[1]
        t2 = i[2]
        t3 = i[3]
        t4 = i[4]
        t5 = i[5]
        t6 = i[6]
    wx = Tk()
    wx.geometry("900x800")
    wx.maxsize(900, 800)
    wx.minsize(900, 800)
    wx.configure(bg="white")
    wx.title("final marksheet")
    l1 = Label(wx, fg="white", bg="cyan", font=(
        "Times New Roman", 20), padx="1000", pady="25").pack()
    l2 = Label(wx, text="Central Board of Secondary Education", fg="white",
               bg="cyan", font=("Times New 		Roman", 20)).place(x=0, y=45)
    l3 = Label(wx, text="केंद्रीय माध्यमिक शिक्षा बोर्ड", fg="white",
               bg="cyan", font=("Times New 	Roman", 20)).place(x=0, y=10)
    l4 = Label(wx, text="Brought to you by National Information							 Centre",
               fg="black", bg="white").place(x=645, y=90)
    l5 = Label(wx, text="CENTRAL BOARD OF SECONDARY EDUCATION", fg="BLUE",
               bg="white", font=("Times 	New Roman", 15, "bold")).place(x=230, y=120)
    l6 = Label(wx, text="Secondary School Examination(Class X) 2021", fg="BLUE",
               bg="white", font=("Times		 New Roman", 15, "bold")).place(x=250, y=150)
    l6 = Label(wx, text="Roll No.:", fg="black",
               bg="white", font="10").place(x=30, y=200)
    l7 = Label(wx, text="Candiate's Name:", fg="black",
               bg="white", font="10").place(x=30, y=200)
    l07 = Label(wx, text=t1, fg="black", bg="white",
                font="3").place(x=210, y=200)
    l8 = Label(wx, text="Mother's Name:", fg="black",
               bg="white", font="10").place(x=30, y=240)
    l08 = Label(wx, text=t3, fg="black", bg="white",
                font="3").place(x=210, y=240)
    l9 = Label(wx, text="Father's Name:", fg="black",
               bg="white", font="10").place(x=30, y=280)
    l09 = Label(wx, text=t2, fg="black", bg="white",
                font="3").place(x=210, y=280)
    l10 = Label(wx, text="Date of Birth:", fg="black",
                bg="white", font="10").place(x=30, y=320)
    l010 = Label(wx, text=t4, fg="black", bg="white",
                 font="3").place(x=210, y=320)
    l11 = Label(wx, text="School's Name:", fg="black",
                bg="white", font="10").place(x=30, y=360)
    l011 = Label(wx, text="Ben-Hur Public School", fg="black",
                 bg="white", font="3").place(x=210, y=360)
    l12 = Label(wx, text="SUB CODE", font=("Times New 	Roman", 10), fg="white",
                bg="blue", width=20, height=2, bd=2, relief=SOLID).place(x=30, y=430)
    l13 = Label(wx, text="184", fg="black", bg="white", width=20,
                height=2, bd=2, relief=SOLID).place(x=30, y=46)
    l14 = Label(wx, text="041", fg="black", bg="lavender", width=20,
                height=2, bd=2, relief=SOLID).place(x=30, y=500)
    l15 = Label(wx, text="087", fg="black", bg="white", width=20,
                height=2, bd=2, relief=SOLID).place(x=30, y=53)
    l16 = Label(wx, text="090", fg="black", bg="lavender", width=20,
                height=2, bd=2, relief=SOLID).place(x=30,	y=570)
    l17 = Label(wx, text="085", fg="black", bg="white", width=20,
                height=2, bd=2, relief=SOLID).place(x=30, y=60)
    l18 = Label(wx, text="402", fg="black", bg="lavender", width=20,
                height=2, bd=2, relief=SOLID).place(x=30,	y=640)
    le = Label(wx, bg="blue", width=20, height=2,
               bd=2, relief=SOLID).place(x=30, y=675)
    ln = Label(wx, bg="blue", width=97, height=2,
               bd=2, relief=SOLID).place(x=175, y=675)
    lr = Label(wx, text="RESULT:", bg="blue", fg="white", width=15,
               height=2, relief=SOLID).place(x=175, y=675)
    lr = Label(wx, text="PASS", bg="blue", fg="white", width=20,
               height=2, relief=SOLID).place(x=280, y=675)
    l19 = Label(wx, bg="blue", text="SUBJECTS", font=("Times New	Roman", 10),
                fg="white", width=35, height=2, bd=2, relief=SOLID).place(x=175, y=430)
    l20 = Label(wx, text="ENGLISH", fg="black", bg="white", width=35,
                height=2, bd=2, relief=SOLID).place(x=175,	y=465)
    l21 = Label(wx, text="MATHS", fg="black", bg="lavender", width=35, height=2, bd=2, relief=SOLID).place(x=17	5, y=500)
    l22 = Label(wx, text="SOCIAL 	SCIENCE", fg="black", bg="white",
                width=35, height=2, bd=2, relief=SOLID).place(x=175, y=535)
    l23 = Label(wx, text="SCIENCE", fg="black", bg="lavender",
                width=35, height=2, bd=2, relief=SOLID).place(x=175, y=570)
    l24 = Label(wx, text="HINDI", fg="black", bg="white", width=35,
                height=2, bd=2, relief=SOLID).place(x=175,	y=605)
    l25 = Label(wx, text="INFORMATION	TECHNOLOGY", fg="black", bg="lavender",
                width=35, height=2, bd=2, relief=SOLID).place(x=175,	y=640)
   l26=Label(wx,bg="blue",text="THEORY MARKS",font=("Times New Roman",10),fg="white",width=20,height=2,bd=2,relief=SOLID).place(x=425,y=430)
  l27=Label(wx,text=ab,bg="white",width=20,height=2,bd=2,relief=SOLID).place(x=425,y=465)
  l28=Label(wx,text=b,bg="lavender",width=20,height=2,bd=2,relief=SOLID).place(x=425,y=500)
  l29=Label(wx,text=c,bg="white",width=20,height=2,bd=2,relief=SOLID).place(x=425,y=535)
   l30=Label(wx,text=d,bg="lavender",width=20,height=2,bd=2,relief=SOLID).place(x=425,y=570)
   l31=Label(wx,text=e,bg="white",width=20,height=2,bd=2,relief=SOLID).place(x=425,y=605)
   l32=Label(wx,text=f,bg="lavender",width=20,height=2,bd=2,relief=SOLID).place(x=425,y=640)
   l33=Label(wx,bg="blue",text="IA/PRACTICAL",font=("Times New 	Roman",10),fg="white",width=20,height=2,bd=2,relief=SOLID).place(x=570,y=430)
   l34=Label(wx,text=g,bg="white",width=20,height=2,bd=2,relief=SOLID).place(x=570,y=465)
   l35=Label(wx,text=g,bg="lavender",width=20,height=2,bd=2,relief=SOLID).place(x=570,y=500)
   l36=Label(wx,text=g,bg="white",width=20,height=2,bd=2,relief=SOLID).place(x=570,y=535)
   l37=Label(wx,text=g,bg="lavender",width=20,height=2,bd=2,relief=SOLID).place(x=570,y=570)
   l38=Label(wx,text=g,bg="white",width=20,height=2,bd=2,relief=SOLID).place(x=570,y=605)
   l39=Label(wx,text=g,bg="lavender",width=20,height=2,bd=2,relief=SOLID).place(x=570,y=640)
   l40=Label(wx,bg="blue",text="GRADE",font=("Times New 	Roman",10),fg="white",width=20,height=2,bd=2,relief=SOLID).place(x=715,y=430)
   l41=Label(wx,text=zz,bg="white",width=20,height=2,bd=2,relief=SOLID).place(x=715,y=465)
   l42=Label(wx,text=za,bg="lavender",width=20,height=2,bd=2,relief=SOLID).place(x=715,y=500)
    l43=Label(wx,text=zb,bg="white",width=20,height=2,bd=2,relief=SOLID).place(x=715,y=535)
    l44=Label(wx,text=zc,bg="lavender",width=20,height=2,bd=2,relief=SOLID).place(x=715,y=570)
    l45=Label(wx,text=zd,bg="white",width=20,height=2,bd=2,relief=SOLID).place(x=715,y=605)
    l46=Label(wx,text=ze,bg="lavender",width=20,height=2,bd=2,relief=SOLID).place(x=715,y=640)
    wx.mainloop()
def marksheetpcm():
    mydb=mysql.connector.connect(host="localhost", user="root", passwd="sarvangi@123", database="marksheet12")
    en=str(e2.get())
    mycursor=mydb.cursor()
    mycursor.execute("select * from pcm where ROLL='"+en+"'")
    for i in mycursor:
        ab=i[1]
        b=i[2]
        c=i[3]
        d=i[4]
        e=i[9]
        f=i[8]
        g=i[5]
        if ab+e>=90:
            zz='A'
        elif ab+e>=80:
            zz='B'
        elif ab+e>=70:
            zz='C'
        else:
            zz='D'
        if b+e>=90:
            za='A'
        elif b+e>=80:
            za='B'
        elif b+e>=70:
            za='C'
        else:
            za='D'
        if c+e>=90:
            zb='A'
        elif c+e>=80:
            zb='B'
        elif c+e>=70:
            zb='C'
        else:
            zb='D'
        if d+e>=90:
            zc='A'
        elif d+e>=80:
            zc='B'
        elif d+e>=70:
            zc='C'
        else:
            zc='D'
        if f+g>=90:
            zd='A'
        elif f+g>=80:
            zd='B'
        elif f+g>=70:
            zd='C'
        else:
            zd='D'
    mycursor2=mydb.cursor()
    mycursor2.execute("select * from pcm where ROLL='"+en+"'")
    for i in mycursor:
        t1=i[1]
        t2=i[2]
        t3=i[3]
        t4=i[4]
        t5=i[6]
        t6=i[7]
        t6=str(t6)
        t7=i[8]
        t8=i[9]
        t9=i[5]
    mydb3=mysql.connector.connect(host="localhost",
                             user="root",
                             passwd="sarvangi@123",
                             database="marksheet12")
    mycursor=mydb3.cursor()
    mycursor.execute("select * from details where ROLL='"+en+"'")
    for i in mycursor:
        v1=i[1]
        v2=i[3]
        v3=i[2]
        v4=i[4]
        v5=i[5]
    wx1=Tk()
    wx1.geometry("900x800")
    wx1.maxsize(900,800)
    wx1.minsize(900,800)
    wx1.configure(bg="white")
    wx1.title("final marksheet")
    l1=Label(wx1,fg="white",bg="cyan",font=("Times New Roman",20),padx="1000",pady="25").pack()
    l2=Label(wx1,text="Central Board of Secondary Education",fg="white",bg="cyan",font=("Times 	NewRoman",20)).place(x=0,y=45)
    l3=Label(wx1,text="केंद्रीय माध्यमिक शिक्षा बोर्ड",fg="white",bg="cyan",font=("Times New			 Roman",20)).place(x=0,y=10)
    l4=Label(wx1,text="Brought to you by National Information 	Centre",fg="black",bg="white").place(x=645,y=90)
    l5=Label(wx1,text="CENTRAL BOARD OF SECONDARY								 EDUCATION",fg="BLUE",bg="white",font=("Times New Roman",15,"bold")).place(x=230,y=120)
l6=Label(wx1,text="Secondary School Examination(Class XII) 	2021",fg="BLUE",bg="white",font=("Times New Roman",15,"bold")).place(x=250,y=150)
l6=Label(wx1,text="Roll No.:",fg="black",bg="white",font="10").place(x=30,y=200)
l7=Label(wx1,text="Candiate's Name:",fg="black",bg="white",font="10").place(x=30,y=200)
l7=Label(wx1,text=v1,fg="black",bg="white",font="10").place(x=210,y=200)
l8=Label(wx1,text="Mother's Name:",fg="black",bg="white",font="10").place(x=30,y=240)
l8=Label(wx1,text=v2,fg="black",bg="white",font="10").place(x=210,y=240)
l9=Label(wx1,text="Father's Name:",fg="black",bg="white",font="10").place(x=30,y=280)
l9=Label(wx1,text=v3,fg="black",bg="white",font="10").place(x=210,y=280)
 l10=Label(wx1,text="Date of Birth:",fg="black",bg="white",font="10").place(x=30,y=320)
l10=Label(wx1,text=v4,fg="black",bg="white",font="10").place(x=210,y=320) 
l11=Label(wx1,text="School's Name:",fg="black",bg="white",font="10").place(x=30,y=360) 
l11=Label(wx1,text="Ben-Hur Public School",fg="black",bg="white",font="10").place(x=210,y=360)	
l12=Label(wx1,bg="blue",text="SUB CODE",font=("Times New							 Roman",10),fg="WHITE",width=20,height=2,bd=2,relief=SOLID).place(x=30,y=430)
 l13=Label(wx1,text="042",fg="black",bg="white",width=20,height=2,bd=2,relief=SOLID).place(x=30	,y=465)
    l14=Label(wx1,text="043",fg="black",bg="lavender",width=20,height=2,bd=2,relief=SOLID).place(x=30,	y=500)
l15=Label(wx1,text="041",fg="black",bg="white",width=20,height=2,bd=2,relief=SOLID).place(x=30,	y=535)
    l16=Label(wx1,text="001",fg="black",bg="lavender",width=20,height=2,bd=2,relief=SOLID).place(x=30,	y=570)
 l17=Label(wx1,text=("0"+t6),bg="white",width=20,height=2,bd=2,relief=SOLID).place(x=30,y=605)
 l18=Label(wx1,bg="blue",width=20,height=2,bd=2,relief=SOLID).place(x=30,y=640)
 l19=Label(wx1,bg="blue",text="SUBJECTS",font=("Times New							 Roman",10),fg="white",width=35,height=2,bd=2,relief=SOLID).place(x=175,y=430)
 l20=Label(wx1,text="PHYSICS",fg="black",bg="white",width=35,height=2,bd=2,relief=SOLID).place	(x=175,y=465)
    l21=Label(wx1,text="CHEMISTRY",fg="black",bg="lavender",width=35,height=2,bd=2,relief=SOLID).place	(x=175,y=500)
l22=Label(wx1,text="MATHEMATICS",fg="black",bg="white",width=35,height=2,bd=2,relief=SOLID)	.place(x=175,y=535)
l23=Label(wx1,text="ENGLISH",fg="black",bg="lavender",width=35,height=2,bd=2,relief=SOLID).	place(x=175,y=570)
l24=Label(wx1,text=t5,fg="black",bg="white",width=35,height=2,bd=2,relief=SOLID).place(x=175,y=605)
l25=Label(wx1,bg="blue",width=97,height=2,bd=2,relief=SOLID).place(x=177,y=640)
 lr=Label(wx1,text="RESULT:",bg="blue",fg="white",width=15,height=2,relief=SOLID).place(x=175,y=640)
lr=Label(wx1,text="PASS",bg="blue",fg="white",width=20,height=2,relief=SOLID).place(x=280,y=640)
l26=Label(wx1,bg="blue",text="THEORY",font=("Times New							 Roman",10),fg="white",width=20,height=2,bd=2,relief=SOLID).place(x=425,y=430)
l27=Label(wx1,text=t1,fg="black",bg="white",width=20,height=2,bd=2,relief=SOLID).place(x=425,y=465)
l28=Label(wx1,text=t2,fg="black",bg="lavender",width=20,height=2,bd=2,relief=SOLID).place(x=425,	y=500)
l29=Label(wx1,text=t3,fg="black",bg="white",width=20,height=2,bd=2,relief=SOLID).place(x=425,y=535)
l30=Label(wx1,text=t4,fg="black",bg="lavender",width=20,height=2,bd=2,relief=SOLID).place(x=425,	y=570)
l31=Label(wx1,text=t7,fg="black",bg="white",width=20,height=2,bd=2,relief=SOLID).place(x=425,y=605)
l33=Label(wx1,bg="blue",text="IA\PRACTICAL",font=("Times New						 Roman",10),fg="white",width=20,height=2,bd=2,relief=SOLID).place(x=570,y=430)
l34=Label(wx1,text=t8,fg="black",bg="white",width=20,height=2,bd=2,relief=SOLID).place(x=570,y=465)
 l35=Label(wx1,text=t8,fg="black",bg="lavender",width=20,height=2,bd=2,relief=SOLID).place(x=570,	y=500)  
l36=Label(wx1,text=t8,fg="black",bg="white",width=20,height=2,bd=2,relief=SOLID).place	(x=570,y=535)
 l37=Label(wx1,text=t8,fg="black",bg="lavender",width=20,height=2,bd=2,relief=SOLID).place		(x=570,	y=570)
 l38=Label(wx1,text=t9,fg="black",bg="white",width=20,height=2,bd=2,relief=SOLID).place		(x=570,y=605)
l40=Label(wx1,bg="blue",text="GRADE",font=("Times New							 Roman",10),fg="white",width=20,height=2,bd=2,relief=SOLID).place(x=715,y=430)
    l41=Label(wx1,text=zz,fg="black",bg="white",width=20,height=2,bd=2,relief=SOLID).place(x=715,y=465)
l42=Label(wx1,text=za,fg="black",bg="lavender",width=20,height=2,bd=2,relief=SOLID).place(x=715,	y=500)
    l43=Label(wx1,text=zb,fg="black",bg="white",width=20,height=2,bd=2,relief=SOLID).place(x=715,y=535)
l44=Label(wx1,text=zc,fg="black",bg="lavender",width=20,height=2,bd=2,relief=SOLID).place(x=715,	y=570)
    l45=Label(wx1,text=zd,fg="black",bg="white",width=20,height=2,bd=2,relief=SOLID).place(x=715,y=605)    
 wx1.mainloop()
def marksheetpcb():
    mydb=mysql.connector.connect(host="localhost",
                             user="root",
                             passwd="sarvangi@123",
                             database="marksheet12")
    mycursor=mydb.cursor()
    en=str(e2.get())
    mycursor.execute("select * from pcb where ROLL='"+en+"'")
    for i in mycursor:
        ab=i[1]
        b=i[2]
        c=i[3]
        d=i[4]
        e=i[9]
        f=i[8]
        g=i[5]
        if ab+e>=90:
            zz='A'
        elif ab+e>=80:
            zz='B'
        elif ab+e>=70:
            zz='C'
        else:
            zz='D'
        if b+e>=90:
            za='A'
        elif b+e>=80:
            za='B'
        elif b+e>=70:
            za='C'
        else:
            za='D'
        if c+e>=90:
            zb='A'
        elif c+e>=80:
            zb='B'
        elif c+e>=70:
            zb='C'
        else:
            zb='D'
        if d+e>=90:
            zc='A'
        elif d+e>=80:
            zc='B'
        elif d+e>=70:
            zc='C'
        else:
            zc='D'
        if f+g>=90:
            zd='A'
        elif f+g>=80:
            zd='B'
        elif f+g>=70:
            zd='C'
        else:
            zd='D'
    mycursor2=mydb.cursor()
    mycursor2.execute("select * from pcb where ROLL='"+en+"'")
    for i in mycursor:
        t1=i[1]
        t2=i[2]
        t3=i[3]
        t4=i[4]
        t5=i[6]
        t6=i[7]
        t6=str(t6)
        t7=i[8]
        t8=i[9]
        t9=i[5]
    mydb3=mysql.connector.connect(host="localhost",
                             user="root",
                             passwd="sarvangi@123",
                             database="marksheet12")
    mycursor=mydb3.cursor()
    mycursor.execute("select * from details where ROLL='"+en+"'")
    for i in mycursor:
        v1=i[1]
        v2=i[3]
        v3=i[2]
        v4=i[4]
        v5=i[5]    
    wx=Tk()
    wx.geometry("900x800")
    wx.maxsize(900,800)
    wx.minsize(900,800)
    wx.configure(bg="white")
    wx.title("final marksheet")
    l1=Label(wx,fg="white",bg="cyan",font=("Times New Roman",20),padx="1000",pady="25").pack()
    l2=Label(wx,text="Central Board of Secondary Education",fg="white",bg="cyan",font=("Times New		 Roman",20)).place(x=0,y=45)
    l3=Label(wx,text="केंद्रीय माध्यमिक शिक्षा बोर्ड",fg="white",bg="cyan",font=("Times New 	Roman",20)).place(x=0,y=10)
    l4=Label(wx,text="Brought to you by National Information							 Centre",fg="black",bg="white").place(x=645,y=90)
    l5=Label(wx,text="CENTRAL BOARD OF SECONDARY EDUCATION",fg="BLUE",bg="white",font=("Times		 New Roman",15,"bold")).place(x=230,y=120)
    l6=Label(wx,text="Secondary School Examination(Class XII) 2021",fg="BLUE",bg="white",font=("Times		 New Roman",15,"bold")).place(x=250,y=150)
    l6=Label(wx,text="Roll No.:",fg="black",bg="white",font="10").place(x=30,y=200)
    l7=Label(wx,text="Candiate's Name:",fg="black",bg="white",font="10").place(x=30,y=200)
    l7=Label(wx,text=v1,fg="black",bg="white",font="10").place(x=210,y=200)
    l8=Label(wx,text="Mother's Name:",fg="black",bg="white",font="10").place(x=30,y=240)
    l8=Label(wx,text=v2,fg="black",bg="white",font="10").place(x=210,y=240)
    l9=Label(wx,text="Father's Name:",fg="black",bg="white",font="10").place(x=30,y=280)
    l9=Label(wx,text=v3,fg="black",bg="white",font="10").place(x=210,y=280)
    l10=Label(wx,text="Date of Birth:",fg="black",bg="white",font="10").place(x=30,y=320)
    l10=Label(wx,text=v4,fg="black",bg="white",font="10").place(x=210,y=320)
    l11=Label(wx,text="School's Name:",fg="black",bg="white",font="10").place(x=30,y=360)
    l11=Label(wx,text="Ben-Hur Public School",fg="black",bg="white",font="10").place(x=210,y=360)
    l12=Label(wx,bg="blue",text="SUB CODE",font=("Times New							 Roman",10),fg="WHITE",width=20,height=2,bd=2,relief=SOLID).place(x=30,y=430)
    l13=Label(wx,text="042",fg="black",bg="white",width=20,height=2,bd=2,relief=SOLID).place(x=30,	y=465)
    l14=Label(wx,text="043",fg="black",bg="lavender",width=20,height=2,bd=2,relief=SOLID).place(x=30,	y=500)
    l15=Label(wx,text="044",fg="black",bg="white",width=20,height=2,bd=2,relief=SOLID).place(x=30,	y=535)
    l16=Label(wx,text="001",fg="black",bg="lavender",width=20,height=2,bd=2,relief=SOLID).place(x=30,	y=570)
    l17=Label(wx,text=("0"+t6),bg="white",width=20,height=2,bd=2,relief=SOLID).place(x=30,y=605)
    l18=Label(wx,bg="blue",width=20,height=2,bd=2,relief=SOLID).place(x=30,y=640)
    l19=Label(wx,bg="blue",text="SUBJECTS",font=("Times New							 Roman",10),fg="white",width=35,height=2,bd=2,relief=SOLID).place(x=175,y=430)
    l20=Label(wx,text="PHYSICS",fg="black",bg="white",width=35,height=2,bd=2,relief=SOLID).place(x=175,	y=465)
    l21=Label(wx,text="CHEMISTRY",fg="black",bg="lavender",width=35,height=2,bd=2,relief=SOLID).place	(x=175,y=500)
l22=Label(wx,text="BIOLOGY",fg="black",bg="white",width=35,height=2,bd=2,relief=SOLID).place	(x=175,y=535)
 l23=Label(wx,text="ENGLISH",fg="black",bg="lavender",width=35,height=2,bd=2,relief=SOLID).place	(x=175,y=570)
    l24=Label(wx,text=t5,fg="black",bg="white",width=35,height=2,bd=2,relief=SOLID).place(x=175,y=605)
 l25=Label(wx,bg="blue",width=97,height=2,bd=2,relief=SOLID).place(x=177,y=640)
    lr=Label(wx,text="RESULT:",bg="blue",fg="white",width=15,height=2,relief=SOLID).place(x=175,y=640)
 lr=Label(wx,text="PASS",bg="blue",fg="white",width=20,height=2,relief=SOLID).place(x=280,y=640)
 l26=Label(wx,bg="blue",text="THEORY",font=("Times New							 Roman",10),fg="white",width=20,height=2,bd=2,relief=SOLID).place(x=425,y=430)
    l27=Label(wx,text=t1,fg="black",bg="white",width=20,height=2,bd=2,relief=SOLID).place(x=425,y=465)
    l28=Label(wx,text=t2,fg="black",bg="lavender",width=20,height=2,bd=2,relief=SOLID).place(x=425,	y=500)
       l29=Label(wx,text=t3,fg="black",bg="white",width=20,height=2,bd=2,relief=SOLID).place(x=425,y=535)
 l30=Label(wx,text=t4,fg="black",bg="lavender",width=20,height=2,bd=2,relief=SOLID).place(x=425,	y=570)
    l31=Label(wx,text=t7,fg="black",bg="white",width=20,height=2,bd=2,relief=SOLID).place(x=425,y=605)
l33=Label(wx,bg="blue",text="IA\PRACTICAL",font=("Times New							 Roman",10),fg="white",width=20,height=2,bd=2,relief=SOLID).place(x=570,y=430)
    l34=Label(wx,text=t8,fg="black",bg="white",width=20,height=2,bd=2,relief=SOLID).place(x=570,y=465)
l35=Label(wx,text=t8,fg="black",bg="lavender",width=20,height=2,bd=2,relief=SOLID).place	(x=570,y=500)
    l36=Label(wx,text=t8,fg="black",bg="white",width=20,height=2,bd=2,relief=SOLID).place(x=570,y=535)
l37=Label(wx,text=t8,fg="black",bg="lavender",width=20,height=2,bd=2,relief=SOLID).place	(x=570,y=570)
    l38=Label(wx,text=t9,fg="black",bg="white",width=20,height=2,bd=2,relief=SOLID).place(x=570,y=605)
l40=Label(wx,bg="blue",text="GRADE",font=("Times New							 Roman",10),fg="white",width=20,height=2,bd=2,relief=SOLID).place(x=715,y=430)
    l41=Label(wx,text=zz,fg="black",bg="white",width=20,height=2,bd=2,relief=SOLID).place(x=715,y=465)
 l42=Label(wx,text=za,fg="black",bg="lavender",width=20,height=2,bd=2,relief=SOLID).place	(x=715,y=500)
    l43=Label(wx,text=zb,fg="black",bg="white",width=20,height=2,bd=2,relief=SOLID).place(x=715,y=535)
l44=Label(wx,text=zc,fg="black",bg="lavender",width=20,height=2,bd=2,relief=SOLID).place	(x=715,y=570)
    l45=Label(wx,text=zd,fg="black",bg="white",width=20,height=2,bd=2,relief=SOLID).place(x=715,y=605)    
    wx.mainloop()
def marksheetcommerce():
    mydb=mysql.connector.connect(host="localhost",
                             user="root",
                             passwd="sarvangi@123",
                             database="marksheet12")
    en=str(e2.get())
    mycursor=mydb.cursor()
    mycursor.execute("select * from commerce where ROLL='"+en+"'")
    for i in mycursor:
        ab=i[1]
        b=i[2]
        c=i[3]
        d=i[4]
        e=i[9]
        f=i[8]
        g=i[5]
        if ab+e>=90:
            zz='A'
        elif ab+e>=80:
            zz='B'
        elif ab+e>=70:
            zz='C'
        else:
            zz='D'
        if b+e>=90:
            za='A'
        elif b+e>=80:
            za='B'
        elif b+e>=70:
            za='C'
        else:
            za='D'
        if c+e>=90:
            zb='A'
        elif c+e>=80:
            zb='B'
        elif c+e>=70:
            zb='C'
        else:
            zb='D'
        if d+e>=90:
            zc='A'
        elif d+e>=80:
            zc='B'
        elif d+e>=70:
            zc='C'
        else:
            zc='D'
        if f+g>=90:
            zd='A'
        elif f+g>=80:
            zd='B'
        elif f+g>=70:
            zd='C'
        else:
            zd='D'
    mycursor2=mydb.cursor()
    mycursor2.execute("select * from commerce where ROLL='"+en+"'")
    for i in mycursor:
        t1=i[1]
        t2=i[2]
        t3=i[3]
        t4=i[4]
        t5=i[6]
        t6=i[7]
        t6=str(t6)
        t7=i[8]
        t8=i[9]
        t9=i[5]
    mydb3=mysql.connector.connect(host="localhost",
                             user="root",
                             passwd="sarvangi@123",
                             database="marksheet12")
    mycursor=mydb3.cursor()
    mycursor.execute("select * from details where ROLL='"+en+"'")
    for i in mycursor:
        v1=i[1]
        v2=i[3]
        v3=i[2]
        v4=i[4]
        v5=i[5]
    wx=Tk()
    wx.geometry("900x800")
    wx.maxsize(900,800)
    wx.minsize(900,800)
    wx.configure(bg="white")
    wx.title("final marksheet")
    l1=Label(wx,fg="white",bg="cyan",font=("Times New Roman",20),padx="1000",pady="25").pack()
    l2=Label(wx,text="Central Board of Secondary Education",fg="white",bg="cyan",font=("Times New		 Roman",20)).place(x=0,y=45)
    l3=Label(wx,text="केंद्रीय माध्यमिक शिक्षा बोर्ड",fg="white",bg="cyan",font=("Times New				 Roman",20)).place(x=0,y=10)
    l4=Label(wx,text="Brought to you by National Information							 Centre",fg="black",bg="white").place(x=645,y=90)
    l5=Label(wx,text="CENTRAL BOARD OF SECONDARY EDUCATION",fg="BLUE",bg="white",font=("Times		 New Roman",15,"bold")).place(x=230,y=120)
    l6=Label(wx,text="Secondary School Examination(Class XII) 2021",fg="BLUE",bg="white",font=("Times		 New Roman",15,"bold")).place(x=250,y=150)
    l6=Label(wx,text="Roll No.:",fg="black",bg="white",font="10").place(x=30,y=200)
    l7=Label(wx,text="Candiate's Name:",fg="black",bg="white",font="10").place(x=30,y=200)
    l7=Label(wx,text=v1,fg="black",bg="white",font="10").place(x=210,y=200)
    l8=Label(wx,text="Mother's Name:",fg="black",bg="white",font="10").place(x=30,y=240)
    l8=Label(wx,text=v2,fg="black",bg="white",font="10").place(x=210,y=240)
    l9=Label(wx,text="Father's Name:",fg="black",bg="white",font="10").place(x=30,y=280)
    l9=Label(wx,text=v3,fg="black",bg="white",font="10").place(x=210,y=280)
    l10=Label(wx,text="Date of Birth:",fg="black",bg="white",font="10").place(x=30,y=320)
    l10=Label(wx,text=v4,fg="black",bg="white",font="10").place(x=210,y=320)
    l11=Label(wx,text="School's Name:",fg="black",bg="white",font="10").place(x=30,y=360)
    l11=Label(wx,text="Ben-Hur Public School",fg="black",bg="white",font="10").place(x=210,y=360)
    l12=Label(wx,bg="blue",text="SUB CODE",font=("Times New							 Roman",10),fg="WHITE",width=20,height=2,bd=2,relief=SOLID).place(x=30,y=430)
    l13=Label(wx,text="055",fg="black",bg="white",width=20,height=2,bd=2,relief=SOLID).place	(x=30,y=465)
    l14=Label(wx,text="054",fg="black",bg="lavender",width=20,height=2,bd=2,relief=SOLID).place	(x=30,y=500)
    l15=Label(wx,text="030",fg="black",bg="white",width=20,height=2,bd=2,relief=SOLID).place	(x=30,y=535)
    l16=Label(wx,text="001",fg="black",bg="lavender",width=20,height=2,bd=2,relief=SOLID).place	(x=30,y=570)
    l17=Label(wx,text=("0"+t6),bg="white",width=20,height=2,bd=2,relief=SOLID).place(x=30,y=605)
    l18=Label(wx,bg="blue",width=20,height=2,bd=2,relief=SOLID).place(x=30,y=640)
    l19=Label(wx,bg="blue",text="SUBJECTS",font=("Times New							 Roman",10),fg="white",width=35,height=2,bd=2,relief=SOLID).place(x=175,y=430)
    l20=Label(wx,text="ACCOUNTS",fg="black",bg="white",width=35,height=2,bd=2,relief=SOLID).place	(x=175,y=465)
    l21=Label(wx,text="BUSINESS											 STUDIES",fg="black",bg="lavender",width=35,height=2,bd=2,relief=SOLID).place(x=175,y=500)
    l22=Label(wx,text="ECONOMICS",fg="black",bg="white",width=35,height=2,bd=2,relief=SOLID).place	(x=175,y=535)
    l23=Label(wx,text="ENGLISH",fg="black",bg="lavender",width=35,height=2,bd=2,relief=SOLID).place	(x=175,y=570)
    l24=Label(wx,text=t5,fg="black",bg="white",width=35,height=2,bd=2,relief=SOLID).place(x=175,y=605)
l25=Label(wx,bg="blue",width=97,height=2,bd=2,relief=SOLID).place(x=177,y=640)
    lr=Label(wx,text="RESULT:",bg="blue",fg="white",width=15,height=2,relief=SOLID).place(x=175,y=640)
lr=Label(wx,text="PASS",bg="blue",fg="white",width=20,height=2,relief=SOLID).place(x=280,y=640)
 l26=Label(wx,bg="blue",text="THEORY",font=("Times New							 Roman",10),fg="white",width=20,height=2,bd=2,relief=SOLID).place(x=425,y=430)
    l27=Label(wx,text=t1,fg="black",bg="white",width=20,height=2,bd=2,relief=SOLID).place(x=425,y=465)
l28=Label(wx,text=t2,fg="black",bg="lavender",width=20,height=2,bd=2,relief=SOLID).place	(x=425,y=500)
    l29=Label(wx,text=t3,fg="black",bg="white",width=20,height=2,bd=2,relief=SOLID).place(x=425,y=535)
 l30=Label(wx,text=t4,fg="black",bg="lavender",width=20,height=2,bd=2,relief=SOLID).place	(x=425,y=570)
    l31=Label(wx,text=t7,fg="black",bg="white",width=20,height=2,bd=2,relief=SOLID).place(x=425,y=605)
l33=Label(wx,bg="blue",text="IA\PRACTICAL",font=("Times New							 Roman",10),fg="white",width=20,height=2,bd=2,relief=SOLID).place(x=570,y=430)
    l34=Label(wx,text=t8,fg="black",bg="white",width=20,height=2,bd=2,relief=SOLID).place(x=570,y=465)
 l35=Label(wx,text=t8,fg="black",bg="lavender",width=20,height=2,bd=2,relief=SOLID).place	(x=570,y=500)
    l36=Label(wx,text=t8,fg="black",bg="white",width=20,height=2,bd=2,relief=SOLID).place(x=570,y=535)
 l37=Label(wx,text=t8,fg="black",bg="lavender",width=20,height=2,bd=2,relief=SOLID).place	(x=570,y=570)
    l38=Label(wx,text=t9,fg="black",bg="white",width=20,height=2,bd=2,relief=SOLID).place(x=570,y=605)
 l40=Label(wx,bg="blue",text="GRADE",font=("Times New							 Roman",10),fg="white",width=20,height=2,bd=2,relief=SOLID).place(x=715,y=430)
    l41=Label(wx,text=zz,fg="black",bg="white",width=20,height=2,bd=2,relief=SOLID).place(x=715,y=465)
l42=Label(wx,text=za,fg="black",bg="lavender",width=20,height=2,bd=2,relief=SOLID).place	(x=715,y=500)
    l43=Label(wx,text=zb,fg="black",bg="white",width=20,height=2,bd=2,relief=SOLID).place(x=715,y=535)
l44=Label(wx,text=zc,fg="black",bg="lavender",width=20,height=2,bd=2,relief=SOLID).place	(x=715,y=570)
    l45=Label(wx,text=zd,fg="black",bg="white",width=20,height=2,bd=2,relief=SOLID).place(x=715,y=605)   
 wx.mainloop()
def marksheethumanities():
    mydb=mysql.connector.connect(host="localhost",
                             user="root",
                             passwd="sarvangi@123",
                             database="marksheet12")
    en=str(e2.get())
    mycursor=mydb.cursor()
    mycursor.execute("select * from humanities where ROLL='"+en+"'")
    for i in mycursor:
        ab=i[1]
        b=i[2]
        c=i[3]
        d=i[4]
        e=i[9]
        f=i[8]
        g=i[5]
        if ab+e>=90:
            zz='A'
        elif ab+e>=80:
            zz='B'
        elif ab+e>=70:
            zz='C'
        else:
            zz='D'
        if b+e>=90:
            za='A'
        elif b+e>=80:
            za='B'
        elif b+e>=70:
            za='C'
        else:
            za='D'
        if c+e>=90:
            zb='A'
        elif c+e>=80:
            zb='B'
        elif c+e>=70:
            zb='C'
        else:
            zb='D'
        if d+e>=90:
            zc='A'
        elif d+e>=80:
            zc='B'
        elif d+e>=70:
            zc='C'
        else:
            zc='D'
        if f+g>=90:
            zd='A'
        elif f+g>=80:
            zd='B'
        elif f+g>=70:
            zd='C'
        else:
            zd='D'
    mycursor2=mydb.cursor()
    mycursor2.execute("select * from humanities where ROLL='"+en+"'")
    for i in mycursor:
        t1=i[1]
        t2=i[2]
        t3=i[3]
        t4=i[4]
        t5=i[6]
        t6=i[7]
        t6=str(t6)
        t7=i[8]
        t8=i[9]
        t9=i[5]
    mydb3=mysql.connector.connect(host="localhost",user="root"=passwd="sarvangi@123",database="marksheet12")
    mycursor=mydb3.cursor()
    mycursor.execute("select * from details where ROLL='"+en+"'")
    for i in mycursor:
        v1=i[1]
        v2=i[3]
        v3=i[2]
        v4=i[4]
        v5=i[5]
    wx=Tk()
    wx.geometry("900x800")
    wx.maxsize(900,800)
    wx.minsize(900,800)
    wx.configure(bg="white")
    wx.title("final marksheet")
    l1=Label(wx,fg="white",bg="cyan",font=("Times New Roman",20),padx="1000",pady="25").pack()
    l2=Label(wx,text="Central Board of Secondary Education",fg="white",bg="cyan",font=("Times New		 Roman",20)).place(x=0,y=45)
    l3=Label(wx,text="केंद्रीय माध्यमिक शिक्षा बोर्ड",fg="white",bg="cyan",font=("Times New				 Roman",20)).place(x=0,y=10)
    l4=Label(wx,text="Brought to you by National Information							 Centre",fg="black",bg="white").place(x=645,y=90)
    l5=Label(wx,text="CENTRAL BOARD OF SECONDARY EDUCATION",fg="BLUE",bg="white",font=("Times 		New Roman",15,"bold")).place(x=230,y=120)
    l6=Label(wx,text="Secondary School Examination(Class XII) 2021",fg="BLUE",bg="white",font=("Times		 New Roman",15,"bold")).place(x=250,y=150)
    l6=Label(wx,text="Roll No.:",fg="black",bg="white",font="10").place(x=30,y=200)
    l7=Label(wx,text="Candiate's Name:",fg="black",bg="white",font="10").place(x=30,y=200)
    l7=Label(wx,text=v1,fg="black",bg="white",font="10").place(x=210,y=200)
    l8=Label(wx,text="Mother's Name:",fg="black",bg="white",font="10").place(x=30,y=240)
    l8=Label(wx,text=v2,fg="black",bg="white",font="10").place(x=210,y=240)
    l9=Label(wx,text="Father's Name:",fg="black",bg="white",font="10").place(x=30,y=280)
    l9=Label(wx,text=v3,fg="black",bg="white",font="10").place(x=210,y=280)
    l10=Label(wx,text="Date of Birth:",fg="black",bg="white",font="10").place(x=30,y=320)
    l10=Label(wx,text=v4,fg="black",bg="white",font="10").place(x=210,y=320)
    l11=Label(wx,text="School's Name:",fg="black",bg="white",font="10").place(x=30,y=360)
    l11=Label(wx,text="Ben-Hur Public School",fg="black",bg="white",font="10").place(x=210,y=360)
    l12=Label(wx,bg="blue",text="SUB CODE",font=("Times New							 Roman",10),fg="WHITE",width=20,height=2,bd=2,relief=SOLID).place(x=30,y=430)
    l13=Label(wx,text="027",fg="black",bg="white",width=20,height=2,bd=2,relief=SOLID).place	(x=30,y=465)
    l14=Label(wx,text="028",fg="black",bg="lavender",width=20,height=2,bd=2,relief=SOLID).place	(x=30,y=500)
    l15=Label(wx,text="039",fg="black",bg="white",width=20,height=2,bd=2,relief=SOLID).place	(x=30,y=535)
    l16=Label(wx,text="001",fg="black",bg="lavender",width=20,height=2,bd=2,relief=SOLID).place	(x=30,y=570)
    l17=Label(wx,text=("0"+t6),bg="white",width=20,height=2,bd=2,relief=SOLID).place(x=30,y=605)
    l18=Label(wx,bg="blue",width=20,height=2,bd=2,relief=SOLID).place(x=30,y=640)
    l19=Label(wx,bg="blue",text="SUBJECTS",font=("Times New							 Roman",10),fg="white",width=35,height=2,bd=2,relief=SOLID).place(x=175,y=430)
    l20=Label(wx,text="HISTORY",fg="black",bg="white",width=35,height=2,bd=2,relief=SOLID).place	(x=175,y=465)
    l21=Label(wx,text="POLITICA	L										 SCIENCE",fg="black",bg="lavender",width=35,height=2,bd=2,relief=SOLID).place(x=175,y=500)
    l22=Label(wx,text="SOCIOLOGY",fg="black",bg="white",width=35,height=2,bd=2,relief=SOLID).place	(x=175,y=535)
    l23=Label(wx,text="ENGLISH",fg="black",bg="lavender",width=35,height=2,bd=2,relief=SOLID).place	(x=175,y=570)
    l24=Label(wx,text=t5,fg="black",bg="white",width=35,height=2,bd=2,relief=SOLID).place(x=175,y=605)
    l25=Label(wx,bg="blue",width=97,height=2,bd=2,relief=SOLID).place(x=177,y=640)
    lr=Label(wx,text="RESULT:",bg="blue",fg="white",width=15,height=2,relief=SOLID).place	(x=175,y=640)
    lr=Label(wx,text="PASS",bg="blue",fg="white",width=20,height=2,relief=SOLID).place(x=280,y=640)
    l26=Label(wx,bg="blue",text="THEORY",font=("Times New							 Roman",10),fg="white",width=20,height=2,bd=2,relief=SOLID).place(x=425,y=430)
    l27=Label(wx,text=t1,fg="black",bg="white",width=20,height=2,bd=2,relief=SOLID).place	(x=425,y=465)
    l28=Label(wx,text=t2,fg="black",bg="lavender",width=20,height=2,bd=2,relief=SOLID).place	(x=425,y=500)
    l29=Label(wx,text=t3,fg="black",bg="white",width=20,height=2,bd=2,relief=SOLID).place	(x=425,y=535)
    l30=Label(wx,text=t4,fg="black",bg="lavender",width=20,height=2,bd=2,relief=SOLID).place	(x=425,y=570)
    l31=Label(wx,text=t7,fg="black",bg="white",width=20,height=2,bd=2,relief=SOLID).	place(x=425,y=605)
    l33=Label(wx,bg="blue",text="IA\PRACTICAL",font=("Times New						 Roman",10),fg="white",width=20,height=2,bd=2,relief=SOLID).place(x=570,y=430)
    l34=Label(wx,text=t8,fg="black",bg="white",width=20,height=2,bd=2,relief=SOLID).place	(x=570,y=465)
    l35=Label(wx,text=t8,fg="black",bg="lavender",width=20,height=2,bd=2,relief=SOLID).place	(x=570,y=500)
    l36=Label(wx,text=t8,fg="black",bg="white",width=20,height=2,bd=2,relief=SOLID).place	(x=570,y=535)
    l37=Label(wx,text=t8,fg="black",bg="lavender",width=20,height=2,bd=2,relief=SOLID).place	(x=570,y=570)
    l38=Label(wx,text=t9,fg="black",bg="white",width=20,height=2,bd=2,relief=SOLID).place	(x=570,y=605)
    l40=Label(wx,bg="blue",text="GRADE",font=("Times New							 Roman",10),fg="white",width=20,height=2,bd=2,relief=SOLID).place(x=715,y=430)
    l41=Label(wx,text=zz,fg="black",bg="white",width=20,height=2,bd=2,relief=SOLID).place	(x=715,y=465)
    l42=Label(wx,text=za,fg="black",bg="lavender",width=20,height=2,bd=2,relief=SOLID).place	(x=715,y=500)
    l43=Label(wx,text=zb,fg="black",bg="white",width=20,height=2,bd=2,relief=SOLID).place	(x=715,y=535)
    l44=Label(wx,text=zc,fg="black",bg="lavender",width=20,height=2,bd=2,relief=SOLID).place	(x=715,y=570)
    l45=Label(wx,text=zd,fg="black",bg="white",width=20,height=2,bd=2,relief=SOLID).place	(x=715,y=605)
    wx.mainloop()
def entrypcm():
    wm=Tk()
    wm.configure(bg="black")
    wm.geometry("1024x724")
    wm.title("Marksheet of Class 12")
    wm.maxsize(1024,724)
    wm.minsize(1024,724)
    f=Frame(wm,width=974,relief=RAISED,height=674,bg='slategray',bd=8)
    f.place(x=25,y=25)
    l1=Label(f,text="MARKSHEET FOR CLASS XII",bg="black",fg="snow",font=("Times New	Roman",20),padx="25",pady="25")
    l1.place(x=280,y=20)
    l2=Label(f,text="ENTER ROLL NUMBER:",font=("Times New Roman",20,"bold"),fg="black",bg="slategray")
    l2.place(x=200,y=200)
    l3=Label(f,text="ENTER CENTRE NUMBER:",font=("Times New Roman",20,"bold"),fg="black",bg="slategray")
    l3.place(x=200,y=300)
    global e2
    e2=Entry(f,bg="snow",width=30,bd=4)
    e2.place(x=600,y=200)
    e3=Entry(f,bg="snow",width=30,bd=4)
    e3.place(x=600,y=300)
    def reset():
        e2.delete(0,"end")
        e3.delete(0,"end")
    bn=Button(f,text="RESET",fg="snow",bg="black",font=("Times New Roman",20),height=1,width=10,command=reset)
    bn.place(x=450,y=450)
    b3=Button(f,text="SUBMIT",fg="snow",bg="black",font=("Times New	Roman",20),height=1,width=10,command=marksheetpcm)
    b3.place(x=350,y=550)
    b4=Button(f,text="EXIT",fg="snow",bg="black",font=("Times New Roman",20),height=1,width=10,command=wm.destroy)
    b4.place(x=550,y=550)
    wm.mainloop()
def entrypcb():
    wm=Tk()
    wm.configure(bg="black")
    wm.geometry("1024x724")
    wm.title("Marksheet of Class 12")
    wm.maxsize(1024,724)
    wm.minsize(1024,724)
    f=Frame(wm,width=974,relief=RAISED,height=674,bg='slategray',bd=8)
    f.place(x=25,y=25)
    l1=Label(f,text="MARKSHEET FOR CLASS XII",bg="black",fg="snow",font=("Times New				 Roman",20),padx="25",pady="25")
    l1.place(x=280,y=20)
    l2=Label(f,text="ENTER ROLL NUMBER:",font=("Times New							 Roman",20,"bold"),fg="black",bg="slategray")
    l2.place(x=200,y=200)
    l3=Label(f,text="ENTER CENTRE NUMBER:",font=("Times New							 Roman",20,"bold"),fg="black",bg="slategray")
    l3.place(x=200,y=300)
    global e2
    e2=Entry(f,bg="snow",width=30,bd=4)
    e2.place(x=600,y=200)
    e3=Entry(f,bg="snow",width=30,bd=4)
    e3.place(x=600,y=300)
    def reset():
        e2.delete(0,"end")
        e3.delete(0,"end" )
    bn=Button(f,text="RESET",fg="snow",bg="black",font=("Times New						 Roman",20),height=1,width=10,command=reset)
    bn.place(x=450,y=450)
    b3=Button(f,text="SUBMIT",fg="snow",bg="black",font=("Times New						 Roman",20),height=1,width=10,command=marksheetpcb)
    b3.place(x=350,y=550)
    b4=Button(f,text="EXIT",fg="snow",bg="black",font=("Times New						 Roman",20),height=1,width=10,command=wm.destroy)
    b4.place(x=550,y=550)
    wm.mainloop()
def entrycommerce():
    wm=Tk()
    wm.configure(bg="black")
    wm.geometry("1024x724")
    wm.title("Marksheet of Class 12")
    wm.maxsize(1024,724)
    wm.minsize(1024,724)
    f=Frame(wm,width=974,relief=RAISED,height=674,bg='slategray',bd=8)
    f.place(x=25,y=25)
    l1=Label(f,text="MARKSHEET FOR CLASS XII",bg="black",fg="snow",font=("Times New				 Roman",20),padx="25",pady="25")
    l1.place(x=280,y=20)
    l2=Label(f,text="ENTER ROLL NUMBER:",font=("Times New Roman",20),fg="black",bg="slategray")
    l2.place(x=200,y=200)
    l3=Label(f,text="ENTER CENTRE NUMBER:",font=("Times New Roman",20),fg="black",bg="slategray")
    l3.place(x=200,y=300)
    global e2
    e2=Entry(f,bg="snow",width=30,bd=4)
    e2.place(x=600,y=200)
    e3=Entry(f,bg="snow",width=30,bd=4)
    e3.place(x=600,y=300)
    def reset():
        e2.delete(0,"end")
        e3.delete(0,"end" )
    bn=Button(f,text="RESET",fg="snow",bg="black",font=("Times New Roman",20),height=1,width=10,command=reset)
    bn.place(x=450,y=450)
    b3=Button(f,text="SUBMIT",fg="snow",bg="black",font=("Times New	Roman",20),height=1,width=10,command=marksheetcommerce)
    b3.place(x=350,y=550)
    b4=Button(f,text="EXIT",fg="snow",bg="black",font=("Times New Roman",20),height=1,width=10,command=wm.destroy)
    b4.place(x=550,y=550)
    wm.mainloop()
def entryhumanities():
    wm=Tk()
    wm.configure(bg="black")
    wm.geometry("1024x724")
    wm.title("Marksheet of Class 12")
    wm.maxsize(1024,724)
    wm.minsize(1024,724)
    f=Frame(wm,width=974,relief=RAISED,height=674,bg='slategray',bd=8)
    f.place(x=25,y=25)
    l1=Label(f,text="MARKSHEET FOR CLASS XII",bg="black",fg="snow",font=("Times New				 Roman",20),padx="25",pady="25")
    l1.place(x=280,y=20)
    l2=Label(f,text="ENTER ROLL NUMBER:",font=("Times New							 Roman",20,"bold"),fg="black",bg="slategray")
    l2.place(x=200,y=200)
    l3=Label(f,text="ENTER CENTRE NUMBER:",font=("Times New							 Roman",20,"bold"),fg="black",bg="slategray")
    l3.place(x=200,y=300)
    global e2
    e2=Entry(f,bg="snow",width=30,bd=4)
    e2.place(x=600,y=200)
    e3=Entry(f,bg="snow",width=30,bd=4)
    e3.place(x=600,y=300)
    def reset():
        e2.delete(0,"end")
        e3.delete(0,"end" )
    bn=Button(f,text="RESET",fg="snow",bg="black",font=("Times New						 Roman",20),height=1,width=10,command=reset)
    bn.place(x=450,y=450)
    b3=Button(f,text="SUBMIT",fg="snow",bg="black",font=("Times New						 Roman",20),height=1,width=10,command=marksheethumanities)
    b3.place(x=350,y=550)
    b4=Button(f,text="EXIT",fg="snow",bg="black",font=("Times New						 Roman",20),height=1,width=10,command=wm.destroy)
    b4.place(x=550,y=550)
    wm.mainloop()
def mainc():
    w=Tk()
    w.geometry("1024x724")
    w.configure(bg="BLACK")
    w.title("Selection window")
    w.maxsize(1024,724)
    w.minsize(1024,724)
    m=Frame(w,width=974,relief=RAISED,height=674,bg='SLATEGRAY',bd=8)
    m.place(x=25,y=25)
    mylabel=Label(m,text="CBSE",fg="Black",bg="slategray",font=("Times New					 Roman",20,"bold")).place(x=440,y=20)
    mylabel1=Label(m,text="Central Board Of Secondary								 Education",fg="Black",bg="slategray",font=("Times New Roman",20,"bold")).place(x=300,y=50)
    mylabel2=Label(m,text="Committed to Equity and Excellence in						 Education",fg="Black",bg="slategray",font=("Times New Roman",20,"bold")).place(x=235,y=80)
    mylabel3=Label(m,text="Click on the link below to fetch the							 results:",fg="Black",bg="slategray",font=("Times New Roman",20,"bold"))
    mylabel3.place(x=260,y=150)
    mylabel4=Label(m,text="For class X:",padx="23",pady="56",fg="Black",bg="slategray",font=("Times		 New Roman",20))
    mylabel5=Label(m,text="For class XII:",padx="23",pady="56",fg="Black",bg="slategray", font=("Times		 New Roman",20))
    mylabel4.place(x=300,y=220)
    mylabel5.place(x=300,y=320)
    b1=Button(m,text="EXIT",fg="snow",bg="black", font=("Times New						 Roman",20),relief=RAISED,command=w.destroy)
    b1.place(x=450,y=450)
    def entry10():        
        w1=Tk()
        w1.configure(bg="black")
        w1.geometry("1024x724")
        w1.title("Marksheet of Class 10")
        w1.maxsize(1024,724)
        w1.minsize(1024,724)
        f=Frame(w1,width=974,relief=RAISED,height=674,bg='slategray',bd=8)
        f.place(x=25,y=25)
        l1=Label(f,text="MARKSHEET FOR CLASS X",bg="black",fg="snow",relief=RAISED,bd=5,font=("Times New Roman",20),padx="25",pady="25")
        l1.place(x=280,y=20)
        l2=Label(f,text="ENTER ROLL NUMBER:",font=("Times New Roman",20),fg="black",bg="slategray")
        l2.place(x=200,y=200)
        l3=Label(f,text="ENTER CENTRE NUMBER:",font=("Times New	Roman",20),fg="black",bg="slategray")
        l3.place(x=200,y=300)
        global e11
        e11=Entry(f,bg="snow",width=30,bd=4)
        e11.place(x=600,y=200)
        e1=Entry(f,bg="snow",width=30,bd=4)
        e1.place(x=600,y=300)
        def reset():
            e11.delete(0,"end")
            e1.delete(0,"end")
        bn=Button(w1,text="RESET",fg="snow",bg="black",font=("Times New					 Roman",20),height=1,width=10,command=reset)
        bn.place(x=450,y=450)
        b3=Button(w1,text="SUBMIT",fg="snow",bg="black",font=("Times New					 Roman",20),height=1,width=10,command=marksheet10)
        b3.place(x=350,y=550)
        b4=Button(w1,text="EXIT",fg="snow",bg="black",font=("Times New						 Roman",20),height=1,width=10,command=w1.destroy)
        b4.place(x=550,y=550)
        w1.mainloop()
    b1=Button(w,text="www.cbse.gov.in\class10",fg="snow",bg="black",font=("Times New			 Roman",10,"bold"),command= entry10).place(x=550,y=310)
    def b2command():
        w2=Tk()
        w2.configure(bg="black")
        w2.geometry("1024x724")
        w2.title("Marksheet of Class 12")
        w2.maxsize(1024,724)
        w2.minsize(1024,724)
        f=Frame(w2,width=974,relief=RAISED,height=674,bg='slategray',bd=8)
        f.place(x=25,y=25)
        l4=Button(f,text="MARKSHEET FOR CLASS XII",bg="black",fg="snow",font=("Times New			 Roman",20,"bold"),relief=RAISED,bd=10,width=25,padx="25",pady="25")
        l4.place(x=280,y=30)
        l5=Label(f,text="CHOOSE YOUR STREAM",fg="black",bg="slategray",font=("Times New			 Roman",20,"bold"))
        l5.place(x=330,y=180)
        b5=Button(f,text="PCM",height=1,width=10,fg="snow",bg="black",bd=5,relief=RAISED,			 font=("Times New Roman",20),padx="35",pady="15",command=entrypcm)
        b5.place(x=230,y=260)
        b6=Button(f,text="PCB",height=1,width=10,fg="snow",bg="black",bd=5,relief=RAISED,font=("Times		 New Roman",20),padx="35",pady="15",command=entrypcb)
        b6.place(x=530,y=260)
        b7=Button(f,text="COMMERCE",height=1,width=10,fg="snow",bg="black",bd=5,relief=RAISED	, font=("Times New Roman",20),padx="35",pady="15",command=entrycommerce)
        b7.place(x=230,y=390)
        b8=Button(f,text="HUMANITIES",height=1,width=10,fg="snow",bg="black",bd=5,relief=RAISED,	font=("Times New Roman",20),padx="35",pady="15",command=entryhumanities)
        b8.place(x=530,y=390)
        b9=Button(f,text="EXIT",height=1,width=6,fg="snow",bg="black",bd=5,relief=RAISED,font=		("Times New Roman",20),padx="35",pady="15",command=w2.destroy)
        b9.place(x=410,y=540)
        w2.mainloop()
    b2=Button(w,text="www.cbse.gov.in\class12",fg="snow",bg="black",font=				("times New Roman",10,"bold"),command=b2command).place(x=550,y=410)
    w.mainloop()
wn=Tk()
wn.geometry("1024x724")
wn.configure(bg="black")
wn.maxsize(1024,724)
wn.minsize(1024,724)
f=Frame(wn,width=974,height=674,relief=RAISED,bd=8,bg='slategray').place(x=25,y=25)
l6=Label(f,text="CBSE REPORT CARD MAKING									 SYSTEM",bg="black",fg="snow",padx="25",pady="25",relief=RAISED,bd=10,font=("Times New		 Roman",20,"bold")).place(x=230,y=50)
l7=Label(f,text="DESIGNED AND DEVELOPED									 BY:",fg="snow",bg="black",bd=8,relief=RAISED,font=("Times New					 Roman",20)).place(x=300,y=190)
l8=Label(f,text="SARVANGI AGARWAL",fg="black",bg="slategray",font=("Times New				 Roman",20,"bold")).place(x=350,y=300)
l9=Label(f,text="SAKSHI CHOPRA",fg="black",bg="slategray",font=("Times New					 Roman",20,"bold")).place(x=350,y=250)
l10=Label(f,text="NAVYA MISHRA",fg="black",bg="slategray",font=("Times New					 Roman",20,"bold")).place(x=350,y=350)
l11=Label(f,text="UNDER THE GUIDANCE OF :",font=("Times New						 Roman",20),bd=8,relief=RAISED,fg="snow",bg="black").place(x=320,y=450)
l12=Label(f,text="MR. SHAKTIRISH KUMAR AGRAWAL",font=("Times New					 Roman",17,"bold"),bg="slategray",fg="black").place(x=300,y=520)
def popup():
    response=messagebox.askyesno("ALERT!", "Are you sure to exit the application?")
    if response == 1:
        command= wn.destroy()
b9=Button(f,text="EXIT",fg="snow",bg="black",font="100",padx="35",pady="15",relief=RAISED,bd=5,command=popup).place(x=550,y=600)    
b9=Button(f,text="NEXT",fg="snow",bg="black",font="100",padx="35",pady="15",relief=RAISED,bd=5,command=mainc).place(x=350,y=600)    
wn.mainloop()

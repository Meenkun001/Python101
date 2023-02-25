from tkinter import *
from tkinter import ttk #theme of tk 
from tkinter import messagebox 

GUI = Tk() #นี่ึิคือหน้าจอหลัก
GUI.title('โปรแกรมบันทึกข้อมูล') #นี้้่คือชื่อโปรแกรม
GUI.geometry('600x500') #นี่คือขนาดโปรแกรม

L1 = Label(GUI,text='โปรแกรมบันทึกความรู้',font=('Angsana New',30),fg='blue')
L1.pack()

#B1 = ttk.Button(GUI,text='มีเงินอยู่กี่บาท')
#B1.pack(ipadx=20,ipady=15)
#############################################################

def Button1():
    text = 'จนๆเลยสาสสสส 300 เอง'
    messagebox.showinfo('เงินในบัญชี',text)

FB1 = Frame(GUI)
FB1.place(x=200,y=70)
B2 = ttk.Button(FB1,text='มีเงินอยู่กี่บาท',command=Button1)
B2.pack(ipadx=20,ipady=15)
#############################################################

def Button2():
    text = 'GUI, Math'
    messagebox.showinfo('ได้เีรียนอะไรมา',text)

FB1 = Frame(GUI)
FB1.place(x=200,y=140)
B2 = ttk.Button(FB1,text='วันได้ี้เรียนอะไีร',command=Button2)
B2.pack(ipadx=20,ipady=15)
#############################################################

def Button3():
    text = 'หล่อสาสสสสส'
    messagebox.showwarning('หลุงหล่อแค่ไหน',text)

FB1 = Frame(GUI)
FB1.place(x=200,y=210)
B2 = ttk.Button(FB1,text='ความหล่อของลุง',command=Button3)
B2.pack(ipadx=20,ipady=15)
#############################################################

def Button4():
    text = 'ไม่บอกว้อยยย'
    messagebox.showwarning('ชื่อของพ่อแม่',text)

FB1 = Frame(GUI)
FB1.place(x=200,y=)
B2 = ttk.Button(FB1,text='พ่อแม่ชื่ออะไร',command=Button4)
B2.pack(ipadx=20,ipady=15)



UI.mainloop()

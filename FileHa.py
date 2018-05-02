import tkMessageBox
from Tkinter import *

seats=0

#ADD THE TICKET_INFO IN FILE
def bookdata():
    if seats<5:
        file = open("/home/honeybarua/Documents/shatabdi.txt", "a+")
        file.write(s1.get() + "\t")
        file.write(s2.get() + "\t")
        file.write(s3.get() + "\t")
        file.write(s4.get() + "\t")
        file.write(s5.get() + "\t")
        file.write("\n")
        s1.set("")
        s2.set("")
        s3.set("")
        s4.set("")
        s5.set("")
        file.close()


#NEW WINDOW FOR BOOKED TICKETS
def check():
    handle=Toplevel(root)
    handle.title("BOOKED TICKET INFORMATION")
    print("/home/honeybarua/Documents/shatabdi.txt")
    file=open("/home/honeybarua/Documents/shatabdi.txt","r")
    label_1 = Label(handle, text="BOOKING INFORMATION OF SHATABDI",font="aerial")
    label_1.pack()
    label=Label(handle,text=file.read())
    label.pack()
    file.close()

#FOR SEATS AVAILABITLITY

def avail():
    av=Toplevel(root)
    av.title("SEATS AVAILABLE")
    label=Label(av,text="AVAILABLE SEATS")
    label1=Label(av,text=seats)
    label.pack()
    label1.pack()


#Generate ticket
def generate():
    gen=Toplevel(root)

    file = open("/home/honeybarua/Documents/shatabdi.txt", "r")
    s = s5.get()
    lines = file.readlines()

    for line in lines:
        j=line.split()

        print(j)


        if(j[4]==s):
            print("ew")
            label = Label(gen, text=line)
            label.pack()
    file.close()





#FOR CANCELLATION
def cancel():

    file = open("/home/honeybarua/Documents/shatabdi.txt", "r")
    s=s5.get()
    s5.set("")
    lines = file.readlines()
    file.close()

    file = open("/home/honeybarua/Documents/shatabdi.txt", "w")
    for line in lines:
        j=line.split()
        if(j[4]!=s):
            file.write(line)
    file.close()

def labelsh():

    labelT = Label(sideframe, text="SHATABDI", font="aerial",bd=5)
    labelT.grid(row=0, column=3)

def labelrj():

    labelT = Label(sideframe, text="RAJDHANI EXPRESS", font="aerial",bd=5)
    labelT.grid(row=0, column=3)

def labelhm():

    labelT = Label(sideframe, text="HUMSAFAR EXPRESS", font="aerial",bd=5)
    labelT.grid(row=0, column=3)



#WINDOW INITIALIZATION
root = Tk()
root.title("RAILWAY TICKET BOOKING WINDOW")





#MENU BAR
menubar = Menu(root,activebackground="lightgreen",activeborderwidth=5,bd=3,fg="blue")
filemenu = Menu(menubar, tearoff=0,activebackground="orange")
filemenu.add_command(label="SHATABDI",command=labelsh)
filemenu.add_command(label="RAJDHANI",command=labelrj)
filemenu.add_command(label="HUMSAFAR EXPRESS",command=labelhm)
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="SELECT THE TRAIN ", menu=filemenu)

helpmenu = Menu(menubar, tearoff=0,activebackground="orange")
helpmenu.add_command(label="Help Index")
helpmenu.add_command(label="About...")
menubar.add_cascade(label="HELP", menu=helpmenu)


#FRAME FOR TICKET BOOKING
photo=PhotoImage(file="honey.png")
sideframe=Frame(root)




s1=StringVar()
s2=StringVar()
s3=StringVar()
s4=StringVar()
s5=StringVar()

label1=Label(sideframe,text="PASSENGER NAME",font="aerial",height=4)


t1=Entry(sideframe,textvariable=s1,bd=5,bg="skyblue")

label2=Label(sideframe,text="PHONE NUMBER",font="aerial",height=4)

t2=Entry(sideframe,textvariable=s5,bd=5,bg="skyblue")

label5=Label(sideframe,text="E-MAIL ID",font="aerial",height=4)
t5=Entry(sideframe,textvariable=s2,bd=5,bg="skyblue")

label3=Label(sideframe,text="FROM",font="aerial",height=4)
t3=Entry(sideframe,textvariable=s3,bd=5,bg="skyblue")

label4=Label(sideframe,text="TO",font="aerial",height=4)
t4=Entry(sideframe,textvariable=s4,bd=5,bg="skyblue")

button1=Button(sideframe,text="BOOK TICKET",font="aerial",command=bookdata,fg="green",height = 1, width = 20)
button1.grid(row=23,column=1)

button2=Button(sideframe,text="CANCEL TICKET",font="aerial",command=cancel,fg="red",height = 1, width = 20)
button2.grid(row=23,column=3)

button3=Button(sideframe,text="CHECK BOOKED TICKETS",font="aerial",command=check,fg="orange",height = 1, width = 20)
button3.grid(row=23,column=2)

button4=Button(sideframe,text="Exit",font="aerial",command=root.quit,fg="red",height = 1, width = 20)
button4.grid(row=25,column=1)

button5=Button(sideframe,text="GENERATE TICKET",font="aerial",command=generate,fg="blue",height = 1, width = 20)
button5.grid(row=25,column=2)

button6=Button(sideframe,text="SEATS AVAILABLE",font="aerial",command=avail,fg="purple",height = 1, width = 20)
button6.grid(row=25,column=3)

label0=Label(sideframe,text="TRAIN",font="aerial",height=4)
label0.grid(row=0,column=1)



label1.grid(row=1,column=1)
t1.grid(row=1,column=3)

label2.grid(row=5,column=1)
t2.grid(row=5,column=3)

label3.grid(row=13,column=1)
t3.grid(row=13,column=3)

label4.grid(row=17,column=1)
t4.grid(row=17,column=3)

label5.grid(row=9,column=1)
t5.grid(row=9,column=3)


sideframe.grid(row=0,column=0)

root.config(menu=menubar)
root.mainloop()
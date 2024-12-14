#TKINTER FROM START
'''Tkinter terminologies
# root.title('My First Window')
# root.geometry("500x300")

We can also make frames
frame=tkinter.Frame(parent(which is root in this case))
frame.pack()

its like in our window there's one more frame in which we are putting our text blocks(means second container in the larger container(window))
after placing everything in frame we have to pack the frame
'''

'''Widgets

#=========================================================
##Label Concepts:
# myLabel1=Label(root,text="Hello World")
# myLabel1.pack(pady=10) #we can also put padding between our texts
# myLabel2=Label(root,text="My name is Umair")
# myLabel2.pack(pady=10)
WE can use pack(side="left or side="right")

# myLabel3=Label(root,text="I hate coding!!")
#We can also use the grid function, we cannot use it with pack
#We can also add columns and rows
# myLabel3.grid(row=0,column=0)  we can change these rows and columns
#==========================================================

#===========================================================
##Button Concepts:
# def click():
#     myLabel=Label(root,text="Yoo!!")
#     myLabel.pack()
#How to create a button
#myButton=Button(root,text="Submit",command=click)
#myButton1=Button(root,text="Submit",command=click,bg="dark green",fg="beige") #to change colours of back groung or fore ground we use bg or fg or we can also use full form.
#Usually we use parenthesis when we call a func but in tkinter we dont put parenthesis bcz if we do then the function will be called automatically 
#myButton1.pack(pady=10)
#we can also Disable the button same as entry
#other than bg and fg we can also change active bgs and fgs by activebackground or activeforeground
#To make a space for buttons we can use pack(fill="x" or "y")
# myButton2=Button(root,borderwidth=5,text="Submit Text",command=inputText)
# myButton2.pack()
#exitButton=Button(root,text="Exit Window",command=root.quit)
#exitButton.pack()
#===============================================================

#===============================================================
##Entry Concepts:
#How to create an entry on the window or an input text
# def inputText():
#     myLabelText=Label(root,text=f"Hello " + myentry.get())
#     myLabelText.pack(pady=10)
# myentry=Entry(root,width=20)
# myentry.pack(pady=10)
#we can also disbale entry by state=DISABLED and hide the text by show='*'
# #If we want to insert something
# #myentry.insert(0,"HAaaaa")
#=================================================================

#==================================================================
Text Concepts:
we can change text width and height and font
tex=Text(root,width=80,height=15,font=("Arial",20)) height 15 means 15 lines
tex.pack()

but=Button(root,text="Get Text",command=text)
'''
'''Layout Managers
1.Pack
    packs the data and show it in screen
    pack(pady=10 or padx=10)
    pack(side="right" or side="left")
    pack(fill="x")    

2.Place
    we have coordinates of the window as (0,0)
    so we can put place(x=position we want,y=position we want)
    but place has drawbacks so we use pack

3.Grid
    in this we use rows and columns
    like grid(row=row number,column=column number)
    if we put (row=0,column=0)
    and (row=10,column=10) it will still be in the next line beause there is no text in between 0 and 10

    if we want anything in the middle then we can simply use columnspan or rowspan

    in grid we also use 
    root.grid_rowconfigure(row number,row weight "means spacing")
    root.gir_columnconfigure(column number,column weight "means spacing")
#=========================================================================================
'''

'''
#===============================================================
Boxes
Spinbox:
we also use spinvar=tkinter.StringVar()

string var means we are creating strings of the elements in ths list of our values
now we do 
def spinPressed():
    print(spinvar.get()) #this will print our values in the spinbox

spin=Spinbox(root,from_=from where to start,to=where to end,increment=if we want to add increment value
,values=list of values(it will overwrite the from and to values),textvariable=spinvar,command=spinPressed)
spin.pack()  #remember pack is the most imp step in every widget

#======================================================================================================
Check Box or Check Button:

 def checkpressed():
    print(checkvar.get())
checkvar=StringVar()

check=Checkbutton(root,text="Check me!,variable=checkvar,onvalue=when button is checked,offvalue=when not checked,command=checkpressed)
check.pack(  #remember pack is the most imp step in every widget)

#===================================================================================================

Radio Button:
radiovar=tkinter.StringVar()

radio=Radiobutton(root,variale=radiovar,text="June",value="June Month")
radio1=Radiobutton(root,variale=radiovar,text="July",value="July Month")
radio2=Radiobutton(root,variale=radiovar,text="August",value="Aug Month")
radio3=Radiobutton(root,variale=radiovar,text="September",value="Sep Month")

"Give commands in each of these and the value goes into the string variable not the text"

radio.pack()
radio1.pack()
radio2.pack()
radio3.pack()

#===========================================================================================
Combo Box:
It is itself an entry 
we import tkinter
but for combo box we have to from tkinter import ttk(themed widgets because combo box doesn't exist in tkinter)
def com(event):
    print(combo.get())

combo=ttk.Combobox(root,values=list of values)
combo.pack()  #most imp step
combo.bind("<<ComboboxSelected>>",com)
we can also set a default value like
combo.set("Select Day") #it will appear in the box
we can also change the state of combo box
like combo["state"]="readonly"

#============================================
List Box:
we dont import ttk
it exists in tkinter
we have to create a variable for values
var=StringVar(values=['Mon','Tue','Wed','Thur','Fri']) #write value= not values= if we writes values it will give an error
listbox=Listbox(root,listvariable=listvar,height=5)  #height is number of rows

#=================================================================
Binding events
for example we have
def but(event): #we have to give this parameter otherwise tk will give error
    print(button.get())
button=Button(root,text="Click me")
button.bind(we have to pass an event,then function) the event will be in "<>"

'''



#Login Screen
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
root=Tk()
root.title("LOGIN SCREEN")
root.geometry("500x300")

# EXAMPLE 1
# If we want something on screen window
def name():
    hello=Label(root,text=f"Hello "+entry.get())
    hello.pack()
    #print(f"Hello "+entry.get())

label=Label(root,text="Your name:")
label.pack()
entry=Entry(root)
entry.pack()

button=Button(root,text="enter name",command=name)
button.pack()

# Example 2
root.configure(bg="Brown")

def login():
    username="Umair"
    password="12345"
    if label2Entry.get()==username and label3Entry.get()==password:
        messagebox.showinfo(title="Login Success",message="You have successfully logged in.")
    else:
        messagebox.showerror(title="Login Error",message="Invalid Login.")    

frame=Frame(root,bg="Brown")

Label1=Label(frame,text="Login Please",bg="Brown",fg="Grey",font=("Arial",25,"bold"))
Label1.grid(row=0,column=0,columnspan=2,pady=10)

Label2=Label(frame,text="Username:",bg="Brown",fg="Grey",font=("Arial",15))
Label2.grid(row=1,column=0,pady=10)

label2Entry=Entry(frame,bg="White",fg="Black",font=("Arial",15))
label2Entry.grid(row=1,column=1)

Label3=Label(frame,text="Password:",bg="Brown",fg="Grey",font=("Arial",15))
Label3.grid(row=2,column=0,pady=10)

label3Entry=Entry(frame,show="*",bg="White",fg="Black",font=("Arial",15))
label3Entry.grid(row=2,column=1)

loginButton=Button(frame,text="Login",bg="Grey",fg="Beige",font=("Arial",20,"bold"),command=login)
loginButton.grid(row=3,column=0,columnspan=2,pady=10)

frame.pack()

# Example 3
def spinpressed():
    print(strinvar.get())
strinvar=StringVar()
spin=Spinbox(root,from_=0,to=100,increment=1,values=['hi','hello'],textvariable=strinvar,command=spinpressed)
spin.pack()

# Example 4
def checkpressed():
    print(checkvar.get())

checkvar=StringVar()
che=Checkbutton(root,text="Check me",variable=checkvar,offvalue="yes",onvalue="no",command=checkpressed) 
che.pack()   

# Example 5
radiovar=StringVar()
#We can also add commands

radio=Radiobutton(root,variable=radiovar,text="June",value="June Month")
radio1=Radiobutton(root,variable=radiovar,text="July",value="July Month")
radio2=Radiobutton(root,variable=radiovar,text="August",value="Aug Month")
radio3=Radiobutton(root,variable=radiovar,text="September",value="Sep Month")

radio.pack()
radio1.pack()
radio2.pack()
radio3.pack()

# Example 6
def but(event): #we have to give this parameter otherwise tk will give error
    print("Hi Umair")
button=Button(root,text="Click me")
button.pack()
button.bind("<Button-1>",but)

# Example 7
def com(event):
    print(combo.get())

combo=ttk.Combobox(root,values=['Mon','Tue','Wed'])
combo.pack()  #most imp step
combo.bind("<<ComboboxSelected>>",com)
combo["state"]="readonly"
combo["values"]=["July","Aug"] #we can also change the values

# Example 8
def listselect(event):
    print(listbox.get(listbox.curselection())) #we have to pass cur selection otherwise it doesn't print anything
var=StringVar(value=['Mon','Tue','Wed','Thur','Fri'])
listbox=Listbox(root,listvariable=var,height=5,selectmode='extended')  #height is number of rows #By select mode we can select all values
listbox.pack()
listbox.bind("<<ListboxSelect>>",listselect)

# Example 9

tex=Text(root,width=10,height=5,font=("Arial",20))
tex.pack()

def text():
    print(tex.get("1.0","1.5"))  #1 means line no and after point character no  get(starting point , ending point) if we write end as ending point then we will get all the text 
but=Button(root,text="Get Text",command=text)
but.pack()

def inse():
    tex.insert("1.0","Hi umair") #(point where to insert,text to insert)
insertButton=Button(root,text="insert text",command=inse)
insertButton.pack()\

def dele():
    tex.delete("1.0","end")

delButton=Button(root,text="Delete Text",command=dele)
delButton.pack()    


root.mainloop()

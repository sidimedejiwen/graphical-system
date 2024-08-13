from tkinter import *



#the registration user for the programme 
def registre_user():
    email_info = email.get()
    password_info = password.get()

    file=open(email_info+".txt", "w")
    file.write(email_info+"\n")
    file.write(password_info)
    file.close()
    email_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(screen1,text="Registration Sucess", foreground="green", font=("Calibri", 11 ) ).pack()
    
def registre():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Registre")
    screen1.geometry("300x250")

    global email
    global password
    global email_entry
    global password_entry
    email = StringVar()
    password = StringVar()

    Label(screen1,text="Please enter your details below ").pack()
    Label(screen1,text="").pack()
    Label(screen1,text="email : ").pack()
    email_entry= Entry(screen1, textvariable= email)
    email_entry.pack()
    Label(screen1,text="Password : ").pack()
    password_entry=Entry(screen1, textvariable=password)
    password_entry.pack()
    Label(screen1,text="").pack()
    Button(screen1,text="Registre",width=10,height=1,command=registre_user).pack()
    
#login 
    
def login():
    print("Hello ! login session started")

def main_screen():
    global screen
    screen=Tk()
    screen.geometry("300x250")
    screen.title("WELCOME")
    Label(text= "WELCOME", bg="grey", width= "300", height= "2",font =("Calibri, 13")).pack()
    Button(text="Login", height="2",width="30", command=login).pack()
    Label(text="").pack()
    Button(text="Registre", height="2",width="30",command=registre).pack()
    screen.mainloop()

main_screen()
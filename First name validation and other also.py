'''from termcolor import *
print(colored('WELCOME TO  THE SPY CHAT!!!','blue','on_white'))
print(colored('LETS INTRODUCE YOURSELF IN SPY CHAT','blue','on_white'))

name = input("enter the user name:")
if name.isalpha() and len(name) > 3:
    print("Valid user name.")
    print("User name:", name)
else:
    print("Invalid user name.")

Age=int(input("enter the age of the user: "))
if Age >= 18 and Age <=40:
    print("Valid user age.")
    print("User age:",Age)
else:
    print("Invalid user age.")

place=input("Enter the birth place")
print("User place:",place)

password=input("Enter your password to"\
               " see your Spy chat:")
if password.isdigit() and len(password)<18:
    print("Accepted password.")
    print("You can see the chat.")
else:
    print("Not accepted.")


from termcolor import  *

print (colored('JUST A WARM WELCOME TO YOU!!!','white','on_grey'))
print(colored('HAVE SOME FUN AND INTRODUCE WITH MORE OTHER PEOPLE!!!','blue','on_white'))
'''

from tkinter import  *
from tkinter import  filedialog
from tkinter import ttk
from stegano import lsb
from tkinter import messagebox

root=Tk()
root.title("The spy chat")
root.config(bg='Powder blue')
tabcontrol = ttk.Notebook(root)
tab1 = ttk.Frame(tabcontrol)
tab2 = ttk.Frame(tabcontrol)
tabcontrol.add(tab1, text="Encode the image")
tabcontrol.add(tab2, text="Decode the image")


def browsefunc(widget):
    filename = filedialog.askopenfilename()
    widget.config(text="Path to the File :" + filename)
    widget.insert(0, filename)
def select_image(path):
    print(path)
def clear_field(widget):
    widget.delete(0,END)

def hide_msg(path,msg):

    hide=lsb.hide(path,msg)
    msg_time=msg.asctime().replace(' ','')
    msg_time=msg_time.replace(':','')
    hide.save('secret-pic'+msg_time+'.jpg')
    messagebox.showinfo("Saved","The image was Succesfully Encrypted and Saved as \nsecret-pic"+msg_time+'.png' )

def decode_image(path):
    print(path)
    msg = lsb.reveal(path)
    messagebox.showinfo("Decoded", "The image was Succesfully Decrypted  \n Showing the mesaage now...")

    #print(" the Secret message is ", msg)
    top=Toplevel(tab2)
    Label(top,text="Message is :"+msg,font=("",16),foreground='black').grid(row=0,column=0)


browsebutton = Button(tab1, text="Browse to Path",width=20,height=1,bd=5, command= lambda : browsefunc(path_entry))
browsebutton.grid(row=3,column=0,padx=10,pady=10)

path_entry = Entry(tab1,width=40,borderwidth=2,relief="groove")
path_entry.grid(row=2,column=1,padx=10,pady=10)
path_entry.config(font=('Times New Roman',12),)
upload_button=Button(tab1,text="Upload File",foreground="blue",bd=5,command=lambda : select_image(path_entry.get()))
upload_button.grid(row=3,column=1,padx=10,pady=10)
reset_but=Button(tab1,text="Reset",foreground="red",bd=5,command=lambda: clear_field(path_entry))
reset_but.grid(row=3,column=3,padx=10,pady=10)
Label(tab1,text="Enter your message here: ",font=("",16)).grid(row=4,column=1,padx=10,pady=10)
msg_entry=Entry(tab1,width=40,borderwidth=2,relief='groove',font=("",16))
msg_entry.grid(row=5,column=1,padx=10,pady=10)

enco_but=Button(tab1,text="Hide the Message",font=("",16),foreground="black",bd=5,command=lambda: hide_msg(path_entry.get(),msg_entry.get()) )
enco_but.grid(row=5,column=2,padx=10,pady=10)

tabcontrol.grid(row=0,column=0)

browsebutton = Button(tab2, text="Browse to Path",width=20,height=1,bd=5, command= lambda : browsefunc(path_entryd))
browsebutton.grid(row=3,column=0,padx=10,pady=10)

path_entryd = Entry(tab2,width=40,borderwidth=2,relief="groove")
path_entryd.grid(row=2,column=1,padx=10,pady=10)
path_entryd.config(font=('Times New Roman',12),)
decode_button=Button(tab2,text="Decode Image",bd=5,foreground="black",font=("",18),command=lambda : decode_image(path_entryd.get()))
decode_button.grid(row=5,column=1,padx=10,pady=10)
reset_but=Button(tab2,text="Reset",foreground="red",bd=5,command=lambda: clear_field(path_entry))
reset_but.grid(row=3,column=2,padx=10,pady=10)

tabcontrol.grid(row=0,column=0)
root.mainloop()














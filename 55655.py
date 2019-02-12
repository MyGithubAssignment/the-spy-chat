from tkinter import*
from tkinter import ttk
###print(lyrics)
root=Tk()
root.title("Lyrics App")
#root.resizable(0,0)
root.geometry("500x400")
root.config(bg="Powder blue")
name=Button(root,font=('arial',10,'bold'),text="Artist Name ",foreground="Black",bd=5).grid(row=4,column=0)
Entry=Entry(root,font=('arial',10,'bold'),text="Path Name",bd=5).grid(row=6,column=0,padx=10,pady=10,)


root.mainloop()


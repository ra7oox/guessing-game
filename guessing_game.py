#Ra7oox


from tkinter import *
from tkinter import messagebox
import random
root=Tk()
root.geometry("400x400")
root.title("brain game")
label1=Label(root,text="enter a number")
label1.place(x=140,y=50)

input=Entry(root)
input.place(x=120,y=80)
random_number=random.randint(1,100)
def check():
    if int(input.get())==random_number:
        messagebox.showinfo("good","good you did it")
        root.destroy()
    elif int(input.get())<random_number:
        messagebox.showwarning("upper","upper")
    elif int(input.get())>random_number:
        messagebox.showwarning("lower","lower")
        
    
    
    


button=Button(root,command=check,text="check",bg="green",border=0)
button.place(x=160,y=120)
root.mainloop()



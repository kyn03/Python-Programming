from tkinter import*

root = Tk()
photo = PhotoImage(file="C:\python\chap 08\ogy.gif")
label = Label(root, image=photo)
label.pack()
root.mainloop()
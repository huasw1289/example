from tkinter import * 

Window=Tk()
Window.title("이준성")
Window.geometry("640x400+100+100")
Window.resizable(False, False)

label=Label(Window, text="파이썬", width=10, height=5, fg="red", relief="solid")
label.pack()

photo= PhotoImage(file="C:/users/Administrator/Downloads/unnamed.png")
Label_2 = Label(Window, image=photo)
Label_2.pack()

Window.mainloop()
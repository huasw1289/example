'''
##텍스트 박스 위젯##

from tkinter import *

root = Tk()
root.title("###")
root.geometry("640x480")

txt = Text(root, width=30, height=5)
txt.pack()
txt.insert(END,"글자를 입력하세요")

#e =Entry(root, width=30)
#e.pack()

root.mainloop()
'''

from tkinter import *

root = Tk()
root.title("이준성")
root.geometry("604x480") ## 가로x세로

txt = Text(root, width=30, height=5)
txt.pack()
txt.insert(END, "글자를 입력하세요.")

e = Entry(root, width=30)
e.pack()
e.insert(0, "한줄만 일력하세요")

def btncmd():
    #내용 출력
    print(txt.get("1.0",END))
    print(e.get())

    #내용 삭제
    txt.delete("1.0", END)
    e.delete(0, END)

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()